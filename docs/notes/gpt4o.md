## gpt4o相关技术学习笔记

### gpt4o的动机和核心技术问题
原有的VLM model：强行把图像当成token，使用语言模型做生成。→ 没有充分设计图像生成。
gpt4o的VLM model：在LLM中引入更先进的图像生成技术来改进图像生成，实现text and image的unified modeling。
使用auto-regressive model做image generation的好处：拆解复杂的图像分布，理解图像细节。→ 这是diffusion model没有的能力。
核心问题：如何在auto-regressive model中同时构建text generator和image generator。
问题拆解：
1. 好的image tokenizer是怎样的？
1. 如何用auto-regressive model做image generation？
1. text和image在auto-regressive model中怎么做交互？
- **OpenAI的说法**
论文集合：[https://github.com/lxa9867/Awesome-Autoregressive-Visual-Generation](https://github.com/lxa9867/Awesome-Autoregressive-Visual-Generation)

---

### Autoregressive image generation的论文总结
大家在解决的问题：
1. 更好的图像生成质量。
1. 更好的图像理解能力。
1. 统一的模型。
大家遵循的技术范式是什么：
1. 使用tokenizer将text、image转为tokens。
1. 基于GPT-based transformer的框架，使用attention layers处理tokens。
1. 使用classification head或者diffusion head输出text、image，即使用discrete tokens或者continuous tokens。
重要的components：
1. Tokenizer
1. 自回归框架
1. 具体的attention设计
1. Output head
1. 生成方式
1. 训练策略
大家在哪些模块上做研究：
1. 应该用什么tokenizer？→ 得到的visual tokens应该有什么样的性质？
1. 如何消除understanding和generation的gap？
1. 如何提升understanding和generation的性能？
1. 如何把visual tokens变得和text一样compact？
- **必要性**
1. 应该使用什么attention modules？
1. 应该使用什么生成方式？→ auto-regressive generation怎么充分考虑图片在spatial smoothness上的特性，block-wise and coarse-to-fine是否就够了？
1. 应该使用什么decoder？
已有的tokenizer：
1. Discrete tokenizer：VQ-VAE、RQ-VAE。
1. Continuous tokenizer：
1. VAE → 常用于Image generation。
1. SigLIP → 常用于Image understanding。
1. Encoder + DiT Decoder。
1. TiTok → 将2D image转为1D token sequence。
1. 使用representation learning的方法，将tokenizer提升为semantic tokenizer。→ OpenAI选用。
已有的attention modules：
1. Causal attention
1. Bidirectional attention
已有的生成方式：
1. 逐步的生成数量：
1. Next-token prediction
1. Block prediction
1. 生成顺序：
1. Raster order
1. Random order
1. Coarse-to-fine地生成：Next-scale prediction、fractal generation。
已有的decoder：
1. Classification head + VQ-VAE。
1. Diffusion head + VAE。

---

### Image tokenization的论文总结
大家在解决的问题：
1. 如何实现understanding和generation的统一？让tokens在understanding和generation的任务上一样好用。→ 重点是让tokens包含高层级语义。
1. tokenization和generation的行为怎么保持一致？→ 比如VQ或VAE是grid tokenization，而next-token prediction的ar model是1D sequential generation，这显然存在gap。
1. 如何降低tokens的数量？如何实现语义层级的压缩，达到像text一样的compact效果。 → 主流的VQ或VAE方案仅仅做了低语义层级上的压缩。
1. 现有方法中，image reconstruction效果越好，image generation效果会变差。怎么解决？→ 因为image reconstruction要求更大的codebook或者更多的image tokens。
有哪些技术范式：
1. 向Text tokens看齐，将Image转为1D token sequence。→ 使用query tokens和ViT做压缩。
1. 对1D token sequence做各种约束：nested dropout、nested CFG、causal attention masking。
1. 对Visual tokens做约束
1. 使用Vision foundation model的feature做约束。
1. 使用Text tokenizer得到的text tokens做约束。
1. 使用Diffusion decoder作为de-tokenizer，从而只需使用diffusion loss，能摒弃L1 loss、LPIPS loss和GAN loss。

---

### Image tokenization的论文整理
#### 2024.06，An Image is Worth 32 Tokens for Reconstruction and Generation
想解决的问题：VQ-VAE处理得到的tokens存在the inherent redundancies present in images。
核心思想：将Image转为1D latent sequence。
具体做法：
1. Encoder：将image patches和latent tokens喂给ViT，期望latent tokens能学到image patches的信息。
1. Decoder：将latent tokens和mask patches喂给ViT，输出image patches。

---

#### 2024.10，LARP: Tokenizing Videos with a Learned Autoregressive Generative Prior
具体的做法：
1. Tokenizer：AR tokenizer。

---

#### 2024.10，ϵ-VAE: DENOISING AS VISUAL DECODING
想解决的问题：没讲清楚。
具体做法：将diffusion model作为image decoder。

---

#### 2024.10，Stabilize the Latent Space for Image Autoregressive Modeling: A Unified Perspective
想解决的问题：为什么基于VQ或VAE得到的tokens，使用AR model做image generation效果不好？
具体做法：Perform K-Means clustering on the feature space of discriminative SSL models to obtain discrete tokens.

---

#### 2024.12，Divot: Diffusion Powers Video Tokenizer for Comprehension and Generation
想解决的问题：没讲清楚想解决啥问题。
具体做法：使用diffusion model作为video decoder，用于video tokenizer的学习。
感觉这篇论文没想清楚自己想解决的问题，以及技术优势。整个技术框架有点乱。

---

#### 2024.12，Tokenflow: Unified image tokenizer for multimodal understanding and generation
想解决什么问题：消除gap between multimodal understanding and generation。
1. Tokenizer：构建了Dual codebook的VQ-VAE。
1. 自回归框架

---

#### 2024.12，Language-Guided Image Tokenization for Generation
想解决的问题：提升compression rate。
