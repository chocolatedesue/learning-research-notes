#!/usr/bin/env python3
"""算出 pengsida.notion.site 中从一批入口可达的**页面闭包**。

为什么需要它：只顺着 child_page 抓会漏掉正文里用行内提及、alias、link_to_page
引到的页面。要"全"，就得把所有引用都当边，跑到不动点。

用法:
    python3 notion_graph.py --entries entries.txt -o graph.json [--max-pages 400]
entries.txt 每行一个页面 ID 或 notion URL。
"""
import argparse
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from notion_cache import cached_blocks  # noqa: E402
from notion_recursive import dashed  # noqa: E402

DELAY = 1.2
PAGE_ID = re.compile(r"([0-9a-fA-F]{32})")


def norm(x: str) -> str:
    m = PAGE_ID.search(x)
    return m.group(1).lower() if m else ""


def refs_in(v: dict) -> set:
    """一个块里引到的其他页面 ID：子页面、alias、link_to_page、行内提及、notion 链接。"""
    out = set()
    t = v.get("type")
    if t == "page":
        out.add(v["id"].replace("-", "").lower())
    if t == "alias" and isinstance(v.get("format", {}).get("alias_pointer"), dict):
        pid = norm(v["format"]["alias_pointer"].get("id", ""))
        if pid:
            out.add(pid)
    if t == "link_to_page":
        p = v.get("properties") or {}
        for key in ("page_id", "block_id"):
            val = p.get(key)
            if isinstance(val, list) and val and isinstance(val[0], list) and val[0]:
                pid = norm(str(val[0][0]))
                if pid:
                    out.add(pid)
    for key, val in (v.get("properties") or {}).items():
        if not isinstance(val, list):
            continue
        for seg in val:
            if not isinstance(seg, list) or len(seg) < 2 or not isinstance(seg[1], list):
                continue
            for a in seg[1]:
                if not isinstance(a, list) or not a:
                    continue
                if a[0] == "p" and len(a) > 1:
                    pid = norm(str(a[1]))
                    if pid:
                        out.add(pid)
                if a[0] == "a" and len(a) > 1 and isinstance(a[1], str):
                    pid = norm(a[1])
                    if pid:
                        out.add(pid)
    return out


def children_of(bl: dict, pid: str) -> list:
    """只把「本页 content 数组里、且 parent_id 就是本页」的 page 块当子页。

    不能简单遍历 recordMap 里所有 page 块：抓子页时父页块也会一起回来，
    那样父子关系会互相指认，形成环。
    """
    self_v = bl.get(dashed(pid)) or {}
    kids = []
    for cid in (self_v.get("content") or []):
        cv = bl.get(cid) or {}
        if cv.get("type") != "page":
            continue
        if cv.get("parent_id") not in (dashed(pid), None):
            continue
        kids.append(cid.replace("-", "").lower())
    return [k for k in dict.fromkeys(kids) if k != pid]


def closure(entry_ids, max_pages=400, log=print):
    pages, frontier, seen = {}, list(dict.fromkeys(entry_ids)), set()
    while frontier and len(pages) < max_pages:
        pid = frontier.pop(0)
        if pid in seen:
            continue
        seen.add(pid)
        bl = cached_blocks(pid)
        if not bl:
            pages[pid] = {"title": "(不可访问)", "parent": None, "children": [],
                          "refs": [], "missing": True}
            log(f"  ! {pid[:8]} 抓取失败（非公开或已删除）")
            continue
        self_v = bl.get(dashed(pid)) or {}
        title = ""
        val = (self_v.get("properties") or {}).get("title")
        if isinstance(val, list):
            title = "".join(s[0] for s in val if isinstance(s, list) and s and isinstance(s[0], str)).strip()
        kids = children_of(bl, pid)
        extra = set()
        for _bid, v in bl.items():
            extra |= refs_in(v)
        extra -= {pid} | set(kids)
        order = [c.replace("-", "").lower() for c in (self_v.get("content") or [])]
        pages[pid] = {"title": title or "(无标题)", "parent": None,
                      "children": kids, "refs": sorted(extra), "order": order}
        new = [x for x in extra if x not in seen and x not in frontier]
        if new:
            log(f"  + {pid[:8]} 引到 {len(new)} 个正文内引用页面")
        frontier.extend(x for x in (kids + sorted(extra)) if x not in seen)
        log(f"  · {pid[:8]} {title[:38]!r} blocks={len(bl)} child={len(kids)} refs={len(extra)}")
    # 填父节点（只认 content 派生的父子关系，避免成环）
    for pid, meta in pages.items():
        for c in meta.get("children", []):
            if c in pages and not pages[c].get("parent"):
                pages[c]["parent"] = pid
    return pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entries", required=True)
    ap.add_argument("-o", "--out", default="graph.json")
    ap.add_argument("--max-pages", type=int, default=400)
    a = ap.parse_args()
    ids = [norm(l) for l in open(a.entries, encoding="utf-8") if l.strip()]
    ids = [i for i in ids if i]
    print(f"入口 {len(ids)} 个", file=sys.stderr)
    pages = closure(ids, a.max_pages)
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(pages, fh, ensure_ascii=False, indent=1)
    ok = [p for p, m in pages.items() if not m.get("missing")]
    print(f"闭包共 {len(pages)} 页，成功 {len(ok)} 页 -> {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
