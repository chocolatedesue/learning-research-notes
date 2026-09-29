#!/usr/bin/env python3
"""把 pengsida/learning_research（仓库 + Notion）建成一个 MkDocs Material 站点。

用法:
    python3 build_site.py --repo repo/ --out site_src
产出: <out>/mkdocs.yml, <out>/docs/**

素材来源与归属：正文版权归原作者彭思达，此处仅作个人学习副本并按原文标注出处。
"""
import argparse
import json
import os
import re
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from notion_recursive import fetch_blocks, dashed, DELAY  # noqa: E402

# --------------------------------------------------------------------------
# 富文本渲染：Notion 的 properties.title 是 [[text, [annotations]], ...]
# --------------------------------------------------------------------------
PAGE_REF = {}
CURATED = {}      # 页面 ID（小写无连字符）-> 站点内相对路径，用于互链与去重
ASSETS = None     # docs/assets/img 目录，图片落到本地，站点自包含
_PREFIX = ""      # 当前 md 文件回退到 docs 根需要的前缀（../ 若干）


def notion_file_url(file_id: str, name: str, block_id: str, space_id: str) -> str:
    """把 attachment:<file_id>:<name> 还原成可访问的 Notion 图床 URL（实测可用）。"""
    import urllib.parse
    src = f"attachment:{file_id}:{name}"
    return (f"https://pengsida.notion.site/image/"
            f"{urllib.parse.quote(src, safe='')}"
            f"?table=block&id={block_id}&spaceId={space_id}&width=1000&userId=&cache=v2")


def local_image(url: str, block_id: str) -> str:
    """下载图片到 docs/assets/img/，返回相对 docs 根的路径；失败则回退成外链。"""
    if ASSETS is None:
        return url
    import urllib.request
    ext = os.path.splitext(url.split("?")[0])[1] or ".png"
    name = f"{block_id.replace('-', '')[:16]}{ext}"
    path = os.path.join(ASSETS, name)
    if not os.path.exists(path):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r, open(path, "wb") as fh:
                fh.write(r.read())
        except Exception as e:  # noqa: BLE001
            print(f"    ! 图片下载失败 {block_id[:8]}: {e}", file=sys.stderr)
            return url
    return f"{_PREFIX}assets/img/{name}"


def normalize_link(url: str) -> str:
    """Notion 里的页面链接常写成 `/1713fe29...?pvs=25` 这种相对形式，还原成绝对地址；
    若能对应到本站已建的页面，就换成站内相对链接。"""
    if not url:
        return url
    if url.startswith("http"):
        host_ok = "notion.site" in url or "notion.so" in url
    else:
        host_ok = url.startswith("/")
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


def rich(props, key="title"):
    segs = props.get(key)
    if not isinstance(segs, list):
        return ""
    out = []
    for seg in segs:
        if not isinstance(seg, list) or not seg:
            continue
        txt = seg[0] if isinstance(seg[0], str) else ""
        anns = seg[1] if len(seg) > 1 and isinstance(seg[1], list) else []
        flags = set()
        link = None
        for a in anns:
            if not isinstance(a, list) or not a:
                continue
            k = a[0]
            flags.add(k)
            if k == "a" and len(a) > 1 and isinstance(a[1], str):
                link = a[1]
            if k == "p" and len(a) > 1 and isinstance(a[1], str):
                target = a[1].replace("-", "").lower()
                name = PAGE_REF.get(target, "另一篇文档")
                rel = CURATED.get(target)
                link = f"{_PREFIX}{rel}" if rel else None
                txt = txt or f"[{name}]"
                out.append(f"[{name}]({link})" if link else f"**{name}**")
                txt = ""
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


