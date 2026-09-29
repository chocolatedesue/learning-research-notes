> 原文：[Notion 原文](https://pengsida.notion.site/9533b857615345108d7624b6e76a2ba3) · 作者可能已更新，以原文为准。

## 3D LLM的pipeline总结

[https://github.com/ActiveVisionLab/Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D)
[https://aicarrier.feishu.cn/wiki/GvibwrWumiYVxYk3Ik5c7Yd3nSb](https://aicarrier.feishu.cn/wiki/GvibwrWumiYVxYk3Ik5c7Yd3nSb)
pipeline整理：
1. 大部分论文的pipeline：Encoder → Projector → LLM
1. Encoder：对point clouds提取特征
1. Projector：使用projector将特征投影到LLM所需的point token
1. LLM：使用LLM预测token
1. Encoder → LLM
1. An Embodied Generalist Agent in 3D World
1. Building object set → LLM
1. ConceptGraphs
Point Encoder的variants
- **将2D image feature反投影到3D point clouds上，获得3D point clouds的feature**
- **Object-level encoder: I2P-MAE**
- **Object-level encoder: Recon++**
- **Object-level encoder: Point-BERT**
- **Object-level encoder: Ulip2 and Uni3D**
- **Object-level encoder: Vanilla transformer structurally equivalent to ViT + 2D model初始化**
- **Scene-level encoder: EPCL**
- **Scene-level encoder: Masked transformer encoder**
- **Scene-level encoder: PointNet++加上spatial transformer**
- **Scene-level encoder: Multi-view transformer + Fusion transformer**
Projector的variants（用于关联Pre-trained vision models和Pre-trained LLMs，efficiently project these features in the pre-trained textual embedding space, enabling effective interpretation of 3D visual information）
- **Perceiver: General perception with iterative attention**
- **QFormers：做aggregation，降低计算量**
- **An MLP**

| 论文 | 论文想解决的问题 | 论文核心的贡献 |
|---|---|---|
| **号称第一个做3D LLM的工作** |   |   |
| 3D-LLM: Injecting the 3D World into Large Language Models | LLM缺少3D的模态 | inject the 3D world into large language models |
| PointLLM: Empowering Large Language Models to Understand Point Clouds | LLM缺少3D的模态 | 将3D information注入到LLM中 |
| Chat-3D: Data-efficiently Tuning Large Language Model for Universal Dialogue of 3D Scenes | 已有3D understanding的工作are limited to specific downstream tasks | align 3D representations into the feature space of LLMs |
|   |   |   |
| **提升3D LLM效果的工作** |   |   |
| **在Point Encoder方面有贡献的论文** |   |   |
| ConceptFusion: Open-set Multimodal 3D Mapping | Most existing approaches that integrate semantic concepts with 3D maps largely remain confined to the closed-set setting | leverages the open-set capabilities of today’s foundation models  实现了open-set grounding |
| ShapeLLM: Universal 3D Object Understanding for Embodied Interaction |   | 提升了point encoder，将RECON拓展为RECON++ |
| Unified Scene Representation and Reconstruction for 3D Large Language Models | 2D-to-3D point feature的做法缺少 3D point-to-point connections | 觉得同时做3D understanding和reconstruction很重要 |
| Scene-LLM: Extending Language Model for 3D Visual Understanding and Reasoning |   | 整合了scene-level 3D information和egocentric 3D information |
| 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment |   | A, a pre-trained Transformer for 3D Vision and Text Alignm |
| [Chat-3D v2: Bridging 3D Scene and Large Language Models with Object Identifiers](https://arxiv.org/pdf/2312.08168.pdf) | current models are constrained to addressing object-centric tasks, where each question-answer pair focuses solely on an individual object  只考虑单个物体 | learning an attribute-aware token and a relation-aware token for each object. These tokens capture the object’s attributes and spatial relationships with surrounding objects in the 3D scene |
|   |   |   |
| **提升Point Cloud和text alignment的效果** |   |   |
| [Point-Bind & Point-LLM: Aligning Point Cloud with Multi-modality for 3D Understanding, Generation, and Instruction Following](https://arxiv.org/pdf/2309.00615.pdf) |   | construct a joint embedding space between 3D and multi-modalities |
| [JM3D & JM3D-LLM: Elevating 3D Representation with Joint Multi-modal Cues](https://arxiv.org/pdf/2310.09503v2.pdf) | straightforwardly resorted to transferring 2D alignment strategies to the 3D domai会遇到3个问题： 1. 信息损失 2. Insufficient Synergy 3. Underutilization | the Structured Multi-modal Organizer (SMO) and the Joint Multi-modal Alignment (JMA) |
| [GPT4Point: A Unified Framework for Point-Language Understanding and Generation](https://arxiv.org/pdf/2312.02980.pdf) | 之前方法对3D world的understanding很deficient | a Bert-based Point-QFormer for point-text feature alignment |
|   |   |   |
| **降低3D LLM的训练成本** |   |   |
| MiniGPT-3D: Efficiently Aligning 3D Point Clouds with Large Language Models using 2D Priors | 已有工作需要太大计算资源：directly aligning point clouds with LLM requires expensive training costs | align 3D point clouds with LLMs using 2D priors from 2D-LLMs  利用2D-LLMs的预训练模型 |
| [Uni3D: Exploring Unified 3D Representation at Scale](https://arxiv.org/abs/2310.06773) |   | uses a 2D initialized ViT end-to-end pretrained to align the 3D point cloud features with the image-text aligned features  利用2D-LLMs的预训练模型 |
| Any2Points | 将2D feature unprotect到3D point cloud方法存在两个问题：loss of spatial geometries and high computation cost. | Given a frozen transformer from any source modality, we propose a 3D-to-any (1D or 2D) virtual projection strategy that correlates the input 3D points to the original 1D or 2D positions within the source modality  提出了3D-to-any virtual projection。 |
|   |   |   |
| **设计新的场景表示** |   |   |
| [ConceptGraphs](https://concept-graphs.github.io/) | 已有工作做per-point feature vector，难以scale up | 设计了新的scene representation  an open-vocabulary graph-structured representation for 3D scenes |
|   |   |   |
| **提升将3D information注入到LLM的有效性** |   |   |
| 3DMIT: 3D MULTI-MODAL INSTRUCTION TUNING FOR SCENE UNDERSTANDING |   | introduce a novel and efficient prompt tuning paradigm  同时做了一个数据集 |
|   |   |   |
| 同时做好Perceiving, Grounding, Reasoning, Planning |   |   |
| LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning | 原先的工作将2D feature反投影到3D上，效果不好 | takes point cloud as direct input |
| An Embodied Generalist Agent in 3D World |   | 主要贡献是个数据集。  Design an LLM-assisted pipeline to produce high-quality 3D VL data |
|   |   |   |
| **将LLM拓展到Multisensory信号** |   |   |
| MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World |   | 主要贡献是个数据集。 |
|   |   |   |
| **考虑了3D任务的特殊性** |   |   |
| [ViewRefer: Grasp the Multi-view Knowledge for 3D Visual Grounding](https://arxiv.org/pdf/2303.16894.pdf) | 已有工作没有考虑当前所在视角的信息：neglect the view cues embedded in the text modality and fail to weigh the relative importance of different views | a multi-view framework for 3D visual grounding exploring how to grasp the view knowledge from both text and 3D modalities |

- **相关论文**
