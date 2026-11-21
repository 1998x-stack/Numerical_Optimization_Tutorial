(() => {
  "use strict";
  const fmt = (n, digits = 2) => Number(n).toFixed(digits);
  const read = (root, key) => Number(root.querySelector('[data-key="' + key + '"]').value);
  const bind = (root, render) => {
    const controls = root.querySelectorAll("input[data-key]");
    const update = () => render(root);
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