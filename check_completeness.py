#!/usr/bin/env python3
"""完整性核对：把每个 Notion 块里的文字，逐条到生成的 Markdown 里找。

这是"一定要全"的验收工具。它不看字数，只看**每一段文字在不在**：
对每个页面，取 recordMap 里所有带文字的块，把文字规范化后到对应 md 里搜，
搜不到就报出来（带块类型和片段）。

用法:
    python3 check_completeness.py --graph graph.json --nav nav.json --docs site_src/docs
nav.json 形如 {"相对路径": "页面ID"}，由 build_site.py --dump-nav 生成。
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from notion_cache import cached_blocks  # noqa: E402
from notion_recursive import dashed  # noqa: E402

TEXTY = {"header", "sub_header", "sub_sub_header", "text", "bulleted_list",
         "numbered_list", "toggle", "to_do", "quote", "callout", "code",
         "table_row", "image", "bookmark", "embed", "video", "file", "pdf"}


def seg_text(val) -> str:
    if not isinstance(val, list):
        return ""
    out = []
    for seg in val:
        if isinstance(seg, list) and seg and isinstance(seg[0], str):
            out.append(seg[0])
    return "".join(out)


def norm_light(s: str) -> str:
    """只压空白，用于第二遍匹配：有些块的文字（文件名、URL）会被渲染进链接目标里，
    第一遍把 URL 删掉就看不见了，所以要拿原文再搜一次。"""
    return re.sub(r"[\s\u00a0]+", "", s)


def norm(s: str) -> str:
    """严格版：先把链接目标与裸 URL 删掉，再剥 Markdown 标记，用于比对可见正文。"""
    s = re.sub(r"\]\([^)]*\)", "]", s)
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"[\s\u00a0]+", "", s)
    for ch in "[]()<>*`~#|\\_":
        s = s.replace(ch, "")
    s = s.replace("（", "(").replace("）", ")").replace("：", ":")
    return s


def block_texts(v: dict) -> list:
    t = v.get("type")
    if t not in TEXTY:
        return []
    p = v.get("properties") or {}
    if t == "table_row":
        return [seg_text(x) for x in p.values() if isinstance(x, list) and seg_text(x)]
    if t == "image":
        return []
    cands = []
    for key in ("title", "caption"):
        s = seg_text(p.get(key))
        if s.strip():
            cands.append(s)
    return cands


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", default="graph.json")
    ap.add_argument("--nav", default="nav.json")
    ap.add_argument("--docs", default="site_src/docs")
    ap.add_argument("--show", type=int, default=4)
    a = ap.parse_args()

    nav = json.load(open(a.nav, encoding="utf-8"))
    graph = json.load(open(a.graph, encoding="utf-8"))
    total_blocks = total_missing = 0
    bad_pages = []
    for rel, pid in nav.items():
        path = os.path.join(a.docs, rel)
        if not os.path.exists(path):
            bad_pages.append((rel, pid, [("文件缺失", "", "")]))
            continue
        md_raw = norm_light(open(path, encoding="utf-8").read())
        md = norm(open(path, encoding="utf-8").read())
        bl = cached_blocks(pid)
        if not bl:
            continue
        missing = []
        for bid, v in bl.items():
            for txt in block_texts(v):
                if len(norm(txt)) < 2:
                    continue
                total_blocks += 1
                if norm(txt) in md:
                    continue
                if len(norm_light(txt)) >= 4 and norm_light(txt) in md_raw:
                    continue
                total_missing += 1
                missing.append((v.get("type"), bid[:8], txt[:90]))
        if missing:
            bad_pages.append((rel, pid, missing))
    print(f"带文字的块合计 {total_blocks}，未出现在对应 md 里的 {total_missing}")
    print(f"有缺漏的页面 {len(bad_pages)} 个")
    for rel, pid, missing in bad_pages:
        print(f"\n## {rel}  ({pid[:8]})  缺 {len(missing)} 条")
        for t, bid, s in missing[:a.show]:
            print(f"   [{t}] {bid} {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
