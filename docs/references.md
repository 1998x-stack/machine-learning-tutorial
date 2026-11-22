# 技术核查与证据边界

下列链接覆盖 01–28 章的官方资料、原始论文、公开数学证明与 API 约定；引用的是概念、算法定义和实现行为，图解及演示数据均重新制作。

| 章节 | 一手/权威来源 | 关注事项 |
|---|---|---|
| 01 | [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html) | 监督、无监督学习与 fit/predict/test 流程 |
| 02 | [NumPy linalg](https://numpy.org/doc/stable/reference/routines.linalg.html) · [SVD](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html) | shape 约束、矩阵乘法、分解的方向与维度 |
| 02 | [scikit-learn PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) | 训练数据中心化后，PCA 的方差与 SVD 关系 |
| 03 | [Bayes theorem proof](https://statproofbook.github.io/P/bayes-th.html) · [MAP definition](https://statproofbook.github.io/D/map.html) | 先验、似然、后验、分母、估计范围 |
| 04 | [Google ML Crash Course — Gradient descent](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent) · [Hyperparameters](https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters) | 目标、梯度、步长及收敛和不稳定性 |
| 05 | [scikit-learn Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) · [Pipeline/ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html) | 训练集外泄、transform 顺序、交叉验证 |
| 05 | [Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html) | 中位数填充、类别填充、缺失指示器 |

## 证据边界

图中点与轨迹都是用来解释几何关系或数值行为的人工构造示例，不是实际训练曲线或文献实验数据。代码输出除非有单独测试记录，否则只说明应观察的可验证性质。

## 第二批技术核查 · 06–10

| 章节 | 官方资料 | 必须保留的解释边界 |
|---|---|---|
| 06 | [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) · [GroupShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html) | 历史区域数据，首次下载需网络；地理分组不代表时间泛化 |
| 07 | [Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) · [Average Precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html) · [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) | AP 不等同梯形 PR AUC；阈值不得用测试集调优 |
| 08 | [Linear Models](https://scikit-learn.org/stable/modules/linear_model.html) · [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) · [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html) | Ridge/Lasso 惩罚目标与 alpha 量纲不同，不能直接对比强度 |
| 09 | [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) · [Calibration](https://scikit-learn.org/stable/modules/calibration.html) | sigmoid 不保证校准；区分排序、阈值与概率质量 |
| 10 | [RandomForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) · [Permutation Importance](https://scikit-learn.org/stable/modules/permutation_importance.html) | OOB 非独立测试；MDI 易受高基数影响，置换重要性受相关性影响 |

新绘制的 15 幅 SVG 是机制解释或人工教学数据；不冒充论文基准实验。远程 California Housing 下载脚本不在离线 CI 结果范围内。

## 第三批技术核查 · 11–15

以下官方资料核对的是原理、API 与适用条件。SVG 全部是原创的解析函数或明确声明的人造教学数据，不是实际 benchmark 曲线。

| 章节 | 一手/官方来源 | 边界和关键纠错 |
| --- | --- | --- |
| 11 | [SVM Guide](https://scikit-learn.org/stable/modules/svm.html) · [SVC API](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) | 几何间隔与函数间隔不同；C 控制违例惩罚，gamma 控制核局部尺度；核 SVM 受输入缩放和样本数限制 |
| 12 | [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html) · [MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) · [Neighbors](https://scikit-learn.org/stable/modules/neighbors.html) | 给定类别条件独立、非负词频与平滑的分母；KNN 依赖度量、尺度和维度 |
| 13 | [Clustering Guide](https://scikit-learn.org/stable/modules/clustering.html) · [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) · [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) | KMeans 局部最优及凸形偏好，DBSCAN min_samples 包括自身，Silhouette 不代表人群真值 |
| 14 | [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) · [Manifold](https://scikit-learn.org/stable/modules/manifold.html) · [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html) · [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html) | t-SNE 不保留全局簇距/密度；TargetEncoder.fit_transform 内部交叉拟合，fit().transform() 可能泄漏；时间/分组任务需自定义 CV；特征选择进入训练折 |
| 15 | [Grid/Random search](https://scikit-learn.org/stable/modules/grid_search.html) · [Nested CV example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html) · [Optuna search spaces](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/002_configurations.html) · [Optuna pruning](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html) | 搜索 CV 选择偏差；内层选参、外层评估；非迭代模型不能虚构 pruning 中间步骤 |

## 跨批次共用事实约束

- Docs 是 Pages 唯一构建工件；相对链接不能越过 `docs/`。指向 `examples/` 源码应直接使用 GitHub 仓库的网页 URL。
- 随机样本或合成数据的数值结果只能说明定义与算法，不代表真实应用准确率或因果效应。
- 对生成的公式曲线验证坐标和峰值，对邻域图核验距离、eps/min_samples 计数，对聚类中心核验平均值。未实测的算法性能图一律注明“示意”。

## 第四批技术核查 · 16–20

| 章节 | 一手论文 / 官方资料 | 必须保留的边界 |
|---|---|---|
| 16 | [SMOTE 原始论文](https://doi.org/10.1613/jair.953) · [imbalanced-learn Pipeline](https://imbalanced-learn.org/stable/references/generated/imblearn.pipeline.Pipeline.html) · [阈值调优](https://scikit-learn.org/stable/modules/classification_threshold.html) · [分类指标](https://scikit-learn.org/stable/modules/model_evaluation.html) | 采样只在训练折；测试分布不变；AP 与梯形 PR-AUC 区分；阈值由验证集和成本决定 |
| 17 | [SHAP 原论文](https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html) · [SHAP TreeExplainer](https://shap.readthedocs.io/en/latest/generated/shap.TreeExplainer.html) · [LIME 原论文](https://doi.org/10.1145/2939672.2939778) · [PDP/ICE](https://scikit-learn.org/stable/modules/partial_dependence.html) | 输出空间与背景分布要明确；相关特征改变归因；局部代理要报告 fidelity；预测解释不是因果解释 |
| 18 | [MLflow Tracking](https://mlflow.org/docs/latest/tracking/) · [Model Registry](https://www.mlflow.org/docs/latest/registry/) · [Feast](https://docs.feast.dev/) · [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) · [Hidden Technical Debt](https://proceedings.neurips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) | 区分 run 与 registry version/alias；point-in-time join 防止未来信息泄漏；MLOps level 是参考框架 |
| 19 | [Backpropagation](https://www.nature.com/articles/323533a0) · [Xavier](https://proceedings.mlr.press/v9/glorot10a.html) · [He initialization](https://openaccess.thecvf.com/content_iccv_2015/html/He_Delving_Deep_into_Rectifiers_Surpassing_Human-Level_Performance_on_ImageNet_ICCV_2015_paper.html) · [BatchNorm](https://proceedings.mlr.press/v37/ioffe15.html) · [PyTorch BatchNorm1d variance estimators](https://docs.pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html) · [Dropout](https://www.jmlr.org/beta/papers/v15/srivastava14a.html) | 初始化取决于 fan/激活；BN 训练与推理统计不同；Dropout 仅训练时随机失活；梯度与参数更新分离 |
| 20 | [Autograd](https://docs.pytorch.org/docs/stable/notes/autograd.html) · [DataLoader](https://docs.pytorch.org/docs/stable/data.html) · [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html) · [AMP](https://docs.pytorch.org/docs/stable/amp.html) · [Saving/Loading](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html) | logits/目标形状匹配；eval 与 grad mode 分离；完整续训需要 optimizer/scaler/scheduler 状态；torch.amp API 按设备和 dtype 使用；CPU CI 不代表 CUDA AMP 已验 |

每章的详细主张、来源定位、状态和限制记录在 docs/evidence/16.json 至 docs/evidence/20.json。18 幅新 SVG 中，数值与机制示例均为解析推导或教学构造；不冒充外部 benchmark。

## 第五批技术核查 · 21–25

| 章节 | 一手论文 / 官方资料 | 必须保留的边界 |
|---|---|---|
| 21 | [ResNet 原论文](https://arxiv.org/abs/1512.03385) · [PyTorch Conv2d](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) · [TorchVision ResNet-50 权重与 transforms](https://docs.pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html) · [TorchVision 模型总览](https://docs.pytorch.org/vision/main/models.html) | 互相关与严格卷积区分；输出尺寸考虑 stride/padding/dilation/groups；3.57% 是原论文集成 top-5 结果；V1.5 stride 与 V2 resize 232/crop 224 需注明 |
| 22 | [LSTM 原论文](https://doi.org/10.1162/neco.1997.9.8.1735) · [Forget gate 后续工作](https://doi.org/10.1162/089976600300015015) · [GRU / RNN Encoder–Decoder](https://arxiv.org/abs/1406.1078) · [Bahdanau Attention](https://arxiv.org/abs/1409.0473) · [Transformer](https://arxiv.org/abs/1706.03762) | 原始 LSTM 与现代 forget-gate 版本分开；GRU 门控约定说明；BPTT 梯度连乘；attention 权重不是因果解释；Transformer 自回归推理仍逐 token |
| 23 | [Word2Vec](https://arxiv.org/abs/1301.3781) · [Transformer](https://arxiv.org/abs/1706.03762) · [BERT](https://arxiv.org/abs/1810.04805) · [RoBERTa](https://arxiv.org/abs/1907.11692) · [Hugging Face Tokenizer](https://huggingface.co/docs/transformers/main_classes/tokenizer) · [PyTorch SDPA](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html) · [MultiheadAttention](https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html) | tokenizer 与模型权重配套；BERT 原始 MLM/NSP 与 RoBERTa 后续设置区分；双向 encoder 与 causal decoder 的可见上下文不同；SDPA bool True=参与，MHA bool mask True=屏蔽，迁移时需反转 |
| 24 | [GAN](https://arxiv.org/abs/1406.2661) · [VAE](https://arxiv.org/abs/1312.6114) · [DDPM](https://arxiv.org/abs/2006.11239) · [Latent Diffusion](https://arxiv.org/abs/2112.10752) · [GPT-2 report](https://openai.com/index/better-language-models/) | 原始 GAN minimax 与 non-saturating loss 区分；VAE 的 ELBO 和 KL 方向正确；DDPM 噪声日程与时间步一致；Latent Diffusion 的收益受编码器表达能力约束 |
| 25 | [Sutton & Barto](http://incompleteideas.net/book/the-book-2nd.html) · [Q-Learning](https://doi.org/10.1007/BF00992698) · [DQN](https://www.nature.com/articles/nature14236) · [Double DQN](https://arxiv.org/abs/1509.06461) · [REINFORCE](https://doi.org/10.1162/neco.1992.4.2.229) · [PPO](https://arxiv.org/abs/1707.06347) · [Gymnasium Env API](https://gymnasium.farama.org/main/api/env/) | 表格 Q-learning 收敛依赖充分探索等条件；DQN target/replay 不保证任意任务稳定；terminated 与 truncated 区分；PPO clipping 不是严格信赖域保证 |

详细主张、来源定位、状态和限制记录在 `docs/evidence/21.json` 至 `25.json`。新增 20 幅 SVG 是原创机制图；19 个 Python 示例使用随机/合成小张量核验形状和更新规则，不构成论文复现或生产模型性能结论。

## 第六批一手来源与技术边界 · 26–28

| 章节 | 一手论文 / 官方资料 | 审计要点 |
|---|---|---|
| 26 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) · [RAG: Lewis et al.](https://arxiv.org/abs/2005.11401) · [LoRA: Hu et al.](https://arxiv.org/abs/2106.09685) · [ReAct](https://arxiv.org/abs/2210.03629) · [Hugging Face KV Cache](https://huggingface.co/docs/transformers/en/kv_cache) | 自回归解码与训练并行计算区分；原始 RAG 与工程检索增强不同；LoRA 的矩阵维度与新增参数可推导；Agent 工具权限不能只靠提示词 |
| 26 | [OWASP LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) · [Microsoft RAG Evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) · [PyTorch SDPA](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html) | 文档/工具输出属于不可信输入；检索 Recall@k 与 groundedness/accuracy 分开评估；不同 mask API 的 True/False 约定必须明确 |
| 27 | [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/) · [FastAPI Lifespan](https://fastapi.tiangolo.com/advanced/events/) · [scikit-learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html) · [ONNX Runtime Python](https://onnxruntime.ai/docs/get-started/with-python) | API 验证、生命周期与 CPU 推理并发；受信任反序列化和依赖兼容；ONNX 输出数值必须同输入对照，不能假设转换必然加速 |
| 27 | [Docker Build Best Practices](https://docs.docker.com/build/building/best-practices/) · [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) · [NumPy Quantile](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html) | 容器仅是构建示例；95/5 发布和 60ms 延迟预算属于人工机制图，不代表任何真实服务或万能阈值 |
| 28 | [Feast historical feature retrieval](https://docs.feast.dev/getting-started/concepts/feature-retrieval) · [scikit-learn TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) · [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) · [Classification threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) | as-of 历史特征、事件时间与 available_at；未来 7 天标签窗口；时序 gap 防跨期泄漏；阈值由验证集选，测试集不可参与调参 |
| 28 | [Randomized uplift model evaluation research](https://www.sciencedirect.com/science/article/pii/S037722172300721X) · [Hidden Technical Debt](https://proceedings.neurips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) · [Model persistence](https://scikit-learn.org/stable/model_persistence.html) | 购买预测概率不同于优惠券处理效应；随机处理/对照和利润成本需要真实实验；model SHA 不能代替来源审查，工件必须可追溯 |

全部新增 15 幅章节 SVG 为原创计算机制图，示意中的企业政策、用户事件、处理组结果、延迟预算、Canary 比例和成本阈值均为构造案例。代码片段的运行成功不等于真实语义检索、云端部署、生产 QPS、商业试验或 LLM 基准复现。逐项来源定位与 verified / derived / illustrative 状态见 `docs/evidence/26.json` 至 `28.json`。

## 全站第二轮审计的优先级

1. 技术事实：文中跨年份模型、框架 API、过时服务建议和引用是否仍符合当前官方版本。
2. 数学与 SVG：分母、矩阵形状、轴含义、箭头起点/终点、数据标签与图注是否一一对应；每张 SVG 应单独以浏览器或 XML 工具打开。
3. Python 示例：固定依赖与随机种子，在 CI 的 Python 3.12 中逐段独立执行；真实模型下载和外部服务不混入离线质量门禁。
4. 移动端与无障碍：360/390px 没有文档级水平溢出；宽图/公式局部滚动；focus 可见；MathML 实际排版及打印/无联网阅读可用。
5. 发布与回滚：先通过 PR 静态、Python、Playwright，再合并并检查 Pages 实际工作流；没有独立在线访问复核则明确标记未验证。

## 第二轮 API 与可访问性复核 · 2026-11-23

本轮检查的是公开文档当日可见的 stable/main API 契约，不将其误写成所有历史版本的共同保证。

| 范围 | 复核来源 | 已纳入正文的边界 |
|---|---|---|
| scikit-learn 1.9.x | [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html) · [Model persistence](https://scikit-learn.org/stable/model_persistence.html) · [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | TargetEncoder.fit_transform 内部交叉拟合；fit().transform() 不能代替它；不可信 pickle/joblib 可执行代码；跨版本持久化不作兼容保证 |
| PyTorch 2.15 docs | [SDPA](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html) · [MultiheadAttention](https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html) · [Conv2d](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) · [AMP](https://docs.pytorch.org/docs/stable/amp.html) | SDPA 布尔 attn_mask 的 True 表示参与；MHA 的布尔 attn_mask/key_padding_mask True 表示屏蔽；Conv2d 实现互相关并按 stride/padding/dilation/groups 决定输出；AMP 使用 torch.amp 设备 API |
| Hugging Face Transformers | [KV cache strategies](https://huggingface.co/docs/transformers/en/kv_cache) | KV cache 既可优化重复计算，也可能成为显存瓶颈；offload/quantized/static cache 有不同内存、速度和编译取舍 |
| FastAPI | [Lifespan events](https://fastapi.tiangolo.com/advanced/events/) · [Request body](https://fastapi.tiangolo.com/tutorial/body/) | lifespan 是资源加载/释放的推荐入口；请求体校验不等于业务 schema 语义验证 |
| Gymnasium | [Env API](https://gymnasium.farama.org/api/env/) | step 返回 terminated 与 truncated；两者都结束 episode，但 bootstrap 语义不同 |
| OWASP | [LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | 文本筛选和 prompt 分隔不是安全边界；授权、参数校验、最小权限及审批必须由模型外部的可信代码执行 |

逐条主张及定位记录在 `docs/evidence/01.json` 至 `28.json`。页面代码示例和图中的教学数据均为小规模合成/离线实验；本轮 API 复核不意味着已在 GPU、云服务或真实生产数据上验证。
