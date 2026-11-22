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