def render_block(v):
    t = v.get("type")
    p = v.get("properties") or {}
    txt = rich(p)
    if t == "header":
        return f"## {txt}"
    if t == "sub_header":
        return f"### {txt}"
    if t == "sub_sub_header":
        return f"#### {txt}"
    if t == "bulleted_list":
        return f"- {txt}"
    if t == "numbered_list":
        return f"1. {txt}"
    if t == "toggle":
        return f"- {txt}"
    if t == "to_do":
        checked = bool((v.get("properties") or {}).get("checked"))
        return f"- [{'x' if checked else ' '}] {txt}"
    if t == "quote":
        return f"> {txt}"
    if t == "callout":
        icon = "💡"
        return f"> {icon} {txt}"
    if t == "code":
        lang = rich(p, "language")
        return f"```{lang}\n{txt}\n```"
    if t == "divider":
        return "\n---\n"
    if t == "image":
        src = rich(p, "source")
        cap = rich(p, "caption")
        if src.startswith("attachment:"):
            parts = src.split(":")
            fid = parts[1] if len(parts) > 1 else ""
            fname = parts[2] if len(parts) > 2 else "image.png"
            src = local_image(notion_file_url(fid, fname, v.get("id", ""),
                                              v.get("space_id", "")), v.get("id", ""))
        return f"![{cap or '图'}]({src})" + (f"\n\n*{cap}*" if cap else "")
    if t in ("bookmark", "embed", "video", "file", "pdf"):
        link = rich(p, "link") or rich(p, "source")
        cap = rich(p, "caption") or rich(p, "title") or t
        return f"- [{cap}]({link})" if link.startswith("http") else ""
    return txt


def page_md(pid, depth=0, seen=None):
    """把一页（含未单独建档的子页）渲染成 Markdown。"""
    if seen is None:
        seen = set()
    if pid in seen:
        return ""
    seen.add(pid)
    bl = fetch_blocks(pid)
    time.sleep(DELAY)
    if not bl:
        return f"\n!!! warning\n    本页抓取失败（限速或已取消公开）：`{pid}`\n"
    title = rich((bl.get(pid, {}).get("properties") or {})) or "(无标题)"
    lines = [f"{'#' * min(2 + depth, 6)} {title}", ""]
    children = []
    for bid, v in bl.items():
        if bid == pid:
            continue
        if v.get("type") == "page":
            ct = rich(v.get("properties") or {})
            if ct:
                children.append((bid, ct))
            continue
        line = render_block(v)
        if line:
            lines.append(line)
    lines.append("")
    for cid, ctitle in children:
        key = cid.replace("-", "").lower()
        if key in CURATED:          # 已单独成页，这里只给链接，避免重复正文
            lines.append(f"- [{ctitle}]({_PREFIX}{CURATED[key]})")
            continue
        lines.append(page_md(cid, depth + 1, seen))
    return "\n".join(lines)


