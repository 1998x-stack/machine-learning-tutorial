# 机器学习图解教程 · Machine Learning, Explained

一条从 **问题 → 直觉 → 原创图解 → 数学推导 → 代码复核 → 适用边界** 的中文机器学习学习路线，共 28 章。

[课程首页](docs/index.html) · [GitHub Pages](https://1998x-stack.github.io/machine-learning-tutorial/)（上线状态以实际部署为准） · [内容工程规范](AGENTS.md) · [来源与核验](docs/references.md)

## 精修批次一 · 01–05

| 章节 | 重点问题 | 图解 |
| --- | --- | --- |
| [01 机器学习概述](docs/chapters/01.html) | 监督信号、经验风险、泛化与数据切分 | 学习范式 / 训练验证测试 |
| [02 线性代数](docs/chapters/02.html) | 矩阵乘法、维度、PCA 与 SVD | 逐元素乘法展开 / PCA 主轴 |
| [03 概率统计](docs/chapters/03.html) | 贝叶斯基准率、MLE 与 MAP | 检测树 / 似然与后验 |
| [04 优化理论](docs/chapters/04.html) | 梯度下降、学习率、链式法则 | 收敛发散轨迹 / 反向传播 |
| [05 预处理与 EDA](docs/chapters/05.html) | 缺失值、管线与信息泄漏 | 正误流程 / ColumnTransformer |

其余 **11–28** 已原样迁移至 `docs/chapters/`，还未完成逐章数学与代码技术审计。所有根目录 `01.html`–`28.html` 是旧地址兼容跳转，避免破坏外部链接。

## 目录结构

```text
docs/
├── index.html                      # 全站门户、章节搜索及学习路线
├── courses.json                    # 28 篇原始章节元数据
├── chapters/
│   ├── 01.html ... 10.html         # 独立重构长文
│   ├── 11.html ... 28.html         # 原稿迁移，等待下批次
│   └── theme.css                   # 老页面的向后兼容样式
├── assets/
│   ├── css/site.css                # 门户 tokens & responsive
│   ├── css/article.css             # 文章排版、公式、打印和导航
│   ├── js/site.js                  # 首页无依赖搜索增强
│   └── svg/01...10/               # 25 幅独立章节 SVG
└── references.md                   # 技术来源及证据边界
scripts/validate_site.py            # 无依赖静态验证
.github/workflows/validate.yml      # PR / push 自动质量检查
.github/workflows/deploy-pages.yml  # main 部署 docs 到 Pages
AGENTS.md                           # 编辑、SVG、数学、QA 与发布规范
index.html, 01.html...28.html       # 老链接转发层
```

## 本地预览与校验

只需要 Python 3.10+：

```bash
python3 -m http.server 8000
# 浏览 http://localhost:8000/docs/
python3 scripts/validate_site.py
```

每篇正文不依赖 CDN。文章中的代码示例按照自身依赖说明单独执行，例如 NumPy、pandas、scikit-learn。静态脚本验证文件、相对路径、SVG XML、目录数量等；**不等同于浏览器截图与实验执行测试**。桌面 1440px、移动端 390/360px、键盘交互、公式显示与 print 仍需按 AGENTS.md 做浏览器复审。

## GitHub Pages 配置

推荐 **Settings → Pages → Build and deployment → GitHub Actions**。合并至 `main` 后，`deploy-pages.yml` 会校验并发布整个 `docs/`。若仍按仓库根目录发布，根目录首页及章节跳转文件可继续将读者带到 `docs/`，但最终部署需实际验证。PR 的存在并不代表已合并或上线。

## 设计原则

优先保证独立可读、论证正确和证据可追踪；每幅 SVG 的箭头必须对应有意义的计算或数据依赖；所有数值教学示例注明它不是论文实验。启发于 [Olah-style-posts](https://github.com/1998x-stack/Olah-style-posts) 及相关解释性写作实践，图解与正文为重新设计，不复制原作。

## 精修批次二 · 06–10

| 章节 | 内容核心 | 新机制图 |
|---|---|---|
| [06 端到端项目](docs/chapters/06.html) | 划分、常数基线、残差、可选 California Housing | 数据边界、模型比较、残差审计 |
| [07 模型评估](docs/chapters/07.html) | 混淆矩阵、阈值滑块、AP / AUC、交叉验证 | 四格指标、分数排序、CV |
| [08 线性回归](docs/chapters/08.html) | OLS、Ridge/Lasso/ElasticNet | 残差、约束几何、系数路径 |
| [09 逻辑回归](docs/chapters/09.html) | Sigmoid、交叉熵、决策阈值与校准 | S 曲线、损失函数、校准流程 |
| [10 树与森林](docs/chapters/10.html) | Gini、剪枝、bootstrap、OOB、置换重要性 | 树分裂、袋外、重要性审计 |

### 执行示例与浏览器 QA

```bash
python3 -m pip install numpy pandas scikit-learn playwright joblib
python3 -m playwright install chromium
python3 scripts/validate_site.py
python3 scripts/run_examples.py
python3 scripts/browser_qa.py
```

十篇内嵌示例在 CI 独立运行。第 06 章另有 `examples/06_california_housing.py`，需要联网下载历史住房区域数据，不属于离线 CI 实验：

```bash
python3 examples/06_california_housing.py
```

该数据不是现代单套房产现价；地理组隔离是教学划分策略，不能当作对当前市场的泛化保证。浏览器检查覆盖首页与 01–10 章节 × 1440/390/360 px，并实际操作章节 07 阈值滑块。
