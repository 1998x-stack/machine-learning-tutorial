# AGENTS.md — machine-learning-tutorial

## Mission
维护一套可独立阅读、中文优先、证据可追踪、离线可渲染的机器学习教程。采用 Olah-style-posts 的渐进式解释方法，但自行绘图与撰文。

## Repo map
- `docs/index.html` 是唯一课程门户；`docs/courses.json` 是章节目录单一来源。
- `docs/chapters/NN.html` 是 28 篇可独立阅读的教程；01–28 已按新规范完成独立重构；后续修改须按分章证据台账与全站质量门禁维护。
- `docs/assets/css/{site,article}.css` 管理视觉 token、移动端和打印；勿在每篇重新复制整套 CSS。
- `docs/assets/svg/NN/` 存放按章节编号的 **独立 SVG**；`docs/assets/js/` 仅增强交互，不承担文章正文内容。
- 根目录 `index.html`、`NN.html` 是旧 URL 兼容入口，非可编辑正文。
- `scripts/validate_site.py` 是静态质量闸门；`.github/workflows` 是 PR 检查及 Pages 发布。

## Authoring gates — must pass before a new chapter is called complete
1. **Truth first**: 核对官方资料、一手论文、API 版本；记录结论适用条件，不能编造数值、实验指标、形状、图、来源。
2. **Self-contained narrative**: 从真实问题开始，解释输入、输出和最小可运行实例。顺序是：直觉 → 最简机制 → 公式及符号/形状 → 图示逐步展开 → 运行代码 → 失效情形 → 来源。禁止“本讲义介绍了”等依赖上下文的套话。
3. **Math**: 数学重要公式使用语义化 MathML（mfrac/msub/上下标），不得伪造纯 Unicode 公式版式。对假设（独立性、可微性、矩阵维度）做解释。复杂表达式装入横向可滚动容器；禁止将 MathML 放在 SVG 内。
4. **Figures**: 每个新重构章节至少 3 幅原创 SVG。每幅有 xmlns、viewBox、title、desc、可辨识标注、图注。路径和箭头严格匹配算法，不以无意义装饰替代机制。统一颜色：青绿=数据/信号，赭色=计算/变换，紫色=结构/条件。手机端图不强制压缩文字，可放在局部横向滚动容器中。
5. **Experiments**: 可执行 Python 例子标注依赖、随机种子、预期性质，而不是声称固定高准确率。模型评估严格训练/验证/测试隔离。实验结果若非实际执行不声称已验证。
6. **Citations**: 文内明确一手或官方来源 URL。不同版本算法要拆开描述；不把玩具结果包装成论文复现。新增章同步更新 `docs/references.md`。
7. **HTML**: 一页一 H1，标题层级有序，main/article/nav/section/figure/figcaption 语义化。每个章节要有上一章/下一章/首页导航，无需 JS 也可阅读。
8. **UX**: 正文 16–18px，正文宽不超过 820px；键盘可导航、明显 focus-visible；390px/360px 无全局水平滚动；公式、代码、密集图局部滚动。支持 prefers-reduced-motion、打印样式、无 CDN 离线字体依赖。
9. **QA**: 本地运行 `python3 scripts/validate_site.py`；逐页检查所有相对资源、SVG XML、索引 28 项。浏览器核验桌面 1440 与移动 390/360、键盘导航、交互、MathML、CLS、图的连线与裁切。没跑过的检查必须标明 **未验证**。
10. **Release**: 提交分支与 PR；核对变更清单、CI、部署，再检查实际 Pages 页面。不自动宣称已发布。只在核验完成后标记章节精修完毕。

## Scope rules
- 全 28 章已建立正文、SVG 与实验基础。后续优先开展逐章事实复审、交叉链接与工程回归；不为凑图数量擅改科学主张。
- `docs/` 是 deployable output/source for this dependency-free static site，无需重复生成的 dist/build 目录。
- 保持旧 `NN.html` 的导航有效，禁止无迁移说明地删除入口。
- 不拷贝 Olah 或第三方图标、图像、图表或代码的受限内容。

## 第二批 (06–10) QA gates
- 远程数据案例说明版本/年代、单位、下载条件及部署边界；离线实验不得伪装成真实 California Housing 结果。
- 优化器、模型选择、交叉验证、概率校准及决策阈值只从训练或验证数据学习，测试数据只允许最终独立报告。
- SVG 的几何线、统计数值、坐标轴、概率峰值必须经推导或代码校核；第二批每篇至少 3 幅独立 SVG。
- 新滑块必须具备原生键盘访问、无 JS 默认含义和可见的数字反馈；浏览器 QA 验证其状态变化。
- `scripts/run_examples.py` 和 `scripts/browser_qa.py` 覆盖全 28 章；离线检查未执行的外部项目不能标为通过。

