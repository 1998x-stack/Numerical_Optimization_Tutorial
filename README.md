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
| 第四章 4.2.2–4.5.2 | 已重构（8 篇） | 全局驻点收敛、λ 根搜索、Hard Case、全局最优证书、局部 Newton、缩放与范数 |
| 第五章 5.1.1–5.1.6 | 已重构（6 篇） | 共轭方向法、CG 基本性质、实用形式、收敛速度、预条件与实用预条件器 |
| 第五章 5.2.1–5.2.6 | 已重构（6 篇） | 非线性 CG：FR、Polak–Ribière 变体、重启、行为、全局收敛与数值表现 |
| 第六章 6.1.1–6.6 | 已重构（9 篇） | BFGS、SR1、Broyden 族、三类收敛分析、要点与练习 |
| 第七章 7.1.1–7.1.5 | 已重构（5 篇） | 不精确牛顿局部收敛、线搜索/信赖域 Newton–CG、预条件与 Newton–Lanczos |
| 第五章 5.3–5.4、第七章 7.2 起及第八章至第十九章 | 保留原始章节结构 | 后续逐篇重构 |
| 附录 A | 保留原始章节结构 | 后续按批次完善 |

> 仓库有 19 个主体章节和一个背景材料附录。目录存在不代表其中每篇内容都已经完成。第一章 1.1–1.9、第二章 2.1–2.2、第三章 3.1–3.7、第四章 4.1.1–4.5.2、第五章 5.1.1–5.1.6、5.2.1–5.2.6、第六章 6.1.1–6.6 与第七章 7.1.1–7.1.5 共七十六篇已重构；其余页面仍保持原始状态。

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

## 第十批：拟牛顿方法 6.1–6.6

本批九篇逐页重建第六章拟牛顿方法，均包含独立 HTML、Markdown、Python、可访问 SVG、参数交互与证据记录：

- [6.1.1 BFGS 的性质](06._Quasi_Newton_Methods/6.1._The_BFGS_Method/00_6.1.1._Properties_of_the_BFGS_Method.html)：割线方程、变分推导与正定性。
- [6.1.2 BFGS 的实现](06._Quasi_Newton_Methods/6.1._The_BFGS_Method/01_6.1.2._Implementation.html)：算法 6.1、初始缩放与存储/计算代价。
- [6.2.1 SR1 更新的性质](06._Quasi_Newton_Methods/6.2._The_SR1_Method/00_6.2.1._Properties_of_SR1_Updating.html)：秩一割线更新与不定性。
- [6.3 Broyden 族](06._Quasi_Newton_Methods/02_6.3._The_Broyden_Class.html)：连接 BFGS 与 DFP 的一参数更新。
- [6.4.1 BFGS 的全局收敛](06._Quasi_Newton_Methods/6.4._Convergence_Analysis/00_6.4.1._Global_Convergence_of_the_BFGS_Method.html)：Zoutendijk 条件与水平集假设。
- [6.4.2 BFGS 的超线性收敛](06._Quasi_Newton_Methods/6.4._Convergence_Analysis/01_6.4.2._Superlinear_Convergence_of_the_BFGS_Method.html)：Dennis–Moré 条件与误差比率。
- [6.4.3 SR1 的收敛分析](06._Quasi_Newton_Methods/6.4._Convergence_Analysis/02_6.4.3._Convergence_Analysis_of_the_SR1_Method.html)：跳过准则与逼近真实 Hessian。
- [6.5 要点与参考](06._Quasi_Newton_Methods/04_6.5._Notes_and_References.html)：四种更新与三类收敛结论的边界。
- [6.6 练习](06._Quasi_Newton_Methods/05_6.6._Exercises.html)：割线方程、正定性与闭式判定。

**重要边界：**BFGS 的全局收敛是 lim inf 形式且依赖 Wolfe 线搜索与凸水平集/ Lipschitz 梯度；超线性是局部结论且依赖 Dennis–Moré 条件；SR1 的分析依赖跳过准则。本批数值例子均为教学算例，不代表一般问题的迭代次数或性能排序。

## 第十一批：大规模无约束优化 7.1.1–7.1.3

本批三篇逐页重建第七章“不精确牛顿法”的前三个小节，均包含独立 HTML、Markdown、Python、可访问 SVG、参数交互与证据记录：

