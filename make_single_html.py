#!/usr/bin/env python3
"""把 site_src/docs 打包成一个自包含的单文件 HTML（左栏导航 + 正文），用于分享预览。

多数文档站（含 sing-box 那套 MkDocs Material）都是多文件；要发一个能直接打开的链接，
就得把样式、正文、图片全塞进一个 html。这个脚本干这件事。

用法:
    uv run --with markdown --with pymdown-extensions python3 make_single_html.py \
        --src site_src --out 科研经验笔记.html
"""
import argparse
import base64
import html as htmlmod
import json
import mimetypes
import os
import re
import sys

import markdown

NAV = [
    ("首页", [("index.md", "首页"),
             ("overview/top-phd.md", "如何努力成为一个 Top Ph.D. Student"),
             ("overview/changelog.md", "更新日志")]),
    ("起步", [("start/getting-started.md", "如何在科研上起步"),
             ("start/psychology.md", "做科研前要有的心理准备"),
             ("start/study-plan-example.md", "学习计划的一个例子"),
             ("start/tooling.md", "常用工具与配置")]),
    ("科研能力", [("skills/overview.md", "如何培养自己的科研能力"),
              ("skills/idea.md", "如何培养想 idea 的能力"),
              ("skills/read-papers.md", "如何有效地读论文"),
              ("skills/find-papers.md", "怎么找论文"),
              ("skills/meet.md", "如何与导师 meet"),
              ("skills/debug-experiment.md", "分析实验不 work 的原因"),
              ("skills/experiment-log.md", "怎么写实验记录")]),
    ("Research Project", [("project/index.md", "如何做 Research Project"),
                          ("project/technical-questions.md", "核心技术问题分析模板"),
                          ("project/taboo.md", "从面试问题反思科研的宝贵品质")]),
    ("论文写作", [("writing/template.md", "论文写作模板"),
              ("writing/practice.md", "如何练习写论文"),
              ("writing/expert-experience.md", "高水平科研工作者的写作经验")]),
    ("汇报与答辩", [("talk/slides.md", "怎么做学术报告 Slides"),
               ("talk/rebuttal.md", "怎么 Rebuttal")]),
    ("他山之石", [("others/qualities.md", "博士生的楷模：Sebastian Starke"),
              ("others/external.md", "外部科研经验")]),
    ("原始资料", [("raw/notion-index.md", "Notion 页面索引"),
              ("raw/assets.md", "原始素材清单")]),
]

CSS = """
:root{--bg:#fff;--fg:#1f2328;--muted:#59636e;--line:#d8dee4;--side:#f6f8fa;
      --accent:#0969da;--code:#f6f8fa}
@media (prefers-color-scheme: dark){
  :root{--bg:#0d1117;--fg:#e6edf3;--muted:#8b949e;--line:#30363d;--side:#010409;
        --accent:#4493f8;--code:#161b22}}
*{box-sizing:border-box}
body{margin:0;font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans SC",
     "PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--fg)}
#wrap{display:flex;min-height:100vh}
#side{width:290px;flex:0 0 290px;background:var(--side);border-right:1px solid var(--line);
      padding:18px 14px 60px;position:sticky;top:0;height:100vh;overflow-y:auto}
#side h1{font-size:16px;margin:6px 8px 4px}
#side .sub{font-size:12px;color:var(--muted);margin:0 8px 14px}
#side .sec{font-size:12px;font-weight:700;color:var(--muted);margin:16px 8px 6px;
           letter-spacing:.06em;text-transform:uppercase}
#side a{display:block;padding:5px 10px;border-radius:6px;color:var(--fg);
        text-decoration:none;font-size:14px}
#side a:hover{background:rgba(127,127,127,.12)}
#side a.on{background:var(--accent);color:#fff}
#main{flex:1;min-width:0;padding:34px 46px 90px;max-width:900px}
#main h1{font-size:28px;margin:.2em 0 .6em;border-bottom:1px solid var(--line);padding-bottom:.3em}
#main h2{font-size:22px;margin:1.7em 0 .6em}
#main h3{font-size:18px;margin:1.4em 0 .5em}
#main a{color:var(--accent)}
#main img{max-width:100%;border:1px solid var(--line);border-radius:6px}
#main blockquote{margin:1em 0;padding:2px 16px;border-left:4px solid var(--line);color:var(--muted)}
#main code{background:var(--code);padding:.15em .4em;border-radius:4px;font-size:.9em}
#main pre{background:var(--code);padding:14px;border-radius:8px;overflow-x:auto}
#main pre code{background:none;padding:0}
#main table{border-collapse:collapse;width:100%;margin:1em 0;font-size:14px}
#main th,#main td{border:1px solid var(--line);padding:7px 10px;text-align:left}
#main hr{border:0;border-top:1px solid var(--line);margin:2em 0}
#banner{background:#fff8c5;color:#4d3800;border:1px solid #d4a72c;border-radius:8px;
        padding:10px 14px;font-size:13px;margin-bottom:22px}
@media (prefers-color-scheme: dark){#banner{background:#3b2d00;color:#f0e2b6;border-color:#7d5d00}}
@media (max-width:860px){#side{display:none}}
"""


