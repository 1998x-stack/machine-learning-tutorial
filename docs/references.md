# 技术核查与证据边界

下列链接是 01–05 章节的官方资料或公开数学证明；引用的是概念、算法定义与 API 行为，图解及演示数据重新制作。

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
| 14 | [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) · [Manifold](https://scikit-learn.org/stable/modules/manifold.html) · [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html) · [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html) | t-SNE 不保留全局簇距/密度；目标编码 fit_transform 内部交叉拟合；特征选择必须进入训练折 |
| 15 | [Grid/Random search](https://scikit-learn.org/stable/modules/grid_search.html) · [Nested CV example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html) · [Optuna search spaces](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/002_configurations.html) · [Optuna pruning](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html) | 搜索 CV 选择偏差；内层选参、外层评估；非迭代模型不能虚构 pruning 中间步骤 |

## 第四批技术核查 · 16–23

以下官方资料核对的是原理、API 与适用条件。本章 SVG 是流程示意或明确声明的人造教学数据，不是实际业务数据集或基准曲线。

| 章节 | 一手/官方来源 | 边界和关键纠错 |
| --- | --- | --- |
| 16 | [SMOTE（Chawla et al., JAIR 2002）](https://doi.org/10.1613/jair.953) · [imbalanced-learn 用户指南](https://imbalanced-learn.org/stable/user_guide.html) · [LogisticRegression class_weight](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) · [模型评估：平衡准确率与 PR 指标](https://scikit-learn.org/stable/modules/model_evaluation.html) · [precision_recall_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html) | 重采样只能作用于训练折；SMOTE 依赖距离度量与缩放；类别权重会移动概率、需重新选阈值；阈值与代价比在验证集上定，不能用测试集挑选；极端稀有可改走异常检测视角 |
| 17 | [SHAP（Lundberg & Lee, NeurIPS 2017）](https://arxiv.org/abs/1705.07874) · [LIME（Ribeiro et al., KDD 2016）](https://arxiv.org/abs/1602.04938) · [置换重要性](https://scikit-learn.org/stable/modules/permutation_importance.html) · [PDP/ICE](https://scikit-learn.org/stable/modules/partial_dependence.html) · [Interpretable ML](https://christophm.github.io/interpretable-ml-book/) | 重要性口径不同（MDI 偏高基数、置换受相关影响）；置换须在留出折上算；SHAP 依赖背景/基线且可加；LIME 局部且对扰动敏感；PDP/ICE 假设特征独立；所有工具解释预测而非因果 |
| 18 | [Pipeline / ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html) · [模型持久化](https://scikit-learn.org/stable/model_persistence.html) · [MLflow](https://mlflow.org/docs/latest/index.html) · [Feast](https://feast.dev/) · [Google MLOps 成熟度](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) | 交付物应为含预处理的整体管线；训练-服务偏差靠共享特征定义消除；实验需记录预算与失败；PSI 等漂移阈值须按业务定义而非通用数字；成熟度阶梯是参考而非硬标准 |
| 19 | [He 初始化](https://arxiv.org/abs/1502.01852) · [Batch Normalization](https://arxiv.org/abs/1502.03167) · [Dropout](https://arxiv.org/abs/1207.0580) · [GELU](https://arxiv.org/abs/1606.08415) · [PyTorch init](https://pytorch.org/docs/stable/nn.init.html) · [BatchNorm1d](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html) | 无非线性时多层塌缩为单层线性；Sigmoid/Tanh 饱和导致梯度消失；Xavier 适合 Sigmoid/Tanh、He 适合 ReLU；BN 训练/推理统计量不同、小 batch 方差；ReLU 可能死亡 |
| 20 | [autograd](https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) · [DataLoader](https://pytorch.org/docs/stable/data.html) · [BCEWithLogitsLoss](https://pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html) · [CrossEntropyLoss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) · [AMP](https://pytorch.org/docs/stable/notes/amp_examples.html) · [可复现性](https://pytorch.org/docs/stable/notes/randomness.html) | 梯度默认累加、需 zero_grad；eval() 与 no_grad() 不同作用；损失函数内置激活不能重复；log-sum-exp 保证数值稳定；混合精度需重验指标；shuffle 仅训练集 |
| 21 | [VGG](https://arxiv.org/abs/1409.1556) · [ResNet](https://arxiv.org/abs/1512.03385) · [EfficientNet](https://arxiv.org/abs/1905.11946) · [PyTorch Conv2d](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) · [torchvision 预训练模型](https://pytorch.org/vision/stable/models.html) | 卷积参数量与分辨率无关；输出尺寸 O=⌊(W−K+2P)/S⌋+1；堆两层 3×3 感受野为 5×5；残差相加需形状一致；迁移学习学习率与解冻策略在验证集确定；增强仅训练集；不转述二手精度数字 |
| 22 | [GRU](https://arxiv.org/abs/1406.1078) · [Seq2Seq](https://arxiv.org/abs/1409.3215) · [Bahdanau 注意力](https://arxiv.org/abs/1409.0473) · [Attention Is All You Need](https://arxiv.org/abs/1706.03762) · [PyTorch LSTM](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html) · [PyTorch GRU](https://pytorch.org/docs/stable/generated/torch.nn.GRU.html) | RNN 共享权重、梯度易消失/爆炸；LSTM 门控与加法细胞状态；GRU 合并门；Seq2Seq 固定向量的瓶颈；注意力为编码器状态加权和；自注意力并行且路径短；变长需 padding/掩码 |
| 23 | [Word2Vec](https://arxiv.org/abs/1301.3781) · [Attention Is All You Need](https://arxiv.org/abs/1706.03762) · [BERT](https://arxiv.org/abs/1810.04805) · [RoBERTa](https://arxiv.org/abs/1907.11692) · [Transformers 文档](https://huggingface.co/docs/transformers/index) | one-hot 正交无相似度；静态嵌入一词一向量、多义无法区分；自注意力双向直接连接；1/√d_k 缩放控制 softmax 尖锐度；MLM 训练/推理掩码不一致；NSP 可去掉；编码器理解、解码器生成 |

## 第五批技术核查 · 24–28

以下官方资料核对的是原理、API 与适用条件。本章 SVG 是机制示意或明确声明的人造教学数据，不是实际模型输出或基准曲线。

| 章节 | 一手/官方来源 | 边界和关键纠错 |
| --- | --- | --- |
| 24 | [GAN（Goodfellow et al., 2014）](https://arxiv.org/abs/1406.2661) · [VAE（Kingma & Welling, 2013）](https://arxiv.org/abs/1312.6114) · [DDPM（Ho et al., 2020）](https://arxiv.org/abs/2006.11239) · [Latent Diffusion（Rombach et al., 2021）](https://arxiv.org/abs/2112.10752) · [top-p（Holtzman et al., 2019）](https://arxiv.org/abs/1904.09751) · [GPT-3（Brown et al., 2020）](https://arxiv.org/abs/2005.14165) | 判别式建模 p(y\|x)、生成式建模 p(x)；GAN 极小极大博弈、判别器最优时才等价于最小化 JS 散度、训练不稳与模式坍塌；VAE 最大化的是证据下界而非真似然、重参数化、对角高斯 KL 有闭式解；扩散前向固定、可一步采样任意 t、简化目标为预测噪声的 MSE、潜空间扩散降算量；自回归逐词分解、温度只重塑分布、top-p 阈值动态；不复述二手基准分数 |
| 25 | [Sutton & Barto, RL: An Introduction（第 2 版）](http://incompleteideas.net/book/the-book-2nd.html) · [DQN（Mnih et al., 2015, Nature）](https://doi.org/10.1038/nature14236) · [Playing Atari with DRL（2013）](https://arxiv.org/abs/1312.5602) · [Double DQN（van Hasselt et al., 2015）](https://arxiv.org/abs/1509.06461) · [PPO（Schulman et al., 2017）](https://arxiv.org/abs/1707.06347) | 监督有标签、RL 只有奖励、数据由行动产生；MDP 马尔可夫假设与折扣 γ；贝尔曼最优方程与 Q-Learning 的 TD 更新、max 使其成为 off-policy；DQN 用神经网络逼近 Q、经验回放打散相关性、目标网络稳定靶子、max 带来过高估计（Double DQN 修正）；策略梯度定理用回报加权 log π、基线降方差；奖励稀疏与 reward hacking；不复述二手基准分数 |
| 26 | [Transformer（Vaswani et al., 2017）](https://arxiv.org/abs/1706.03762) · [GPT-3（Brown et al., 2020）](https://arxiv.org/abs/2005.14165) · [CoT（Wei et al., 2022）](https://arxiv.org/abs/2201.11903) · [RAG（Lewis et al., 2020）](https://arxiv.org/abs/2005.11401) · [Lost in the Middle（Liu et al., 2023）](https://arxiv.org/abs/2307.03172) · [LoRA（Hu et al., 2021）](https://arxiv.org/abs/2106.09685) · [涌现溯源（Schaeffer et al., 2023）](https://arxiv.org/abs/2304.15004) | 解码器因果掩码、预训练目标为逐词负对数似然；训练可并行、推理逐词串行；上下文学习不改权重；“涌现能力”存在争议，不能当作已证规律；RAG 对检索文档边缘化、检索召回是首要指标、中间位置利用较弱；LoRA 冻结 W₀ 加低秩 BA、参数量 r(d+k)、B 零初始化使起点一致、合并后无推理延迟；提示工程不稳定与数据污染；不复述二手基准分数 |
| 27 | [FastAPI](https://fastapi.tiangolo.com/) · [ONNX](https://onnx.ai/) · [ONNX Runtime 量化](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) · [Docker 文档](https://docs.docker.com/) · [scikit-learn 模型持久化](https://scikit-learn.org/stable/model_persistence.html) · [Hidden Technical Debt（Sculley et al., 2015）](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) · [概念漂移综述（Gama et al., 2014）](https://doi.org/10.1145/2523813) | 部署关注延迟/吞吐/可复现/可扩展/可观测；预处理与模型打包同一管线以降训练—服务偏差；批处理提吞吐但增延迟；ONNX 解耦训练与推理引擎；量化后必须重测精度；无状态副本 + 负载均衡水平扩展；数据漂移与概念漂移不同；PSI＞0.25 仅经验阈值、阈值需按业务定；回滚是一等公民 |
| 28 | [scikit-learn Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) · [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) · [Pipeline / ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html) · [模型评估](https://scikit-learn.org/stable/modules/model_evaluation.html) · [Google Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml) · [Hidden Technical Debt（Sculley et al., 2015）](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) · [Leakage in Data Mining（Kaufman et al., 2012）](https://doi.org/10.1145/2382577.2382579) | 项目为教学设定、不冒真实平台数据；时间场景随机切分会泄露、必须时间切分与前向链式切分；预处理与模型同管线、每折只在训练部分拟合；目标编码需交叉拟合；先建基线再上复杂模型；不平衡下准确率具欺骗性、看 PR-AUC / recall@k；阈值按代价 C_FN·FN + C_FP·FP 选且在验证集；上线后闭环重训与干预偏差、离线涨不等于线上涨；第 07 节数据为人为构造教学数据 |

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
| 20 | [Autograd](https://docs.pytorch.org/docs/stable/notes/autograd.html) · [DataLoader](https://docs.pytorch.org/docs/stable/data.html) · [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html) · [AMP](https://docs.pytorch.org/docs/stable/amp.html) · [Saving/Loading](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html) | logits/目标形状匹配；eval 与 grad mode 分离；完整续训需要 optimizer/scaler/scheduler 状态；CUDA AMP 不可由 CPU CI 代替 |

每章的详细主张、来源定位、状态和限制记录在 docs/evidence/16.json 至 docs/evidence/20.json。18 幅新 SVG 中，数值与机制示例均为解析推导或教学构造；不冒充外部 benchmark。

## 第五批技术核查 · 21–25

| 章节 | 一手论文 / 官方资料 | 必须保留的边界 |
|---|---|---|
| 21 | [ResNet 原论文](https://arxiv.org/abs/1512.03385) · [PyTorch Conv2d](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) · [TorchVision ResNet-50 权重与 transforms](https://docs.pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html) · [TorchVision 模型总览](https://docs.pytorch.org/vision/main/models.html) | 互相关与严格卷积区分；输出尺寸考虑 stride/padding/dilation/groups；3.57% 是原论文集成 top-5 结果；V1.5 stride 与 V2 resize 232/crop 224 需注明 |
| 22 | [LSTM 原论文](https://doi.org/10.1162/neco.1997.9.8.1735) · [Forget gate 后续工作](https://doi.org/10.1162/089976600300015015) · [GRU / RNN Encoder–Decoder](https://arxiv.org/abs/1406.1078) · [Bahdanau Attention](https://arxiv.org/abs/1409.0473) · [Transformer](https://arxiv.org/abs/1706.03762) | 原始 LSTM 与现代 forget-gate 版本分开；GRU 门控约定说明；BPTT 梯度连乘；attention 权重不是因果解释；Transformer 自回归推理仍逐 token |
| 23 | [Word2Vec](https://arxiv.org/abs/1301.3781) · [Transformer](https://arxiv.org/abs/1706.03762) · [BERT](https://arxiv.org/abs/1810.04805) · [RoBERTa](https://arxiv.org/abs/1907.11692) · [Hugging Face Tokenizer](https://huggingface.co/docs/transformers/main_classes/tokenizer) | tokenizer 与模型权重配套；BERT 原始 MLM/NSP 与 RoBERTa 后续设置区分；双向 encoder 与 causal decoder 的可见上下文不同 |
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