## Third-wave gates (11–15)
- SVM 文章必须区分几何间隔、函数间隔、C 的软间隔惩罚与 gamma 的 RBF 相似性范围；可分情形的解析图不能冒充真实样本决策边界。
- Naive Bayes 的条件独立属于给定类别的假设；MultinomialNB 输入必须非负。KNN 需要说明样本存储成本、距离尺度和 k 的验证选择。
- 聚类无标签不得套用分类准确率；DBSCAN 的 min_samples 包含中心样本。Silhouette 与 KMeans inertia 不可被称作自动真值或因果分组。
- PCA/t-SNE 解决的目标不同；目标编码的 fit_transform 需考虑训练内部交叉拟合及时间/分组边界，测试标签不得参与。
- 任何搜索预算必须记录候选参数个数、CV 折数及 refit；嵌套 CV 的内层只选择、外层只评估。只有真实报告中间指标的迭代模型才可演示 Optuna pruning。
- 11–15 每篇至少 3 幅 title/desc/viewBox 完整的独立 SVG，图中的每个数学量或点的邻域分类都应交叉核验。
- 静态验证只接受部署在 docs/ 内部的相对站内资源；源码示例链接使用 GitHub 官方仓库地址。CI 覆盖全 28 章示例与 87 组页面/视口组合。

## Fourth-wave gates (16–20)
- 不平衡分类必须分别解释基率、排序指标、阈值与错误成本；SMOTE 只能在每个训练折内部拟合，验证/测试数据保持原始分布。AP 不得无条件写成梯形 PR-AUC。
- SHAP 必须说明基线、输出空间、背景数据与特征依赖假设；LIME 必须检查局部 fidelity；PDP/ICE 不得被解释为因果效应，相关特征可能生成低概率组合。
- MLflow 区分 Tracking Run、模型工件、Registry 版本与 alias；Feature Store 必须解释事件时间与 point-in-time join；MLOps 成熟度层级注明是参考框架。
- 神经网络每个公式标明张量形状；区分反向传播求梯度与优化器更新；Xavier/He 公式必须说明 fan 与激活假设；BN/Dropout 的 train/eval 行为不可混淆。
- PyTorch 必须区分 model.eval() 与 inference_mode/no_grad；BCEWithLogitsLoss/CrossEntropyLoss 接收 logits；Checkpoint 需包含优化器状态；AMP 说明设备、dtype、GradScaler 和 unscale/clip 顺序。
- 16–20 每章至少 3 幅独立 SVG，并建立 docs/evidence/NN.json 逐条登记重要主张、来源定位和 verified/derived/illustrative 状态。
- CI 必须执行全部 28 章的正文 Python 代码块，覆盖首页+28 章在 1440/390/360px 的 87 组浏览器检查，并验证所有新证据台账 JSON。

## Fifth-wave gates (21–25)
- CNN 的 Conv2d 公式必须标出 NCHW、groups、stride、padding 与 dilation；互相关与严格数学卷积应区分。残差相加前两支形状必须一致，projection shortcut、bottleneck 和 TorchVision ResNet V1.5 stride 位置不得混淆。
- 迁移学习必须把权重版本与 transforms 配套；冻结 backbone 时说明 BatchNorm train/eval 行为；增强必须保持任务标签语义，验证/测试预处理确定性。
- RNN/LSTM/GRU 公式要注明 hidden/state 形状与门控约定；原始 1997 LSTM 与后续 forget-gate 变体分开叙述；teacher forcing 与自回归推理差异、padding mask 与 loss mask 必须解释。
- Attention 需明确 query/key 维、softmax 轴、mask 的 1/0 语义；Transformer 的并行训练不等于自回归生成并行，标准全注意力具有序列长度平方级交互。
- NLP tokenizer 与权重必须成对；BERT 原始 MLM/NSP、RoBERTa 去 NSP 的后续实验和 GPT causal LM 分开说明；静态 embedding 不得与 contextual representation 混为一谈。
- GAN 原始 minimax 与 non-saturating generator loss 分开；VAE ELBO 两项和 reparameterization 正确；DDPM 前向闭式采样、时间步与噪声日程一致；不要声称任一生成家族在所有任务上全面胜出。
- RL 必须区分 state/observation、terminated/truncated、on-policy/off-policy、terminal bootstrap 与 time-limit bootstrap；Q-learning/DQN/REINFORCE/PPO 的目标和适用条件不能混用。
- 21–25 每章至少 4 幅独立 SVG，建立 docs/evidence/NN.json 主张—来源台账；每章正文 Python 示例全部进入 run_examples.py。