def data_uri(path: str) -> str:
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as fh:
        return f"data:{mime};base64," + base64.b64encode(fh.read()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="site_src")
    ap.add_argument("--out", default="index.html")
    a = ap.parse_args()
    docs = os.path.join(a.src, "docs")
    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc", "admonition", "attr_list"])

    pages, navmeta = {}, []
    for section, items in NAV:
        entries = []
        for rel, title in items:
            p = os.path.join(docs, rel)
            if not os.path.exists(p):
                print(f"  ! 缺文件 {rel}", file=sys.stderr)
                continue
            text = open(p, encoding="utf-8").read()
            # 站内 .md 链接换成锚点
            text = re.sub(r"(\]\()((?:\.\./)*)([a-z0-9\-/]+)\.md\)",
                          lambda m: f"{m.group(1)}#{'/'.join(x for x in m.group(3).split('/') if x != '..')})",
                          text)
            # 图片内联成 data URI
            for img in set(re.findall(r"\]\(([^)]*assets/img/[^)]+)\)", text)):
                full = os.path.normpath(os.path.join(os.path.dirname(p), img))
                if os.path.exists(full):
                    text = text.replace(img, data_uri(full))
                else:
                    print(f"  ! 图片缺失 {img} -> {full}", file=sys.stderr)
            md.reset()
            pages[rel] = md.convert(text)
            entries.append({"rel": rel, "title": title})
        navmeta.append({"section": section, "items": entries})

    body = json.dumps(pages, ensure_ascii=False)
    navjs = json.dumps(navmeta, ensure_ascii=False)
    out = f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>科研经验笔记</title><style>{CSS}</style></head>
<body><div id="wrap">
<aside id="side">
  <h1>科研经验笔记</h1>
  <p class="sub">彭思达《本人的科研经验》整理版</p>
  <div id="nav"></div>
</aside>
<main id="main">
  <div id="banner">正文版权归原作者彭思达所有，本页为个人学习整理，<b>以 Notion 原文为准</b>。</div>
  <div id="content"></div>
</main>
</div>
<script>
const PAGES={body}, NAV={navjs};
function render(rel){{
  document.getElementById('content').innerHTML = PAGES[rel] || '<p>页面缺失</p>';
  document.querySelectorAll('#nav a').forEach(a=>a.classList.toggle('on',a.dataset.rel===rel));
  location.hash = rel; window.scrollTo(0,0);
}}
const nav=document.getElementById('nav');
NAV.forEach(g=>{{
  const h=document.createElement('div');h.className='sec';h.textContent=g.section;nav.appendChild(h);
  g.items.forEach(it=>{{
    const a=document.createElement('a');a.textContent=it.title;a.dataset.rel=it.rel;
    a.href='#'+it.rel;a.onclick=e=>{{e.preventDefault();render(it.rel);}};nav.appendChild(a);
  }});
}});
render((location.hash||'').slice(1) in PAGES ? location.hash.slice(1) : 'index.md');
window.addEventListener('hashchange',()=>{{const r=location.hash.slice(1); if(r in PAGES) render(r);}});
</script></body></html>
"""
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"[ok] {a.out}  {os.path.getsize(a.out)/1024:.0f} KB, {len(pages)} 页")


if __name__ == "__main__":
    main()
