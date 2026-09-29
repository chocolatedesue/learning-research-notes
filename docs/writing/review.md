> 原文：[Notion 原文](https://pengsida.notion.site/eed9ed1e9dc44a1c9437b114e6d5d9fd) · 作者可能已更新，以原文为准。

## 怎么审论文

> 文档汇总（GitHub Repo）：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)
仔细检查论⽂是否存在被拒的因素。逐条过一遍就知道这篇论文是否应该被拒了。
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/91553421-1cdf-46aa-8a87-8e898edb2e54/Untitled.png)
论文被接收的原因。论文需要做到以下三点：
1. contribution足够（需要包含其中的几点：Novel task, Novel pipeline, Novel pipeline module, Novel design choices, New experimental findings, New insights）
1. 实验效果比之前的方法好。
1. ablation studies和comparison experiments充分。
论文被拒的原因。常见的被拒的原因：
1. contribution不够（论文没有给读者带来新的知识，一般会包含其中的几点：想解决的failure cases很常见；提出的技术已经被well-explored了，该技术带来的performance improvement是可预见的/well-known的）
1. 写作不清楚（缺少技术细节，不可复现；某个方法模块缺少motivation）
1. 实验效果不够好（只比之前的方法好了一点；虽然比之前的方法效果好，但效果仍然不够好）
1. 实验测试不充分（缺少ablation studies；缺少重要的baselines；缺少重要的evaluation metric；数据太简单，无法证明方法是否真的work）
1. 方法设计有问题（实验的setting不实际；方法存在技术缺陷，看起来不合理；方法不鲁棒，需要每个场景上调超参；新的方法设计在带来benefit的同时，引入了更强的limitation，导致新方法的收益为负）

### 未归位的内容（未挂在块树上，兜底列出）

1. Adversarial writing：自己review自己的论文，考虑reviewer可能会问的所有问题，并一一解决。
