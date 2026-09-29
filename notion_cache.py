#!/usr/bin/env python3
"""带磁盘缓存的 Notion 块读取。反复重建站点时不必重抓，也天然绕开限速。

用法:
    from notion_cache import cached_blocks, dashed
    bl = cached_blocks(pid)        # pid 可带或不带连字符
缓存目录默认 ./cache/notion/<pid>.json，可用 NOTION_CACHE 覆盖。
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from notion_recursive import fetch_blocks, dashed  # noqa: E402

CACHE = os.environ.get("NOTION_CACHE", os.path.join(HERE, "cache", "notion"))
DELAY = float(os.environ.get("NOTION_DELAY", "1.2"))


def path_of(pid: str) -> str:
    return os.path.join(CACHE, dashed(pid).replace("-", "").lower() + ".json")


def cached_blocks(pid: str, refresh: bool = False) -> dict:
    p = path_of(pid)
    if not refresh and os.path.exists(p):
        try:
            return json.load(open(p, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    bl = fetch_blocks(dashed(pid))
    if bl:
        os.makedirs(CACHE, exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(bl, fh, ensure_ascii=False)
        time.sleep(DELAY)
    return bl