## Sixth-wave gates (26–28)
- 26 LLM：区分训练时可并行计算的 causal attention 和自回归逐 token 生成；KV Cache 节约历史重复计算但增加显存，GQA/MQA 的 KV head 形状与 Query head 不必一致。不要臆测闭源模型参数或特定 token 长度。
- 26 RAG：原始 RAG-Sequence / RAG-Token 与当代 top-k 拼接检索区分；文本切块、访问控制、索引版本、时效性和来源 ID 都属于被检索上下文的契约。Recall@k 必须说明需要标注相关集合；引用支持与答案正确性分别审查。
- 26 Agent：外部检索内容/工具输出是不可信数据，不能提升为系统级指令；工具权限、参数 schema、时间/调用额度、审批与审计由独立可信控制器执行，而非仅由 prompt 承诺。工具示例不得真的执行有副作用的网络操作。
- 26 LoRA：W0∈R^(dout×din)、A∈R^(r×din)、B∈R^(dout×r)，明确缩放 α/r 和可训练参数数量 r(din+dout) 的适用条件；不写固定百分比节省或零成本无损结论。
- 27 服务：明确 schema、正类/类别顺序、预处理、模型版本和错误契约。CPU-bound 同步推理不因 async 自动加速；使用 lifespan 和 TestClient 演示，不声称这是包含认证的生产服务。
- 27 ONNX：导出后对 shape、dtype、类别顺序与预测概率做可重现浮点容差断言；转换并不自动保证实际加速。Dockerfile 属于需要上下文文件的示意，不可作为已构建的容器发布结果。
- 27 监控：P95 是端到端请求延迟的统计分位数；不允许把组件 P95 简单相加。数据漂移、概念漂移、缺失标签、业务结果和时延必须区分；5% 金丝雀及阈值是人工示意而非通用统计规则。
- 28 特征：每个样本以预测时点 t 锚定，历史可见特征来自 t 之前（含 available_at 可用性约束），未来七天标签仅为训练监督目标；时序 split 必须为标签成熟期设置 gap，测试集只最终独立报告。
- 28 营销：购买概率模型 ≠ 优惠券增量效果；处理效应需随机试验或明确识别假设与净价值分析。人工生成数据、随机实验与便捷模型仅能证明代码/定义，不是实际线上转化增量。
- 28 工件：训练与服务 Pipeline、schema、阈值、数据/代码/依赖版本、工件 SHA 和回滚目标共同记录。joblib/pickle 只允许加载自己可信创建的产物，SHA 校验不证明工件是安全代码。
- 26–28 每章至少 5 幅独立 title/desc/viewBox SVG，建立 docs/evidence/26.json 至 28.json；所有 Python 代码块进入 CI，非 Python 的 Dockerfile 用 <pre><samp> 保留，不作为 Python 运行。
- 全站发布门禁必须运行静态检查、全部正文 59 个 Python 实验、首页和 28 章的 87 组 Chromium 视口测试，并确保 GitHub Pages 部署工作流成功。只有实际检查过的项目才标记为 passed；网络部署、GPU、真实云服务和真实商业效果不得由 CPU 教学 CI 冒充。

## Second-pass maintenance gates (2026-11-23)
- `docs/courses.json` is the single source for chapter prerequisites/related concepts. Each of the 28 article pages renders its curated links in a `related-concepts` section and the article TOC must link to that section. Keep every link's reason specific; do not generate generic "see also" lists.
- Each `docs/evidence/NN.json` ledger records at least four claim-level records with `id`, `claim`, `kind`, `source_url`, `locator`, `status`, and `notes`. Status is one of `verified`, `derived`, `illustrative`, or `unverified`. A verified claim must be traceable to an official document, primary paper, or authoritative proof; derived claims must state their derivation; illustrative values must never be described as observed results.
- Every MathML expression has an accessible name. Display-equation wrappers use `role="group"`, `tabindex="0"`, and a concise `aria-label`; wide equations, code blocks, and dense diagrams scroll locally and are keyboard-focusable.
- Every article has one `main#content[tabindex="-1"]` and a skip link targeting it. The homepage has one `main#main[tabindex="-1"]`; its route diagram is a named keyboard-scrollable region. Every `aria-labelledby` target must exist.
- Each chapter declares its canonical URL and Open Graph title/description. `docs/sitemap.xml` must contain the homepage and all 28 canonical lesson URLs in order; `docs/robots.txt` advertises that sitemap.
- The static gate validates local HTML/CSS assets, fragment links, SVG XML/title/desc/viewBox, MathML structure and names, chapter evidence ledgers, cross-links, and redirects. Do not weaken a check just to get green CI; correct either the markup or the assumption in the test.
- Browser QA covers the 29 pages at 1440/390/360 px, first-Tab skip-link focus and destination focus, print visibility, reduced-motion behavior, search/threshold interactions, MathML geometry, image decoding, and browser console errors. A green static gate is not a substitute for the browser run.
- Current API references are version-scoped. On 2026-11-23, scikit-learn stable is 1.9.1 and PyTorch stable docs are 2.15; recheck official release/docs pages before changing these labels or relying on version-specific behavior.
