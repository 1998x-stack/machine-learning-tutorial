# 机器学习图解教程 · Machine Learning, Explained

一条从问题、数学、传统算法到深度学习、现代 NLP、生成建模与强化学习的中文学习路线。全书 28 章，其中 **01–25 章已五批深度重构**；26–28 章保留原稿，等待下一轮逐篇技术审计。

- [GitHub Pages 首页](https://1998x-stack.github.io/machine-learning-tutorial/)
- [课程索引](docs/index.html)
- [写作与验收规范](AGENTS.md)
- [技术来源与证据边界](docs/references.md)

## 课程进展

| 批次 | 章节 | 重构重点 | 状态 |
| --- | --- | --- | --- |
| 第一批 | 01–05 | 学习范式、线性代数、概率、优化、数据预处理 | 完成正文、数学和 10 幅章节 SVG |
| 第二批 | 06–10 | 端到端回归项目、评估、线性/逻辑回归、树与森林 | 完成正文、15 幅 SVG、可操作阈值实验 |
| 第三批 | 11–15 | SVM、朴素贝叶斯/KNN、聚类、降维/特征、调参与 AutoML | 完成正文、15 幅 SVG、可运行示例 |
| 第四批 | 16–20 | 不平衡分类、XAI、MLOps、神经网络、PyTorch | 完成正文、18 幅 SVG、证据台账与可运行示例 |
| 第五批 | 21–25 | CNN、RNN/LSTM、NLP/Transformer、GAN/VAE/Diffusion、强化学习 | 完成正文、20 幅 SVG、证据台账与可运行示例 |
| 待精修 | 26–28 | LLM/RAG、模型部署、端到端毕业项目 | 原稿保留，未作深度技术审计 |

### 第五批完成的五章

| 章节 | 核心问题 | 图解与实验 |
| --- | --- | --- |
| [21 · 卷积神经网络](docs/chapters/21.html) | 卷积如何利用空间局部性，深层网络如何优化？ | 卷积窗口、输出形状、ResNet 捷径、迁移学习；PyTorch shape/gradient/augmentation 检查 |
| [22 · 循环神经网络](docs/chapters/22.html) | 如何跨时间步保留信息并对齐输入输出？ | RNN 展开、LSTM 门控、Attention 对齐、梯度路径；RNN/LSTM 张量和 mask 实验 |
| [23 · 自然语言处理](docs/chapters/23.html) | 文本怎样成为 token，模型怎样利用上下文？ | 子词流水线、自注意力、双向/因果 mask、MLM 对比；SGNS 与 attention 张量实验 |
| [24 · 生成式模型](docs/chapters/24.html) | GAN、VAE、Diffusion 和自回归分别学习什么？ | 生成范式、GAN 博弈、VAE 潜变量、扩散链；采样、ELBO 与加噪实验 |
| [25 · 强化学习](docs/chapters/25.html) | 如何通过行动反馈优化长期回报？ | Agent–Environment、MDP/Bellman、Q 更新、DQN/Actor-Critic；Q-Learning、TD target、REINFORCE/PPO 实验 |

每篇新文章独立解释问题、符号、假设、机制、代码形状与失败边界。重要事实记录在 `docs/evidence/21.json` 至 `25.json`，并同步进入 `docs/references.md`。所有示意图均原创；手工数字、合成数据和简化实现不会伪装成论文 benchmark。

## 仓库结构

    docs/
    ├── index.html                         # 课程门户、学习路线、28 章目录与搜索
    ├── chapters/
    │   ├── 01.html ... 25.html            # 按独立长文规范重构
    │   ├── 26.html ... 28.html            # 原稿保留，待技术审计
    │   └── theme.css                      # 旧文兼容样式
    ├── assets/
    │   ├── css/{site,article,labs}.css    # 共享视觉/文章/交互设计系统
    │   ├── js/{site,threshold-lab}.js
    │   └── svg/01/...25/                  # 78 幅章节机制图 + 1 幅首页图
    ├── evidence/16.json ... 25.json       # 逐章主张—来源—状态台账
    ├── courses.json                       # 28 章目录单一来源
    └── references.md                      # 一手论文、官方 API 与适用边界
    examples/
    ├── 06_california_housing.py           # 可选网络下载的历史区域房价数据
    └── 15_optuna_search.py                # 可选 Optuna 搜索示例
    scripts/
    ├── validate_site.py                   # 资源路径、语义结构、SVG XML、证据台账
    ├── run_examples.py                    # 01–25 章正文代码块逐个执行
    └── browser_qa.py                      # 78 组页面/视口检查
    .github/workflows/                     # PR QA 和 Pages 部署
    AGENTS.md                              # 写作、数学、SVG、证据及验收门禁

## 本地预览和验收

    python3 -m http.server 8000
    # http://localhost:8000/docs/

    python3 -m pip install numpy pandas scikit-learn imbalanced-learn shap mlflow joblib
    python3 -m pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
    python3 -m pip install playwright
    python3 -m playwright install chromium

    python3 scripts/validate_site.py
    python3 scripts/run_examples.py
    python3 scripts/browser_qa.py

CI 的 Python 示例路径使用 CPU PyTorch；CUDA AMP 仅在具有兼容 CUDA 设备的环境中启用，CPU CI 不冒充 GPU 性能验证。浏览器检查覆盖首页和前 25 章在 1440/390/360px 的页面溢出、图片、MathML 与搜索/阈值交互。19 个新增 Python 代码块覆盖卷积、残差块、序列状态、attention mask、SGNS、GAN/VAE/DDPM、Q-Learning、DQN 和 PPO 目标。

可选脚本：首次下载 California Housing 历史区域数据需要联网；Optuna 搜索脚本需要额外安装 optuna。California Housing 是历史街区级别数据，不代表当代单套房产交易；Optuna 脚本是可选搜索演示。未在 CI 或终端实际运行的外部示例不得标注为已验收。

## 发布与设计约束

GitHub Pages 使用 `.github/workflows/deploy-pages.yml` 从 `main` 部署 `docs/`。在 Pages 设置中选 GitHub Actions；PR 经静态、代码、浏览器检查后方可合并。参考 [Olah-style-posts](https://github.com/1998x-stack/Olah-style-posts) 的渐进解释、图解分镜、公式语义、证据台账和浏览器验收方法；文章文字与 SVG 均独立制作，不复制其视觉资产或原文。

每篇必须独立解释定义、变量及适用条件，区分论文结论、官方 API 行为、推导值、教学示例和真实实验输出。全站支持无 JS 正文阅读、键盘导航、局部横向滚动、MathML 与打印排版。
