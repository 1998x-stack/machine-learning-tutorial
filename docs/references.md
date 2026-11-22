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
