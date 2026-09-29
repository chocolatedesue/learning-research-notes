> 原文：[Notion 原文](https://pengsida.notion.site/d9b48545884a47799fc5829cad8af2b6) · 作者可能已更新，以原文为准。

## Ross Girshick的talk笔记

- 附件：Ross_Girshick的Talk.pdf —— [在原页查看](https://pengsida.notion.site/d9b48545884a47799fc5829cad8af2b6)（原页附件，本站未镜像）
NLP部分的Take away message：
1. Ross认为NLP里的Parser是fake task。
1. Ross认为NLP里的real task是text generation。
1. NLP中之所以能成功，还有额外的原因：
1. Massive high-quality data
1. Supervised training
1. Test task = training task，NLP里text generation确实是最重要的目标了
CV部分的Take away message：
1. CV面临的问题：
1. Image/Video generation虽然重要，但不是CV领域最重要的任务
1. 高质量的训练数据不多
1. Generation task难以说是感知/决策任务的good proxy task
1. Ross认为CV里的Real task是recognition
> 为什么有这样的结论，这是从CV的真正应用得出的结论。
1. 对于弱视的人，CV要做的是Open-ended visual QA about the real world
2. 对于robot，CV要做的是“cook me dinner”
3. 对于internet agent，CV要做的是“shop for me”
1. 我们需要思考CV里面哪些任务是“NLP领域的Parser”、是fake task
> **思考的方法论，**Real task不一定需要哪些intermediate tasks，只是我们人为地认为他们需要：
1. classification, detection, segmentation
2. 3D reconstruction
1. Ross认为CV里面最重要的科学问题（the most scientifically important direction）：基于人类日常接触的数据，设计并训练人工智能模型（Algorithms that learn with human-like data constraints）
> 人类日常接触的数据的特征：
1. Ego-centric video
2. Limited embodied control
3. Observations have very different statistics cf. web data
4. Long term
Ross科研经验上的分享，虽然现在来看detection这个任务是错的，但他非常有收获
> 抱着尝鲜、获得新知识的姿态来探索有意思的科学问题、技术问题，会非常fruitful。
（Trying to solve a scientifically interesting problem with no other motivation than gaining knowledge can be extremely fruitful）

我的个人理解：如果整天只想着让一个事情work，导致只敢用一些well established techniques，这样在研究上反而失去意义了。
