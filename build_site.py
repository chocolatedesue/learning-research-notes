#!/usr/bin/env python3
"""把 pengsida/learning_research（仓库正文 + Notion 页面闭包）建成一个 MkDocs Material 站点。

与上一版的差别（上一版漏内容的根因）：
  1. 不再平铺遍历 recordMap——那样拿不到顺序，也漏掉嵌套。改为从页面根沿 `content` 数组递归走树，
     toggle / column / table 里的内容才不会被丢或错序。
  2. 支持 `table` / `table_row`。Notion 表格的行存在按列 id 命名的 properties 里，
     上一版只认 `title`，于是整张表被丢掉（「论文写作模板」一页就丢了 725 字）。
  3. 子页面既可能挂在页面根，也可能挂在 column / toggle 等容器里，因此子页识别同样走 content 树。
  4. 页面集合取 notion_graph.py 算出的闭包（含正文行内提及的页面），不再只取 child_page。

用法:
    python3 notion_graph.py --entries entries.txt -o graph.json     # 先算闭包
    python3 build_site.py --repo repo/ --out site_src
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from notion_cache import cached_blocks  # noqa: E402
from notion_recursive import dashed  # noqa: E402

PAGE_REF = {}      # 页面 ID（无连字符小写）-> 标题
CURATED = {}       # 页面 ID -> 站点内相对路径
ASSETS = None
_PREFIX = ""
WARN = []

REPO_NAME = "pengsida/learning_research"
REPO_HOME = "https://github.com/pengsida/learning_research"
REPO_BLOB = "https://github.com/pengsida/learning_research/blob/master/"


def source_line(label: str, url: str, tail: str = "作者可能已更新，以原文为准。") -> str:
    """每页开头的出处行：一个直链加一句提醒。"""
    return f"> 原文：[{label}]({url}) · {tail}\n"


# --------------------------------------------------------------------------- #
# 页面结构
# --------------------------------------------------------------------------- #
def walk_tree(bl: dict, root: str):
    """沿 content 递归，返回 [(block_id, depth)]，顺序即页面顺序。"""
    out, seen = [], set()

    def rec(bid, depth):
        if bid in seen or bid not in bl:
            return
        seen.add(bid)
        out.append((bid, depth))
        for c in (bl[bid].get("content") or []):
            rec(c, depth + 1)

    rec(root, 0)
    return out


def child_pages(bl: dict, root: str):
    """页面根底下（含 column / toggle 等容器内）的全部子页面。"""
    kids = []
    for bid, _d in walk_tree(bl, root)[1:]:
        if (bl.get(bid) or {}).get("type") == "page":
            kids.append(bid)
    return kids


# --------------------------------------------------------------------------- #
# 富文本
# --------------------------------------------------------------------------- #
def normalize_link(url: str) -> str:
    if not url:
        return url
    host_ok = ("notion.site" in url or "notion.so" in url) if url.startswith("http") \
        else url.startswith("/")
    if host_ok:
        m = re.search(r"([0-9a-fA-F]{32})", url)
        if m:
            pid = m.group(1).lower()
            rel = CURATED.get(pid)
            if rel:
                return f"{_PREFIX}{rel}"
            return f"https://pengsida.notion.site/{m.group(1)}"
    if url.startswith("/"):
        return "https://pengsida.notion.site" + url
    return url


def notion_file_url(file_id: str, name: str, block_id: str, space_id: str) -> str:
    src = f"attachment:{file_id}:{name}"
    return ("https://pengsida.notion.site/image/"
            + urllib.parse.quote(src, safe="")
            + f"?table=block&id={block_id}&spaceId={space_id}&width=1000&userId=&cache=v2")


def local_image(url: str, block_id: str) -> str:
    if ASSETS is None or not url.startswith("http"):
        return url
    ext = os.path.splitext(url.split("?")[0])[1] or ".png"
    name = f"{block_id.replace('-', '')[:16]}{ext}"
    path = os.path.join(ASSETS, name)
    if not os.path.exists(path):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r, open(path, "wb") as fh:
                fh.write(r.read())
        except Exception as e:  # noqa: BLE001
            WARN.append(f"图片下载失败 {block_id[:8]}: {e}")
            return url
    return f"{_PREFIX}assets/img/{name}"


def rich(props, key="title") -> str:
    segs = (props or {}).get(key)
    if not isinstance(segs, list):
        return ""
    out = []
    for seg in segs:
        if not isinstance(seg, list) or not seg:
            continue
        txt = seg[0] if isinstance(seg[0], str) else ""
        anns = seg[1] if len(seg) > 1 and isinstance(seg[1], list) else []
        flags, link, emitted = set(), None, False
        for a in anns:
            if not isinstance(a, list) or not a:
                continue
            flags.add(a[0])
            if a[0] == "a" and len(a) > 1 and isinstance(a[1], str):
                link = a[1]
            if a[0] == "p" and len(a) > 1 and isinstance(a[1], str):
                target = str(a[1]).replace("-", "").lower()
                name = PAGE_REF.get(target) or txt or "另一篇文档"
                rel = CURATED.get(target)
                out.append(f"[{name}]({_PREFIX}{rel})" if rel else f"**{name}**")
                emitted = True
        if emitted:
            continue
        if not txt:
            continue
        if "c" in flags:
            txt = f"`{txt}`"
        if "b" in flags:
            txt = f"**{txt}**"
        if "i" in flags:
            txt = f"*{txt}*"
        if "s" in flags:
            txt = f"~~{txt}~~"
        if link:
            txt = f"[{txt}]({normalize_link(link)})"
        out.append(txt)
    return "".join(out)


def render_table(bl: dict, v: dict) -> list:
    fmt = v.get("format") or {}
    cols = fmt.get("table_block_column_order") or []
    rows = [bl[c] for c in (v.get("content") or [])
            if (bl.get(c) or {}).get("type") == "table_row"]
    if not cols or not rows:
        return []

    def cell(r, c):
        t = rich(r.get("properties") or {}, c).replace("|", "\\|").replace("\n", " ").strip()
        return t or " "

    head = ["| " + " | ".join(cell(rows[0], c) for c in cols) + " |",
            "|" + "---|" * len(cols)]
    body = ["| " + " | ".join(cell(r, c) for c in cols) + " |" for r in rows[1:]]
    return [""] + head + body + [""]


CONTAINERS = {"column_list", "column", "table_of_contents", "breadcrumb",
              "collection_view_page", "collection_view"}


def render_block(bl: dict, bid: str, v: dict) -> list:
    t = v.get("type")
    p = v.get("properties") or {}
    txt = rich(p)
    if t in CONTAINERS:
        return []
    if t == "header":
        return [f"## {txt}"]
    if t == "sub_header":
        return [f"### {txt}"]
    if t == "sub_sub_header":
        return [f"#### {txt}"]
    if t == "bulleted_list":
        return [f"- {txt}"]
    if t == "numbered_list":
        return [f"1. {txt}"]
    if t == "toggle":
        return [f"- **{txt}**"]
    if t == "to_do":
        checked = bool(p.get("checked"))
        return [f"- [{'x' if checked else ' '}] {txt}"]
    if t in ("quote", "callout"):
        return [f"> {txt}"]
    if t == "code":
        return [f"```{rich(p, 'language')}", rich(p, "title"), "```"]
    if t == "divider":
        return ["", "---", ""]
    if t == "table":
        return render_table(bl, v)
    if t in ("table_row", "page"):
        return []
    if t == "image":
        src = rich(p, "source")
        cap = rich(p, "caption")
        if src.startswith("attachment:"):
            parts = src.split(":")
            fid = parts[1] if len(parts) > 1 else ""
            fname = parts[2] if len(parts) > 2 else "image.png"
            src = local_image(notion_file_url(fid, fname, v.get("id", ""), v.get("space_id", "")),
                              v.get("id", ""))
        out = [f"![{cap or '图'}]({src})"]
        if cap:
            out += ["", f"*{cap}*"]
        return out
    if t in ("bookmark", "embed", "video"):
        link = rich(p, "link") or rich(p, "source")
        cap = rich(p, "caption") or rich(p, "title") or t
        return [f"- [{cap}]({normalize_link(link)})"] if link.startswith("http") else []
    if t in ("file", "pdf"):
        # 附件走 attachment:<file_id>:<name>，/file/ 端点只回 HTML，取不到原文件，
        # 所以这里给出文件名并链到所在原页，正文照旧可见。
        name = rich(p, "title") or rich(p, "caption") or "附件"
        src = rich(p, "source")
        pid = (v.get("parent_id") or "").replace("-", "")
        url = f"https://pengsida.notion.site/{pid}" if len(pid) == 32 else ""
        tail = "（原页附件，本站未镜像）" if src.startswith("attachment:") else ""
        return [f"- 附件：{name}" + (f" —— [在原页查看]({url})" if url else "") + tail]
    if t == "link_to_page":
        for key in ("page_id", "block_id"):
            val = p.get(key)
            if isinstance(val, list) and val and isinstance(val[0], list) and val[0]:
                pid = str(val[0][0]).replace("-", "").lower()
                name = PAGE_REF.get(pid, "另一篇文档")
                rel = CURATED.get(pid)
                return [f"- [{name}]({_PREFIX}{rel})" if rel else f"- {name}（原文外链）"]
        return []
    if t == "alias":
        ptr = (v.get("format") or {}).get("alias_pointer") or {}
        pid = str(ptr.get("id", "")).replace("-", "").lower()
        if pid:
            name = PAGE_REF.get(pid, "另一篇文档")
            rel = CURATED.get(pid)
            return [f"- [{name}]({_PREFIX}{rel})" if rel else f"- {name}（原文外链）"]
        return []
    if txt:
        return [txt]
    return []


def page_md(pid: str) -> str:
    bl = cached_blocks(pid)
    if not bl:
        return ('\n!!! warning "本页不可访问"\n'
                f'    该页面未公开或已删除，抓取接口取不到：`{pid}`\n')
    root = dashed(pid)
    order = walk_tree(bl, root)
    if not order:
        return '\n!!! warning "抓取异常"\n    块树为空。\n'
    title = rich(bl[root].get("properties") or {}) or PAGE_REF.get(pid) or "(无标题)"
    # 每页开头给原文直链，方便跳回 Notion 核对最新版本
    src = source_line("Notion 原文", f"https://pengsida.notion.site/{pid}")
    lines, kids, orphans = [src, f"## {title}", ""], [], []
    reached = {b for b, _ in order}
    for bid, _d in order[1:]:
        v = bl.get(bid) or {}
        if v.get("type") == "page":
            kids.append((bid, rich(v.get("properties") or {}) or PAGE_REF.get(bid) or "子页面"))
            continue
        lines += render_block(bl, bid, v)
    for bid, v in bl.items():                 # 树里没走到的块，兜底补进正文
        if bid in reached or v.get("type") == "page":
            continue
        orphans += render_block(bl, bid, v)
    if orphans:
        lines += ["", "### 未归位的内容（未挂在块树上，兜底列出）", ""] + orphans
    if kids:
        lines += ["", "### 子页面", ""]
        for cid, ctitle in kids:
            rel = CURATED.get(cid.replace("-", "").lower())
            if rel:
                lines.append(f"- [{ctitle}]({_PREFIX}{rel})")
            else:
                WARN.append(f"子页面未建页: {cid[:8]} {ctitle}")
                lines.append(f"- {ctitle}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
NAV = [
    ("首页", [
        ("index.md", None, "首页"),
        ("overview/top-phd.md", "repo:README.md", "如何努力成为一个 Top Ph.D. Student"),
        ("overview/changelog.md", "repo:changelog", "更新日志"),
    ]),
    ("起步", [
        ("start/getting-started.md", "repo:getting_started_in_research.md", "如何在科研上起步"),
        ("start/psychology.md", "a3fe9f17", "科研学习与课程学习的不同之处"),
        ("start/study-plan-example.md", "8911dcc5", "学习计划参考例子"),
        ("start/tooling.md", "59569d7b", "设备配置"),
    ]),
    ("科研能力", [
        ("skills/overview.md", "repo:getting_advanced_in_research.md", "如何培养自己的科研能力"),
        ("skills/idea.md", "da6ce171", "如何培养想 idea 的能力"),
        ("skills/read-papers.md", "d192db87", "如何有效地读论文"),
        ("skills/literature-tree.md", "f8b36e48", "如何构建 literature tree"),
        ("skills/find-papers.md", "c278dab7", "怎么找论文"),
        ("skills/meet.md", "d697ef57", "如何高效地讨论"),
        ("skills/debug-experiment.md", "1aee6e71", "如何找到实验不 work 的原因"),
        ("skills/experiment-log.md", "caf34717", "怎么做实验记录"),
        ("skills/experiment-log-template.md", "a7b846d0", "实验记录模板"),
        ("skills/experiment-log-example.md", "492bf030", "实验记录示例（3.24）"),
    ]),
    ("Research Project", [
        ("project/index.md", "b43507ef", "如何做 Research Project"),
        ("project/technical-questions.md", "1753fe29", "核心技术问题分析模板"),
        ("project/taboo.md", "1fa3fe29", "科研上忌讳的事情有哪些"),
        ("project/qualities-from-interview.md", "1d13fe29", "从面试问题反思科研的宝贵品质"),
    ]),
    ("论文写作", [
        ("writing/template.md", "c1a22465", "论文写作模板"),
        ("writing/practice.md", "c13c7e52", "怎么练习写论文"),
        ("writing/expert-experience.md", "74aef88b", "高水平科研工作者的写作经验"),
        ("writing/revise.md", "1293fe29", "如何改一篇论文的写作"),
        ("writing/review.md", "eed9ed1e", "怎么审论文"),
        ("writing/copilot-english.md", "1143fe29", "如何用 copilot 和 GPT 辅助英语写作"),
        ("writing/examples.md", "1723fe29", "写作思路典例"),
    ]),
    ("汇报与答辩", [
        ("talk/slides.md", "810f0267", "如何做学术报告 slides"),
        ("talk/rebuttal.md", "af99ce47", "怎么 rebuttal"),
    ]),
    ("他山之石", [
        ("others/qualities.md", "1713fe29", "博士生的楷模：Sebastian Starke"),
        ("others/phase.md", "1703fe29", "Phase for Character Control"),
        ("others/external.md", None, "外部科研经验"),
        ("others/unavailable.md", None, "未公开的引用页面"),
    ]),
    ("个人学习笔记", [
        ("notes/sida-peng.md", "471320cc", "Sida Peng（彭思达）"),
        ("notes/minimal-viable.md", "2863fe29", "探索性实验应遵循最小可行性"),
        ("notes/science-definition.md", "1053fe29", "自然科学的定义"),
        ("notes/deep-rl.md", "24e3fe29", "《深度强化学习》学习笔记"),
        ("notes/zhang-xiangyu.md", "2213fe29", "张祥雨访谈笔记"),
        ("notes/gpt4o.md", "1c63fe29", "GPT-4o 相关技术笔记"),
        ("notes/3d-llm.md", "9533b857", "3D LLM 的 pipeline 总结"),
        ("notes/embodied.md", "092795ee", "具身智能的 pipeline 总结"),
        ("notes/ross-girshick.md", "d9b48545", "Ross Girshick 的 talk 笔记"),
        ("notes/lecun.md", "1223fe29", "LeCun Talk 笔记"),
    ]),
    ("原始资料", [
        ("raw/notion-index.md", None, "Notion 页面索引"),
        ("raw/assets.md", None, "原始素材清单"),
    ]),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="repo")
    ap.add_argument("--graph", default="graph.json")
    ap.add_argument("--out", default="site_src")
    a = ap.parse_args()

    graph = json.load(open(a.graph, encoding="utf-8"))
    for pid, m in graph.items():
        PAGE_REF[pid] = m.get("title", "")

    def have(prefix):
        for p in graph:
            if p.startswith(prefix):
                return p
        return None

    docs = os.path.join(a.out, "docs")
    if os.path.isdir(a.out):
        shutil.rmtree(a.out)
    os.makedirs(docs, exist_ok=True)
    for _sec, items in NAV:
        for rel, spec, _t in items:
            if spec and not spec.startswith("repo:"):
                pid = have(spec)
                if pid:
                    CURATED[pid] = rel
                else:
                    WARN.append(f"闭包里找不到 {spec}（{rel}）")

    inv_path = os.path.join(a.out, "_inv.json")
    subprocess.run([sys.executable, os.path.join(HERE, "inventory_links.py"),
                    a.repo, "-o", os.path.join(a.out, "_inv")], check=True)
    inv = json.load(open(inv_path, encoding="utf-8"))

    def write(rel, text):
        path = os.path.join(docs, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text.rstrip() + "\n")
        print(f"  + docs/{rel}  ({len(text)} chars)", file=sys.stderr)

    def set_prefix(rel):
        global _PREFIX
        _PREFIX = "../" * rel.count("/")

    REPO_LINKS = {
        "./getting_started_in_research.md": "start/getting-started.md",
        "getting_started_in_research.md": "start/getting-started.md",
        "./getting_advanced_in_research.md": "skills/overview.md",
        "getting_advanced_in_research.md": "skills/overview.md",
    }

    global ASSETS
    ASSETS = os.path.join(docs, "assets", "img")
    os.makedirs(ASSETS, exist_ok=True)

    missing = sorted(p for p, m in graph.items() if m.get("missing"))
    ok_n = len(graph) - len(missing)
    index_md = source_line(REPO_NAME, REPO_HOME, "本站为整理副本，正文版权归原作者。") + f"""\n# 科研经验笔记

