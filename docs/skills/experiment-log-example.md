## 3.24 实验记录

本周目标：
1. 替换generalizable的rendering head
1. 在DTU pretrain一个相同结构的rendering head
1. 替换进去
发现替换进去不太work
1. 怀疑是采样数量的原因
1. 怀疑是code有bug
1. 尝试single point
1. 研究K-Planes 和 K-Planes IBR分别需要多少个points work
1. K-Planes:
1. 4,8,48
1. K-Planes IBR
1. 4,8,48
1. 使用depth + 1个point
发现效果很差
### 1. 边缘抖动
1. 加了mask之后能解决，但也和时间有关系
- [6.3hours wo mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/42f4fb4e-d13d-4c63-a8cc-0930f0a29a09/step00000000.mp4)
- [with mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/97f19d17-7881-44e8-8a0c-e93fbd2eaa89/step00000000.mp4)
- [4.2 hours wo mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/63b38420-3d24-42f2-83db-b8bd8bc3b3b8/step00030000.mp4)
- [w mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/6bc223f5-db39-48bd-84d8-7553eed6c2cb/step00030000.mp4)
- [2.1 hours wo mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/74e39da6-2e6c-40be-b21d-4eaa898c9f9c/step00060000.mp4)
- [w mask](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/84ab22d8-e6a8-4fcf-ade7-b82bb14fea5d/step00060000.mp4)
### 2. 替换generalizable 的rendering head
#### 2.1 pretrain enerf rendering head
1. 修改enerf rendering head与vox feat无关
1. 修改enerf rendering
#### 2.2 替换rendering head之后，发现效果变差很多
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/475ed71e-d469-4457-9709-eaf38a53a046/Untitled.png)
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
#### 2.2 可能的原因
1. 泛化能力不够
1.  看看ENeRF在这个场景上的泛化能力怎么样 
1. 解决方案:
1. 快速ft 一帧。
1. 用一个稍微复杂一点的策略，前n帧 ft，后面帧每隔10帧ft一次。
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/627be11c-e969-4622-8447-21afa3ab15e7/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/6cbe547b-7af4-40d2-8235-4c1a427d3d18/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/45b2ef08-12ae-46c6-bc32-3e33521d0662/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/4d295337-272c-419b-a550-775158e46125/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/915c2a39-3e86-4ed9-a33b-3de61d63355a/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/fb526109-e081-4908-8cb2-175c83d6427c/Untitled.png)
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/e6de1d19-e42d-4a00-9837-90412cc81fa3/Untitled.png)
#### 2.3 替换Ft一帧的rendering head后效果变得比较好
目前的问题：
1. 训练时间仍然较长
1. path渲染结果有一些鬼影
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/bbb55e4e-1bfd-45cc-b62a-1cd97f207880/Untitled.png)
**KPlanes**
KPlanes IBR Joint Training
### 3. Depth 采样
1. 不太work，可能点数少了之后无法收敛
![图](https://prod-files-secure.s3.us-west-2.amazonaws.com/952f5f87-b692-4249-a557-7f7ad0a77d56/b718942e-8ef2-450f-a433-0f5811ad99cc/Untitled.png)
