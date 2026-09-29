#!/usr/bin/env python3
"""递归抓取 pengsida.notion.site 公开页面，输出 Markdown。

用法:
    python3 notion_recursive.py <page-id-or-url> [<page-id-or-url> ...] -o out.md

原理: 公开分享的 Notion 站点渲染时会把整棵块树发给浏览器，
      POST /api/v3/loadCachedPageChunkV2 就是那条通道，匿名可用。
注意: 该接口无常量文档，且连续快请求会返回空 recordMap —— 本脚本每次调用间隔 1.5s，
      遇到空结果重试 3 次。失败页面记录到 stderr，不静默丢。
"""
import argparse
import json
import re
import sys
import time
import urllib.request

API = "https://pengsida.notion.site/api/v3/loadCachedPageChunkV2"
DELAY = 1.5
RETRY = 3


def dashed(x: str) -> str:
    x = re.sub(r"[^0-9a-fA-F]", "", x)
    return f"{x[0:8]}-{x[8:12]}-{x[12:16]}-{x[16:20]}-{x[20:32]}"


def fetch_blocks(pid: str, max_chunk: int = 20) -> dict:
    """取一页的全部块（自动翻 cursor）。空 recordMap 视为限速，重试。"""
    for attempt in range(RETRY):
        out, cursor, chunk = {}, {"stack": []}, 0
        try:
            while chunk < max_chunk:
                body = json.dumps({
                    "page": {"id": pid}, "limit": 100, "cursor": cursor,
                    "chunkNumber": chunk, "verticalColumns": False,
                }).encode()
                req = urllib.request.Request(
                    API, data=body,
                    headers={"Content-Type": "application/json",
                             "User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=30) as r:
                    rm = json.load(r).get("recordMap", {})
                bl = rm.get("block") or {}
                if not bl:
                    break
                for k, v in bl.items():
                    val = (v.get("value") or {}).get("value") or v.get("value") or {}
                    if val:
                        out[k] = val
                cur = rm.get("cursors") or []
                if not cur:
                    break
                cursor, chunk = cur[0], chunk + 1
        except Exception as e:  # noqa: BLE001
            print(f"  ! {pid[:8]} 第 {attempt+1} 次请求异常: {e}", file=sys.stderr)
            out = {}
        if out:
            if attempt:
                print(f"  · {pid[:8]} 第 {attempt+1} 次成功", file=sys.stderr)
            return out
        time.sleep(2 * (attempt + 1))
    return {}


def rich_text(props: dict, key: str) -> str:
    segs = props.get(key)
    if not isinstance(segs, list):
        return ""
    parts = []
    for seg in segs:
        if isinstance(seg, list) and seg and isinstance(seg[0], str):
            parts.append(seg[0])
    return "".join(parts)


def title_of(v: dict) -> str:
    return rich_text(v.get("properties") or {}, "title").strip()


def render(pid: str, v: dict) -> str:
    """把一个块渲染成 Markdown 行（只处理最常用的几类）。"""
    t = v.get("type")
    p = v.get("properties") or {}
    txt = rich_text(p, "title")
    if t == "header":
        return f"# {txt}"
    if t == "sub_header":
        return f"## {txt}"
    if t == "sub_sub_header":
        return f"### {txt}"
    if t in ("bulleted_list", "toggle"):
        return f"- {txt}"
    if t == "numbered_list":
        return f"1. {txt}"
    if t == "quote":
        return f"> {txt}"
    if t == "code":
        return f"```\n{txt}\n```"
    if t == "image":
        src = rich_text(p, "source") or rich_text(p, "caption")
        return f"![image]({src})"
    return txt


def walk(pid, acc, seen, depth, max_depth):
    if pid in seen:
        return
    seen.add(pid)
    bl = fetch_blocks(pid)
    time.sleep(DELAY)
    if not bl:
        print(f"  ! {pid[:8]} 抓取失败（限速或非公开）", file=sys.stderr)
        return
    self_v = bl.get(pid, {})
    title = title_of(self_v) or "(untitled)"
    acc.append(f"{'#' * min(2 + depth, 6)} {title}\n")
    body, children = [], []
    for bid, v in bl.items():
        if bid == pid:
            continue
        if v.get("type") == "page":
            ct = title_of(v)
            if ct:
                children.append((bid, ct))
            continue
        line = render(bid, v)
        if line:
            body.append(line)
    acc.append("\n".join(body) + "\n")
    for cid, ctitle in children:
        print(f"  {'  ' * depth}-> {ctitle[:50]}", file=sys.stderr)
        if depth + 1 > max_depth:
            acc.append(f"{'#' * min(3 + depth, 6)} {ctitle} （已达深度上限，未展开）\n")
            continue
        walk(cid, acc, seen, depth + 1, max_depth)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pages", nargs="+", help="页面 ID 或 notion.site URL")
    ap.add_argument("-o", "--out", default="notion_dump.md")
    ap.add_argument("--max-depth", type=int, default=6)
    a = ap.parse_args()

    ids = []
    for p in a.pages:
        m = re.search(r"([0-9a-fA-F]{32})", p)
        if not m:
            sys.exit(f"无法从 {p!r} 里解析页面 ID")
        ids.append(dashed(m.group(1)))

    acc, seen = [], set()
    for pid in ids:
        print(f"[page] {pid}", file=sys.stderr)
        walk(pid, acc, seen, 0, a.max_depth)
        print("---", file=sys.stderr)

    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(acc))
    print(f"抓到 {len(seen)} 页 -> {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