把 [pengsida/learning_research](https://github.com/pengsida/learning_research)（《本人的科研经验》，
作者彭思达，浙江大学）与它外链的 Notion 文档整理成的一个站点，框架是 MkDocs + Material for MkDocs。

!!! warning "内容归属"
    正文版权归原作者所有，本站是个人学习副本，**以 Notion 原文为准**。每页顶部都标了原文出处。
    原作者要求撤下时会立即删除。

## 收录范围

从仓库正文里的 {len(inv['notion'])} 个 Notion 入口出发做**闭包**遍历——子页面、正文行内提及、
alias、link_to_page 各算一条边，一直走到不再有新页面为止。共得到 {len(graph)} 个页面，
其中可抓取 {ok_n} 个，已全部收进左侧栏目；剩下 {len(missing)} 个未公开，记在「他山之石 → 未公开的引用页面」。

## 栏目

| 栏目 | 内容 |
|---|---|
| 起步 | 三阶段学习路线、科研与课程学习的差别、学习计划范例、设备配置 |
| 科研能力 | 想 idea、读论文、构建 literature tree、找论文、高效讨论、排查实验不 work、写实验记录 |
| Research Project | 博士生应具备的意识与能力、核心技术问题分析模板、科研上的忌讳、面试角度的反思 |
| 论文写作 | 写作模板、练习写论文、改论文、审论文、用 AI 辅助英语写作、写作思路典例 |
| 汇报与答辩 | 学术报告 slides、rebuttal |
| 他山之石 | 博士生楷模个案、外部科研经验链接 |
| 个人学习笔记 | 原 Notion 工作区里的学习笔记（与"博士生培养"主题不完全重合） |
| 原始资料 | Notion 页面索引、原始素材清单 |
"""

    navmap = {}
    for section, items in NAV:
        for rel, spec, title in items:
            set_prefix(rel)
            if rel == "index.md":
                write(rel, index_md)
            elif rel == "others/external.md":
                body = [source_line(REPO_NAME, REPO_HOME, "下列材料由原作者推荐，本站只给链接。"), "",
                        "# 外部科研经验", "",
                        "下面是原作者推荐的高水平科研工作者的科研经验，原件托管在 `pengsida.net`，"
                        "本站不转载正文，只给链接。", ""]
                for u in inv["pdf"]:
                    u = u["url"]
                    if "How_to_do_research" in u or "learning_research" in u:
                        name = os.path.basename(u).replace("_How_to_do_research.pdf", "").replace(".pdf", "")
                        body.append(f"- [{name}]({u})")
                if inv["image"]:
                    body.append(f"- [Xiangyang Shen（图片）]({inv['image'][0]['url']})")
                body += ["", "## GAMES003 课程", "",
                         "- [课程主页](https://pengsida.net/games003/)"]
                for x in inv["pdf"]:
                    if "games003" in x["url"]:
                        body.append(f"- [课程 slides {os.path.basename(x['url'])}]({x['url']})")
                body += ["- [课程视频（B 站，11 讲）](https://www.bilibili.com/video/BV1RitTezEa9)",
                         "- [《learning research》Talk Video](https://www.bilibili.com/video/BV1DA4m1V7D3/)"]
                write(rel, "\n".join(body))
            elif rel == "others/unavailable.md":
                body = [source_line(REPO_NAME, REPO_HOME, "下列页面被正文引用但未公开分享。"), "",
                        "# 未公开的引用页面", "",
                        "正文里引到了下面这些页面，但它们没有公开分享，抓取接口返回 400/404，"
                        "所以只能记下引用位置，正文无法收录。", ""]
                for pid in missing:
                    body.append(f"- `{pid}`")
                body += ["", "其中 `0051678d2df74d73ae236b9b44875193` 在原文档里被标为"
                             "「论文画图模板（未对外公开）」；`1b53504d…` 只在"
                             "《深度强化学习》学习笔记里被引用。"]
                write(rel, "\n".join(body))
            elif rel == "raw/notion-index.md":
                body = [source_line(REPO_NAME, REPO_HOME, "索引由本站整理。"), "",
                        "# Notion 页面索引", "",
                        f"仓库正文指向 {len(inv['notion'])} 个 Notion 入口；闭包展开后共 {len(graph)} 个页面。",
                        "", "## 入口页面", ""]
                for it in sorted(inv["notion"], key=lambda x: x["id"]):
                    name = PAGE_REF.get(it["id"], "")
                    body.append(f"- `{it['id']}`" + (f" —— {name}" if name else ""))
                body += ["", "## 闭包内的全部页面", ""]
                for pid, m in sorted(graph.items(), key=lambda kv: kv[1].get("title", "")):
                    body.append(f"- `{pid}` —— {m.get('title', '?')}"
                                + ("（不可访问）" if m.get("missing") else ""))
                write(rel, "\n".join(body))
            elif rel == "raw/assets.md":
                body = [source_line(REPO_NAME, REPO_HOME, "清单由本站整理。"), "",
                        "# 原始素材清单", "",
                        f"仓库正文共抽出 Notion 入口 {len(inv['notion'])} 个、PDF {len(inv['pdf'])} 个、"
                        f"图片 {len(inv['image'])} 个、视频 {len(inv['video'])} 个、"
                        f"其他站点链接 {len(inv['web'])} 个。", "", "## PDF", ""]
                body += [f"- {x['url']}" for x in inv["pdf"]]
                body += ["", "## 其他站点链接", ""]
                body += [f"- {x['url']}" for x in inv["web"]]
                write(rel, "\n".join(body))
            elif spec and spec.startswith("repo:"):
                src = os.path.join(a.repo, spec.split(":", 1)[1])
                text = open(src, encoding="utf-8").read()
                fname = spec.split(":", 1)[1]
                head = source_line(f"{REPO_NAME} · {fname}", REPO_BLOB + fname,
                                   "仓库正文；Notion 侧若更新不会反映在这里。")
                if spec.endswith("README.md"):
                    text = re.sub(r"^# .*$", "", text, count=1, flags=re.M)
                for old, new in REPO_LINKS.items():
                    text = text.replace(f"]({old})", f"]({_PREFIX}{new})")
                write(rel, head + text)
            elif spec:
                pid = have(spec)
                navmap[rel] = pid
                write(rel, page_md(pid))

    with open(os.path.join(a.out, "nav.json"), "w", encoding="utf-8") as fh:
        json.dump(navmap, fh, ensure_ascii=False, indent=1)
    nav_full = [{"section": sec, "title": t, "rel": rel, "pid": navmap.get(rel)}
                for sec, items in NAV for rel, _s, t in items]
    with open(os.path.join(a.out, "nav_full.json"), "w", encoding="utf-8") as fh:
        json.dump(nav_full, fh, ensure_ascii=False, indent=1)

    def nav_yaml():
        out = []
        for section, items in NAV:
            out.append(f"  - {section}:")
            for rel, _spec, title in items:
                out.append(f"      - {title}: {rel}")
        return "\n".join(out)

    cfg = f"""site_name: 科研经验笔记
site_url: https://chocolatedesue.github.io/learning-research-notes/
site_description: 彭思达《本人的科研经验》整理版（含 Notion 页面闭包）
docs_dir: docs
theme:
  name: material
  language: zh
  features:
    - navigation.tracking
    - navigation.tabs
    - navigation.indexes
    - navigation.expand
    - navigation.sections
    - navigation.top
    - header.autohide
    - content.code.copy
    - toc.follow
    - search.suggest
    - search.highlight
  palette:
    - media: "(prefers-color-scheme)"
      toggle:
        icon: material/link
        name: 跟随系统
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: white
      toggle:
        icon: material/toggle-switch
        name: 切换到暗色
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: black
      toggle:
        icon: material/toggle-switch-off
        name: 切换到亮色
markdown_extensions:
  - toc:
      permalink: true
  - admonition
  - attr_list
  - md_in_html
  - footnotes
  - def_list
  - pymdownx.details
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.highlight:
      anchor_linenums: true
nav:
{nav_yaml()}
copyright: 正文版权归原作者彭思达所有 · 本站为个人学习整理
"""
    with open(os.path.join(a.out, "mkdocs.yml"), "w", encoding="utf-8") as fh:
        fh.write(cfg)
    print(f"\n[ok] {a.out}/mkdocs.yml 与 docs/ 生成完毕", file=sys.stderr)
    if WARN:
        print("\n[warn]", file=sys.stderr)
        for w in WARN[:40]:
            print(f"  - {w}", file=sys.stderr)


if __name__ == "__main__":
    main()
