> 出处：[原文链接](https://pengsida.notion.site/1713fe292ff1808eb33be93ea2d79ad9)

## 博士生的楷模：Sebastian Starke

> 文档汇总（GitHub Repo）：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)
这两天读了Sebastian Starke博士期间在Character Control上的系列论文，学习了很多（[论文笔记](https://pengsida.notion.site/1703fe292ff1809e92d2ff48f47e06de)）。我不认识Sebastian Starke，但仅阅读他的系列论文，就深感佩服，有很多感悟，为了日后温习反思，在此记录自己的想法。
[Sebastian Starke](https://github.com/sebastianstarke)博士在Taku Komura组就读，他博士期间每年在SIGGRAPH上发表一篇文章，通过5年的时间搭建出一套接近商业化的Character Control系统，令人惊叹，极大地推动了产业界游戏动作系统的可用水平。在GitHub上，他的[AI4Animation](https://github.com/sebastianstarke/AI4Animation)收获7.4k stars。在学术上，他每一篇SIGGRAPH论文都逐步攻克更难的业界问题，朝着一个方向往深了研究，其博士期间的最后一篇论文DeepPhase也终于斩获SIGGRAPH最佳论文，实至名归。
通过阅读Sebastian Starke博士的系列论文，能看出他的研究风格：
1. **有非常明确且长期的目标，问题驱动式科研。**他的论文始终在解决Character Control系统中的各种问题，从早期的简单周期性运动控制，到后面的复杂运动控制，征服了Character Control方向的一座座高山。
1. **总能找到有价值的问题。**可能受益于Taku组的长期积累，Sebastian的论文总能找到Character Control中优先级最高的问题，而不是把精力花在一些无关痛痒或暂时不重要的问题上。
1. **不畏难地填坑，挑战“没答案”的问题。**Sebastian猛就猛在敢去攻克难题、不断填坑。Character Control方向的一大重要问题是目标动作的复杂度。他师兄Daniel Holden的PFNN解决了简单周期运动，他的Local Motion Phase进一步提升，解决了组合式运动，然后又通过DeepPhase（SIGGRAPH最佳论文）解决了复杂非周期运动，几乎解决了动作复杂性的这一问题。
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
相比于“目标动作复杂度”，Character Control方向有其他更好发论文的问题，比如Multi-modal Control。Sebastian没有因为它们更好发论文而去解决这些问题，而是始终把精力放在最重要的问题上，这样的问题都没有well-established solution。他不畏难地不断填坑，是他能推动产业进步的关键。

### Phase for Character Control

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
> 💡 
**Phase怎么用于Character Control：**
1. 给定一个motion capture data，首先标定每一个时刻的Phase。
1. 构建一个基于Phase的character control framework。
1. 使用第一步中提取得到的训练数据，训练第二步中的character control network。
注意，Phase并不表示运动的频率，仅表示特定时刻的状态。
1. 给定一个Phase，有一个Hypernetwork预测Character Control Network的weights。
1. 构造Character Control Network，其输入是（Previous frame的状态，User input），输出是（Next-step movement，Phase change）。
1. 基于Phase change更新Phase。回到第a步。
**为什么要设计Phase：为了让Character Control Network能力更强。**
1. 如果没有Phase，那么全局只有一个Character Control Network，其需要记忆所有状态的input-output mapping。
1. 如有有Phase，那么每一个Phase都有一个Character Control Network，该网络只需要记忆这个状态下的input-output mapping。
**Phase存在的问题：一些运动不具有周期性。**
> 💡 
**救星：Local Motion Phase。**把复杂的运动过程拆解掉，转换成几个简单周期运动过程的组合。
> 💡 
**Local Motion Phase怎么用于Character Control：**
1. 给定一个motion capture data，首先标定每一个时刻的Local Phases。
1. 构建一个基于Local Phases的character control framework。
1. 使用第一步中提取得到的训练数据，训练第二步中的character control network。
**Local Phase存在的问题：**
1. **难以从Whole-body Motion中分解得到各个周期性的子动作。**比如，怎么对“踢足球”进行拆解。
1. **无法处理非周期性运动。**比如，无法拆解“跳舞”。
**救星：DeepPhase。**训练一个Auto-Encoder，从Motion Data中提取Phase vectors。
**DeepPhase怎么用于Character Control：**
1. 给定一个motion capture data，首先使用DeepPhase提取每一个时刻的Phase vector。
1. 构建一个基于Phase vector的character control framework。
1. 使用第一步中提取得到的训练数据，训练第二步中的character control network。
有周期性的运动：走路；原地拍球。
无周期性的运动：边走路边拍球；四足动物走路。
例子
人打篮球，包含了：左右脚触地，左右手掌球，以及拍打球。
Local Motion Phase首先拆解“打篮球”这个过程，把几个核心过程取出来，包括左脚运动，右脚运动，左手和球的互动，右手和球的互动，球与地面的接触。使用这几个核心过程组合得到“打篮球”这个过程。
1. 给定一组Local Phases，有一个Hypernetwork预测Character Control Network的weights。
1. 构造Character Control Network，其输入是（Previous frame的状态，User input），输出是（Next-step movement，Local Phases’ change）。
1. 基于Local Phases’ change更新Local Phases。回到第a步。
- 具体步骤（类似Phase和Local Phase一样使用character control network）

#### Sida Peng (彭思达)

> 该页面主要用于分享在Notion上的开源学习笔记

---

#### 科研素养笔记
科研经验笔记：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)
[博士生的楷模：Sebastian Starke](../others/qualities.md)
[从面试问题的角度反思科研的宝贵品质](../project/taboo.md)
[自然科学的定义（数学与科学的区别）](https://pengsida.notion.site/1053fe292ff18015b2f3cde4498a5f0f)

---

#### 技术学习笔记
最近的技术学习笔记主要更新在小红书：[链接](https://www.xiaohongshu.com/user/profile/56daf09784edcd4fa92ef524)
更早的笔记：
[《深度强化学习》学习笔记](https://pengsida.notion.site/24e3fe292ff180d582e8cdb0a03cb8c2)
[张祥雨访谈-多模态&AGI认知学习笔记](https://pengsida.notion.site/2213fe292ff18044b20ffe15db83f4f8)
[gpt4o相关技术学习笔记](https://pengsida.notion.site/1c63fe292ff180499ea0cc4e1e1b163e)
[3D LLM的pipeline总结](https://pengsida.notion.site/9533b857615345108d7624b6e76a2ba3)
[如何使用copilot和gpt辅助英语写作](https://pengsida.notion.site/1143fe292ff180feb5d0fe76d05e085b)
[具身智能的pipeline总结](https://pengsida.notion.site/092795ee24fb408fb0eb340186949c78)
[Ross Girshick的talk笔记](https://pengsida.notion.site/d9b48545884a47799fc5829cad8af2b6)
[LeCun Talk笔记](https://pengsida.notion.site/1223fe292ff180eaaa49ca6ac47988bc)
![图](../assets/img/2583fe292ff18018.png)
[Homepage](https://pengsida.net/)
[GitHub](https://github.com/pengsida/)   
[Google Scholar](https://scholar.google.com/citations?user=l9NCksYAAAAJ&hl=en)  
Short Bio
I am an assistant professor (ZJU-100 Young Professor) at Zhejiang University. I received my Ph.D. degree from College of Computer Science and Technology at Zhejiang University in 2023, supervised by Prof. Xiaowei Zhou and Prof. Hujun Bao, and obtained my bachelor degree in Information Engineering from Zhejiang University in 2018. I received the [2024 CCF Outstanding Doctoral Dissertation Award](https://mp.weixin.qq.com/s/a8RQ8FCwMKoDXwjjXJ7v1g) and was selected as the [2022 Apple Scholar in AI/ML](https://machinelearning.apple.com/updates/apple-scholars-aiml-2022).
I work closely with Prof. Xiaowei Zhou. We are looking for students, postdocs and research assistants. Please [apply to our lab here](https://docs.qq.com/form/page/DZkxUcXRteEhnWktK) if you are interested in working with us.

##### 探索性实验应遵循最小可行性

#### 最小可行性是什么
科研中的最小可行性是指用最少的资源、时间和精力，构建一个刚好能验证核心科学假设或技术原理的简化版实验、模型或原型。

---

#### 最小可行性的好处
**核心重要性：降低风险，提高效率**
这是最小可行性（MV）最根本的价值。科研本质上是探索未知，充满了不确定性和失败的风险。
- 快速验证假设，避免方向性错误：你可能有一个非常巧妙的想法，但其中可能隐藏着致命的逻辑缺陷或未被考虑的实际约束。投入大量时间精力建造一个复杂的实验系统后才发现根本行不通，是巨大的浪费。MV方法让你能快速做一个简单实验，先回答“这个想法原则上是否可能？”这个问题。如果简单实验都失败了，你可以果断放弃或转向，节省了大量宝贵资源。
- 高效利用有限资源：科研资源（经费、设备、学生时间、计算资源）永远是稀缺的。MV迫使你聚焦于最核心的问题，避免在项目早期就陷入优化细节、构建完美系统的陷阱。把好钢用在刀刃上。
- 快速获得反馈，迭代推进：MV产出的是一个“虽然简陋但能工作”的初版。你可以用它来收集初步数据，向导师、同行展示，申请预研经费，或者发现设计中的问题。基于这些早期反馈，你可以进行有针对性的迭代和改进，使研究路线始终沿着最高效的方向演进。这是一个“构建-测量-学习”（Build-Measure-Learn）的循环。

---

#### 做探索性实验具体怎么执行最小可行性的规则
**核心思想：以最小成本验证想法的可行性。**
**第一步：定义“可行性”的标准（明确目标）**
在开始任何实验之前，你必须清晰地回答：这个最小实验要验证什么？成功的标准是什么？
这个“可行性”标准必须是二元的、明确的、可测量的（是/否，达到/未达到）。它就是你这次探索的“罗盘”。
**第二步：设计“最小”的实验（极致简化）**
这一步的任务是剥离所有非必要因素，构建一个能回答第一步中核心问题的最简单系统。
具体执行方法： “如果我现在只有一天时间，我能做什么最简单的实验来检验我的想法？”
**第三步：执行与学习（快速行动，聚焦反馈）**
1. 快速执行： 目标是尽快完成实验，拿到原始数据。不要追求完美无瑕的实验记录（但要保证可重复），接受一定的“粗糙度”。
1. 分析结果，对照标准： 将得到的数据与第一步设定的“可行性标准”进行严格对比。
1. 做出明确的决策： 结果只导向三个清晰的行动方向：
- 成功（假设得到支持）： 证明核心想法是可行的。下一步是：设计一个更严谨、更大规模的实验来巩固发现。你可以开始增加复杂度，优化细节。
- 失败（假设被推翻）： 核心想法不成立。这是一个巨大的成功！ 因为你用最小的成本避免了一个大坑。下一步是：深刻分析失败原因，是想法根本错误，还是实现方式有问题？基于此，果断 pivot（转向） 到一个新的想法，或者终止这个方向。
- 不确定/数据模糊： 结果既不支持也不推翻假设。这通常意味着实验设计得不够好，“最小可行性”的“可行性”标准没设定清楚。下一步是：重新审视第一步，优化实验设计，让它能给出更明确的答案。可能需要一个更“精炼”的最小实验。



- [博士生的楷模：Sebastian Starke](../others/qualities.md)
- [从面试问题的角度反思科研的宝贵品质](../project/taboo.md)
##### 自然科学的定义（数学与科学的区别）

转载自：[https://hr.edu.cn/xueshu/202209/t20220908_2244759.shtml](https://hr.edu.cn/xueshu/202209/t20220908_2244759.shtml)
科学起源于数学，数学早于科学产生（注：这里的科学特指自然科学）。5000多年前，四大文明古国和古希腊都产生了数学，公元前300年左右，古希腊数学蓬勃发展，产生了真正成体系的欧几里得几何学。当数学蓬勃发展的时候，产生了科学的萌芽，而科学则是产生于14世纪中叶至17世纪初在欧洲发生的思想文化运动后，在伽利略等人的努力下制定了科学研究的规范，才产生真正意义上的科学。用我们今天定义的数学和科学来区分年代的话，科学只有400多年的历史，而数学却有2000多年的历史。
研究对象不同。数学是用符号语言研究数量和空间关系，研究对象可以是实的，也可以是虚的，具有很强的抽象性。科学则是研究自然界物质的现象和事物的发生、发展和变化规律，既包括物体个体、物体系统、物体细分，也包括宏观现象、微观现象等，科学研究的对象必须是实的，具有很强的实证性。
研究方法不同。数学比较注重逻辑推理，2000多年前的数学家们就确定了“大胆猜测，严密论证”的演绎论证方法。所有数学定理全部要经过演绎论证，否则不可以进入严密认证自洽的数学体系。科学则侧重于实验，是基于假设，推理的摸索与探索，自然科学的所有学科都是注重实验、观察的科学，从可重复的实验中得出的结论。
结论的可靠性不同。数学定理一般非常可靠，等同于真理，不易被后来者推翻。科学上的结论往往只是一个时代的真理，随着数学理论的更加完善，实验和检测手段的不断提高，其它学科提供了更加充分的证据，使得有些前人认为是真理的东西被证明不是自洽的，科学结论过了它所处的时代可能就不再可靠了。
数学是科学的先锋。马克思曾明确指出“一种科学只有在成功运用数学时，才算达到了真正完善的地步”。数学为科学研究提供了工具，数学推理为科学探索提供了指引和借鉴。只有数学发展到更高水平，科学才能上升迈上新的理论体系。如在物理学领域，当数学发展水平处于欧几里德几何学时期，科学研究只能建立在静止力学的基础上，对应的科学体系是托勒玫的“地心说”；牛顿发明了微积分，科学研究才可能在动态力学的基础上进行，逐步建立了哥白尼—牛顿的科学体系；当数学发展到非欧几里德几何学阶段，爱因斯坦以发展演变的动态宇宙观，用黎曼几何推演，才发现了广义相对论，建立了当今的爱因斯坦—霍金的科学体系。
科学的好奇和探索推动数学不断向前发展，在科学发展过程中，也给数学提出一些新的课题。量子力学是在20世纪初由一大批科学家共同创立的，创立初期所用的数学是线性代数，彻底改变了科学家对物质组成成分的观点。量子力学研究了差不多一百年，特别是对量子纠缠的研究，有些现象既无法用代数来描写，也无法用分析来推演，由于数学发展水平的限制，至今无重大突破，并没有改变大众对物质组成成分的认知。量子力学没有取得突破，是因为没有现成可用的数学方法，急需要发明新的数学理论和方法。
数学与科学有着天然的联系。现代科技的发展得益于数学的发展，可以说几乎所有科技领域都用到数学，数学用地越好，科技水平和技术含量就越高。数学认知能力的发展是人类探究和解决问题的前提，人类解决问题，从宏观到微观，从宇宙到地球，所有的探索都离不开数学。

##### 《深度强化学习》学习笔记

#### 需要学习的知识点
1. Value-based RL（深度Q函数，DQN及其训练方法）
1. Policy-based RL（深度策略函数）
1. Model-based RL
1. 模仿学习
1. 离线强化学习
1. 元强化学习
1. RL的Open Challenges

---

#### 知识点笔记
- 深度Q函数（DQN及其训练方法）
- Value-based RL的高级技巧（如何提升Value-based RL的效果）
- 深度策略函数（策略学习）
- 如何基于Actor-Critic优化深度策略函数
- 策略学习高级技巧（如何提升Policy-based RL的效果）1：带基线的策略梯度方法
- 策略学习高级技巧（如何提升Policy-based RL的效果）2：Trust Region Policy Optimization (TRPO)
- 策略学习高级技巧（如何提升Policy-based RL的效果）3：PPO
- 策略学习高级技巧（如何提升Policy-based RL的效果）4：熵正则 (Entropy Regularization)
- 策略学习高级技巧（如何提升Policy-based RL的效果）5：异策略（离线策略）
- 模型预测控制
- Model-based Policy Optimization
1. DQN
1. DQN的训练方法（时间差分 (TD) 算法）
1. Value-based RL的高级技巧（如何提升Value-based RL的效果）
1. 经验回放
1. 高估问题及解决方法（Target Network、Double DQN）
1. 对决网络 (Dueling Network)
1. 噪声网络
1. Multi-step TD target
1. 策略网络
1. 怎么通过策略梯度优化策略网络
1. 怎么计算策略梯度-方法1：REINFORCE
1. 怎么计算策略梯度-方法2：Actor-Critic
1. 策略学习高级技巧（如何提升Policy-based RL的效果）
1. Actor
1. Critic：动作价值函数
1. 如何学习动作价值函数（SARSA算法、Reward model）
1. 带基线的策略梯度方法
1. Trust Region Policy Optimization (TRPO)：一种策略学习方法，可以代替策略梯度方法
1. PPO：改进TRPO
1. 熵正则 (Entropy Regularization)
1. 异策略（离线策略）
1. 策略梯度中的基线
1. 带基线的 REINFORCE 算法
1. Advantage Actor-Critic (A2C)
1. 深度确定策略梯度（DDPG）
1. SAC
1. 深度Model-based RL
1. 传统Model-based RL（因为很经典，所以了解一下）：动态规划
1. 模型预测控制
1. Model-based Policy Optimization
1. Dyna-Q
1. 行为克隆
1. 逆向强化学习
1. 生成判别模仿学习 (GAIL)
1. 怎么构建Model
1. 如何提升Sampling Efficiency
1. 如何在奖励函数并不明确的场景下学习有效的策略
1. 如何在奖励稀疏的场景下学习有效的策略
1. 多智能体强化学习
- 传统Model-based RL（因为很经典，所以了解一下）
- 离线强化学习
- 元强化学习

---

#### 参考材料
超级清楚的深度强化学习课程：[https://www.bilibili.com/video/BV12o4y197US/?vd_source=1b53504d594b3b106e5065f1298139ba](https://www.bilibili.com/video/BV12o4y197US/?vd_source=1b53504d594b3b106e5065f1298139ba)
介绍PPO、Model-based RL：[https://www.bilibili.com/video/BV199pzeUEMA?vd_source=1b53504d594b3b106e5065f1298139ba&spm_id_from=333.788.videopod.sections](https://www.bilibili.com/video/BV199pzeUEMA?vd_source=1b53504d594b3b106e5065f1298139ba&spm_id_from=333.788.videopod.sections)
书本：[https://github.com/wangshusen/DRL/tree/master/Notes_CN](https://github.com/wangshusen/DRL/tree/master/Notes_CN)
判断自己是否真得懂了这些算法，看这个教程里的代码，看看是否能看懂：[https://hrl.boyuai.com/chapter/2/dqn算法](https://hrl.boyuai.com/chapter/2/dqn%E7%AE%97%E6%B3%95)
[http://rail.eecs.berkeley.edu/deeprlcourse/](http://rail.eecs.berkeley.edu/deeprlcourse/)
[https://github.com/wangshusen/DRL](https://github.com/wangshusen/DRL)
学习资料：[https://www.xiaogeedu.net/sys-nd/199.html](https://www.xiaogeedu.net/sys-nd/199.html)

##### 张祥雨访谈-多模态&AGI认知学习笔记

[https://zhuanlan.zhihu.com/p/1913377304173872183](https://zhuanlan.zhihu.com/p/1913377304173872183)
多模态模型相关的观点：
> 💡 
- 观点1：静态图像在智能发展上存在根本局限，难以单独支撑人类级别的智能实现，因其理解、生成和对齐三大要素本质割裂。
- 观点2：实现视觉智能，短期内视觉-语言对齐（VL Model）是可行方向，但存在局限性。长期看视频数据与具身智能可能是视觉智能的终极解决方案。
- 观点3：遇到的困境，多模态模型中的理解模型和生成模型各自变强，但融合后无协同效应（1+1=2，未达到1+1>2）。此外，多模态训练导致文本性能下降的问题尚未解决，因为现有生成方法（如Diffusion或Auto Regressive）有根本性局限。
- 观点4：O1的出现为提升多模态模型的能力提供了新思路，核心在于将语言模型中成功实现的“反思驱动决策”和“网状思维链”范式引入视觉领域，突破传统单步生成的复杂度限制。但即使引入CoT机制，虽在特定任务上有提升，但动作空间设计无法迁移到新任务。
- 观点5：视觉生成CoT泛化差的一个原因是，视觉动作空间未被预训练充分覆盖，而预训练数据决定能力上限，RL只能优化预训练已有的模式，无法创造新能力。
- 观点6：多模态GPT时刻依赖于构建视觉CoT预训练语料技术的突破。此外，要分阶段解锁多模态模型的能力，优先实现“简单域高可控生成”是关键跳板。
AGI相关的观点：
- 观点1：AGI中Long Context问题的解药不是延长Token窗口，而是重构记忆架构，用分工协作模拟人脑，用动态隔离实现高效推理。
- 观点2：实现AGI的必经之路是让模型像人类一样从多维度反馈中主动学习。
- 观点3：当前行业所称的"Agent"多属第二级（Rhythm），本质是工具链的智能串联，而非真正的Agent。真Agent需等待自主学习和在线学习算法突破。
简略总结：
纯静态图像学习不Work
→ 多模态模型（Vision-Language Model）可行
→ 但发现多模态模型中的理解模型和生成模型融合后无协同效应
→ O1为多模态模型提供CoT机制的思路，突破传统单步生成的复杂度限制
→ 实验发现多模态模型CoT的泛化能力有限，原因是视觉动作空间未被预训练充分覆盖，而RL只能优化预训练已有的模式
→ 多模态GPT时刻依赖数据工程突破，并且要分阶段解锁能力，优先实现“简单域高可控生成”是关键跳板

##### gpt4o相关技术学习笔记

### gpt4o的动机和核心技术问题
原有的VLM model：强行把图像当成token，使用语言模型做生成。→ 没有充分设计图像生成。
gpt4o的VLM model：在LLM中引入更先进的图像生成技术来改进图像生成，实现text and image的unified modeling。
使用auto-regressive model做image generation的好处：拆解复杂的图像分布，理解图像细节。→ 这是diffusion model没有的能力。
核心问题：如何在auto-regressive model中同时构建text generator和image generator。
问题拆解：
1. 好的image tokenizer是怎样的？
1. 如何用auto-regressive model做image generation？
1. text和image在auto-regressive model中怎么做交互？
- OpenAI的说法
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
1. 训练策略
大家在哪些模块上做研究：
1. 应该用什么tokenizer？→ 得到的visual tokens应该有什么样的性质？
1. 应该使用什么attention modules？
1. 应该使用什么生成方式？→ auto-regressive generation怎么充分考虑图片在spatial smoothness上的特性，block-wise and coarse-to-fine是否就够了？
1. 应该使用什么decoder？
已有的tokenizer：
1. Discrete tokenizer：VQ-VAE、RQ-VAE。
1. Continuous tokenizer：
1. 使用representation learning的方法，将tokenizer提升为semantic tokenizer。→ OpenAI选用。
已有的attention modules：
1. Causal attention
1. Bidirectional attention
已有的生成方式：
1. 逐步的生成数量：
1. 生成顺序：
1. 具体的attention设计
1. Output head
1. 生成方式
1. 如何消除understanding和generation的gap？
1. 如何提升understanding和generation的性能？
1. 如何把visual tokens变得和text一样compact？
- 必要性
1. VAE → 常用于Image generation。
1. SigLIP → 常用于Image understanding。
1. Encoder + DiT Decoder。
1. TiTok → 将2D image转为1D token sequence。
1. Next-token prediction
1. Block prediction
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
1. 对Visual tokens做约束
1. 使用Diffusion decoder作为de-tokenizer，从而只需使用diffusion loss，能摒弃L1 loss、LPIPS loss和GAN loss。

---

### Image tokenization的论文整理
#### 2024.06，An Image is Worth 32 Tokens for Reconstruction and Generation
想解决的问题：VQ-VAE处理得到的tokens存在the inherent redundancies present in images。
核心思想：将Image转为1D latent sequence。
具体做法：
1. Encoder：将image patches和latent tokens喂给ViT，期望latent tokens能学到image patches的信息。
1. Decoder：将latent tokens和mask patches喂给ViT，输出image patches。
1. 对1D token sequence做各种约束：nested dropout、nested CFG、causal attention masking。
1. 使用Vision foundation model的feature做约束。
1. 使用Text tokenizer得到的text tokens做约束。

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

##### 3D LLM的pipeline总结

[https://github.com/ActiveVisionLab/Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D)
[https://aicarrier.feishu.cn/wiki/GvibwrWumiYVxYk3Ik5c7Yd3nSb](https://aicarrier.feishu.cn/wiki/GvibwrWumiYVxYk3Ik5c7Yd3nSb)
pipeline整理：
1. 大部分论文的pipeline：Encoder → Projector → LLM
1. Encoder → LLM
1. Building object set → LLM
Point Encoder的variants
- 将2D image feature反投影到3D point clouds上，获得3D point clouds的feature
- Object-level encoder: I2P-MAE
- Object-level encoder: Recon++
- Object-level encoder: Point-BERT
- Object-level encoder: Ulip2 and Uni3D
- Object-level encoder: Vanilla transformer structurally equivalent to ViT + 2D model初始化
- Scene-level encoder: EPCL
- Scene-level encoder: Masked transformer encoder
- Scene-level encoder: PointNet++加上spatial transformer
- Scene-level encoder: Multi-view transformer + Fusion transformer
Projector的variants（用于关联Pre-trained vision models和Pre-trained LLMs，efficiently project these features in the pre-trained textual embedding space, enabling effective interpretation of 3D visual information）
- Perceiver: General perception with iterative attention
- QFormers：做aggregation，降低计算量
- An MLP
1. Encoder：对point clouds提取特征
1. Projector：使用projector将特征投影到LLM所需的point token
1. LLM：使用LLM预测token
1. An Embodied Generalist Agent in 3D World
1. ConceptGraphs
- 相关论文

##### 如何使用copilot和gpt辅助英语写作

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

###### 写作思路典例

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


##### 具身智能的pipeline总结

具身智能的pipeline（服务于最终的决策）：
- 根据observations做决策
- 根据之前的actions和observations做决策
- 根据observations和goal imagination做决策
- 用一些策略让representation中包含future information，然后根据learned representation和observations做决策
其他的相关工作：
- 主要做3D grounding的工作。大多数embodied AI的工作建立在强大的3D LLM的基础上
- 称为world model，但其实只是做future prediction，没有和planning接起来的工作
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

##### Ross Girshick的talk笔记

NLP部分的Take away message：
1. Ross认为NLP里的Parser是fake task。
1. Ross认为NLP里的real task是text generation。
1. NLP中之所以能成功，还有额外的原因：
CV部分的Take away message：
1. CV面临的问题：
1. Ross认为CV里的Real task是recognition
1. 我们需要思考CV里面哪些任务是“NLP领域的Parser”、是fake task
1. Ross认为CV里面最重要的科学问题（the most scientifically important direction）：基于人类日常接触的数据，设计并训练人工智能模型（Algorithms that learn with human-like data constraints）
Ross科研经验上的分享，虽然现在来看detection这个任务是错的，但他非常有收获
> 💡 抱着尝鲜、获得新知识的姿态来探索有意思的科学问题、技术问题，会非常fruitful。
（Trying to solve a scientifically interesting problem with no other motivation than gaining knowledge can be extremely fruitful）

我的个人理解：如果整天只想着让一个事情work，导致只敢用一些well established techniques，这样在研究上反而失去意义了。
1. Massive high-quality data
1. Supervised training
1. Test task = training task，NLP里text generation确实是最重要的目标了
1. Image/Video generation虽然重要，但不是CV领域最重要的任务
1. 高质量的训练数据不多
1. Generation task难以说是感知/决策任务的good proxy task
> 💡 为什么有这样的结论，这是从CV的真正应用得出的结论。
1. 对于弱视的人，CV要做的是Open-ended visual QA about the real world
2. 对于robot，CV要做的是“cook me dinner”
3. 对于internet agent，CV要做的是“shop for me”
> 💡 **思考的方法论，**Real task不一定需要哪些intermediate tasks，只是我们人为地认为他们需要：
1. classification, detection, segmentation
2. 3D reconstruction
> 💡 人类日常接触的数据的特征：
1. Ego-centric video
2. Limited embodied control
3. Observations have very different statistics cf. web data
4. Long term

##### LeCun Talk笔记

LeCun认为的关键AI能力：
1. 关于世界如何运作的心理模型
1. 拥有持久的记忆
1. 能够规划复杂动作序列
1. 可控和安全的系统
过去AI成功的关键：自监督学习
1. 目标：试图以一种良好的方式表示input。
1. 流行范式：从损坏中重建。训练一个巨大的神经网络来重建完整的、未损坏的版本。
1. Message：
自回归预测：典型的自监督学习模型
1. 输入和输出：给它看一段文本，你让它预测文本中的下一个单词或下一个标记。
1. 局限性：
1. 推论：我们通过让系统观看视频或生活在现实世界中来学习常识和物理直觉。
更强大的AI系统：
1. 直觉：
1. 正式的流程：
1. 和已有“模型预测控制”方法的区别：
1. 新AI系统的组件：
1. 仍未解决的问题：
当前学习世界模型的范式：
1. 自监督学习只有从冗余数据中学习到一些有用的东西，如果数据是高度压缩的，这意味着它是完全随机的。
1. 没有通常意义上的真正推理。
1. 只适用于以离散对象、符号、标记、单词这些你可以离散化的数据。
1. 参考人类婴儿的智力发育，不可能通过仅仅训练文本就达到接近人类水平的智力。
1. 推理过程不仅仅是运行神经网络的几层，而是实际上运行一个优化算法。
1. 人类的感知系统就是这样做的，如果你对一个特定的感知有多个解释，你的大脑会自发地循环遍历这些解释。
1. 想象你可能会采取的一系列动作。
1. 你的世界模型将允许你预测这一系列动作对世界的影响，以及预测世界中将要发生的事情的整个轨迹。
1. 将世界模型的预测馈送到一堆目标函数，一个目标函数测量目标实现的程度，任务完成的程度。
1. 迭代a-c步，找到使这些目标最小化的动作序列。有两种最小化方法：
1. 可以通过搜索离散选项。
1. 一个更好的方法是确保a-c步都是可微的，你通过它们反向传播梯度，并使用梯度下降来更新动作序列。
1. 我们正在学习世界模型。
1. 我们正在学习将提取世界情况的适当抽象表示的感知系统。
1. 世界模型
1. 可以根据手前任务配置的成本函数
1. 执行器，它是真正优化的模块，根据世界模型找到最佳动作序列
1. 短期记忆
1. 感知系统
1. 分层规划
1. 如何学习具有层次结构、在几个不同抽象层次上工作的世界模型
1. 具体做法：取一个输入，以某种方式破坏它，并训练一个大型神经网络来预测缺失的部分。如果你训练一个系统来预测视频中将要发生的事情，就像我们训练神经网络来预测文本中将要发生的事情一样。
1. **Message：LeCun认为是一个失败的范式**
1. 为什么失败：因为有很多可能的未来，在像文本这样的离散空间中，你无法预测哪个单词将跟随一个单词序列，但你可以生成字典中所有可能单词的概率分布。但如果是视频，视频帧，**我们没有很好的方法来表示视频帧上的概率分布**。
LeCun推崇的新的世界模型学习范式：联合嵌入预测架构
1. 具体做法：
1. 本质：学习一个关于世界中发生的事情的抽象表示，然后在该表示空间中预测该抽象表示的未来状态。
1. 难点：如果你只是使用梯度下降、反向传播来训练这样的系统，以最小化预测误差，将会崩溃。它将学习一个常数的表示，使预测变得超级容易。
1. 如何防止学习过程崩塌：
1. 举例解释：如果我拍下这个房间的视频，我拿一个相机，我拍下那部分，然后我停止视频，我让系统预测视频中的下一个是什么，它可能会预测在某个时候会有房间的其余部分，会有墙，会有人坐着，密度可能与左边相似，但它不可能在像素级别上准确地预测你们所有人的样子，世界的纹理是什么样子，房间的精确大小，以及所有类似的事情。你不可能准确地预测所有这些细节。
1. **我的个人理解：用白话说，就是像素信息太丰富，而且太冗余，不适合用来作为未来预测的目标。**
1. 输入：x的损坏版本、y
1. 编码：encoder 1编码损坏的x，encoder 2编码y
1. 目标：基于x的表示预测y的表示。
1. 方法一：有一些成本函数来测量来自编码器的表示的信息内容，并尝试最大化信息内容或最小化负信息。→ 希望从输入中提取尽可能多的信息。 → LeCun没有详细讲如何测量信息。
1. 方法二：蒸馏式方法。只更新这个架构的一半，不在另一半上反向传播梯度，然后以一种有趣的方式共享权重。
