#!/usr/bin/env python3
"""把 site_src/docs 打包成自包含的单文件 HTML（左栏导航 + 正文），用于分享预览。

文档站（含 sing-box 那套 MkDocs Material）通常是多文件；要发一个能直接打开、能转发的链接，
就得把样式、正文、图片全塞进一个 html。导航直接读 build_site.py 生成的 nav_full.json，
所以栏目结构与站点始终保持一致。

用法:
    uv run --with markdown --with pymdown-extensions python3 make_single_html.py \
        --src site_src --out single.html
"""
import argparse
import base64
import json
import mimetypes
import os
import re
import sys

import markdown

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
#side{width:300px;flex:0 0 300px;background:var(--side);border-right:1px solid var(--line);
      padding:18px 14px 60px;position:sticky;top:0;height:100vh;overflow-y:auto}
#side h1{font-size:16px;margin:6px 8px 4px}
#side .sub{font-size:12px;color:var(--muted);margin:0 8px 14px}
#side .sec{font-size:12px;font-weight:700;color:var(--muted);margin:16px 8px 6px;
           letter-spacing:.06em}
#side a{display:block;padding:4px 10px;border-radius:6px;color:var(--fg);
        text-decoration:none;font-size:14px;line-height:1.45}
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
#main th,#main td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
#main hr{border:0;border-top:1px solid var(--line);margin:2em 0}
#banner{background:#fff8c5;color:#4d3800;border:1px solid #d4a72c;border-radius:8px;
        padding:10px 14px;font-size:13px;margin-bottom:22px}
@media (prefers-color-scheme: dark){#banner{background:#3b2d00;color:#f0e2b6;border-color:#7d5d00}}
@media (max-width:880px){#side{display:none}}
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
    nav = json.load(open(os.path.join(a.src, "nav_full.json"), encoding="utf-8"))
    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc", "admonition", "attr_list"])

    pages, groups = {}, []
    for item in nav:
        rel = item["rel"]
        path = os.path.join(docs, rel)
        if not os.path.exists(path):
            print(f"  ! 缺文件 {rel}", file=sys.stderr)
            continue
        text = open(path, encoding="utf-8").read()
        # 站内 .md 链接换成锚点
        text = re.sub(r"(\]\()((?:\.\./)*)([A-Za-z0-9\-/]+)\.md\)",
                      lambda m: f"{m.group(1)}#{m.group(3).split('/')[-1]})", text)
        for img in set(re.findall(r"\]\(([^)]*assets/img/[^)]+)\)", text)):
            full = os.path.normpath(os.path.join(os.path.dirname(path), img))
            if os.path.exists(full):
                text = text.replace(img, data_uri(full))
            else:
                print(f"  ! 图片缺失 {img}", file=sys.stderr)
        md.reset()
        pages[rel] = md.convert(text)
        if not groups or groups[-1]["section"] != item["section"]:
            groups.append({"section": item["section"], "items": []})
        groups[-1]["items"].append({"rel": rel, "title": item["title"]})

    body = json.dumps(pages, ensure_ascii=False)
    navjs = json.dumps(groups, ensure_ascii=False)
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
  try{{location.hash = rel;}}catch(e){{}}
  window.scrollTo(0,0);
}}
const nav=document.getElementById('nav');
NAV.forEach(g=>{{
  const h=document.createElement('div');h.className='sec';h.textContent=g.section;nav.appendChild(h);
  g.items.forEach(it=>{{
    const a=document.createElement('a');a.textContent=it.title;a.dataset.rel=it.rel;
    a.href='#'+it.rel;a.onclick=e=>{{e.preventDefault();render(it.rel);}};nav.appendChild(a);
  }});
}});
const first=(location.hash||'').slice(1);
render(first in PAGES ? first : 'index.md');
window.addEventListener('hashchange',()=>{{const r=location.hash.slice(1); if(r in PAGES) render(r);}});
</script></body></html>
"""
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"[ok] {a.out}  {os.path.getsize(a.out)/1024:.0f} KB, {len(pages)} 页, {len(groups)} 栏")


if __name__ == "__main__":
    main()
