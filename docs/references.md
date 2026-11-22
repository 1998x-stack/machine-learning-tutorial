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

## 第四批技术核查 · 16–21

以下官方资料核对的是原理、API 与适用条件。本章 SVG 是流程示意或明确声明的人造教学数据，不是实际业务数据集或基准曲线。

| 章节 | 一手/官方来源 | 边界和关键纠错 |
| --- | --- | --- |
| 16 | [SMOTE（Chawla et al., JAIR 2002）](https://doi.org/10.1613/jair.953) · [imbalanced-learn 用户指南](https://imbalanced-learn.org/stable/user_guide.html) · [LogisticRegression class_weight](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) · [模型评估：平衡准确率与 PR 指标](https://scikit-learn.org/stable/modules/model_evaluation.html) · [precision_recall_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html) | 重采样只能作用于训练折；SMOTE 依赖距离度量与缩放；类别权重会移动概率、需重新选阈值；阈值与代价比在验证集上定，不能用测试集挑选；极端稀有可改走异常检测视角 |
| 17 | [SHAP（Lundberg & Lee, NeurIPS 2017）](https://arxiv.org/abs/1705.07874) · [LIME（Ribeiro et al., KDD 2016）](https://arxiv.org/abs/1602.04938) · [置换重要性](https://scikit-learn.org/stable/modules/permutation_importance.html) · [PDP/ICE](https://scikit-learn.org/stable/modules/partial_dependence.html) · [Interpretable ML](https://christophm.github.io/interpretable-ml-book/) | 重要性口径不同（MDI 偏高基数、置换受相关影响）；置换须在留出折上算；SHAP 依赖背景/基线且可加；LIME 局部且对扰动敏感；PDP/ICE 假设特征独立；所有工具解释预测而非因果 |
| 18 | [Pipeline / ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html) · [模型持久化](https://scikit-learn.org/stable/model_persistence.html) · [MLflow](https://mlflow.org/docs/latest/index.html) · [Feast](https://feast.dev/) · [Google MLOps 成熟度](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) | 交付物应为含预处理的整体管线；训练-服务偏差靠共享特征定义消除；实验需记录预算与失败；PSI 等漂移阈值须按业务定义而非通用数字；成熟度阶梯是参考而非硬标准 |
| 19 | [He 初始化](https://arxiv.org/abs/1502.01852) · [Batch Normalization](https://arxiv.org/abs/1502.03167) · [Dropout](https://arxiv.org/abs/1207.0580) · [GELU](https://arxiv.org/abs/1606.08415) · [PyTorch init](https://pytorch.org/docs/stable/nn.init.html) · [BatchNorm1d](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html) | 无非线性时多层塌缩为单层线性；Sigmoid/Tanh 饱和导致梯度消失；Xavier 适合 Sigmoid/Tanh、He 适合 ReLU；BN 训练/推理统计量不同、小 batch 方差；ReLU 可能死亡 |
| 20 | [autograd](https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) · [DataLoader](https://pytorch.org/docs/stable/data.html) · [BCEWithLogitsLoss](https://pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html) · [CrossEntropyLoss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) · [AMP](https://pytorch.org/docs/stable/notes/amp_examples.html) · [可复现性](https://pytorch.org/docs/stable/notes/randomness.html) | 梯度默认累加、需 zero_grad；eval() 与 no_grad() 不同作用；损失函数内置激活不能重复；log-sum-exp 保证数值稳定；混合精度需重验指标；shuffle 仅训练集 |
| 21 | [VGG](https://arxiv.org/abs/1409.1556) · [ResNet](https://arxiv.org/abs/1512.03385) · [EfficientNet](https://arxiv.org/abs/1905.11946) · [PyTorch Conv2d](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) · [torchvision 预训练模型](https://pytorch.org/vision/stable/models.html) | 卷积参数量与分辨率无关；输出尺寸 O=⌊(W−K+2P)/S⌋+1；堆两层 3×3 感受野为 5×5；残差相加需形状一致；迁移学习学习率与解冻策略在验证集确定；增强仅训练集；不转述二手精度数字 |

## 跨批次共用事实约束

- Docs 是 Pages 唯一构建工件；相对链接不能越过 `docs/`。指向 `examples/` 源码应直接使用 GitHub 仓库的网页 URL。
- 随机样本或合成数据的数值结果只能说明定义与算法，不代表真实应用准确率或因果效应。
- 对生成的公式曲线验证坐标和峰值，对邻域图核验距离、eps/min_samples 计数，对聚类中心核验平均值。未实测的算法性能图一律注明“示意”。
