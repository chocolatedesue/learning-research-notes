> 原文：[Notion 原文](https://pengsida.notion.site/092795ee24fb408fb0eb340186949c78) · 作者可能已更新，以原文为准。

## 具身智能的pipeline总结

具身智能的pipeline（服务于最终的决策）：
- **根据observations做决策**
- **根据之前的actions和observations做决策**
- **根据observations和goal imagination做决策**
- **用一些策略让representation中包含future information，然后根据learned representation和observations做决策**
其他的相关工作：
- **主要做3D grounding的工作。大多数embodied AI的工作建立在强大的3D LLM的基础上**
- **称为world model，但其实只是做future prediction，没有和planning接起来的工作**
相关论文：
1. [https://worldmodels.github.io/](https://worldmodels.github.io/)
1. 3D VLA
1. genie
1. palm-e
1. rt-2
1. copa
1. vlp
1. [https://mimic-play.github.io/](https://mimic-play.github.io/)
1. Diffusion Policy
1. GenFlow
1. VPDD
1. [ManiGaussian](https://arxiv.org/abs/2403.08321)
1. [3D-LLM](https://github.com/UMass-Foundation-Model/3D-LLM)
1. COMBO
1. An Embodied Generalist Agent in 3D World
1. ConceptGraphs
1. VoxPoser
1. Generalized Predictive Model for Autonomous Driving
1. WorldGPT: A Sora-Inspired Video AI Agent as Rich World Models from Text and Image Inputs
1. DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation
1. Learning and Leveraging World Models in Visual Representation Learning
1. Humanoid Locomotion as Next Token Prediction
1. Slot Structured World Models
1. WorldDreamer: Towards General World Models for Video Generation via Predicting Masked Tokens
1. EgoGen: An Egocentric Synthetic Data Generator
1. MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World
1. [Language Models Meet World Models](https://neurips.cc/virtual/2023/tutorial/73952)
1. ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation
1. WoVoGen: World Volume-aware Diffusion for Controllable Multi-camera Driving Scene Generation
1. Towards Learning a Generalist Model for Embodied Navigation
1. LanGWM: Language Grounded World Model
1. OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving
1. V-JEPA
1. world model on million-length video
