> 出处：[原文链接](https://pengsida.notion.site/caf34717f4c046c69ee7e14ea953c46f)

## 怎么做实验记录

> 文档汇总（GitHub Repo）：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)
一个实验记录一般这么组织 (文字上不用很详细，自己看得懂就行。实验记录一般是给自己看的)：
1. 实验的目的：描述为什么做这个实验，想通过实验获得什么。
1. 实验的setting：什么样的数据上做的实验，算法上有什么改动。
1. 记录实验结果：记录效果好和效果不好的实验结果，包括可视化结果和量化结果。
1. 分析实验结果：观察实验结果是否符合预期。如果不符合预期，需要[分析实验不work的原因](../skills/debug-experiment.md)。
1. Next step：你是project的leader，不断地思考如何进行下一步，列出接下来要做的实验，而不是等待instructions。
例子：

### 实验记录模板

### 实验的目的
描述为什么做这个实验，想通过实验获得什么
### 实验的setting
什么样的数据上做的实验，算法上有什么改动
### 记录实验结果
记录效果好和效果不好的实验结果，包括可视化结果和量化结果。
### 分析实验结果，可能的原因
观察实验结果是否符合预期。如果不符合预期，需要[分析实验不work的原因](../skills/debug-experiment.md)。
### 接下来要做的实验
你是project的leader，不断地思考如何进行下一步，列出接下来要做的实验，而不是等待instructions。

- [怎么做实验记录](../skills/experiment-log.md)
- [如何找到实验不work的原因](../skills/debug-experiment.md)
### 3.24 实验记录

本周目标：
1. 替换generalizable的rendering head
1. 尝试single point
### 1. 边缘抖动
1. 加了mask之后能解决，但也和时间有关系
### 2. 替换generalizable 的rendering head
#### 2.1 pretrain enerf rendering head
1. 修改enerf rendering head与vox feat无关
1. 修改enerf rendering
#### 2.2 替换rendering head之后，发现效果变差很多
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/475ed71e-d469-4457-9709-eaf38a53a046/Untitled.png)
#### 2.2 可能的原因
1. 泛化能力不够
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/6cbe547b-7af4-40d2-8235-4c1a427d3d18/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/45b2ef08-12ae-46c6-bc32-3e33521d0662/Untitled.png)
1. 在DTU pretrain一个相同结构的rendering head
1. 替换进去
发现替换进去不太work
1. 怀疑是采样数量的原因
1. 怀疑是code有bug
1. 研究K-Planes 和 K-Planes IBR分别需要多少个points work
1. 使用depth + 1个point
1. K-Planes:
1. K-Planes IBR
1. 4,8,48
1. 4,8,48
发现效果很差
- [6.3hours wo mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/42f4fb4e-d13d-4c63-a8cc-0930f0a29a09/step00000000.mp4)
- [with mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/97f19d17-7881-44e8-8a0c-e93fbd2eaa89/step00000000.mp4)
- [4.2 hours wo mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/63b38420-3d24-42f2-83db-b8bd8bc3b3b8/step00030000.mp4)
- [w mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/6bc223f5-db39-48bd-84d8-7553eed6c2cb/step00030000.mp4)
- [2.1 hours wo mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/74e39da6-2e6c-40be-b21d-4eaa898c9f9c/step00060000.mp4)
- [w mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/84ab22d8-e6a8-4fcf-ade7-b82bb14fea5d/step00060000.mp4)
![joint training](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/61aa8c42-ad24-4a21-b797-3f2f9fb954bd/Untitled.png)

*joint training*
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/95477c71-afa2-40ad-962e-71cc8f1a8562/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/e8482d91-db30-4e46-9605-ac132a47c4ee/Untitled.png)
![no pretrain](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/b591b293-fc9e-4b2e-a9cc-ec0cdcb71e4a/Untitled.png)

*no pretrain*
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/e5d20b49-6cd7-4969-b527-211d9ba454df/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/626d04d0-33bc-4771-baad-8edb3d1abd6a/Untitled.png)
![with pretrain](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/fab98fbf-02f0-4841-a3c5-aff3fbde54e6/Untitled.png)

*with pretrain*
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/59941c59-0886-4256-82e1-034d33b3c785/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/e9659e6e-e930-47a2-a557-4af984ca057b/Untitled.png)
1.  看看ENeRF在这个场景上的泛化能力怎么样 
1. 解决方案:
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/627be11c-e969-4622-8447-21afa3ab15e7/Untitled.png)
1. 快速ft 一帧。
1. 用一个稍微复杂一点的策略，前n帧 ft，后面帧每隔10帧ft一次。
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/4d295337-272c-419b-a550-775158e46125/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/915c2a39-3e86-4ed9-a33b-3de61d63355a/Untitled.png)
#### 2.3 替换Ft一帧的rendering head后效果变得比较好
目前的问题：
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/bbb55e4e-1bfd-45cc-b62a-1cd97f207880/Untitled.png)
**KPlanes**
KPlanes IBR Joint Training
### 3. Depth 采样
1. 不太work，可能点数少了之后无法收敛
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/b718942e-8ef2-450f-a433-0f5811ad99cc/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/fb526109-e081-4908-8cb2-175c83d6427c/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/e6de1d19-e42d-4a00-9837-90412cc81fa3/Untitled.png)
1. 训练时间仍然较长
1. path渲染结果有一些鬼影

- [怎么做实验记录](../skills/experiment-log.md)
- [如何找到实验不work的原因](../skills/debug-experiment.md)
