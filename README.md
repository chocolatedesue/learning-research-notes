# 科研经验笔记

把 [pengsida/learning_research](https://github.com/pengsida/learning_research)（《本人的科研经验》，作者彭思达，浙江大学）
与它外链的 Notion 文档整理成的一个文档站，框架是 **MkDocs + Material for MkDocs**（与
[sing-box 的文档站](https://sing-box.sagernet.org/) 同款主题配置）。

站点入口：[index.html](https://chocolatedesue.github.io/learning-research-notes/)

## 内容归属

**正文版权归原作者彭思达所有。** 本仓库是非商业的个人学习镜像，仅做重新组织与排版，未改动原意；
每页顶部都标注了 Notion 原文出处。原作者若要求撤下，请提 issue，会立即删除。

作者开源这份文档的动机之一就是"希望对实验室以外的同学有所帮助"，本镜像据此保留公开访问。

## 仓库结构

| 分支 | 内容 |
|---|---|
| `gh-pages` | 构建产物，GitHub Pages 从这里发布 |
| `main` | MkDocs 源码：`mkdocs.yml` + `docs/` + 抓取脚本 |

## 重新构建

```bash
pip install mkdocs-material
# 或：uvx --from mkdocs-material mkdocs build
mkdocs build          # 产物在 site/
```

内容来源分两部分：仓库内的 Markdown 直接搬运；Notion 部分由 `notion_recursive.py` / `build_site.py`
通过公开分享接口递归抓取后转成 Markdown。
