# 机器学习图解教程 · Machine Learning, Explained

一个以独立长文、原创 SVG、语义化 MathML、可复现 Python 实验和一手证据为核心的中文机器学习知识库。课程包含 **28 章，已完成六批逐章重构**：从数学基础、经典 ML、模型评估，到深度学习、Transformer、RAG、可靠部署与完整端到端项目。

- [GitHub Pages 课程首页](https://1998x-stack.github.io/machine-learning-tutorial/)
- [在线课程目录（源文件）](docs/index.html)
- [写作、SVG、MathML 与质量门禁](AGENTS.md)
- [一手论文与官方 API 来源](docs/references.md)

## 28 章进展

| 批次 | 章节 | 工程成果 |
| --- | --- | --- |
| 第一批 | 01–05 | 学习范式、线性代数、概率、优化、预处理；10 幅章节 SVG |
| 第二批 | 06–10 | 第一个 ML 项目、模型评估、线性/逻辑回归、树与森林；15 幅 SVG 与阈值交互 |
| 第三批 | 11–15 | SVM、NB/KNN、聚类、降维、模型选择；15 幅 SVG 和代码 |
| 第四批 | 16–20 | 类别不平衡、可解释性、MLOps、神经网络、PyTorch；18 幅 SVG、证据台账 |
| 第五批 | 21–25 | CNN、RNN/LSTM、NLP/Transformer、生成式模型、强化学习；20 幅 SVG、证据台账 |
| **第六批** | **26–28** | **LLM/RAG/Agent/LoRA、模型服务与 ONNX、时序数据安全的毕业项目；15 幅 SVG、证据台账** |

### 第六批：最后三章

| 页面 | 新增机制图 | 可运行实验与关键纠错 |
| --- | --- | --- |
| [26 · LLM、RAG、Agent 与 LoRA](docs/chapters/26.html) | KV Cache、RAG 双路径、检索门禁、LoRA 矩阵与 Agent 控制器 | KV shape、权限感知词法检索、工具白名单、低秩梯度；引用不等于事实真值，prompt 不能替代 ACL |
| [27 · 模型部署与服务化](docs/chapters/27.html) | 输入/服务契约、延迟预算、ONNX parity、金丝雀发布、漂移监控 | FastAPI TestClient、人工延迟分布、ONNX Runtime 等价检查、回滚决策；async 不会自动加速 CPU 推理 |
| [28 · 端到端毕业项目](docs/chapters/28.html) | 预测时点、7 天标签窗口、时序切分、全链路、增量实验、发布清单 | as-of 样本、label embargo、独立验证选阈值、工件 manifest、随机处理/对照；购买倾向不等于发券 uplift |

所有重构后的章节都应在没有前置上下文的情况下独立阅读，包含问题、符号与形状、机制、限制、实验和出处。机制图、训练数字及用户/政策数据为独立创作的教学示例，不冒充 benchmark 或真实业务。

## 工程结构

    docs/
    ├── index.html                       # 课程门户、5 个学习阶段、28 章目录与搜索
    ├── chapters/
    │   ├── 01.html ... 28.html          # 28 篇独立教程
    │   └── theme.css                    # 兼容旧章节资源
    ├── assets/
    │   ├── css/{site,article,labs}.css  # 共享设计与交互样式
    │   ├── js/{site,threshold-lab}.js
    │   └── svg/01/...28/                # 93 幅独立章节 SVG
    ├── evidence/16.json ... 28.json     # 逐章主张、出处定位与证据状态
    ├── courses.json                     # 单一章节元数据目录
    └── references.md                    # 一手论文、官方 API 与适用范围
    examples/                            # 可选网络数据/Optuna 扩展实例
    scripts/
    ├── validate_site.py                 # 28 篇、94 SVG、链接与证据台账
    ├── run_examples.py                  # 01–28 章正文代码块逐个运行
    └── browser_qa.py                    # 87 页面×视口组合、MathML、SVG、搜索与交互
    .github/workflows/                   # PR 静态/Python/Playwright CI 和 Pages 部署
    AGENTS.md                            # 规范、适用条件与放行门禁

## 本地验收

    python3 -m http.server 8000
    # 打开 http://localhost:8000/docs/

    python3 -m pip install numpy pandas scikit-learn imbalanced-learn shap mlflow joblib
    python3 -m pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
    python3 -m pip install fastapi httpx skl2onnx onnx onnxruntime playwright
    python3 -m playwright install chromium

    python3 scripts/validate_site.py
    python3 scripts/run_examples.py
    python3 scripts/browser_qa.py

- **静态检查**：28 章完整、旧 URL 重定向保留、SVG XML 与图注/资源路径正确、证据台账字段完整。
- **代码检查**：独立执行正文 Python 示例；人工数据不代表实际数据质量或模型基准。
- **浏览器检查**：课程首页 + 28 章 × 1440/390/360px，共 87 个视口—页面组合；检查水平溢出、图片解码、MathML、搜索以及第 07 章阈值互动。
- **外部服务边界**：若没有实际运行 FastAPI 对外服务、构建 Docker 镜像、部署云基础设施或采集真实电商标签，则不能把这些工作标成通过。CPU CI 也不代表 GPU/CUDA AMP 已验证。

加州住房数据首次下载需网络；Optuna 扩展示例需额外依赖。最新代码中的 RAG 是词法检索教学例子，不调用外部模型，也不是生产的语义检索；毕业项目使用合成用户事件与模拟 A/B 数据。

## 页面发布与设计来源

静态站点由 `.github/workflows/deploy-pages.yml` 在 `main` 更新后部署 `docs/`；只有经 CI 与 GitHub PR 验收、合并并检查 GitHub Pages 工作流，才应声称网站发布完成。

文章的渐进解释、图解分镜、数学语义、证据边界和浏览器 QA 借鉴 [Olah-style-posts](https://github.com/1998x-stack/Olah-style-posts) 的规范，不复制其受限视觉资产。每一幅 SVG 和每一段中文正文独立制作。质量判断以可复现实验、官方接口和一手论文为准，不以“图解数量”代替数学及工程正确性。
