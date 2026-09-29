#!/usr/bin/env python3
"""步骤 0：扫描 learning_research 仓库正文，抽出全部外链并按类型归好。

用法:
    python3 inventory_links.py repo/ -o inventory

产出:
    inventory.json  —— 机器读，供后续抓取脚本消费
    inventory.md    —— 人读，核对哪些入口漏了

分类: notion / pdf / image / video / web
"""
import argparse
import json
import os
import re
import sys

URL = re.compile(r"https?://[^\s\)\]<>\"'，。；、]+")
NOTION_ID = re.compile(r"([0-9a-fA-F]{32})")


def classify(u: str) -> str:
    low = u.lower()
    if "notion" in low:
        return "notion"
    if low.endswith(".pdf"):
        return "pdf"
    if low.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
        return "image"
    if "bilibili.com" in low or "youtube.com" in low or "youtu.be" in low:
        return "video"
    return "web"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", help="克隆下来的仓库目录")
    ap.add_argument("-o", "--out", default="inventory")
    a = ap.parse_args()

    buckets = {"notion": {}, "pdf": {}, "image": {}, "video": {}, "web": {}}
    scanned = []
    for root, _dirs, files in os.walk(a.repo):
        if ".git" in root.split(os.sep):
            continue
        for fn in files:
            if not (fn.endswith((".md", ".markdown")) or fn == "changelog"):
                continue
            path = os.path.join(root, fn)
            scanned.append(path)
            text = open(path, encoding="utf-8", errors="ignore").read()
            for u in URL.findall(text):
                u = u.rstrip(".,;。；、")
                kind = classify(u)
                if kind == "notion":
                    m = NOTION_ID.search(u)
                    if not m:
                        continue
                    pid = m.group(1).lower()
                    buckets["notion"].setdefault(pid, {"id": pid, "urls": [], "sources": []})
                    buckets["notion"][pid]["urls"].append(u)
                    buckets["notion"][pid]["sources"].append(path)
                else:
                    buckets[kind].setdefault(u, {"url": u, "sources": []})
                    buckets[kind][u]["sources"].append(path)

    out = {k: list(v.values()) for k, v in buckets.items()}
    out["_meta"] = {"scanned": scanned, "counts": {k: len(v) for k, v in out.items() if k != "_meta"}}
    with open(a.out + ".json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    lines = ["# 外链清单", "", f"扫描文件：{len(scanned)} 个", ""]
    labels = {"notion": "Notion 页面", "pdf": "PDF", "image": "图片", "video": "视频", "web": "其他站点"}
    for k in ("notion", "pdf", "image", "video", "web"):
        items = out[k]
        lines.append(f"## {labels[k]}（{len(items)}）")
        lines.append("")
        for it in items:
            if k == "notion":
                lines.append(f"- `{it['id']}`")
            else:
                lines.append(f"- {it['url']}")
        lines.append("")
    with open(a.out + ".md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(json.dumps(out["_meta"]["counts"], ensure_ascii=False))
    print(f"-> {a.out}.json / {a.out}.md", file=sys.stderr)


if __name__ == "__main__":
    main()
