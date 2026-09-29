## 《深度强化学习》学习笔记

#### 需要学习的知识点
1. Value-based RL（深度Q函数，DQN及其训练方法）
1. DQN
1. DQN的训练方法（时间差分 (TD) 算法）
1. Value-based RL的高级技巧（如何提升Value-based RL的效果）
1. 经验回放
1. 高估问题及解决方法（Target Network、Double DQN）
1. 对决网络 (Dueling Network)
1. 噪声网络
1. Multi-step TD target
1. Policy-based RL（深度策略函数）
1. 策略网络
1. 怎么通过策略梯度优化策略网络
1. 怎么计算策略梯度-方法1：REINFORCE
1. 怎么计算策略梯度-方法2：Actor-Critic
1. Actor
1. Critic：动作价值函数
1. 如何学习动作价值函数（SARSA算法、Reward model）
1. 策略学习高级技巧（如何提升Policy-based RL的效果）
1. 带基线的策略梯度方法
1. 策略梯度中的基线
1. 带基线的 REINFORCE 算法
1. Advantage Actor-Critic (A2C)
1. Trust Region Policy Optimization (TRPO)：一种策略学习方法，可以代替策略梯度方法
1. PPO：改进TRPO
1. 熵正则 (Entropy Regularization)
1. 异策略（离线策略）
1. 深度确定策略梯度（DDPG）
1. SAC
1. Model-based RL
1. 深度Model-based RL
1. 模型预测控制
1. Model-based Policy Optimization
1. 传统Model-based RL（因为很经典，所以了解一下）：动态规划
1. Dyna-Q
1. 模仿学习
1. 行为克隆
1. 逆向强化学习
1. 生成判别模仿学习 (GAIL)
1. 离线强化学习
1. 元强化学习
1. RL的Open Challenges
1. 怎么构建Model
1. 如何提升Sampling Efficiency
1. 如何在奖励函数并不明确的场景下学习有效的策略
1. 如何在奖励稀疏的场景下学习有效的策略
1. 多智能体强化学习

---

#### 知识点笔记
- **深度Q函数（DQN及其训练方法）**
- **Value-based RL的高级技巧（如何提升Value-based RL的效果）**
- **深度策略函数（策略学习）**
- **如何基于Actor-Critic优化深度策略函数**
- **策略学习高级技巧（如何提升Policy-based RL的效果）1：带基线的策略梯度方法**
- **策略学习高级技巧（如何提升Policy-based RL的效果）2：Trust Region Policy Optimization (TRPO)**
- **策略学习高级技巧（如何提升Policy-based RL的效果）3：PPO**
- **策略学习高级技巧（如何提升Policy-based RL的效果）4：熵正则 (Entropy Regularization)**
- **策略学习高级技巧（如何提升Policy-based RL的效果）5：异策略（离线策略）**
- **模型预测控制**
- **Model-based Policy Optimization**
- **传统Model-based RL（因为很经典，所以了解一下）**
- **离线强化学习**
- **元强化学习**

---

#### 参考材料
超级清楚的深度强化学习课程：[https://www.bilibili.com/video/BV12o4y197US/?vd_source=1b53504d594b3b106e5065f1298139ba](https://www.bilibili.com/video/BV12o4y197US/?vd_source=1b53504d594b3b106e5065f1298139ba)
介绍PPO、Model-based RL：[https://www.bilibili.com/video/BV199pzeUEMA?vd_source=1b53504d594b3b106e5065f1298139ba&spm_id_from=333.788.videopod.sections](https://www.bilibili.com/video/BV199pzeUEMA?vd_source=1b53504d594b3b106e5065f1298139ba&spm_id_from=333.788.videopod.sections)
书本：[https://github.com/wangshusen/DRL/tree/master/Notes_CN](https://github.com/wangshusen/DRL/tree/master/Notes_CN)
判断自己是否真得懂了这些算法，看这个教程里的代码，看看是否能看懂：[https://hrl.boyuai.com/chapter/2/dqn算法](https://hrl.boyuai.com/chapter/2/dqn%E7%AE%97%E6%B3%95)
[http://rail.eecs.berkeley.edu/deeprlcourse/](http://rail.eecs.berkeley.edu/deeprlcourse/)
[https://github.com/wangshusen/DRL](https://github.com/wangshusen/DRL)
学习资料：[https://www.xiaogeedu.net/sys-nd/199.html](https://www.xiaogeedu.net/sys-nd/199.html)
