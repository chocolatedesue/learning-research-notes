#!/usr/bin/env python3
"""判断 markitdown 抽出的 Markdown 是否需要改走 OCR，输出可疑文件与首段预览。

为什么不能只看字节数：有些 PDF 的中文字体没有 ToUnicode 映射，抽出来是一串
`!"#$%&'()*+,-./` 之类的符号，字节数照样够，看着像成功。
判据（在本库 3 份样本上量过，见下），取两个特征：

  sym   —— ASCII 标点占比：乱码 0.226 / 中文正常 0.11 / 英文正常 0.038
  rare  —— `# $ % & * + < > @ [ ] ^ _ \\ | { } ~` 占比：乱码 0.074 / 正常 ≤0.042

命中 sym > 0.20 或 rare > 0.05 即标为可疑；可疑不等于一定乱码，所以同时打印首段
供人工确认——这是本步骤的检查点，不要跳过。

用法:
    python3 md_quality.py out/pdf/*.md
    python3 md_quality.py --json out/pdf/*.md
"""
import json
import re
import sys

SYM = re.compile(r"[!-/:-@\[-`{-~]")
RARE = re.compile(r"[#$%&*+<>@\[\]^_\\|{}~]")
CJK = re.compile(r"[\u4e00-\u9fff]")


def verdict(text: str, preview_len: int = 120) -> dict:
    dense = re.sub(r"\s+", "", text)
    n = len(dense)
    if n < 200:
        return {"suspect": True, "reason": f"仅 {n} 个非空白字符，基本没抽出内容",
                "preview": text[:preview_len]}
    sym = len(SYM.findall(dense)) / n
    rare = len(RARE.findall(dense)) / n
    cjk = len(CJK.findall(dense)) / n
    suspect = sym > 0.20 or rare > 0.05
    return {
        "suspect": suspect,
        "reason": (f"sym={sym:.3f} rare={rare:.3f} cjk={cjk:.3f}，"
                   + ("疑为字体缺 ToUnicode 映射，请换 OCR 工具" if suspect else "正常")),
        "sym": round(sym, 3), "rare": round(rare, 3), "cjk": round(cjk, 3),
        "chars": n, "preview": re.sub(r"\s+", " ", text)[:preview_len],
    }


def main():
    as_json = "--json" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    out = {}
    for p in paths:
        try:
            out[p] = verdict(open(p, encoding="utf-8", errors="ignore").read())
        except OSError as e:
            out[p] = {"suspect": True, "reason": f"读取失败: {e}", "preview": ""}
    if as_json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0
    bad = 0
    for p, r in out.items():
        flag = "OCR?" if r["suspect"] else " ok "
        print(f"[{flag}] {r['reason']:<70} {p}")
        if r["suspect"]:
            bad += 1
            print(f"         预览: {r.get('preview','')}")
    print(f"\n共 {len(out)} 份，其中 {bad} 份需人工确认/换 OCR")
    return 0


if __name__ == "__main__":
    sys.exit(main())
