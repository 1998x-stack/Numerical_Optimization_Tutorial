(() => {
  "use strict";
  const fmt = (n, digits = 2) => Number(n).toFixed(digits);
  const read = (root, key) => Number(root.querySelector('[data-key="' + key + '"]').value);
  const bind = (root, render) => {
    const controls = root.querySelectorAll("input[data-key]");
    const update = () => {
      controls.forEach(control => {
        const value = root.querySelector('[data-value-for="' + control.dataset.key + '"]');
        if (value) value.textContent = control.value;
      });
      render(root);
    };
    controls.forEach(control => control.addEventListener("input", update));
    update();
  };
  document.querySelectorAll("[data-demo]").forEach(root => {
    const kind = root.dataset.demo;
    const output = root.querySelector("[data-output]");
    if (!output) return;
    if (kind === "formulation") bind(root, el => {
      const x = read(el, "x1"), y = read(el, "x2");
      const value = (x - 1) ** 2 + (y - 1) ** 2;
      const feasible = x >= 0 && y >= 0 && x + y >= 3;
      output.innerHTML = '<strong>f(x₁,x₂) = ' + fmt(value) + '</strong> · ' +
        (feasible ? "满足全部约束" : "当前点不可行") +
        ' · x₁ + x₂ = ' + fmt(x + y);
    });
    if (kind === "transportation") bind(root, el => {
      const x = read(el, "ax");
      const y = Math.min(25, 35 - x);
      const z = 35 - x - y;
      const bx = 20 - x, by = 25 - y, bz = 15 - z;
      const cost = 4*x + 6*y + 8*z + 5*bx + 4*by + 3*bz;
      output.innerHTML = '<strong>总成本 = ' + fmt(cost, 0) + '</strong> · A→X ' + fmt(x,0) +
        '，A→Y ' + fmt(y,0) + '，A→Z ' + fmt(z,0) +
        '；B→X ' + fmt(bx,0) + '，B→Y ' + fmt(by,0) + '，B→Z ' + fmt(bz,0) +
        '。该滑块只沿一族可行方案移动。';
    });
    if (kind === "integrality") bind(root, el => {
      const x = read(el, "x");
      const nearest = Math.round(x);
      const continuous = (x - 2.4) ** 2;
      const discrete = (nearest - 2.4) ** 2;
      output.innerHTML = '<strong>当前连续候选成本 = ' + fmt(continuous) + '</strong> · 最近整数决策 x = ' +
        nearest + '，对应成本 ' + fmt(discrete) + '。整数问题的最优值为 0.16（x = 2）。';
    });
    if (kind === "constraint") bind(root, el => {
      const x = read(el, "x");
      const value = (x - 2) ** 2;
      output.innerHTML = '<strong>f(x) = ' + fmt(value) + '</strong> · ' +
        (x <= 1 ? "可行" : "违反约束 x ≤ 1") +
        '。无约束最优点 x = 2；约束问题最优点 x = 1，目标值 1。';
    });
    if (kind === "local-global") bind(root, el => {
      let x = read(el, "x0");
      const start = x;
      const alpha = 0.01;
      for (let i = 0; i < 5000; i++) {
        const gradient = 4*x*(x*x - 1) + 0.4;
        const next = x - alpha * gradient;
        if (!Number.isFinite(next) || Math.abs(next) > 10) break;
        if (Math.abs(next - x) < 1e-11) { x = next; break; }
        x = next;
      }
      const value = (x*x - 1) ** 2 + 0.4*x;
      const basin = x < 0 ? "全局极小值附近" : "非全局局部极小值附近";
      output.innerHTML = '<strong>起点 x₀ = ' + fmt(start,2) + '</strong> → x ≈ ' +
        fmt(x,4) + '，f(x) ≈ ' + fmt(value,4) + '。当前轨迹落在：' + basin +
        '。这是固定步长梯度下降的示意，不是全局最优性证明。';
    });
    if (kind === "stochastic") bind(root, el => {
      const x = read(el, "x");
      const risk = ((x - 1) ** 2 + (x - 2) ** 2 + (x - 4) ** 2) / 3;
      output.innerHTML = '<strong>R(x) = ' + fmt(risk, 4) + '</strong> · 固定预测 D=2 的损失 ' +
        fmt((x - 2) ** 2, 4) + ' · 三场景最优 x*=7/3，R*=14/9 ≈ 1.5556';
    });
    if (kind === "convexity") bind(root, el => {
      const theta = read(el, "theta");
      const x = 4 * (1 - theta), curve = (x - 1) ** 2;
      const chord = theta * 1 + (1 - theta) * 9;
      output.innerHTML = '<strong>x = ' + fmt(x) + '，f(x) = ' + fmt(curve) + '</strong> · 弦高 ' +
        fmt(chord) + ' · 凸性差值 ' + fmt(chord - curve);
    });
    if (kind === "algorithm") bind(root, el => {
      const alpha = read(el, "alpha"), x1 = 6 * alpha;
      const contraction = Math.abs(1 - 2 * alpha);
      output.innerHTML = '<strong>梯度一步 x₁ = ' + fmt(x1) + '</strong> · f(x₁) = ' +
        fmt((x1 - 3) ** 2 + 1, 4) + ' · 误差因子 |1−2α| = ' + fmt(contraction) +
        '（' + (contraction < 1 ? "收缩" : contraction === 1 ? "不收缩" : "放大") +
        '）。牛顿一步 x₁ = 3。';
    });
    if (kind === "references") bind(root, el => {
      const k = read(el, "k"), h = 10 ** (-k), x = 1.25;
      const f = value => (value - 2) ** 2 + 1;
      const estimate = (f(x + h) - f(x - h)) / (2 * h);
      output.innerHTML = '<strong>h = 10⁻' + k + ' · 差分 = ' + fmt(estimate, 9) +
        '</strong> · 精确导数 −1.5 · 绝对误差 ' + Math.abs(estimate + 1.5).toExponential(3);
    });
    if (kind === "solution") bind(root, el => {
      const x = read(el, "x");
      output.innerHTML = '<strong>f(x) = ' + fmt((x - 2) ** 2 + 0.5, 4) +
        '</strong> · f′(x) = ' + fmt(2 * (x - 2), 4) +
        ' · 距离最优点 |x−2| = ' + fmt(Math.abs(x - 2), 4) +
        ' · 最优值 f*=0.5';
    });
    if (kind === "local-minimum") bind(root, el => {
      const a = read(el, "l1"), b = read(el, "l2"), tol = 1e-8;
      let result;
      if (a > tol && b > tol) result = "正定 Hessian：二阶充分条件，严格局部极小";
      else if (a < -tol && b < -tol) result = "负定 Hessian：严格局部极大";
      else if (a < -tol && b > tol || b < -tol && a > tol) result = "特征值异号：Hessian 不定，驻点为鞍点";
      else if (a >= -tol && b >= -tol) result = "Hessian 半正定：二阶必要条件通过，但仍需高阶信息";
      else if (a <= tol && b <= tol) result = "Hessian 半负定：二阶检验不能单独确定结论";
      else result = "至少一个曲率方向需要进一步分析";
      output.innerHTML = '<strong>λ₁=' + fmt(a, 2) + '，λ₂=' + fmt(b, 2) + '</strong> · ' + result;
    });
    if (kind === "nonsmooth") bind(root, el => {
      const y = read(el, "y"), lam = read(el, "lambda");
      const x = Math.sign(y) * Math.max(Math.abs(y) - lam, 0);
      const value = 0.5 * (x - y) ** 2 + lam * Math.abs(x);
      output.innerHTML = '<strong>x* = ' + fmt(x, 3) + '</strong> · 目标值 ' + fmt(value, 4) +
        ' · ' + (x === 0 ? '零落在次梯度区间内，系数被阈值化' : '最优系数保留了观测信号的符号');
    });
    if (kind === "strategies") bind(root, el => {
      const alpha = read(el, "alpha"), delta = read(el, "delta");
      const xLine = 1 - 8 * alpha, pTrust = -Math.min(delta, 1), xTrust = 1 + pTrust;
      output.innerHTML = '<strong>线搜索：</strong>α=' + fmt(alpha, 3) + '，x₁=' + fmt(xLine, 3) +
        '，f=' + fmt(4 * xLine * xLine, 4) + ' · <strong>信赖域：</strong>Δ=' + fmt(delta, 2) +
        '，x₁=' + fmt(xTrust, 3) + '，f=' + fmt(4 * xTrust * xTrust, 4);
    });
    if (kind === "direction") bind(root, el => {
      const angle = read(el, "theta"), slope = -Math.cos(angle * Math.PI / 180);
      output.innerHTML = '<strong>gᵀp = ' + fmt(slope, 4) + '</strong> · ' +
        (slope < -1e-8 ? '严格下降方向' : slope > 1e-8 ? '上升方向' : '一阶方向导数为零，不能据此判断');
    });
    if (kind === "trust-model") bind(root, el => {
      const delta = read(el, "delta"), p = -Math.min(delta, 1);
      const predicted = 1 - (1 + p + 0.5 * p * p);
      const actual = 1 - Math.exp(p);
      const rho = actual / predicted;
      output.innerHTML = '<strong>步 p=' + fmt(p, 3) + '</strong> · 预测下降 ' + fmt(predicted, 5) +
        ' · 实际下降 ' + fmt(actual, 5) + ' · ρ=' + fmt(rho, 5) +
        ' · ' + (rho > 0.75 ? '模型预测较准确，可考虑扩大半径（若步子触及边界）' : '继续评估模型与半径');
    });
    if (kind === "scaling") bind(root, el => {
      const scale = read(el, "scale"), eig = 100 * scale * scale;
      const condition = Math.max(eig, 1) / Math.min(eig, 1);
      output.innerHTML = '<strong>缩放后 Hessian = diag(' + fmt(eig, 4) + ', 1)</strong> · 条件数 κ₂ = ' +
        fmt(condition, 4) + (Math.abs(condition - 1) < 1e-8 ? ' · 本例已变为单位矩阵' : '');
    });
    if (kind === "exercises") bind(root, el => {
      const n = Math.round(read(el, "problem"));
      const answers = {
        1: "x*=8/3，y*=−4/3；H 特征值 1、3；f*=−16/3。",
        2: "软阈值解 x*=1；此时次梯度为 {1}，一阶条件成立。",
        3: "gᵀp₁=−1：下降；gᵀp₂=0：不是严格下降方向。",
        4: "预测下降 0.21875，实际下降约 0.221199，ρ≈1.0112。",
        5: "取 s=0.2，缩放后 Hessian 为 I，条件数由 25 降至 1。"
      };
      output.textContent = '题 ' + n + '：' + answers[n];
    });
    if (kind === "step-length") bind(root, el => {
      const alpha = read(el, "alpha");
      const phi = (4 * alpha - 2) ** 2, slope0 = -16, slope = 32 * alpha - 16;
      const armijoBound = 4 + 1e-4 * alpha * slope0;
      const c = 0.2, goldLower = 4 + (1-c) * alpha * slope0, goldUpper = 4 + c * alpha * slope0;
      const armijo = phi <= armijoBound + 1e-12;
      const weak = armijo && slope >= 0.9 * slope0;
      const strong = armijo && Math.abs(slope) <= 0.9 * Math.abs(slope0);
      const gold = phi >= goldLower - 1e-12 && phi <= goldUpper + 1e-12;
      output.innerHTML = '<strong>φ(α)=' + fmt(phi, 4) + '</strong> · Armijo ' + (armijo ? '通过' : '未通过') +
        ' · 弱 Wolfe ' + (weak ? '通过' : '未通过') + ' · 强 Wolfe ' + (strong ? '通过' : '未通过') +
        ' · Goldstein ' + (gold ? '通过' : '未通过');
    });
  });
  const search = document.querySelector("[data-course-search]");
  if (search) {
    const cards = [...document.querySelectorAll("[data-chapter-card]")];
    const count = document.querySelector("[data-chapter-count]");
    const update = () => {
      const query = search.value.trim().toLocaleLowerCase();
      let visible = 0;
      cards.forEach(card => {
        const match = card.textContent.toLocaleLowerCase().includes(query);
        card.hidden = !match;
        if (match) visible++;
      });
      if (count) count.textContent = "显示 " + visible + " / " + cards.length + " 个章节";
    };
    search.addEventListener("input", update);
    update();
  }
})();