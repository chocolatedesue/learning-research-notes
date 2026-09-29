> 原文：[Notion 原文](https://pengsida.notion.site/1723fe292ff18053ade0d7afa6c0328a) · 作者可能已更新，以原文为准。

## 写作思路典例

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
a. Given a 3D point x, the geometry model maps it to a signed distance, which is defined as: z(x), s(x) = F_s(x),
b. where F_s is implemented as an MLP network, and z(x) is the geometry feature.
4. 描述color network:
a. To approximate the radiance function, the appearance model takes the spatial point x, the viewing direction d, the normal n(x), and the geometry feature z(x) as inputs, which is defined as: c(x) = F_c(x, d, n(x), z(x)),
b. where we obtain the normal n(x) by computing the gradient of the signed distance s(x) at point x.
5. 描述用volume rendering训练the scene representation:
a. Following \cite{volsdf, neus}, we adopt the volume rendering scheme to learn the scene representation from images. ->
b. 对于一个image pixel, we sample N points along its camera ray. ->
c. 预测每个点的signed distance and colors. ->
d. Then, 用公式1把signed distance转成density ->
e. 然后用volume rendering的公式得到颜色 ->
f. 描述image loss
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
