# 机器学习图解教程 · Machine Learning, Explained

一条从**直觉、原理、机制 SVG、数学推导、可运行代码到失败模式**的中文机器学习学习路线。全书 28 章，其中 **01–15 章已三批重构**，16–28 章保持旧稿等待技术审计。

[GitHub Pages 首页](https://1998x-stack.github.io/machine-learning-tutorial/) · [课程索引](docs/index.html) · [AGENTS.md 写作与验证规范](AGENTS.md) · [技术来源](docs/references.md)

## 课程进展

| 批次 | 章节 | 重构重点 | 状态 |
| --- | --- | --- | --- |
| 第一批 | 01–05 | 学习范式、线性代数、概率、优化、数据预处理 | 完成正文、数学和 10 幅章节 SVG |
| 第二批 | 06–10 | 端到端回归项目、评估、线性/逻辑回归、树与森林 | 完成正文、15 幅 SVG、可操作阈值实验 |
| 第三批 | 11–15 | SVM、朴素贝叶斯/KNN、聚类、降维/特征、调参与 AutoML | 完成正文、15 幅 SVG、可运行示例 |
| 待精修 | 16–28 | 后续传统 ML、神经网络、现代应用与部署 | 原稿保留，未作深度技术审计 |

### 新完成的 5 章

| 章节 | 重点解释 | 机制图 |
| --- | --- | --- |
| [11 · SVM](docs/chapters/11.html) | 最大间隔、支持向量、hinge loss、核与 C/gamma | 间隔、损失曲线、RBF 影响 |
| [12 · 朴素贝叶斯与 KNN](docs/chapters/12.html) | 条件独立、Laplace 平滑、近邻投票、维度影响 | NB 证据分解、词频概率、最近邻 |
| [13 · 聚类](docs/chapters/13.html) | K-Means 迭代、DBSCAN 密度、层次合并、Silhouette | 质心更新、核心/边界/噪声、轮廓 |
| [14 · 降维与特征工程](docs/chapters/14.html) | PCA、t-SNE、特征选择、目标编码交叉拟合 | 降维目标、筛选路径、编码防泄漏 |
| [15 · 超参数优化](docs/chapters/15.html) | Grid/Random、Nested CV、Optuna、pruning | 搜索覆盖、嵌套评估、预算分配 |

所有章节均可从 [课程首页](docs/index.html) 访问，也可直接使用 `docs/chapters/NN.html` 的相对路径。旧的根目录及 Pages 章节地址保留重定向入口。

## 目录

```text
docs/
├── index.html                       # 首页、学习路线、28 章目录与搜索
├── chapters/
│   ├── 01.html ... 15.html          # 按独立长文规范精修
│   ├── 16.html ... 28.html          # 迁移旧稿，待技术审计
│   └── theme.css                    # 旧文兼容样式
├── assets/
│   ├── css/{site,article,labs}.css  # 共享视觉/文章/交互设计系统
│   ├── js/{site,threshold-lab}.js
│   └── svg/01/...15/                # 40 幅章节机制图 + 首页图
├── courses.json                     # 28 章目录数据
└── references.md                    # 事实、一手文献与 API 来源
examples/
├── 06_california_housing.py         # 可选网络下载的真实历史房价数据
└── 15_optuna_search.py              # 可选 Optuna 搜索示例
scripts/
├── validate_site.py                 # 资源路径、语义结构与 SVG XML
├── run_examples.py                  # 01–15 章代码块逐个执行
└── browser_qa.py                    # 48 组浏览器尺寸/页面测试
.github/workflows/                  # PR QA 和 Pages 部署
AGENTS.md                            # 编辑、数学、SVG、证据及验收门禁
```

## 本地预览和验收

```bash
python3 -m http.server 8000
# http://localhost:8000/docs/

python3 -m pip install numpy pandas scikit-learn playwright joblib
python3 -m playwright install chromium

python3 scripts/validate_site.py
python3 scripts/run_examples.py
python3 scripts/browser_qa.py
```

在 GitHub Actions 中，静态检查覆盖全部 28 章位置、前 15 章新模板、40 幅章节 SVG、双重旧链接和资源路径；Python 示例验证前 15 章所有正文代码块；浏览器检查覆盖首页与前 15 章在 1440/390/360px 下的图片、MathML、水平溢出和已有阈值交互。

可选脚本：

```bash
# 首次下载 California Housing 历史区域数据需联网
python3 examples/06_california_housing.py

# 需要额外 optuna 依赖，不计入正文默认离线实验
python3 -m pip install optuna
python3 examples/15_optuna_search.py
```

California Housing 是历史街区级别数据，不能代表当代单套房产交易；Optuna 脚本额外输出真实搜索结果，但不能将它当作任何真实业务的最优模型。**未在 CI 或终端实际运行的外部示例不得标注为“已验收”。**

## 发布与设计约束

GitHub Pages 使用 `.github/workflows/deploy-pages.yml` 从 `main` 部署 `docs/`。在 Pages 设置中选 **GitHub Actions**；PR 经静态、代码、浏览器检查后方可合并。参考 [Olah-style-posts](https://github.com/1998x-stack/Olah-style-posts) 的循序解释原则，但图形和正文均独立制作，不复制其视觉资产或原文。

每篇必须独立解释定义、变量及适用条件，区分“公式解析的教学值”“手工示例”“真实运行的实验输出”。全站应支持无 JS 正文阅读、可聚焦导航、屏幕窄时局部横向滚动、MathML 与打印排版。
