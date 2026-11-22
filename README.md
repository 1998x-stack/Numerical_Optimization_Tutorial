# Numerical Optimization Tutorial

**从优化建模到数值算法的结构化学习仓库。**

课程围绕 Nocedal 与 Wright 的 *Numerical Optimization*（第二版）组织，覆盖无约束优化、线搜索、信赖域、共轭梯度、拟牛顿、导数计算、约束最优性条件、线性规划、二次规划、SQP 与内点方法。

- 课程首页：<https://1998x-stack.github.io/Numerical_Optimization_Tutorial/>
- GitHub 仓库：<https://github.com/1998x-stack/Numerical_Optimization_Tutorial>
- 教材出版信息：[Springer — Numerical Optimization, 2nd edition](https://doi.org/10.1007/978-0-387-40065-5)

## 当前内容状态

| 范围 | 状态 | 本次处理 |
|---|---|---|
| 第一章 1.1–1.9 | 已重构 | 前两批：九篇独立文章、公式、SVG、交互、Python 与证据 |
| 第二章 2.1：解、局部极小、非光滑 | 已重构 | 解的概念、Hessian 判别、次梯度与 L1 模型 |
| 第二章 2.2：算法概览与练习 | 已重构 | 线搜索、信赖域、方向、局部模型、尺度与原创练习 |
| 第三章 3.1：步长选择 | 已重构 | Armijo、弱/强 Wolfe、Goldstein 与回溯 |
| 第三章 3.1.1–3.1.3 | 已重构 | Wolfe、Goldstein、充分下降与回溯 |
| 第三章 3.2–3.3.3 | 已重构 | Zoutendijk 全局收敛、收敛速度、最速下降、Newton 与拟 Newton |
| 第三章 3.4–3.5.2 | 已重构 | Hessian 修正、谱裁剪、单位矩阵平移、修正分解、插值与步长初值 |
| 第三章 3.5.3–3.7 | 已重构 | 强 Wolfe/zoom、浮点诊断与四道原创练习 |
| 第四章 4.1.1–4.2.1 | 已重构（5 篇） | Cauchy 点、方向改善、Dogleg、二维子空间与下降界 |
| 第四章 4.2.2 及后续至第十九章 | 保留原始章节结构 | 后续逐篇重构 |
| 附录 A | 保留原始章节结构 | 后续按批次完善 |

> 仓库有 19 个主体章节和一个背景材料附录。目录存在不代表其中每篇内容都已经完成。第一章 1.1–1.9、第二章 2.1–2.2、第三章 3.1–3.7 与第四章 4.1.1–4.2.1 共四十二篇已重构；其余页面仍保持原始状态。

## 从哪里开始

建议按以下顺序阅读：

1. [1.1 优化问题的数学表达](01._Introduction/00_1.1._Mathematical_Formulation.html)：变量、目标函数、约束和可行域。
2. [1.2 运输问题](01._Introduction/01_1.2._Example:_A_Transportation_Problem.html)：把物流决策写成线性规划，并证明一个小例子的最优性。
3. [1.3 连续与离散优化](01._Introduction/02_1.3._Continuous_vs._Discrete_Optimization.html)：变量类型如何改变可行集合与求解方式。
4. [1.4 有约束与无约束优化](01._Introduction/03_1.4._Constrained_and_Unconstrained_Optimization.html)：边界最优点、拉格朗日函数和 KKT 条件预览。
5. [1.5 全局与局部最优](01._Introduction/04_1.5._Global_and_Local_Optimization.html)：非凸函数、多个局部极小值、吸引域和凸性保证。

## 第二批：1.6–2.1

本批五篇均拥有完整 HTML、同步 Markdown、可运行 Python、独立 SVG、交互检查与证据账本：

1. [1.6 随机优化与确定性优化](01._Introduction/05_1.6._Stochastic_and_Deterministic_Optimization.html)：有限场景平方损失、期望目标与 SAA。
2. [1.7 凸性](01._Introduction/06_1.7._Convexity.html)：凸函数定义、插值不等式、Hessian 与全局最优。
3. [1.8 优化算法](01._Introduction/07_1.8._Optimization_Algorithms.html)：梯度下降、牛顿法、步长和停止条件。
4. [1.9 注释与参考](01._Introduction/08_1.9._Notes_and_References.html)：独立导数检查、误差来源与可复现记录。
5. [2.1 什么才算解](02._Fundamentals_of_Unconstrained_Optimization/00_2.1._What_Is_a_Solution%3F.html)：驻点、下确界、最优值与存在性。

**阅读边界：**本批中的教学数据和程序均为独立构造，不代表教材原始数值实验。

## 第三批：第二章补充与第三章 3.1

本批八篇都包含完整 HTML、同步 Markdown、可运行 Python、独立 SVG、交互演示与证据账本：

1. [识别局部极小点](02._Fundamentals_of_Unconstrained_Optimization/01_2.2._Recognizing_a_Local_Minimum.html)：梯度必要条件、Hessian 半正定与正定充分条件。
2. [非光滑问题](02._Fundamentals_of_Unconstrained_Optimization/02_2.3._Nonsmooth_Problems.html)：凸次微分、Fermat 条件与 L1 软阈值。
3. [线搜索与信赖域](02._Fundamentals_of_Unconstrained_Optimization/2.4._Overview_of_Algorithms/00_2.4.1._Two_Strategies:_Line_Search_and_Trust_Region.html)：两种全局化策略的机制与差异。
4. [搜索方向](02._Fundamentals_of_Unconstrained_Optimization/2.4._Overview_of_Algorithms/01_2.4.2._Search_Directions_for_Line_Search_Methods.html)：方向导数、最速下降与 Newton 方向。
5. [信赖域模型](02._Fundamentals_of_Unconstrained_Optimization/2.4._Overview_of_Algorithms/02_2.4.3._Models_for_Trust_Region_Methods.html)：二次模型、信赖域子问题与实际/预测下降比。
6. [尺度变换](02._Fundamentals_of_Unconstrained_Optimization/2.4._Overview_of_Algorithms/03_2.4.4._Scaling.html)：坐标变换、Hessian 条件数与数值尺度。
7. [综合练习](02._Fundamentals_of_Unconstrained_Optimization/04_2.5._Exercises.html)：五道原创题及可展开的完整解答。
8. [步长选择](03._Line_Search_Methods/00_3.1._Step_Length.html)：Armijo、弱/强 Wolfe、Goldstein 与回溯线搜索。

**目录编号说明：**教材目录将“识别局部极小点”和“非光滑问题”列为 2.1 下的子主题；算法概览为 2.2，其下的线搜索/信赖域、搜索方向、局部模型和尺度在目录中没有独立小节编号。为了不破坏旧仓库 URL，本批保留原文件路径，页面标题和阅读导航则按教材目录纠正显示。

## 第六批：Wolfe 搜索与信赖域基础

从第三章最后三个模块过渡到第四章前五个信赖域模块，八篇均配备独立 HTML、Markdown、Python、原创建模图和可调参数实验：

- [03.5.3 Wolfe 搜索与 zoom](03._Line_Search_Methods/17_3.5.3._A_Line_Search_Algorithm_for_the_Wolfe_Conditions.html)：两阶段搜索、强 Wolfe 条件和有界终止。
- [03.6 线搜索的浮点边界](03._Line_Search_Methods/18_3.6._Notes_and_References.html)：不可区分的函数值、步长与负曲率。
- [03.7 四组可执行练习](03._Line_Search_Methods/19_3.7._Exercises.html)：曲率区间、精确步长、回溯与修正 Newton。
- [04.1.1 Cauchy 点](04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/00_4.1.1._The_Cauchy_Point.html)：负梯度方向上的球内最佳模型步。
- [04.1.2 改进 Cauchy 点](04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/01_4.1.2._Improving_on_the_Cauchy_Point.html)：相同信赖域半径内利用曲率获得更多下降。
- [04.1.3 Dogleg 折线法](04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/02_4.1.3._The_Dogleg_Method.html)：三种半径分支与球面交点。
- [04.1.4 二维子空间最小化](04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/03_4.1.4._Two_Dimensional_Subspace_Minimization.html)：子空间包含 Dogleg 路径，模型下降可能更优。
- [04.2.1 Cauchy 模型下降界](04._Trust_Region_Methods/4.2._Global_Convergence/00_4.2.1._Reduction_Obtained_by_the_Cauchy_Point.html)：半径、梯度和曲率范数给出的统一下界。

**理论边界：**Wolfe 算法的教学二分 zoom 不等于工业级线搜索；Cauchy 下界保证的是模型下降，不等于真实函数值下降。正定模型上的 Dogleg 与二维子空间计算不自动覆盖不定 Hessian 情形。

## 第五批：Hessian 修正与步长算法

已完成八篇独立教程，保留原始章节 URL，并提供 HTML、同步 Markdown、Python、原创 SVG、交互演示及证据账本：

- [03.4 Hessian 修正总览](03._Line_Search_Methods/09_3.4._Newton’s_Method_with_Hessian_Modification.html)：在不定曲率下重新构造严格下降方向。
- [03.4.1 特征值裁剪](03._Line_Search_Methods/10_3.4.1._Eigenvalue_Modification.html)：修复过小特征值，同时保留可信方向信息。
- [03.4.2 对角平移 τI](03._Line_Search_Methods/11_3.4.2._Adding_a_Multiple_of_the_Identity.html)：以 Cholesky 反馈寻找足够大的平移量。
- [03.4.3 修正 Cholesky](03._Line_Search_Methods/12_3.4.3._Modified_Cholesky_Factorization.html)：主元下界、因子增长控制与二维重建。
- [03.4.4 对称不定块修正](03._Line_Search_Methods/13_3.4.4._Modified_Symmetric_Indefinite_Factorization.html)：2×2 主元、矩阵惯性与非对角修正。
- [03.5 线搜索步长选择](03._Line_Search_Methods/14_3.5._Step_Length_Selection_Algorithms.html)：初始试探、括区间与缩小候选范围。
- [03.5.1 二次插值候选步长](03._Line_Search_Methods/15_3.5.1._Interpolation.html)：从函数值与方向导数估计曲线低谷。
- [03.5.2 初始步长热启动](03._Line_Search_Methods/16_3.5.2._Initial_Step_Length.html)：使用历史方向导数改善首次试探。

**必要区分：**正定修正保证下降方向，不自动给出全局最优；插值和历史步长只提供搜索候选，不等于通过 Armijo/Wolfe。本批范围止于 3.5.2；第六批已继续补齐 3.5.3–3.7。

## 第四批：第三章步长条件与收敛分析

本批八篇均为独立页面，包含 HTML、同步 Markdown、可运行 Python、原创 SVG、交互实验与证据账本：

1. [3.1.1 Wolfe 条件](03._Line_Search_Methods/01_3.1.1._The_Wolfe_Conditions.html)：Armijo 充分下降、弱/强 Wolfe 曲率条件与可接受步长存在性。
2. [3.1.2 Goldstein 条件](03._Line_Search_Methods/02_3.1.2._The_Goldstein_Conditions.html)：函数值上下界、与 Wolfe 的差异，以及 Goldstein 下界排除精确一维极小点的构造反例。
3. [3.1.3 充分下降与回溯](03._Line_Search_Methods/03_3.1.3._Sufficient_Decrease_and_Backtracking.html)：Armijo 几何意义、有限终止证明与回溯实现。
4. [3.2 线搜索方法的全局收敛](03._Line_Search_Methods/04_3.2._Convergence_of_Line_Search_Methods.html)：Zoutendijk 定理、夹角余弦与梯度趋零的条件。
5. [3.3 收敛速度](03._Line_Search_Methods/05_3.3._Rate_of_Convergence.html)：Q-线性、超线性、二次与 R-线性。
6. [3.3.1 最速下降法](03._Line_Search_Methods/06_3.3.1._Convergence_Rate_of_Steepest_Descent.html)：精确线搜索、能量范数收缩界与条件数。
7. [3.3.2 Newton 法](03._Line_Search_Methods/07_3.3.2._Newton’s_Method.html)：局部二次收敛假设、单位步长和 Hessian 不定时的失败模式。
8. [3.3.3 拟 Newton 法](03._Line_Search_Methods/08_3.3.3._Quasi_Newton_Methods.html)：割线条件、BFGS 正定性、Wolfe 曲率与 Dennis–Moré 超线性条件。

**阅读边界：**全局收敛与局部收敛速度是不同结论；Newton/拟 Newton 的快速局部速度不等于任意初始点都能直接接受单位步长。所有数值例子和图解均独立构造，不是教材实验或解答手册。

## 学习路线

- **基础语言（第 1–2 章）**：优化建模、可行域、局部极小、算法总览。
- **无约束优化（第 3–11 章）**：线搜索、信赖域、共轭梯度、拟牛顿、大规模算法、导数和最小二乘。
- **约束优化（第 12–19 章）**：KKT、线性规划、内点法、二次规划、罚函数、SQP 和非线性规划。

完整章节入口见[课程首页](index.html#chapters)。尚未重构的章节链接会指向原始 GitHub 目录，不会伪装成已完成文章。

## 本批内容的约定

- 每篇 HTML 都有自己的问题背景、符号定义、推导、例子、边界条件和参考资料；不要求读者先打开其他文章。
- Markdown 与 HTML 保留同一组核心章节、结论和示例；Python 文件对应页面中的可运行代码。
- 复杂公式使用浏览器原生 MathML；新页面不依赖 CDN、外部字体或在线公式脚本。
- 图示是独立绘制的 SVG；数值例子会标记为教学数据或推导结果。
- 每篇文章有独立的 evidence/*.json，记录事实主张、来源定位与验证状态。
- 教学示例不是通用求解器，也不等于对教材中所有算法或实验的复现。

## 本仓库结构

~~~~text
.
├── index.html                    # 新课程门户与章节导航
├── README.md                     # 项目说明、进度与阅读路线
├── README.html                   # HTML 版入口说明
├── AGENTS.md                     # 内容工程与验收规范
├── main.py                       # 安全兼容入口；旧的破坏性脚手架已退役
├── assets/
│   ├── course.css                # 新页面共享设计系统
│   ├── course.js                 # 搜索与教学交互
│   └── figures/*.svg             # 独立图解
├── 01._Introduction/
│   ├── *.html                    # 第一章文章页面
│   ├── *.md                      # Markdown 源内容
│   └── *.py                      # 可运行示例
├── 02._.../ … 19._.../            # 原有章节路径，逐批完善
├── Appendix_A._Background_Material/
├── evidence/                     # 文章证据账本
├── scripts/
│   ├── validate_course.py        # 静态内容与链接检查
│   └── browser_check.py          # Playwright 多视口验收
├── tests/
│   └── test_course.py            # 自动化回归测试
└── .github/workflows/
    ├── validate.yml              # 静态、代码和浏览器测试
    └── pages.yml                 # GitHub Pages 部署
~~~~

原有 markdown.css、markdown.js 和 style.css 暂时保留，以免影响尚未迁移的旧页面。新页面统一使用 assets/course.css 与 assets/course.js。

**安全说明：**旧版 main.py 会重新生成目录、覆盖 README.md，并把既有 Markdown/Python 文章重置成占位文件。该破坏性脚手架已经替换为只读提示入口；不要恢复会覆盖人工内容的递归生成逻辑。

## 本地阅读

在仓库根目录执行：

~~~~bash
python -m http.server 8000
~~~~

打开 <http://localhost:8000/>。建议通过本地 HTTP 服务访问，而不是直接双击 HTML，以便相对路径与页面链接行为一致。

## 验收命令

仅使用 Python 标准库即可执行静态校验和示例程序测试：

~~~~bash
python scripts/validate_course.py
python -m unittest discover -s tests -v
~~~~

浏览器验收需要安装 Playwright：

~~~~bash
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python scripts/browser_check.py --output reports/course
~~~~

浏览器检查覆盖 1440、768、390、360 像素视口、打印模式、控制台异常、页面溢出、MathML 可见尺寸和交互输出。未实际运行的检查不会标记为通过。

## 发布与 GitHub Pages

- validate.yml 在 Pull Request 和主分支更新时运行。
- pages.yml 在主分支更新时部署静态站点。
- GitHub Pages 是否成功上线，以仓库 Actions 中最新的 Pages 部署记录和实际站点访问结果为准；存在 workflow 文件本身不等于部署已经成功。

## 版权与引用

本仓库是学习笔记与独立教学解释，不是教材全文、扫描件或逐段翻译。章节组织和概念范围参考：

Jorge Nocedal and Stephen J. Wright, *Numerical Optimization*, 2nd edition, Springer, 2006. DOI: [10.1007/978-0-387-40065-5](https://doi.org/10.1007/978-0-387-40065-5).

图示、例子和代码独立编写。对教材中的概念、定理或结构进行解释时，在对应文章中标明章节定位；所有自构造的教学数值都与原书实验数据区分。
