> 原文：[Notion 原文](https://pengsida.notion.site/1713fe292ff1808eb33be93ea2d79ad9) · 作者可能已更新，以原文为准。

## 博士生的楷模：Sebastian Starke

> 文档汇总（GitHub Repo）：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)
这两天读了Sebastian Starke博士期间在Character Control上的系列论文，学习了很多（[论文笔记](../others/phase.md)）。我不认识Sebastian Starke，但仅阅读他的系列论文，就深感佩服，有很多感悟，为了日后温习反思，在此记录自己的想法。
[Sebastian Starke](https://github.com/sebastianstarke)博士在Taku Komura组就读，他博士期间每年在SIGGRAPH上发表一篇文章，通过5年的时间搭建出一套接近商业化的Character Control系统，令人惊叹，极大地推动了产业界游戏动作系统的可用水平。在GitHub上，他的[AI4Animation](https://github.com/sebastianstarke/AI4Animation)收获7.4k stars。在学术上，他每一篇SIGGRAPH论文都逐步攻克更难的业界问题，朝着一个方向往深了研究，其博士期间的最后一篇论文DeepPhase也终于斩获SIGGRAPH最佳论文，实至名归。
通过阅读Sebastian Starke博士的系列论文，能看出他的研究风格：
1. **有非常明确且长期的目标，问题驱动式科研。**他的论文始终在解决Character Control系统中的各种问题，从早期的简单周期性运动控制，到后面的复杂运动控制，征服了Character Control方向的一座座高山。
1. **总能找到有价值的问题。**可能受益于Taku组的长期积累，Sebastian的论文总能找到Character Control中优先级最高的问题，而不是把精力花在一些无关痛痒或暂时不重要的问题上。
1. **不畏难地填坑，挑战“没答案”的问题。**Sebastian猛就猛在敢去攻克难题、不断填坑。Character Control方向的一大重要问题是目标动作的复杂度。他师兄Daniel Holden的PFNN解决了简单周期运动，他的Local Motion Phase进一步提升，解决了组合式运动，然后又通过DeepPhase（SIGGRAPH最佳论文）解决了复杂非周期运动，几乎解决了动作复杂性的这一问题。
相比于“目标动作复杂度”，Character Control方向有其他更好发论文的问题，比如Multi-modal Control。Sebastian没有因为它们更好发论文而去解决这些问题，而是始终把精力放在最重要的问题上，这样的问题都没有well-established solution。他不畏难地不断填坑，是他能推动产业进步的关键。
1. **极强的技术能力。**前面3个研究风格让Sebastian把精力集中在解决最重要的问题上，但要能解决问题，靠的是Sebastian本人极强的技术能力，包括广阔的技术积累、深入的技术思考、硬核的工程能力。Sebastian应该把Character Control相关的技术栈都摸了遍，包括Motion Capture、Fitting、Animation、Deep Learning、Unity等。
1. **尝鲜新技术。**Sebastian的论文里总会尝试那一时期的前沿技术，比如DeepPhase中探索了Representation Learning在motion中的应用。我相信，如果他只是沿着Local Motion Phase的技术路径去解决复杂非周期运动的控制问题，不太可能会有这么大的效果提升。
当我仔细学习、总结Sebastian Starke的研究风格以后，我反思了自己读博期间犯过的错误。这些错误在我带的一些学生中偶尔也会出现，导致他们的聪明才智没有用在正确的地方。具体的错误如下：
1. **缺少长期目标，没有专注解决一个方向上的问题。**我读博的时候，前三年换了三个Topics：Object Pose Estimation、Instance Segmentation、Dynamic 3D Reconstruction，所幸最后在Dynamic 3D Reconstruction方向稳定下来。如果我一开始专注在Object Pose Estimation方向，我的科研会更顺利，能在Object Pose领域做出更好的工作，也能较早地有一个自己的标签。
1. **倾向于解决容易的问题，没有去寻找最有价值的问题。**我博士三年级的时候，当时觉得Dynamic Human Surface Reconstruction这问题好解决、好发文章，花了半年做了Animatable SDF这个Project。现在回想起来，这半年完全是浪费，没有学习新知识。如果当时能花时间解决有价值的问题，如提升三维人体渲染质量，我的技术水平能有更多提升，也更有机会在Dynamic 3D Reconstruction这个方向有更大的影响力。
1. **缺少把问题解决到99%程度的意识。**我做完Neural Body以后，把渲染质量提升到了能看的程度。当时追求Fancy，紧接着去解决Animatable Human的问题。那两年经常有业界的人和我提起动态人体渲染质量亟需提升的事情，可惜我当时没去解决。现在回想起来，我在动态人体重建领域只是发了几篇论文，但啥问题都没真正解决，成了“只会发论文、对产业没实际贡献”的人。
1. **把时间浪费在解决“有答案”的问题。**我博士二年级做的Deep Snake，其想解决的问题已经被之前的论文Curve-GCN较好地解决，我只是在其基础上修修补补。现在想起很没意思，其实我当时做得也是充满自我怀疑。这样的Project只能是在消耗人的科研热情，只有坏处，没有好处。
1. **论文阅读面窄，技术积累少。**我自己没有这方面的问题，但见到有些同学没有广泛阅读论文的习惯，甚是可惜。
1. **没有尝鲜新技术。**读博期间，有一些新技术兴起，比如Transformer、Diffusion Model、Video Model。我当时的思维很怪，总觉得新兴技术就是炒作，简直是大清思维，把很多时间花在原有技术框架的小修小改上。如果当时能把新兴技术当作一种希望，看看能否解决自己领域内的一些难题，应该能做出一些更好的工作。其实我的PVNet、Neural Body是用好了新兴技术的典例，但是我以前完全没意识到它们为什么强，能做出这两个工作全靠周老师指导得好，给了我好的问题，坚决让我不要用旧的技术方案。
写下这篇文章，总结了Sebastian成功的地方，也反思了自己很多犯过的错误。希望自己以后能更积极地向大佬们学习，把精力放在解决重要的问题上，总是能走在尝试新技术的第一线。
文章日期：2025年1月4日
