# AGENTS.md — machine-learning-tutorial

## Mission
维护一套可独立阅读、中文优先、证据可追踪、离线可渲染的机器学习教程。采用 Olah-style-posts 的渐进式解释方法，但自行绘图与撰文。

## Repo map
- `docs/index.html` 是唯一课程门户；`docs/courses.json` 是章节目录单一来源。
- `docs/chapters/NN.html` 是 28 篇可独立阅读的教程；01–10 已按新规范精修，11–28 是待逐篇复审的兼容旧稿。
- `docs/assets/css/{site,article}.css` 管理视觉 token、移动端和打印；勿在每篇重新复制整套 CSS。
- `docs/assets/svg/NN/` 存放按章节编号的 **独立 SVG**；`docs/assets/js/` 仅增强交互，不承担文章正文内容。
- 根目录 `index.html`、`NN.html` 是旧 URL 兼容入口，非可编辑正文。
- `scripts/validate_site.py` 是静态质量闸门；`.github/workflows` 是 PR 检查及 Pages 发布。

## Authoring gates — must pass before a new chapter is called complete
1. **Truth first**: 核对官方资料、一手论文、API 版本；记录结论适用条件，不能编造数值、实验指标、形状、图、来源。
2. **Self-contained narrative**: 从真实问题开始，解释输入、输出和最小可运行实例。顺序是：直觉 → 最简机制 → 公式及符号/形状 → 图示逐步展开 → 运行代码 → 失效情形 → 来源。禁止“本讲义介绍了”等依赖上下文的套话。
3. **Math**: 数学重要公式使用语义化 MathML（mfrac/msub/上下标），不得伪造纯 Unicode 公式版式。对假设（独立性、可微性、矩阵维度）做解释。复杂表达式装入横向可滚动容器；禁止将 MathML 放在 SVG 内。
4. **Figures**: 每个新重构章节至少 2 幅原创 SVG。每幅有 xmlns、viewBox、title、desc、可辨识标注、图注。路径和箭头严格匹配算法，不以无意义装饰替代机制。统一颜色：青绿=数据/信号，赭色=计算/变换，紫色=结构/条件。手机端图不强制压缩文字，可放在局部横向滚动容器中。
5. **Experiments**: 可执行 Python 例子标注依赖、随机种子、预期性质，而不是声称固定高准确率。模型评估严格训练/验证/测试隔离。实验结果若非实际执行不声称已验证。
6. **Citations**: 文内明确一手或官方来源 URL。不同版本算法要拆开描述；不把玩具结果包装成论文复现。新增章同步更新 `docs/references.md`。
7. **HTML**: 一页一 H1，标题层级有序，main/article/nav/section/figure/figcaption 语义化。每个章节要有上一章/下一章/首页导航，无需 JS 也可阅读。
8. **UX**: 正文 16–18px，正文宽不超过 820px；键盘可导航、明显 focus-visible；390px/360px 无全局水平滚动；公式、代码、密集图局部滚动。支持 prefers-reduced-motion、打印样式、无 CDN 离线字体依赖。
9. **QA**: 本地运行 `python3 scripts/validate_site.py`；逐页检查所有相对资源、SVG XML、索引 28 项。浏览器核验桌面 1440 与移动 390/360、键盘导航、交互、MathML、CLS、图的连线与裁切。没跑过的检查必须标明 **未验证**。
10. **Release**: 提交分支与 PR；核对变更清单、CI、部署，再检查实际 Pages 页面。不自动宣称已发布。只在核验完成后标记章节精修完毕。

## Scope rules
- 按批次逐章重构，**不要顺手替换** 尚未审查的 11–28 数学内容。
- `docs/` 是 deployable output/source for this dependency-free static site，无需重复生成的 dist/build 目录。
- 保持旧 `NN.html` 的导航有效，禁止无迁移说明地删除入口。
- 不拷贝 Olah 或第三方图标、图像、图表或代码的受限内容。

## 第二批 (06–10) QA gates
- 远程数据案例说明版本/年代、单位、下载条件及部署边界；离线实验不得伪装成真实 California Housing 结果。
- 优化器、模型选择、交叉验证、概率校准及决策阈值只从训练或验证数据学习，测试数据只允许最终独立报告。
- SVG 的几何线、统计数值、坐标轴、概率峰值必须经推导或代码校核；第二批每篇至少 3 幅独立 SVG。
- 新滑块必须具备原生键盘访问、无 JS 默认含义和可见的数字反馈；浏览器 QA 验证其状态变化。
- `scripts/run_examples.py` 和 `scripts/browser_qa.py` 覆盖前十章；离线检查未执行的外部项目不能标为通过。
