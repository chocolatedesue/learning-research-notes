> 出处：[原文链接](https://pengsida.notion.site/c1a22465a0fa4b15a12985223916048e)

## 论文写作模板

> 文档汇总（GitHub Repo）：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)
将本写作模板转为Vibe Writing Skills的仓库：[https://github.com/Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- 论文写作规划图
> 💡 
> 💡 段落写作原则：
1. 一段文字只讲一个Message，并表达清楚，不要把几个Messages杂糅在一起。
2. 一段文字开头第一句就要让读者知道这段在说什么。（金字塔原理，塔尖是想传达的观点，塔基是支撑观点的逻辑论据）

英语写作的基本思路：先列写作思路，然后细化每一部分的思路，再写具体的英语句子。注意段落、句子之间的flow。（flow的概念具体看这个[文档](../writing/expert-experience.md)。）

**写论文一定要“如切如磋，如琢如磨”，反复品味，揣摩读者是否读得懂。
“自我评阅论文写作是否清楚”的能力非常重要。知道有问题才能知道要改。**
- 写论文的关键
- 如何判断论文段落的写作是否清楚（**重要**）
[如何使用copilot和gpt辅助英语写作](https://pengsida.notion.site/1143fe292ff180feb5d0fe76d05e085b)（**重要，**LLM时代的基本技能）
[如何改一篇论文的写作](https://pengsida.notion.site/1293fe292ff180bfa5deeed526821d78)
> 💡 什么时候要开始写论文：一般情况下，至少要在**截稿时间一个月前**就开始写论文。
- 论文写作的关键时间点（从截稿时间一个月前开始计划）
- 论文标题
- Abstract
- Introduction
- Method
- Implementation details
- 论文画图
论文收获好review的关键：**把论文做得漂亮、美观，让人第一印象觉得这篇论文很高级。**
怎么让论文第一眼看起来很漂亮、高级：
1. 好看的teaser figure、pipeline figure。
2. 好看的表格和结果图。
3. 整齐的排版。
- 论文画表
- Experiments
- Related work
- Conclusion
- 怎么改论文
> 💡 **需要注意论文中所有的claim（特别是abstract和introduction里的claim），需要不犯错，也得有实验support。不然一些reviewer会直接以此拒掉论文。**
**保证论文质量的非常重要的方式：追求完美主义。**
1. Adversarial writing：自己review自己的论文，考虑reviewer可能会问的所有问题，并一一解决。
1. 请自己的导师给自己的论文提修改意见，越多越好（相当于reviewer提前review论文了。导师给出的修改意见越多，自己如果fix了，那么reviewer能提出的问题就越少）。

- [高水平科研工作者的写作经验](../writing/expert-experience.md)
### 如何使用copilot和gpt辅助英语写作

> 文档汇总（GitHub Repo）：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)
使用copilot和gpt辅助写Introduction的完整录屏：[https://www.bilibili.com/video/BV1jdxDeZEtq](https://www.bilibili.com/video/BV1jdxDeZEtq)
> 💡 
- 什么是写作思路
- 怎么列论文的写作思路
如何借助copilot和gpt辅助**英语段落**写作（[**完整视频**](https://www.bilibili.com/video/BV1PP4Le6EcW)）。基本流程：
1. 列出整个Introduction的基本思路
1. 进行逐段落的写作
如何借助copilot和gpt辅助**英语句子**写作（[**完整视频**](https://www.bilibili.com/video/BV1pkxDeqE1t)）。基本流程：
1. 初步列出一句话的思路
1. 根据这句话的思路，借助copilot辅助写作
1. copilot给出来的词汇不一定准确，需要借助gpt润色
1. 基于copilot和gpt给出的英语句子，自己再润色一次
1. 在句子写作的过程中，refine句子的写作思路
该技巧核心：先列清楚写作思路，理清楚要表达的内容，再用AI辅助英语写作。
写作思路要细化到知道每一句话写什么内容。
- 例子
1. 初步列出段落中每一句话的思路
1. 根据每句话的思路，借助copilot辅助写作
1. 在逐句写作过程中，refine段落的写作思路（**段落思路清晰的关键**）
- 例子
- 例子
- 例子
- 例子
- 例子
1. 做法1：以中英混合的方式，直接让其改进英语句子（**好用**）
1. 做法2：询问单词
- 例子
- 例子
- 例子

#### 写作思路典例

### **Introduction**
#### **段落粒度的写作思路**
1. 要解决的问题：场景重建 -> colmap效果很好，具体方法 -> colmap在地面、墙面这些无纹理区域效果不好，具体原因。
2. 传统方法：用plane帮助场景重建 -> 流程复杂，很多要调的参数 -> plane效果不好，重建质量不好。
3. 最近的方法：nerf、volsdf、neus在物体重建上效果很好 -> experiments show that 他们在室内无纹理区域效果不好 -> 大片无纹理区域存在很多可以解释的几何。
4. 我们的方法：用语义帮助重建，并且在重建的同时优化语义信息 -> Specifically, 检测地面和墙面，让他们符合语义性质 -> 假设曼哈顿结构，地面和墙面上的表面点normal要符合相应的性质。墙面的normal是优化出来的。-> 考虑到分割可能不准的问题，我们定义了semantic mlp。-> 利用multi-view consistency提升semantic segmentation的准确性。同时用几何的loss优化分割的probability。
5. Experiments
#### 句子粒度的写作思路
**要解决的问题**
1. Reconstructing 3D scenes from multi-view images is a cornerstone of many applications such as augmented reality, robotics, and autonomous driving.
2. Given input images, traditional methods generally estimate the depth map for each image based on the multi-view stereo and then fuse estimated depth maps into 3D geometries.
3. Although these methods achieve impressive reconstruction results, they have difficulty in handling low-textured regions such as floors and walls of indoor scenes due to unreliable matching in these regions.
**传统方法利用planar prior来提升效果**
1. To overcome this problem, some methods utilize the planar prior to help reconstruction.
2. They 怎么用planar prior的
3. plane怎么建模：triangulation \cite{planar prior}, superpixel \cite{tapa}, or learning-based plane segmentation methods \cite{}.
4. Although these methods improve the performance, when depth estimation or plane segmentation is inaccurate, they tend to perform poorly.
**最近的方法**
1. Recently, \cite{SRN, NeRF, IDR} represent 3D scenes as implicit neural representations and learn the representations from images with differentiable renderers.
2. IDR \cite{} uses a signed distance field to represent the scene and renders it into images based on the differentiable surface rendering. -> Although it produces high-quality reconstruction results, it tends to fail in complex scenes, as illustrated in \cite{volsdf, neus}. -> A reason is that the surface rendering only enables the gradient back-propagation on the surface point, which is prone to local optima.
3. To solve this problem, \cite{unsurf, volsdf, neus} propose to render implicit surfaces with volume rendering techniques, which produce gradient signals on multiple points along camera rays. -> This enables them to handle complex scenes without the additional mask supervision.
4. However, they still have poor performance in low-textured planar regions, as demonstrated by our experiments in Section~\ref{}.
5. This is because that there are many possible 3D representations that produce the same observed images, especially in low-textured planar regions.
**我们的方法**
1. In this paper, we propose a novel implicit neural representation that encodes geometric and semantic information for 3D reconstruction of indoor scenes.
2. Our innovation is utilizing semantic properties of planar regions to resolve ambiguities in the reconstruction, while optimizing the estimated plane segmentation based on the geometric properties.
3. Specifically, we use an MLP network to predict the signed distance and color for any point in 3D space. Given the segmentation of floor and wall regions, we enforce the signed distance field to respect corresponding geometric structures in these regions based on the Manhattan-world assumption.
4. Considering that inaccurate segmentation results may mislead the optimization, we additionally use a network to predict a semantic label for each 3D point and jointly optimize it based on the geometric loss.
### **Related work**
**Depth map reconstruction.**
1. Given a set of images with calibrated camera poses, \cite{point clouds, volumetric, MVS} aim to recover the underlying 3D shape of the captured scene. This is a long standing problem in computer vision.
2. Many methods adopt a two-stage pipeline: they first estimate the depth map for each image based on multi-view stereo \cite{} and then perform depth fusion \cite{} to obtain the final reconstruction results. -> Traditional multi-view stereo methods \cite{} are able to reconstruct very accurate 3D shapes and have been used in many downstream applications \cite{view synthesis, human reconstruction}. -> However, they tend to give poor performances on texture-less regions. -> A reason is that texture-less regions make dense feature matching intractable.
3. To overcome this problem, some works improve the reconstruction pipeline with deep learning techniques. -> \cite{gift, loftr} 改进了feature matching. -> MVSNet构造cost volume来预测depth map。
4. Another line of works \cite{} utilize scene priors to help the reconstruction. -> 用平面帮助colmap的场景重建。-> 浩宇之前论文引用的一些工作。
**Volumetric reconstruction**
1. These methods \cite{} directly predict the properties of points in the 3D space.
2. Atlas具体怎么做的。
3. NeuralRecon具体怎么做的 -> 达到了实时重建。
4. They represent 3D scenes with discretized voxels, resulting in the high memory consumption.
5. Recently, some methods \cite{occupancy network, deepsdf, SRN, nerf, IDR, volsdf, neus} represent scenes with neural implicit representations.
6. IDR具体怎么做的
7. Neus具体怎么做的
8. They mostly present reconstruction results of scenes with rich textures.
**语义分割**
1. Deep learning based methods achieve impressive progress on semantic segmentation.
2. 2d语义分割: CNN-based methods \cite{deeplab, pspnet, ade20k、其他工作} 怎么做的 -> some methods \cite{} 怎么用 transformers to improve the performance.
3. 3d语义分割: \cite{pointnet、pointnet++、其他工作} develop networks to process different representations of 3D data。-> \cite{semantic nerf} 具体怎么做的。
4. some methods \cite{} 利用2d和3d的关系提升the performance of 2D and 3D segmentation。
### Method
#### **Sub-section粒度的写作思路**
1. Problem statement.
2. Overview of our method.
3. Volume rendering of signed distance fields.
4. Semantics-guided scene reconstruction
5. Joint optimization of semantics and geometry
#### 句子粒度的写作思路
**Problem statement and overview**
1. Given multi-view images with camera poses of an indoor scene, our goal is to reconstruct the high-quality scene geometry.
2. The overview of our approach is illustrated in Figure 1.
3. We represent the scene geometry and appearance with signed distance and color fields, which are learned from images with volume rendering techniques (Section 3.1).
4. To improve the reconstruction quality in floors and walls, we perform semantic segmentation to detect these regions and apply the geometric constraints based on the Manhattan-world assumption (Section 3.2).
5. To overcome the inaccuracy of semantic segmentation, we additionally encode the semantic information into the implicit scene representation and jointly optimize the  semantics with the geometry and appearance of the scene (Section 3.3).
**Volume rendering of signed distance fields**
1. In contrast to multi-view stereo based methods, we model the scene as an implicit neural representation and learn it from images with a differentiable renderer.
2. Inspired by \cite{idr, volsdf, neus}, we represent the scene geometry and appearance with signed distance and color fields.
3. 描述geometry network:
4. 描述color network:
5. 描述用volume rendering训练the scene representation:
6. 描述用colmap得到的depth map来作为loss：
**Semantics-guided scene reconstruction**
1. We observe that most texture-less planar regions lie on floors and walls.
2. As pointed by the Manhattan-world assumption \cite{}, floors and walls of indoor scenes generally aligned with three dominant directions.
3. In this assumption, the floor are horizontal, while walls are vertical to the floor and are vertical to each other.
4. Motivated by this, we propose to apply the geometric constraints to the regions of floors and walls.
5. Specifically, we first use a 2D semantic segmentation network \cite{} to obtain the regions of floors and walls.
6. Then, we apply loss functions to enforce the scene representation to satisfy that the surface points on a planar region share the same normal direction.
7. To supervise the walls, a learnable normal $n_w$ is predefined.
8. Following the Manhattan-world assumption, we design a loss that make the normals of surface points on walls are aligned or vertical with the learnable normal $n_w$, which is defined as:
9. where $n’_w$ is the normal of surface points calculated as the gradient of the signed distance s(x) at point x.
10. The learnable normal $n_w$ is randomly initialized and is jointly optimized with the network parameters. We found that it can stably converge to the ground-truth normal in our experiments.
11. For the supervision of floor region, we assume that it is aligned with the z-axis, which are correct in most scenes. The normal loss for the floor is defined as:
12. where $n_f$ is <0, 0, 1>, and $n’_f$ is the normal of surface points on the floor.
13. Moreover, we add an additional geometric constraint to the floor region, which enforces its surface points have the same height. This geometric constraint is defined as:
14. where $p_z$ is the z-component of surface point $p$, and $h$ is a learnable scalar that denotes the height of floor.
15. We initialize $h$ by clustering the point clouds in the floor region from multi-view stereo methods.
16. The height $h$ is also jointly optimized with our model parameters. The loss function for the floor is defined as:
a. Given a 3D point x, the geometry model maps it to a signed distance, which is defined as: z(x), s(x) = F_s(x),
b. where F_s is implemented as an MLP network, and z(x) is the geometry feature.
a. To approximate the radiance function, the appearance model takes the spatial point x, the viewing direction d, the normal n(x), and the geometry feature z(x) as inputs, which is defined as: c(x) = F_c(x, d, n(x), z(x)),
b. where we obtain the normal n(x) by computing the gradient of the signed distance s(x) at point x.
a. Following \cite{volsdf, neus}, we adopt the volume rendering scheme to learn the scene representation from images. ->
b. 对于一个image pixel, we sample N points along its camera ray. ->
c. 预测每个点的signed distance and colors. ->
d. Then, 用公式1把signed distance转成density ->
e. 然后用volume rendering的公式得到颜色 ->
f. 描述image loss


### 如何改一篇论文的写作

> 文档汇总（GitHub Repo）：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)
> 💡 
#### 写作思路上的改进
对于abstract、introduction、method或者某一个段落，改进其思路的步骤如下：
1. **编码：**将raw text转换为high-level写作思路
1. **在思路上分析：**回答以下两个问题，以期找到思路逻辑的不合理之处：
1. **在思路上改进：**针对不合理之处，修改思路
1. **解码：**将high-level写作思路转为raw text
- 具体的写作例子（**好用，建议看**）
#### Sentence flow（句子流畅性）的改进
Sentence flow的定义：两个句子之间的思路逻辑是连贯的，没有出现跳变。
如何改进Sentence flow：
1. 对着每两个句子，回答以下问题，以期找到句子之间sentence flow的不合理之处：
1. 根据不合理之处，修改这两个句子，使其符合sentence flow。可以使用GPT辅助。
- 具体的写作例子（**好用，建议看**）
为什么要写这篇文档：迭代改进论文是写好一篇论文的关键。
1. 该思路是否体现了想表达的内容？
1. 思路逻辑是否流畅？
1. 第二个句子是否有接着第一个句子讲一些内容？
1. 如果第二句话没有接着第一句话说东西，句子之间是否有进行过渡？
1. 第二句话是否出现了新名词，该名词的出现是否突兀？

### 怎么审论文

1. Adversarial writing：自己review自己的论文，考虑reviewer可能会问的所有问题，并一一解决。
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

- [论文写作模板](../writing/template.md)
