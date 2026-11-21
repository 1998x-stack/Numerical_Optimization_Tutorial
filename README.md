# Numerical Optimization Tutorial

**从优化建模到数值算法的结构化学习仓库。**

课程围绕 Nocedal 与 Wright 的 *Numerical Optimization*（第二版）组织，覆盖无约束优化、线搜索、信赖域、共轭梯度、拟牛顿、导数计算、约束最优性条件、线性规划、二次规划、SQP 与内点方法。

- 课程首页：<https://1998x-stack.github.io/Numerical_Optimization_Tutorial/>
- GitHub 仓库：<https://github.com/1998x-stack/Numerical_Optimization_Tutorial>
- 教材出版信息：[Springer — Numerical Optimization, 2nd edition](https://doi.org/10.1007/978-0-387-40065-5)

## 当前内容状态

| 范围 | 状态 | 本次处理 |
|---|---|---|
| 第一章 1.1–1.5 | 已重构 | 第一批：独立文章、公式、SVG、交互、Python、证据 |
| 第一章 1.6–1.9 | 已重构 | 第二批：随机性、凸性、算法与参考方法 |
| 第二章 2.1 | 已重构 | 第二批：解的存在性、驻点与最优性证据 |
| 第二章 2.2 至第十九章 | 保留原始章节结构 | 后续逐篇重构 |
| 附录 A | 保留原始章节结构 | 后续按批次完善 |

> 仓库有 19 个主体章节和一个背景材料附录。目录存在不代表其中每篇内容都已经完成。第一章 1.1–1.9 与第二章 2.1 共十篇已重构；其余页面仍保持原始状态。

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

**阅读边界：**这五篇中的教学数据和程序均为独立构造，不代表教材原始数值实验。下一批建议从 2.2 开始。

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
