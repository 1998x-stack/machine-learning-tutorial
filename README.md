# 机器学习图解教程 · Machine Learning, Explained

一条从问题、数学、算法、可解释性到深度学习工程的中文机器学习学习路线。全书 28 章，其中 **01–20 章已四批深度重构**；21–28 章保留原稿，等待下一轮逐篇技术审计。

GitHub Pages 首页：https://1998x-stack.github.io/machine-learning-tutorial/
课程索引：docs/index.html
写作规范：AGENTS.md
技术来源：docs/references.md

## 课程进展

| 批次 | 章节 | 重构重点 | 状态 |
| --- | --- | --- | --- |
| 第一批 | 01–05 | 学习范式、线性代数、概率、优化、数据预处理 | 完成正文、数学和 10 幅章节 SVG |
| 第二批 | 06–10 | 端到端回归项目、评估、线性/逻辑回归、树与森林 | 完成正文、15 幅 SVG、可操作阈值实验 |
| 第三批 | 11–15 | SVM、朴素贝叶斯/KNN、聚类、降维/特征、调参与 AutoML | 完成正文、15 幅 SVG、可运行示例 |
| 第四批 | 16–20 | 不平衡分类、XAI、MLOps、神经网络、PyTorch | 完成正文、18 幅 SVG、证据台账与可运行示例 |
| 待精修 | 21–28 | CNN、序列模型、NLP、生成模型、强化学习、LLM/RAG、部署、毕业项目 | 原稿保留，未作深度技术审计 |

### 第四批新完成的五章

| 章节 | 核心问题 | 图解与实验 |
| --- | --- | --- |
| [16 · 不平衡分类](docs/chapters/16.html) | 为什么 Accuracy 会掩盖少数类失败？ | 混淆矩阵、SMOTE 插值、PR/阈值；验证集选成本阈值，测试集不重采样 |
| [17 · 模型可解释性](docs/chapters/17.html) | 归因能否解释现实因果？ | SHAP waterfall、LIME 局部代理、PDP/ICE；验证加法一致性与局部拟合 |
| [18 · ML 系统工程化](docs/chapters/18.html) | 怎样让实验可追溯、服务可回滚？ | MLOps pipeline、离线/在线特征、模型谱系；Pipeline 与 MLflow Tracking 实验 |
| [19 · 神经网络基础](docs/chapters/19.html) | 深层网络如何传递信号与梯度？ | 神经元张量形状、激活曲线、反向传播、初始化、BN/Dropout；有限差分核验梯度 |
| [20 · PyTorch 训练实战](docs/chapters/20.html) | 怎样构成正确、可恢复的训练循环？ | Autograd DAG、DataLoader、训练步、Checkpoint/AMP；CPU 训练与状态恢复实验 |

每篇新文章独立解释问题、符号、假设、机制和失败条件；docs/evidence/16.json 至 20.json 将重要主张映射到官方文档或原始论文。所有图中手工数字均标明是推导或教学示例，不伪装成 benchmark。

## 仓库结构

    docs/
    ├── index.html                         # 课程门户、学习路线、28 章目录与搜索
    ├── chapters/
    │   ├── 01.html ... 20.html            # 按独立长文规范重构
    │   ├── 21.html ... 28.html            # 原稿保留，待技术审计
    │   └── theme.css                      # 旧文兼容样式
    ├── assets/
    │   ├── css/{site,article,labs}.css    # 共享视觉/文章/交互设计系统
    │   ├── js/{site,threshold-lab}.js
    │   └── svg/01/...20/                  # 58 幅章节机制图 + 首页图
    ├── evidence/16.json ... 20.json       # 逐章主张—来源—状态台账
    ├── courses.json                       # 28 章目录单一来源
    └── references.md                      # 一手论文、官方 API 与适用边界
    examples/
    ├── 06_california_housing.py           # 可选网络下载的历史区域房价数据
    └── 15_optuna_search.py                # 可选 Optuna 搜索示例
    scripts/
    ├── validate_site.py                   # 资源路径、语义结构、SVG XML、证据台账
    ├── run_examples.py                    # 01–20 章正文代码块逐个执行
    └── browser_qa.py                      # 63 组页面/视口检查
    .github/workflows/                     # PR QA 和 Pages 部署
    AGENTS.md                              # 写作、数学、SVG、证据及验收门禁

## 本地预览和验收

    python3 -m http.server 8000
    # http://localhost:8000/docs/

    python3 -m pip install numpy pandas scikit-learn imbalanced-learn shap mlflow-skinny joblib
    python3 -m pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
    python3 -m pip install playwright
    python3 -m playwright install chromium

    python3 scripts/validate_site.py
    python3 scripts/run_examples.py
    python3 scripts/browser_qa.py

GitHub Actions 的默认 Python 示例路径使用 CPU PyTorch；CUDA AMP 仅在具有兼容 CUDA 设备的环境中启用，CI 不把 CPU 测试冒充 GPU 性能验证。浏览器检查覆盖首页和前 20 章在 1440/390/360px 的页面溢出、图片、MathML 与搜索/阈值交互。

可选脚本：首次下载 California Housing 历史区域数据需要联网；Optuna 搜索脚本需要额外安装 optuna。California Housing 是历史街区级别数据，不代表当代单套房产交易；Optuna 脚本是可选搜索演示。未在 CI 或终端实际运行的外部示例不得标注为已验收。

## 发布与设计约束

GitHub Pages 使用 .github/workflows/deploy-pages.yml 从 main 部署 docs/。在 Pages 设置中选 GitHub Actions；PR 经静态、代码、浏览器检查后方可合并。参考 Olah-style-posts 的渐进解释、图解分镜、公式语义、证据台账和浏览器验收方法；文章文字与 SVG 均独立制作，不复制其视觉资产或原文。

每篇必须独立解释定义、变量及适用条件，区分论文结论、官方 API 行为、推导值、教学示例和真实实验输出。全站支持无 JS 正文阅读、键盘导航、局部横向滚动、MathML 与打印排版。