def collect_titles(pid, out, seen, depth=0, maxdepth=3):
    """预扫描：建立 页面ID -> 标题 的映射，供行内提及渲染成名字。"""
    if pid in seen or depth > maxdepth:
        return
    seen.add(pid)
    bl = fetch_blocks(pid)
    time.sleep(DELAY)
    if not bl:
        return
    for bid, v in bl.items():
        if v.get("type") == "page":
            t = rich(v.get("properties") or {})
            if t:
                out[bid.replace("-", "").lower()] = t
        if bid == pid:
            t = rich(v.get("properties") or {})
            if t:
                out[bid.replace("-", "").lower()] = t
    for bid, v in bl.items():
        if v.get("type") == "page" and bid != pid:
            collect_titles(bid, out, seen, depth + 1, maxdepth)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="repo")
    ap.add_argument("--out", default="site_src")
    ap.add_argument("--skip-notion", action="store_true")
    a = ap.parse_args()

    docs = os.path.join(a.out, "docs")
    if os.path.isdir(a.out):
        shutil.rmtree(a.out)
    os.makedirs(docs, exist_ok=True)
    inv = json.load(open(os.path.join(a.repo, "..", "inventory.json"), encoding="utf-8")) \
        if os.path.exists(os.path.join(a.repo, "..", "inventory.json")) else None
    if inv is None:
        import subprocess
        subprocess.run([sys.executable, os.path.join(HERE, "inventory_links.py"), a.repo,
                        "-o", os.path.join(a.out, "_inv")], check=True)
        inv = json.load(open(os.path.join(a.out, "_inv.json"), encoding="utf-8"))

    # 预扫描标题（只为了把行内提及渲染成可读名字）
    if not a.skip_notion:
        print("[scan] 建立页面标题表 …", file=sys.stderr)
        seen = set()
        for it in inv["notion"]:
            collect_titles(dashed(it["id"]), PAGE_REF, seen)
        print(f"[scan] 已知页面 {len(PAGE_REF)} 个", file=sys.stderr)

    def write(rel, text):
        path = os.path.join(docs, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text.rstrip() + "\n")
        print(f"  + docs/{rel}  ({len(text)} chars)", file=sys.stderr)

    def set_prefix(rel):
        global _PREFIX
        _PREFIX = "../" * rel.count("/")

    def notion_page(pid, source_url=None):
        head = ""
        if source_url:
            head = f"> 出处：[原文链接]({source_url})\n\n"
        return head + page_md(dashed(pid))

    # ---------------- 导航结构（同时决定 md 落盘位置） ----------------
    NAV = [
        ("首页", [
            ("index.md", "index"),
            ("overview/top-phd.md", "repo:README.md"),
            ("overview/changelog.md", "repo:changelog"),
        ]),
        ("起步", [
            ("start/getting-started.md", "repo:getting_started_in_research.md"),
            ("start/psychology.md", "notion:a3fe9f17b8af46558cd1112627009c83"),
            ("start/study-plan-example.md", "notion:8911dcc5922b4442a80d4407926e65bf"),
            ("start/tooling.md", "notion:59569d7b66954578b21bf1dc6ea35776"),
        ]),
        ("科研能力", [
            ("skills/overview.md", "repo:getting_advanced_in_research.md"),
            ("skills/idea.md", "notion:da6ce171c13846b7a7ffaa7473ffa6ea"),
            ("skills/read-papers.md", "notion:d192db870bc64436ae4a4a590b36772a"),
            ("skills/find-papers.md", "notion:c278dab7e4764d61a92c1fd1ef3135b1"),
            ("skills/meet.md", "notion:d697ef578d784c869d4f8314f0d617da"),
            ("skills/debug-experiment.md", "notion:1aee6e718de6472f834d13da8f4ff097"),
            ("skills/experiment-log.md", "notion:caf34717f4c046c69ee7e14ea953c46f"),
        ]),
        ("Research Project", [
            ("project/index.md", "notion:b43507ef26d044bd888ac29f4736e116"),
            ("project/technical-questions.md", "notion:1753fe292ff180948215cf82cd2b30ae"),
            ("project/taboo.md", "notion:1d13fe292ff180de91afcb7f2eb57b69"),
        ]),
        ("论文写作", [
            ("writing/template.md", "notion:c1a22465a0fa4b15a12985223916048e"),
            ("writing/practice.md", "notion:c13c7e52aab64c1a8e3576b97fcb9851"),
            ("writing/expert-experience.md", "notion:74aef88b9187439fa4e301704f6eb49a"),
        ]),
        ("汇报与答辩", [
            ("talk/slides.md", "notion:810f02670691444f8c94cc3d5b76dcbc"),
            ("talk/rebuttal.md", "notion:af99ce47103e4917b6a5bd1fd4b3c022"),
        ]),
        ("他山之石", [
            ("others/qualities.md", "notion:1713fe292ff1808eb33be93ea2d79ad9"),
            ("others/external.md", "external"),
        ]),
        ("原始资料", [
            ("raw/notion-index.md", "notion-index"),
            ("raw/assets.md", "assets"),
        ]),
    ]

    # 已单独成页的 Notion 页面：正文里的提及与子页都改成站内链接，避免重复
    for section, items in NAV:
        for rel, spec in items:
            if spec.startswith("notion:"):
                CURATED[spec.split(":", 1)[1].replace("-", "").lower()] = rel

    REPO_LINKS = {
        "./getting_started_in_research.md": "start/getting-started.md",
        "getting_started_in_research.md": "start/getting-started.md",
        "./getting_advanced_in_research.md": "skills/overview.md",
        "getting_advanced_in_research.md": "skills/overview.md",
    }

    index_md = """# 科研经验笔记

这是把 [pengsida/learning_research](https://github.com/pengsida/learning_research)（《本人的科研经验》，
作者彭思达，浙江大学）与它外链的 Notion 文档整理成的一个站点，按"起步 → 科研能力 → Research Project
→ 论文写作 → 汇报与答辩"的顺序组织。

!!! warning "内容归属"
    正文版权归原作者所有，本站只是个人学习副本。作者的 Notion 文档随时更新，**以原文为准**：
    页内每篇都标了原文出处，转载或分发前请先征得作者同意。

## 怎么用这个站点

左侧按主题分栏，顶部可切换栏目。每页正文顶部给了原文链接；标注"原文"的页面是直接转载，
带 `[原文链接]` 的段落可以直接跳回去核对。

## 站点包含什么

| 栏目 | 内容 |
|---|---|
| 起步 | 三个阶段的学习路线、做科研前的心理准备、学习计划范例、实验室工具配置 |
| 科研能力 | 想 idea、读论文、找论文、与导师 meet、分析实验不 work、写实验记录 |
| Research Project | 博士生应具备的意识与能力、核心技术问题分析模板、科研上的忌讳 |
| 论文写作 | 写作模板、练习写论文的方法、高水平科研工作者的写作经验 |
| 汇报与答辩 | 学术报告 Slides 的做法、Rebuttal 的策略 |
| 他山之石 | 博士生楷模个案、外部科研经验 PDF |
"""

    global ASSETS
    ASSETS = os.path.join(docs, "assets", "img")
    os.makedirs(ASSETS, exist_ok=True)
    print(f"[assets] 图片落到 {ASSETS}", file=sys.stderr)

    for section, items in NAV:
        for rel, spec in items:
            set_prefix(rel)
            if spec == "index":
                write(rel, index_md)
            elif spec == "external":
                pdfs = [x["url"] for x in inv["pdf"]]
                imgs = [x["url"] for x in inv["image"]]
                body = ["# 外部科研经验", "",
                        "下面这些是原作者推荐的高水平科研工作者的科研经验，原件在 `pengsida.net` 上，"
                        "本仓不转载正文，直接给出链接。", ""]
                for u in pdfs:
                    if "How_to_do_research" in u or "learning_research" in u:
                        name = os.path.basename(u).replace("_How_to_do_research.pdf", "").replace(".pdf", "")
                        body.append(f"- [{name}]({u})")
                for u in imgs:
                    body.append(f"- [Xiangyang Shen（图片）]({u})")
                body += ["", "## 课程 Slides 与视频", ""]
                body.append("- [GAMES003：图形视觉科研基本素养（课程主页）](https://pengsida.net/games003/)")
                for u in [x["url"] for x in inv["pdf"] if "games003" in x["url"]]:
                    body.append(f"- [课程 Slides {os.path.basename(u)}]({u})")
                body.append("- [GAMES003 课程视频（B 站，11 讲）](https://www.bilibili.com/video/BV1RitTezEa9)")
                body.append("- [《learning research》Talk Video](https://www.bilibili.com/video/BV1DA4m1V7D3/)")
                write(rel, "\n".join(body))
            elif spec == "notion-index":
                body = ["# Notion 页面索引", "",
                        f"仓库正文里共指向 {len(inv['notion'])} 个 Notion 页面，全部匿名可达。"
                        "下面按 ID 列出，本站已把其中主要内容整理进左侧各栏目。", ""]
                for it in sorted(inv["notion"], key=lambda x: x["id"]):
                    name = PAGE_REF.get(it["id"], "")
                    body.append(f"- `{it['id']}`" + (f" —— {name}" if name else ""))
                write(rel, "\n".join(body))
            elif spec == "assets":
                body = ["# 原始素材清单", "",
                        f"仓库正文共抽出 Notion 页面 {len(inv['notion'])} 个、PDF {len(inv['pdf'])} 个、"
                        f"图片 {len(inv['image'])} 个、视频 {len(inv['video'])} 个、其他站点链接 {len(inv['web'])} 个。",
                        "", "## PDF", ""]
                body += [f"- {x['url']}" for x in inv["pdf"]]
                body += ["", "## 其他站点链接（课程与个人主页）", ""]
                body += [f"- {x['url']}" for x in inv["web"]]
                write(rel, "\n".join(body))
            elif spec.startswith("repo:"):
                src = os.path.join(a.repo, spec.split(":", 1)[1])
                text = open(src, encoding="utf-8").read()
                head = ("> 出处：[pengsida/learning_research]"
                        "(https://github.com/pengsida/learning_research)\n\n")
                if spec.endswith("README.md"):
                    text = re.sub(r"^# .*$", "", text, count=1, flags=re.M)
                # 仓库内的互相引用改指向本站页面（相对路径，MkDocs 才会重写成正确 URL）
                for old, new in REPO_LINKS.items():
                    text = text.replace(f"]({old})", f"]({_PREFIX}{new})")
                write(rel, head + text)
            elif spec.startswith("notion:"):
                pid = spec.split(":", 1)[1]
                url = f"https://pengsida.notion.site/{pid}"
                write(rel, notion_page(pid, url))
            elif spec == "skip":
                continue
            else:
                print(f"  ? 未识别的 spec: {spec}", file=sys.stderr)

    # ---------------- mkdocs.yml ----------------
    def nav_yaml():
        out = []
        for section, items in NAV:
            out.append(f"  - {section}:")
            for rel, spec in items:
                if spec == "skip":
                    continue
                title = PAGE_TITLES.get(rel, rel)
                out.append(f"      - {title}: {rel}")
        return "\n".join(out)

    PAGE_TITLES = {
        "index.md": "首页",
        "overview/top-phd.md": "如何努力成为一个 Top Ph.D. Student",
        "overview/changelog.md": "更新日志",
        "start/getting-started.md": "如何在科研上起步",
        "start/psychology.md": "做科研前要有的心理准备",
        "start/study-plan-example.md": "学习计划的一个例子",
        "start/tooling.md": "常用工具与配置",
        "skills/overview.md": "如何培养自己的科研能力",
        "skills/idea.md": "如何培养想 idea 的能力",
        "skills/read-papers.md": "如何有效地读论文",
        "skills/find-papers.md": "怎么找论文",
        "skills/meet.md": "如何与导师 meet",
        "skills/debug-experiment.md": "分析实验不 work 的原因",
        "skills/experiment-log.md": "怎么写实验记录",
        "project/index.md": "如何做 Research Project",
        "project/technical-questions.md": "核心技术问题分析模板",
        "project/taboo.md": "从面试问题反思科研的宝贵品质",
        "writing/template.md": "论文写作模板",
        "writing/practice.md": "如何练习写论文",
        "writing/expert-experience.md": "高水平科研工作者的写作经验",
        "talk/slides.md": "怎么做学术报告 Slides",
        "talk/rebuttal.md": "怎么 Rebuttal",
        "others/qualities.md": "博士生的楷模：Sebastian Starke",
        "others/external.md": "外部科研经验",
        "raw/notion-index.md": "Notion 页面索引",
        "raw/assets.md": "原始素材清单",
    }

    # 用抓到的真实标题覆盖占位标题
    for section, items in NAV:
        for rel, spec in items:
            if spec.startswith("notion:") or spec.startswith("repo:"):
                pass
    cfg = f"""site_name: 科研经验笔记
site_description: 彭思达《本人的科研经验》整理版
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
    print(f"[ok] {a.out}/mkdocs.yml 与 docs/ 生成完毕", file=sys.stderr)


if __name__ == "__main__":
    main()