- [7.1.1 不精确牛顿法的局部收敛](07._Large_Scale_Unconstrained_Optimization/7.1._Inexact_Newton_Methods/00_7.1.1._Local_Convergence_of_Inexact_Newton_Methods.html)：forcing 项 ηₖ 如何决定线性、超线性与二次收敛。
- [7.1.2 线搜索 Newton–CG](07._Large_Scale_Unconstrained_Optimization/7.1._Inexact_Newton_Methods/01_7.1.2._Line_Search_Newton–CG_Method.html)：用截断共轭梯度解牛顿方程、残差容差与负曲率处理。
- [7.1.3 信赖域 Newton–CG](07._Large_Scale_Unconstrained_Optimization/7.1._Inexact_Newton_Methods/02_7.1.3._Trust_Region_Newton–CG_Method.html)：在半径 Δ 内近似求解子问题的三种退出方式。

**重要边界：**三篇的收敛阶与数值结果都以局部假设为前提；一维/二维算例用于区分概念，不代表任何大规模基准。7.2 以后仍保持原始状态。

## 第十二批：大规模无约束优化 7.1.4–7.1.5

本批两篇重建第七章“不精确牛顿法”的后两个小节，均包含独立 HTML、Markdown、Python、可访问 SVG、参数交互与证据记录：

- [7.1.4 预条件信赖域 Newton–CG](07._Large_Scale_Unconstrained_Optimization/7.1._Inexact_Newton_Methods/03_7.1.4._Preconditioning_the_Trust_Region_Newton–CG_Method.html)：变量替换 p=Cv 把球约束变成 M-椭球，边界步改用 M-范数。
- [7.1.5 信赖域 Newton–Lanczos](07._Large_Scale_Unconstrained_Optimization/7.1._Inexact_Newton_Methods/04_7.1.5._Trust_Region_Newton–Lanczos_Method.html)：Krylov 子空间、三对角投影与长期方程。

**重要边界：**两篇的数值结果均为教学算例；预条件在二维精确运算下不体现迭代优势，Newton–Lanczos 的 j 维近似以三对角子问题为对象，均不代表大规模基准或性能排序。7.2 以后仍保持原始状态。

## 第九批：非线性共轭梯度 5.2

本批六篇逐页重建 5.2 非线性共轭梯度，均包含独立 HTML、Markdown、Python、可访问 SVG、参数交互与证据记录：

- [5.2.1 Fletcher–Reeves 方法](05._Conjugate_Gradient_Methods/5.2._Nonlinear_Conjugate_Gradient_Methods/00_5.2.1._The_Fletcher–Reeves_Method.html)：梯度平方范数之比作为系数与下降性质。
- [5.2.2 Polak–Ribière 与变体](05._Conjugate_Gradient_Methods/5.2._Nonlinear_Conjugate_Gradient_Methods/01_5.2.2._The_Polak–Ribiere_Method_and_Variants.html)：PR、Hestenes–Stiefel、PR+ 与精确线搜索下的等价。
- [5.2.3 二次终止与重启](05._Conjugate_Gradient_Methods/5.2._Nonlinear_Conjugate_Gradient_Methods/02_5.2.3._Quadratic_Termination_and_Restarts.html)：每 n+1 步定期重启与 Powell 判据。
- [5.2.4 Fletcher–Reeves 的行为](05._Conjugate_Gradient_Methods/5.2._Nonlinear_Conjugate_Gradient_Methods/03_5.2.4._Behavior_of_the_Fletcher–Reeves_Method.html)：下降角、停滞与不精确线搜索的影响。
- [5.2.5 全局收敛](05._Conjugate_Gradient_Methods/5.2._Nonlinear_Conjugate_Gradient_Methods/04_5.2.5._Global_Convergence.html)：Zoutendijk 条件、β 有界性与 PR 停滞反例。
- [5.2.6 数值表现](05._Conjugate_Gradient_Methods/5.2._Nonlinear_Conjugate_Gradient_Methods/05_5.2.6._Numerical_Performance.html)：评估账目与系数选择的经验结论。

**重要边界：**5.2 的收敛结论都以目标光滑、水平集有界、梯度 Lipschitz 且线搜索满足 Wolfe/强 Wolfe 为前提；本批数值例子均为教学算例，不代表一般问题的迭代次数或性能排序。

