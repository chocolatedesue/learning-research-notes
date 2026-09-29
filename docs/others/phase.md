> 原文：[Notion 原文](https://pengsida.notion.site/1703fe292ff1809e92d2ff48f47e06de) · 作者可能已更新，以原文为准。

## Phase for Character Control

参考文章：
1. [动作生成的智能之路(I) : PFNN](https://zhuanlan.zhihu.com/p/485607474)
1. [动作生成的智能之路(II) : Local Motion Phase](https://zhuanlan.zhihu.com/p/486996982)
1. [动作生成的智能之路(III)：DeepPhase](https://zhuanlan.zhihu.com/p/562089658)
本文章思路：
1. Phase是什么。
1. Phase怎么用于Character Control。
1. 为什么要设计Phase。
1. Phase存在的问题。
1. 对Phase的改进：Local Motion Phase。
1. Local Motion Phase怎么用于Character Control。
1. Local Phase存在的问题。
1. 对Local Phase的改进：DeepPhase。
1. DeepPhase怎么用于Character Control。
**Phase是什么：将人的运动状态定义成周期函数，Phase代表特定的状态，Phase是[0, 2Pi]之间的连续值。**比如，走路的运动状态，左脚着地为0，右脚着地为Pi；打球的运动状态，球在手上为0，球在地上为Pi。
> 
注意，Phase并不表示运动的频率，仅表示特定时刻的状态。
**Phase怎么用于Character Control：**
1. 给定一个motion capture data，首先标定每一个时刻的Phase。
1. 构建一个基于Phase的character control framework。
1. 给定一个Phase，有一个Hypernetwork预测Character Control Network的weights。
1. 构造Character Control Network，其输入是（Previous frame的状态，User input），输出是（Next-step movement，Phase change）。
1. 基于Phase change更新Phase。回到第a步。
1. 使用第一步中提取得到的训练数据，训练第二步中的character control network。
**为什么要设计Phase：为了让Character Control Network能力更强。**
1. 如果没有Phase，那么全局只有一个Character Control Network，其需要记忆所有状态的input-output mapping。
1. 如有有Phase，那么每一个Phase都有一个Character Control Network，该网络只需要记忆这个状态下的input-output mapping。
**Phase存在的问题：一些运动不具有周期性。**
> 
有周期性的运动：走路；原地拍球。
无周期性的运动：边走路边拍球；四足动物走路。
**救星：Local Motion Phase。**把复杂的运动过程拆解掉，转换成几个简单周期运动过程的组合。
> 
例子
人打篮球，包含了：左右脚触地，左右手掌球，以及拍打球。
Local Motion Phase首先拆解“打篮球”这个过程，把几个核心过程取出来，包括左脚运动，右脚运动，左手和球的互动，右手和球的互动，球与地面的接触。使用这几个核心过程组合得到“打篮球”这个过程。
**Local Motion Phase怎么用于Character Control：**
1. 给定一个motion capture data，首先标定每一个时刻的Local Phases。
1. 构建一个基于Local Phases的character control framework。
1. 给定一组Local Phases，有一个Hypernetwork预测Character Control Network的weights。
1. 构造Character Control Network，其输入是（Previous frame的状态，User input），输出是（Next-step movement，Local Phases’ change）。
1. 基于Local Phases’ change更新Local Phases。回到第a步。
1. 使用第一步中提取得到的训练数据，训练第二步中的character control network。
**Local Phase存在的问题：**
1. **难以从Whole-body Motion中分解得到各个周期性的子动作。**比如，怎么对“踢足球”进行拆解。
1. **无法处理非周期性运动。**比如，无法拆解“跳舞”。
**救星：DeepPhase。**训练一个Auto-Encoder，从Motion Data中提取Phase vectors。
**DeepPhase怎么用于Character Control：**
1. 给定一个motion capture data，首先使用DeepPhase提取每一个时刻的Phase vector。
1. 构建一个基于Phase vector的character control framework。
- **具体步骤（类似Phase和Local Phase一样使用character control network）**
1. 使用第一步中提取得到的训练数据，训练第二步中的character control network。