## 第八批：共轭梯度法 5.1

本批六篇逐页重建 5.1 线性共轭梯度，均包含独立 HTML、Markdown、Python、可访问 SVG、参数交互与证据记录：

- [5.1.1 共轭方向法](05._Conjugate_Gradient_Methods/5.1._The_Linear_Conjugate_Gradient_Method/00_5.1.1._Conjugate_Direction_Methods.html)：Q-共轭方向与正定二次问题的 n 步终止。
- [5.1.2 共轭梯度法的基本性质](05._Conjugate_Gradient_Methods/5.1._The_Linear_Conjugate_Gradient_Method/01_5.1.2._Basic_Properties_of_the_Conjugate_Gradient_Method.html)：自动共轭、残余正交与 Krylov 子空间最优性。
- [5.1.3 线性共轭梯度法的实用形式](05._Conjugate_Gradient_Methods/5.1._The_Linear_Conjugate_Gradient_Method/02_5.1.3._A_Practical_Form_of_the_Conjugate_Gradient_Method.html)：算法 5.2、向量递归与 O(n) 存储。
- [5.1.4 收敛速度](05._Conjugate_Gradient_Methods/5.1._The_Linear_Conjugate_Gradient_Method/03_5.1.4._Rate_of_Convergence.html)：κ-界、能量范数与特征值有限终止。
- [5.1.5 预条件](05._Conjugate_Gradient_Methods/5.1._The_Linear_Conjugate_Gradient_Method/04_5.1.5._Preconditioning.html)：变换后的系统与算法 5.3。
- [5.1.6 实用预条件器](05._Conjugate_Gradient_Methods/5.1._The_Linear_Conjugate_Gradient_Method/05_5.1.6._Practical_Preconditioners.html)：Jacobi、不完全 Cholesky、SSOR 与稀疏近似逆的取舍。

**重要边界：**5.1 的性质与收敛界都以对称正定矩阵、精确线搜索和精确算术为前提；浮点环境下需要重启与预条件，非线性目标属于 5.2 节。本批的数值例子均为教学算例，不代表一般问题的迭代次数或性能。

## 第七批：信赖域收敛、Hard Case 与尺度

本批八篇逐页保留原仓库路径；均包含独立 HTML、Markdown、Python、可访问 SVG、参数交互与证据记录：

- [4.2.2 收敛到驻点](04._Trust_Region_Methods/4.2._Global_Convergence/01_4.2.2._Convergence_to_Stationary_Points.html)：η=0 和 η>0 的不同全局收敛结论。
- [4.3 迭代求解子问题](04._Trust_Region_Methods/02_4.3._Iterative_Solution_of_the_Subproblem.html)：乘子 λ、谱单调性与 secular 方程。
- [4.3.1 Hard Case](04._Trust_Region_Methods/03_4.3.1._The_Hard_Case.html)：最负特征值零空间补足球面分量。
- [4.3.2 信赖域全局最优证书](04._Trust_Region_Methods/04_4.3.2._Proof_of_Theorem_4.1.html)：两个非负项给出球内全局最优性。
- [4.3.3 近精确子问题](04._Trust_Region_Methods/05_4.3.3._Convergence_of_Algorithms_Based_on_Nearly_Exact_Solutions.html)：最优模型下降比例与二阶信息。
- [4.4 信赖域 Newton 的局部速度](04._Trust_Region_Methods/06_4.4._Local_Convergence_of_Trust_Region_Newton_Methods.html)：信赖域约束消失后继承快速收敛。
- [4.5.1 尺度变换](04._Trust_Region_Methods/4.5._Other_Enhancements/00_4.5.1._Scaling.html)：正对角 D 把椭球变为圆。
- [4.5.2 其他范数](04._Trust_Region_Methods/4.5._Other_Enhancements/01_4.5.2._Trust_Regions_in_Other_Norms.html)：L1、L2 与 L∞ 球的形状和盒约束。

**重要边界：**η=0 的收敛结论弱于固定 η>0；Hard Case 不能靠简单的 secular 根搜索解决；近精确下降不等于外层优化已经收敛；尺度/范数改变可行集合，不能脱离问题结构宣称更优。

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
