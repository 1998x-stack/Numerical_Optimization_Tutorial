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
    if (kind === "wolfe") bind(root, el => {
      const alpha = read(el, "alpha"), c1 = 1e-4, c2 = 0.9;
      const phi = (4 * alpha - 2) ** 2, slope0 = -16, slope = 32 * alpha - 16;
      const armijo = phi <= 4 + c1 * alpha * slope0 + 1e-12;
      const weak = armijo && slope >= c2 * slope0;
      const strong = armijo && Math.abs(slope) <= c2 * Math.abs(slope0);
      output.innerHTML = '<strong>φ(α)=' + fmt(phi, 4) + '</strong> · φ′(α)=' + fmt(slope, 3) +
        ' · Armijo ' + (armijo ? '通过' : '未通过') +
        ' · 弱 Wolfe ' + (weak ? '通过' : '未通过') +
        ' · 强 Wolfe ' + (strong ? '通过' : '未通过');
    });
    if (kind === "goldstein") bind(root, el => {
      const alpha = read(el, "alpha"), c = 0.2;
      const phi = 19 * alpha ** 3 - 28 * alpha ** 2 - alpha;
      const slope0 = -1;
      const lower = (1-c) * alpha * slope0, upper = c * alpha * slope0;
      const accepted = phi >= lower - 1e-10 && phi <= upper + 1e-10;
      output.innerHTML = '<strong>φ(α)=' + fmt(phi, 4) + '</strong> · Goldstein 区间 [' +
        fmt(lower, 3) + ', ' + fmt(upper, 3) + '] · ' +
        (accepted ? '候选步通过' : '候选步不通过') +
        (Math.abs(alpha-1)<1e-8 ? ' · α=1 是本例的精确极小点' : '');
    });
    if (kind === "backtracking") bind(root, el => {
      const alpha0 = read(el, "alpha0"), rho = read(el, "rho"), c = 1e-4;
      let alpha = alpha0, trials = 0, accepted = false;
      while (trials < 100) {
        trials += 1;
        const value = (4 * alpha - 2) ** 2;
        if (value <= 4 + c * alpha * (-16) + 1e-12) { accepted = true; break; }
        alpha *= rho;
      }
      const value = (4 * alpha - 2) ** 2;
      output.innerHTML = '<strong>' + (accepted ? '接受 α=' + fmt(alpha, 5) : '未在 100 次内通过') +
        '</strong> · 试探次数 ' + trials + ' · φ(α)=' + fmt(value, 5) +
        ' · 最终步长 / 初始步长 = ' + fmt(alpha / alpha0, 4);
    });
    if (kind === "zoutendijk") bind(root, el => {
      const delta = read(el, "delta"), n = Math.round(read(el, "n"));
      let harmonic = 0;
      for (let k = 1; k <= n; k++) harmonic += 1 / (k * k);
      const sumA = delta * delta * harmonic;
      const sumB = harmonic;
      output.innerHTML = '<strong>A 组加权和 ≈ ' + fmt(sumA, 5) + '</strong> · 最后梯度范数 1/N=' +
        fmt(1 / n, 5) + '，趋于 0 · <strong>B 组加权和 ≈ ' + fmt(sumB, 5) +
        '</strong> · 梯度范数始终为 1；它说明缺少角度下界时不能推出梯度趋零。';
    });
    if (kind === "rates") bind(root, el => {
      const n = Math.round(read(el, "steps"));
      let linear = 0.5, superlinear = 0.5, quadratic = 0.5;
      for (let k = 0; k < n; k++) {
        linear *= 0.5;
        superlinear = Math.pow(superlinear, 1.5);
        quadratic *= quadratic;
      }
      const prevSuper = Math.pow(superlinear, 1 / 1.5);
      const prevQuad = Math.sqrt(quadratic);
      output.innerHTML = '<strong>第 ' + n + ' 轮误差：</strong>线性 ' + linear.toExponential(3) +
        ' · 超线性 ' + superlinear.toExponential(3) + ' · 二次 ' + quadratic.toExponential(3) +
        '<br>本轮相邻比值：线性 0.5 · 超线性 ' + fmt(superlinear / prevSuper, 5) +
        ' · 二次 ' + fmt(quadratic / prevQuad, 5);
    });
    if (kind === "steepest") bind(root, el => {
      const kappa = read(el, "kappa"), steps = Math.round(read(el, "steps"));
      let x = [1, 1], f = 0.5 * (1 + kappa);
      for (let k = 0; k < steps; k++) {
        const g = [x[0], kappa * x[1]];
        const numerator = g[0] * g[0] + g[1] * g[1];
        if (numerator < 1e-28) break;
        const denominator = g[0] * g[0] + kappa * g[1] * g[1];
        const alpha = numerator / denominator;
        x = [x[0] - alpha * g[0], x[1] - alpha * g[1]];
        f = 0.5 * (x[0] * x[0] + kappa * x[1] * x[1]);
      }
      const factor = ((kappa - 1) / (kappa + 1)) ** 2;
      output.innerHTML = '<strong>κ=' + fmt(kappa, 0) + '，第 ' + steps + ' 轮 f=' + f.toExponential(3) +
        '</strong> · 理论最坏情况因子 ' + fmt(factor, 5) +
        ' · 当前点 (' + fmt(x[0], 5) + ', ' + fmt(x[1], 5) + ')';
    });
    if (kind === "newton") bind(root, el => {
      let x = read(el, "x0"), history = [x];
      for (let k = 0; k < 6; k++) {
        x -= (x + x ** 3) / (1 + 3 * x * x);
        history.push(x);
      }
      const e = Math.abs(history[history.length - 1]);
      const ratio = Math.abs(history[2]) / (Math.abs(history[1]) ** 2);
      output.innerHTML = '<strong>x₆=' + fmt(x, 8) + '</strong> · |x₆−x*|=' + e.toExponential(3) +
        ' · 第一次二次比值 e₂/e₁²=' + fmt(ratio, 5) +
        ' · 误差序列：' + history.slice(0, 4).map(v => fmt(Math.abs(v), 5)).join(' → ');
    });
    if (kind === "quasi") bind(root, el => {
      const scale = read(el, "scale"), Q = [[4,1],[1,3]];
      let B = [[scale,0],[0,1]], x = [2,-1], records = [];
      const dot = (a,b) => a[0]*b[0] + a[1]*b[1];
      const mv = (A,v) => [A[0][0]*v[0]+A[0][1]*v[1], A[1][0]*v[0]+A[1][1]*v[1]];
      const solve = (A,b) => {
        const det = A[0][0]*A[1][1]-A[0][1]*A[1][0];
        return [(A[1][1]*b[0]-A[0][1]*b[1])/det,(-A[1][0]*b[0]+A[0][0]*b[1])/det];
      };
      for (let k=0;k<5;k++) {
        const g=mv(Q,x);
        if (Math.hypot(g[0],g[1])<1e-10) break;
        const p=solve(B,[-g[0],-g[1]]);
        const Qp=mv(Q,p), alpha=-dot(g,p)/dot(p,Qp);
        const s=[alpha*p[0],alpha*p[1]], xn=[x[0]+s[0],x[1]+s[1]], gn=mv(Q,xn);
        const y=[gn[0]-g[0],gn[1]-g[1]], Bs=mv(B,s), sBs=dot(s,Bs), ys=dot(y,s);
        if (sBs<=0 || ys<=0) break;
        const Bn=B.map((row,i)=>row.map((v,j)=>v-Bs[i]*Bs[j]/sBs+y[i]*y[j]/ys));
        const sec=mv(Bn,s), residual=Math.max(Math.abs(sec[0]-y[0]),Math.abs(sec[1]-y[1]));
        const det=Bn[0][0]*Bn[1][1]-Bn[0][1]*Bn[1][0];
        records.push({ys,residual,det}); B=Bn; x=xn;
      }
      const worst=records.reduce((m,r)=>Math.max(m,r.residual),0);
      const minYs=records.reduce((m,r)=>Math.min(m,r.ys),Infinity);
      output.innerHTML = '<strong>完成 ' + records.length + ' 次 BFGS 更新</strong> · 最小 yᵀs=' +
        fmt(minYs, 5) + ' · 最大割线残差=' + worst.toExponential(2) +
        ' · 最终 det(B)=' + fmt(records.length ? records[records.length-1].det : 0, 5) +
        ' · x≈(' + fmt(x[0], 5) + ', ' + fmt(x[1], 5) + ')';
    });
    if (kind === "hessian-overview") bind(root, el => {
      const tau = read(el, "tau"), a = tau + 2, b = tau - 2;
      if (Math.abs(a) < 1e-10 || Math.abs(b) < 1e-10) {
        output.innerHTML = '<strong>B 在当前 τ 下奇异</strong>，无法唯一解 Bp=−g；需要继续增大修正。';
        return;
      }
      const p = [-2/a, 2/b], slope = 2*p[0]-2*p[1];
      output.innerHTML = '<strong>λ(B)=(' + fmt(a,2) + ', ' + fmt(b,2) + ')</strong> · p=(' +
        fmt(p[0],3) + ', ' + fmt(p[1],3) + ') · gᵀp=' + fmt(slope,4) + ' · ' +
        (a>0 && b>0 ? '严格正定，保证下降' : '不满足正定性保证');
    });
    if (kind === "eigenfloor") bind(root, el => {
      const d=read(el,"delta"), pos=Math.max(3,d), neg=d;
      const a=(pos+neg)/2, b=(pos-neg)/2, det=pos*neg;
      const p0=(-a+2*b)/det, p1=(b-2*a)/det, slope=p0+2*p1;
      output.innerHTML = '<strong>裁剪后特征值 (' + fmt(pos,2) + ', ' + fmt(neg,2) +
        ')</strong> · B=[[' + fmt(a,3) + ',' + fmt(b,3) + '],[' + fmt(b,3) + ',' +
        fmt(a,3) + ']] · gᵀp=' + fmt(slope,4) + ' · κ(B)=' + fmt(Math.max(pos,neg)/Math.min(pos,neg),3);
    });
    if (kind === "identityshift") bind(root, el => {
      const tau=read(el,"tau"), a=tau-1, b=tau+3;
      if (a<=0 || b<=0) {
        output.innerHTML = '<strong>λ(B)=(' + fmt(a,2) + ',' + fmt(b,2) +
          ')</strong> · B 尚未严格正定；不能保证修正方向下降。';
        return;
      }
      const p=[-1/a,-2/b], slope=p[0]+2*p[1];
      output.innerHTML = '<strong>λ(B)=(' + fmt(a,2) + ',' + fmt(b,2) +
        ')</strong> · p=(' + fmt(p[0],4) + ',' + fmt(p[1],4) + ') · gᵀp=' +
        fmt(slope,4) + ' · κ(B)=' + fmt(b/a,3);
    });
    if (kind === "modcholesky") bind(root, el => {
      const delta=read(el,"delta"), d1=Math.max(1,delta), l=2/d1;
      const raw2=1-l*l*d1, d2=Math.max(raw2,delta);
      const a=d1,b=2,c=l*l*d1+d2, det=a*c-b*b;
      const p0=(-c+b)/det,p1=(b-a)/det;
      output.innerHTML = '<strong>原第二主元 c₂₂=' + fmt(raw2,3) +
        ' → 修正 d₂=' + fmt(d2,3) + '</strong> · det(B)=' + fmt(det,3) +
        ' · p=(' + fmt(p0,3) + ',' + fmt(p1,3) + ') · gᵀp=' + fmt(p0+p1,3);
    });
    if (kind === "indefiniteblock") bind(root, el => {
      const delta=read(el,"delta"), a=(2+delta)/2, b=(2-delta)/2;
      const p=1/delta, slope=-2*p;
      output.innerHTML = '<strong>修正特征值 (2, ' + fmt(delta,2) +
        ')</strong> · B=[[' + fmt(a,3) + ',' + fmt(b,3) + '],[' +
        fmt(b,3) + ',' + fmt(a,3) + ']] · det(B)=' + fmt(2*delta,3) +
        ' · gᵀp=' + fmt(slope,3);
    });
    if (kind === "bracketsearch") bind(root, el => {
      const n=Math.round(read(el,"n"));let lo=0,hi=5;const mids=[];
      for(let k=0;k<n;k++){
        const mid=(lo+hi)/2;mids.push(fmt(mid,5));
        const deriv=2*(mid-2);
        if(deriv>0)hi=mid;else if(deriv<0)lo=mid;else{lo=hi=mid;break;}
      }
      output.innerHTML = '<strong>新区间 [' + fmt(lo,6) + ', ' + fmt(hi,6) +
        ']</strong> · 宽度 ' + fmt(hi-lo,6) +
        ' · 中点序列：' + mids.join(' → ') + ' · 真实驻点 α*=2 仍被括住';
    });
    if (kind === "interpsearch") bind(root, el => {
      const eps=read(el,"eps"), estimate=2/(1+eps);
      const exact=eps===0?2:(-2+Math.sqrt(4+48*eps))/(6*eps);
      const phi=a=>(a-2)**2+eps*a**3;
      output.innerHTML = '<strong>插值候选 α=' + fmt(estimate,5) +
        '</strong> · 真实驻点 α*=' + fmt(exact,5) +
        ' · |候选−驻点|=' + fmt(Math.abs(estimate-exact),5) +
        ' · φ(候选)=' + fmt(phi(estimate),5);
    });
    if (kind === "initialstep") bind(root, el => {
      const prev=read(el,"prev"), alpha=Math.max(0.1,Math.min(4,prev*2));
      const f=(alpha-2)**2, d=2*(alpha-2);
      const armijo=f<=4+1e-4*alpha*(-4);
      const strong=armijo&&Math.abs(d)<=3.6;
      output.innerHTML = '<strong>建议 α₀=' + fmt(alpha,3) + '</strong> · φ(α₀)=' +
        fmt(f,4) + ' · Armijo：' + (armijo?'通过':'未通过') +
        ' · 强 Wolfe：' + (strong?'通过':'未通过') + '。候选不通过时必须继续线搜索。';
    });
    if (kind === "wolfezoom") bind(root, el => {
      const start=read(el,"start"), c1=1e-4, c2=0.1, f=a=>(a-2)**2, g=a=>2*(a-2);
      const good=a=>f(a)<=4-4*c1*a;
      let lo=0, hi=start, a=start, previous=0, trials=[], accepted=null;
      for(let i=0;i<28;i++){
        trials.push("试探 "+fmt(a,3));
        if(!good(a)||(i>0&&f(a)>=f(previous))){lo=previous;hi=a;break;}
        if(Math.abs(g(a))<=4*c2){accepted=a;break;}
        if(g(a)>=0){lo=a;hi=previous;break;}
        previous=a; a=Math.min(2*a,16);
        if(a===previous)break;
      }
      if(accepted===null){
        for(let j=0;j<50;j++){
          const mid=(lo+hi)/2;
          trials.push("zoom "+fmt(mid,3));
          if(Math.abs(hi-lo)<1e-11)break;
          if(!good(mid)||f(mid)>=f(lo))hi=mid;
          else{
            const slope=g(mid);
            if(Math.abs(slope)<=4*c2){accepted=mid;break;}
            if(slope*(hi-lo)>=0)hi=lo;
            lo=mid;
          }
        }
      }
      const aout=accepted===null?"尚未找到":fmt(accepted,5);
      output.innerHTML='<strong>α='+aout+'</strong> · 初始 α₁='+fmt(start,2)+
        ' · 试探：'+trials.join(' → ')+
        (accepted===null?' · 搜索失败':' · Armijo 与强 Wolfe 同时通过');
    });
    if (kind === "floatingstop") bind(root, el => {
      const n=Math.round(read(el,"power")), x=10**n;
      const next=x+1, same=next===x, ulp=2**(Math.floor(Math.log2(x))-52);
      output.innerHTML='<strong>10^'+n+' + 1 '+(same?'等于':'不等于')+' 10^'+n+
        '</strong> · 该尺度附近浮点相邻间距约 '+ulp.toExponential(3)+
        ' · '+(same?'新点未改变，应报告精度停滞':'新点仍可区分');
    });
    if (kind === "lineexercises") bind(root, el => {
      const n=Math.round(read(el,"exercise"));
      const answers=[
        '强 Wolfe：|2(α−2)|≤0.4，曲率区间为 [1.8,2.2]；α=2 也通过 Armijo。',
        '二次精确线搜索：α=(gᵀg)/(gᵀBg)=17/65≈0.261538；新点位于同一条下降直线上。',
        'Armijo 回溯：8 拒绝、4 拒绝、2 接受，共三次函数值试探。',
        '不定 Hessian：gᵀpᴺ=3.5，上坡；正定修正后 gᵀp=−4.25，严格下降。'
      ];
      output.innerHTML='<strong>练习 '+n+'：</strong>'+answers[n-1];
    });
    if (kind === "trcauchy") bind(root, el => {
      const D=read(el,"radius"),t=Math.min(.25,D/2), p=-2*t, dec=-2*p-2*p*p;
      output.innerHTML='<strong>Δ='+fmt(D,2)+'，Cauchy p=('+fmt(p,4)+', 0)</strong>'+
        ' · 预测下降 '+fmt(dec,5)+' · '+(2*t<D-1e-10?'位于球内':'由半径限制');
    });
    if (kind === "trbetter") bind(root, el => {
      const theta=read(el,"angle")*Math.PI/180, p=[-Math.cos(theta),-Math.sin(theta)];
      const reduction=v=>-(2*v[0]+2*v[1]+.5*(4*v[0]**2+v[1]**2));
      const base=[-1/Math.SQRT2,-1/Math.SQRT2], current=reduction(p), baseline=reduction(base);
      output.innerHTML='<strong>θ='+fmt(read(el,"angle"),0)+'°，候选下降='+fmt(current,5)+'</strong>'+
        ' · Cauchy 基准 '+fmt(baseline,5)+' · '+(current>baseline?'候选改善模型下降':'该候选未超过基准')+
        ' · ‖p‖=1';
    });
    if (kind === "trdogleg") bind(root, el => {
      const D=read(el,"radius"),u=[-.8,-.8],N=[-.5,-2],norm=Math.hypot;
      const du=norm(...u),dn=norm(...N);
      let p,phase;
      if(D<=du){p=[-D/Math.SQRT2,-D/Math.SQRT2];phase="负梯度段";}
      else if(D>=dn){p=N;phase="完整 Newton 步";}
      else{
        const v=[N[0]-u[0],N[1]-u[1]],A=v[0]**2+v[1]**2,B=2*(u[0]*v[0]+u[1]*v[1]),C=u[0]**2+u[1]**2-D*D;
        const t=(-B+Math.sqrt(Math.max(0,B*B-4*A*C)))/(2*A);
        p=[u[0]+t*v[0],u[1]+t*v[1]];phase="折线第二段";
      }
      const dec=-(2*p[0]+2*p[1]+.5*(4*p[0]**2+p[1]**2));
      output.innerHTML='<strong>'+phase+'：p=('+fmt(p[0],4)+','+fmt(p[1],4)+')</strong>'+
        ' · ‖p‖='+fmt(norm(...p),4)+' ≤ Δ='+fmt(D,2)+' · 模型下降 '+fmt(dec,5);
    });
    if (kind === "trsubspace") bind(root, el => {
      const D=read(el,"radius"),n=l=>Math.hypot(2/(4+l),2/(1+l));
      let lam=0;
      if(n(0)>D){
        let lo=0,hi=1;
        while(n(hi)>D && hi<1e8)hi*=2;
        for(let i=0;i<80;i++){const mid=(lo+hi)/2;if(n(mid)>D)lo=mid;else hi=mid;}
        lam=(lo+hi)/2;
      }
      const p=[-2/(4+lam),-2/(1+lam)],drop=-(2*p[0]+2*p[1]+.5*(4*p[0]**2+p[1]**2));
      output.innerHTML='<strong>λ='+fmt(lam,6)+'，p=('+fmt(p[0],4)+','+fmt(p[1],4)+')</strong>'+
        ' · ‖p‖='+fmt(n(lam),4)+' · 模型下降 '+fmt(drop,6)+
        (lam===0?' · Newton 步在球内':' · 半径约束激活');
    });
    if (kind === "trbound") bind(root, el => {
      const D=read(el,"radius"),t=Math.min(.25,D/2),p=-2*t;
      const reduction=-2*p-2*p*p,low=Math.min(D,.5);
      output.innerHTML='<strong>Δ='+fmt(D,2)+'：Cauchy 下降='+fmt(reduction,6)+'</strong>'+
        ' · 理论下界='+fmt(low,6)+' · 下降 ≥ 下界：'+(reduction+1e-12>=low?'成立':'不成立');
    });

    if (kind === "tr-stationary") bind(root, el => {
      const D=read(el,"delta"),t=1;
      const f=y=>.5*(y-1)**2+.1*(y-1)**4;
      const g=1.4,h=2.2,p=Math.max(-D,Math.min(D,-g/h));
      const pred=-g*p-.5*h*p*p,act=f(2)-f(2+p),rho=act/pred;
      output.innerHTML='<strong>Δ='+fmt(D,2)+'，p='+fmt(p,5)+'</strong> · 预测下降 '+fmt(pred,5)+
        ' · 实际下降 '+fmt(act,5)+' · ρ='+fmt(rho,5)+(rho>=.1?' · 达到 η=0.1':' · 不接受');
    });
    if (kind === "tr-secular") bind(root, el => {
      const D=read(el,"delta"),p=l=>[-2/(4+l),-2/(1+l)];
      const n=l=>Math.hypot(...p(l));
      let lambda=0;
      if(n(0)>D) {
        let lo=0,hi=1;
        while(n(hi)>D)hi*=2;
        for(let k=0;k<64;k++){
          const m=(lo+hi)/2;
          if(n(m)>D)lo=m;else hi=m;
        }
        lambda=(lo+hi)/2;
      }
      const v=p(lambda);
      const drop=-(2*v[0]+2*v[1]+.5*(4*v[0]*v[0]+v[1]*v[1]));
      output.innerHTML='<strong>λ='+fmt(lambda,6)+'</strong> · p=('+
        fmt(v[0],5)+', '+fmt(v[1],5)+') · ‖p‖='+fmt(n(lambda),5)+
        ' · 模型下降 '+fmt(drop,6);
    });
    if (kind === "tr-hardcase") bind(root, el => {
      const D=read(el,"delta");
      const x=Math.sqrt(Math.max(0,D*D-1/9)),y=-1/3;
      const q=y-x*x+.5*y*y;
      output.innerHTML='<strong>临界 λ=2，p=(±'+fmt(x,6)+', '+fmt(y,5)+')</strong>'+
        ' · ‖p‖='+fmt(Math.hypot(x,y),5)+' · 模型最小值 '+fmt(q,6)+
        ' · 开区间 λ>2 的最小范数步无法到达该半径';
    });
    if (kind === "tr-certificate") bind(root, el => {
      const angle=read(el,"theta")*Math.PI/180,radius=1.6;
      const v=[radius*Math.cos(angle),radius*Math.sin(angle)];
      const star=[Math.sqrt(35)/3,-1/3],q=p=>p[1]-p[0]*p[0]+.5*p[1]*p[1];
      const first=1.5*(v[1]-star[1])**2,second=4-radius*radius;
      const diff=q(v)-q(star);
      output.innerHTML='<strong>q(v)−q(p*)='+fmt(diff,6)+'</strong>'+
        ' · 曲率项 '+fmt(first,6)+' + 球面互补项 '+fmt(second,6)+
        ' · 两项非负，解析证书成立';
    });
    if (kind === "tr-nearly-exact") bind(root, el => {
      const t=read(el,"t"),drop=t*t+5/18,ratio=drop/(25/6);
      output.innerHTML='<strong>t='+fmt(t,2)+'，预测下降='+fmt(drop,6)+'</strong>'+
        ' · 最优下降 25/6 · 比例 '+fmt(100*ratio,2)+'%'+
        (ratio>=.6?' · 满足 c₁=0.6':' · 未达到 c₁=0.6')+
        ' · ‖p‖='+fmt(Math.hypot(t,1/3),5);
    });
    if (kind === "tr-newton-local") bind(root, el => {
      const x=read(el,"x"),g=x+.3*x*x+.2*x**3,h=1+.6*x+.6*x*x;
      const n=-g/h,D=.3,p=Math.max(-D,Math.min(D,n));
      const f=z=>.5*z*z+.1*z**3+.05*z**4;
      const pred=-g*p-.5*h*p*p,rho=(f(x)-f(x+p))/pred;
      output.innerHTML='<strong>完整 Newton 步 '+fmt(n,6)+'</strong>'+
        ' · Δ='+fmt(D,2)+' · 使用步 '+fmt(p,6)+
        ' · ρ='+fmt(rho,5)+' · '+(Math.abs(n)<=D?'完整 Newton 步可行':'需要截断');
    });
    if (kind === "tr-scaling") bind(root, el => {
      const d=read(el,"scale"),g=[10/d,1],B=[100/(d*d),1],r=1;
      const p=l=>[-g[0]/(B[0]+l),-g[1]/(B[1]+l)];
      const n=l=>Math.hypot(...p(l));
      let lambda=0;
      if(n(0)>r){
        let lo=0,hi=1;
        while(n(hi)>r)hi*=2;
        for(let k=0;k<65;k++){const m=(lo+hi)/2;if(n(m)>r)lo=m;else hi=m;}
        lambda=(lo+hi)/2;
      }
      const v=p(lambda),original=[v[0]/d,v[1]];
      const drop=-(10*original[0]+original[1]+.5*(100*original[0]**2+original[1]**2));
      output.innerHTML='<strong>D=diag('+fmt(d,0)+',1)</strong> · 缩放后 B̃=diag('+
        fmt(B[0],4)+',1) · p=('+fmt(original[0],5)+','+fmt(original[1],5)+
        ') · ‖Dp‖='+fmt(n(lambda),5)+' · 模型下降 '+fmt(drop,6);
    });
    if (kind === "tr-norms") bind(root, el => {
      const D=read(el,"delta"),X=[.2,.3];
      const p=[Math.max(-Math.min(X[0],D),Math.min(D,-.5)),
               Math.max(-Math.min(X[1],D),Math.min(D,-.5))];
      const n1=Math.abs(p[0])+Math.abs(p[1]),n2=Math.hypot(...p),ni=Math.max(Math.abs(p[0]),Math.abs(p[1]));
      const drop=-(p[0]+2*p[1]+p[0]**2+2*p[1]**2);
      output.innerHTML='<strong>盒内最优 p=('+fmt(p[0],3)+','+fmt(p[1],3)+')</strong>'+
        ' · 预测下降 '+fmt(drop,5)+' · ‖p‖₁='+fmt(n1,4)+
        '，‖p‖₂='+fmt(n2,4)+'，‖p‖∞='+fmt(ni,4);
    });
    if (kind === "cg-conjugate") bind(root, el => {
      const t = read(el, "slope");
      const Q = [[3, 1], [1, 3]], b = [5, 7];
      const mv = v => [Q[0][0]*v[0] + Q[0][1]*v[1], Q[1][0]*v[0] + Q[1][1]*v[1]];
      const dot = (u, v) => u[0]*v[0] + u[1]*v[1];
      const grad = x => { const q = mv(x); return [q[0]-b[0], q[1]-b[1]]; };
      let x = [0, 0];
      const p0 = [1, 0];
      let a = -dot(grad(x), p0) / dot(p0, mv(p0));
      x = [x[0] + a*p0[0], x[1] + a*p0[1]];
      const p1 = [1, t];
      a = -dot(grad(x), p1) / dot(p1, mv(p1));
      x = [x[0] + a*p1[0], x[1] + a*p1[1]];
      const conj = 3 + t, err = Math.hypot(x[0]-1, x[1]-2);
      output.innerHTML = '<strong>p₁=(1,' + fmt(t,1) + ')，x₂=(' + fmt(x[0],4) + ', ' +
        fmt(x[1],4) + ')</strong> · p₁ᵗQp₀=' + fmt(conj,3) + ' · 与 x* 距离 ' + err.toExponential(2) +
        (err < 1e-9 ? ' · 共轭，两步命中 x*' : ' · 不共轭');
    });
    if (kind === "cg-orthogonal") bind(root, el => {
      const t = read(el, "t");
      const Q = [[3, 1], [1, 3]], b = [5, 7];
      const mv = v => [Q[0][0]*v[0] + Q[0][1]*v[1], Q[1][0]*v[0] + Q[1][1]*v[1]];
      const dot = (u, v) => u[0]*v[0] + u[1]*v[1];
      const grad = x => { const q = mv(x); return [q[0]-b[0], q[1]-b[1]]; };
      let x = [t, t];
      const g0 = grad(x);
      let g = g0, p = [-g[0], -g[1]];
      let a = -dot(g, p) / dot(p, mv(p));
      x = [x[0] + a*p[0], x[1] + a*p[1]];
      const g1 = grad(x);
      const beta = dot(g1, g1) / dot(g, g);
      p = [-g1[0] + beta*p[0], -g1[1] + beta*p[1]];
      g = g1;
      a = -dot(g, p) / dot(p, mv(p));
      x = [x[0] + a*p[0], x[1] + a*p[1]];
      const orth = dot(g0, g1), err = Math.hypot(x[0]-1, x[1]-2);
      output.innerHTML = '<strong>x₀=(' + fmt(t,1) + ',' + fmt(t,1) + ')，x₂=(' +
        fmt(x[0],4) + ', ' + fmt(x[1],4) + ')</strong> · g₀ᵗg₁=' + orth.toExponential(2) +
        ' · 与 x* 距离 ' + err.toExponential(2) +
        (Math.abs(orth) < 1e-9 && err < 1e-9 ? ' · 正交且两步命中' : ' · 数值退化');
    });
    if (kind === "cg-practical") bind(root, el => {
      const t = read(el, "t");
      const Q = [[3, 1], [1, 3]], b = [5, 7];
      const mv = v => [Q[0][0]*v[0] + Q[0][1]*v[1], Q[1][0]*v[0] + Q[1][1]*v[1]];
      const dot = (u, v) => u[0]*v[0] + u[1]*v[1];
      let x = [t, t];
      let g = [mv(x)[0]-b[0], mv(x)[1]-b[1]];
      let p = [-g[0], -g[1]];
      let gn = dot(g, g);
      const rows = ['k=0: ‖g‖=' + Math.sqrt(gn).toFixed(4)];
      for (let k = 0; k < 3; k++) {
        if (Math.sqrt(gn) <= 1e-9) break;
        const Qp = mv(p);
        const alpha = gn / dot(p, Qp);
        x = [x[0] + alpha*p[0], x[1] + alpha*p[1]];
        g = [g[0] + alpha*Qp[0], g[1] + alpha*Qp[1]];
        const gnNew = dot(g, g), beta = gnNew / gn;
        rows.push('k=' + (k+1) + ': α=' + alpha.toFixed(4) + ', β=' + beta.toFixed(4) +
          ', ‖g‖=' + Math.sqrt(gnNew).toFixed(4));
        p = [-g[0] + beta*p[0], -g[1] + beta*p[1]];
        gn = gnNew;
      }
      output.innerHTML = '<strong>x₀=(' + fmt(t,1) + ',' + fmt(t,1) + ')</strong><br>' +
        rows.join('<br>') + '<br>结束时 ‖g‖=' + Math.sqrt(gn).toExponential(2) +
        '，x≈(' + fmt(x[0],4) + ', ' + fmt(x[1],4) + ')';
    });
    if (kind === "cg-rate") bind(root, el => {
      const kappa = read(el, "kappa"), n = 20;
      const lam = Array.from({length:n}, (_, i) => 1 + (kappa-1)*i/(n-1));
      const dot = (u, v) => u.reduce((s, x, i) => s + x*v[i], 0);
      const mulQ = v => v.map((x, i) => lam[i]*x);
      let x = new Array(n).fill(0);
      let g = lam.map(l => -l);
      let p = g.map(v => -v);
      let gn = dot(g, g);
      const energy = () => Math.sqrt(lam.reduce((s, l, i) => s + l*(x[i]-1)**2, 0));
      const target = 5;
      let actual = energy();
      for (let k = 0; k < target; k++) {
        if (Math.sqrt(gn) <= 1e-14) break;
        const Qp = mulQ(p);
        const alpha = gn / dot(p, Qp);
        x = x.map((v, i) => v + alpha*p[i]);
        g = g.map((v, i) => v + alpha*Qp[i]);
        const gnNew = dot(g, g), beta = gnNew/gn;
        p = p.map((v, i) => -g[i] + beta*v);
        gn = gnNew;
        actual = energy();
      }
      const rho = (Math.sqrt(kappa)-1)/(Math.sqrt(kappa)+1);
      const e0 = Math.sqrt(lam.reduce((s, l) => s + l, 0));
      const bound = 2*Math.pow(rho, target)*e0;
      output.innerHTML = '<strong>κ=' + fmt(kappa,1) + '，ρ=' + fmt(rho,4) + '</strong><br>' +
        '5 步后实际能量范数误差 ' + actual.toExponential(2) +
        '<br>定理 5.3 上界 ' + bound.toExponential(2) + '（初始误差 ' + e0.toFixed(3) + '）' +
        (actual <= bound + 1e-12 ? ' · 满足上界' : ' · 超出上界');
    });
    if (kind === "cg-precond") bind(root, el => {
      const pp = read(el, "p");
      const lam = [1, 4, 16, 64], n = 4;
      const m = lam.map(l => Math.pow(l, pp));
      let x = new Array(n).fill(0);
      let g = lam.map(l => -l);
      let z = g.map((v, i) => v/m[i]);
      let pd = z.map(v => -v);
      let gz = g.reduce((s, v, i) => s + v*z[i], 0);
      const norm = () => Math.sqrt(g.reduce((s, v) => s + v*v, 0));
      let iters = 0;
      for (let k = 0; k < 10; k++) {
        if (norm() <= 1e-10) break;
        const Qp = pd.map((v, i) => lam[i]*v);
        const alpha = gz / pd.reduce((s, v, i) => s + v*Qp[i], 0);
        x = x.map((v, i) => v + alpha*pd[i]);
        g = g.map((v, i) => v + alpha*Qp[i]);
        z = g.map((v, i) => v/m[i]);
        const gzNew = g.reduce((s, v, i) => s + v*z[i], 0), beta = gzNew/gz;
        pd = pd.map((v, i) => -z[i] + beta*v);
        gz = gzNew;
        iters++;
      }
      const err = Math.sqrt(x.reduce((s, v) => s + (v-1)*(v-1), 0));
      const kappa = Math.pow(64, 1 - pp);
      output.innerHTML = '<strong>p=' + fmt(pp,1) + '，κ(M⁻¹Q)=' +
        (kappa < 1.0001 ? '1' : fmt(kappa,2)) + '</strong><br>' +
        '停止迭代次数 ' + iters + '（容差 1e-10）<br>最终误差 ‖x−x*‖=' + err.toExponential(2);
    });
    if (kind === "cg-pprec") bind(root, el => {
      const n = read(el, "n");
      const kappaQ = 1 / Math.pow(Math.tan(Math.PI/(2*(n+1))), 2);
      output.innerHTML = '<strong>n=' + fmt(n, 0) + '</strong><br>' +
        '无预条件 / Jacobi：κ(Q)=' + fmt(kappaQ, 2) +
        '<br>保留三对角结构的精确分解：κ(M⁻¹Q)=1';
    });
    if (kind === "fr-convergence") bind(root, el => {
      const kappa = read(el, "kappa");
      const Q = [1, kappa];
      const run = fr => {
        let x = [1, 1];
        let g = [x[0], Q[1]*x[1]];
        let p = [-g[0], -g[1]];
        let it = 0;
        for (; it < 1000000; it++) {
          const Qp = [Q[0]*p[0], Q[1]*p[1]];
          const alpha = -(g[0]*p[0]+g[1]*p[1]) / (p[0]*Qp[0]+p[1]*Qp[1]);
          x = [x[0]+alpha*p[0], x[1]+alpha*p[1]];
          const g2 = [Q[0]*x[0], Q[1]*x[1]];
          const norm2 = g2[0]*g2[0]+g2[1]*g2[1];
          if (norm2 < 1e-16) break;
          if (fr) {
            const beta = norm2 / (g[0]*g[0]+g[1]*g[1]);
            p = [-g2[0]+beta*p[0], -g2[1]+beta*p[1]];
          } else {
            p = [-g2[0], -g2[1]];
          }
          g = g2;
        }
        return it;
      };
      output.innerHTML = '<strong>κ=' + fmt(kappa, 1) + '</strong> · 最速下降 ' + run(false) +
        ' 步 · Fletcher–Reeves ' + run(true) + ' 步（阈值 ‖g‖<1e-8，精确线搜索）';
    });
    if (kind === "pr-variants") bind(root, el => {
      const c = read(el, "c");
      const Q = [[3, 1], [1, 3]], b = [5, 7];
      const mv = v => [Q[0][0]*v[0] + Q[0][1]*v[1], Q[1][0]*v[0] + Q[1][1]*v[1]];
      const dot = (u, v) => u[0]*v[0] + u[1]*v[1];
      const grad = x => { const q = mv(x); return [q[0]-b[0], q[1]-b[1]]; };
      let x = [0, 0], g = grad(x), p = [-g[0], -g[1]];
      let a = -dot(g, p) / dot(p, mv(p));
      x = [x[0] + a*p[0], x[1] + a*p[1]];
      const g1 = grad(x);
      const b1 = dot(g1, g1) / dot(g, g);
      p = [-g1[0] + b1*p[0], -g1[1] + b1*p[1]];
      a = -dot(g1, p) / dot(p, mv(p));
      const x2 = [x[0] + c*a*p[0], x[1] + c*a*p[1]];
      const g2 = grad(x2), y = [g2[0]-g1[0], g2[1]-g1[1]];
      const fr = dot(g2, g2) / dot(g1, g1);
      const pr = dot(g2, y) / dot(g1, g1);
      const hs = dot(g2, y) / dot(p, y);
      output.innerHTML = '<strong>c=' + fmt(c, 2) + '</strong> · β_FR=' + fmt(fr, 4) +
        ' · β_PR=' + fmt(pr, 4) + ' · β_HS=' + fmt(hs, 4) + ' · PR+=' + fmt(Math.max(0, pr), 4);
    });
    if (kind === "cg-restart") bind(root, el => {
      const c = read(el, "c");
      const Q = [[3, 1], [1, 3]], b = [5, 7];
      const mv = v => [Q[0][0]*v[0] + Q[0][1]*v[1], Q[1][0]*v[0] + Q[1][1]*v[1]];
      const dot = (u, v) => u[0]*v[0] + u[1]*v[1];
      const grad = x => { const q = mv(x); return [q[0]-b[0], q[1]-b[1]]; };
      let x = [0, 0], g = grad(x), p = [-g[0], -g[1]];
      let a = -dot(g, p) / dot(p, mv(p));
      x = [x[0] + a*p[0], x[1] + a*p[1]];
      const g1 = grad(x);
      const b1 = dot(g1, g1) / dot(g, g);
      p = [-g1[0] + b1*p[0], -g1[1] + b1*p[1]];
      a = -dot(g1, p) / dot(p, mv(p));
      const x2 = [x[0] + c*a*p[0], x[1] + c*a*p[1]];
      const g2 = grad(x2);
      const ratio = Math.abs(dot(g2, g1)) / dot(g2, g2);
      const nu = 0.1;
      output.innerHTML = '<strong>c=' + fmt(c, 2) + '</strong> · |g₂ᵀg₁|/‖g₂‖²=' + fmt(ratio, 4) +
        ' · 阈值 ν=' + nu + ' · ' + (ratio >= nu ? '触发重启（β 置零）' : '无需重启');
    });
    if (kind === "fr-angle") bind(root, el => {
      const c1 = read(el, "c1");
      const f = p => (p[0]-1)**2 + 5*(p[1]-p[0]*p[0])**2;
      const grad = p => [2*(p[0]-1) - 20*p[0]*(p[1]-p[0]*p[0]), 10*(p[1]-p[0]*p[0])];
      let x = [-1.2, 1], g = grad(x), p = [-g[0], -g[1]], minCos = 1, it = 0;
      for (; it < 400 && Math.hypot(g[0], g[1]) > 1e-6; it++) {
        const slope = g[0]*p[0] + g[1]*p[1];
        let a = 1;
        for (let t = 0; t < 40; t++) {
          if (f([x[0]+a*p[0], x[1]+a*p[1]]) <= f(x) + c1*a*slope) break;
          a *= 0.5;
        }
        x = [x[0]+a*p[0], x[1]+a*p[1]];
        const gn = grad(x);
        const beta = (gn[0]**2 + gn[1]**2) / (g[0]**2 + g[1]**2);
        p = [-gn[0] + beta*p[0], -gn[1] + beta*p[1]];
        const cos = -(gn[0]*p[0] + gn[1]*p[1]) / (Math.hypot(gn[0], gn[1])*Math.hypot(p[0], p[1]));
        if (cos < minCos) minCos = cos;
        g = gn;
      }
      output.innerHTML = '<strong>c₁=' + fmt(c1, 4) + '</strong> · 步数 ' + it +
        ' · 最小 cosθ=' + fmt(minCos, 4) + ' · 末态‖g‖=' + fmt(Math.hypot(g[0], g[1]), 2) + '（教学玩具）';
    });
    if (kind === "cg-zoutendijk") bind(root, el => {
      const r = read(el, "r");
      const c2 = 0.25, n = 200;
      let s = 0;
      for (let k = 1; k <= n; k++) s += c2*Math.pow(r*r, k);
      const finite = r < 1;
      const limit = finite ? c2*r*r/(1 - r*r) : Infinity;
      output.innerHTML = '<strong>r=' + fmt(r, 2) + '</strong> · 200 项部分和=' + fmt(s, 4) +
        (finite ? ' · 极限 ' + fmt(limit, 4) + '（有界）' : ' · 继续增长（无界）') + ' · cos²θ=0.25';
    });
    if (kind === "cg-perf") bind(root, el => {
      const n = read(el, "n");
      const Q = [];
      for (let i = 0; i < n; i++) Q.push(i + 1);
      const run = kind => {
        let x = new Array(n).fill(1), g = Q.map((q, i) => q*x[i]), p = g.map(v => -v);
        let ev = 0, k = 0;
        for (; k < 400; k++) {
          let denom = 0, num = 0;
          for (let i = 0; i < n; i++) { denom += p[i]*Q[i]*p[i]; num += g[i]*p[i]; }
          const a = -num/denom;
          for (let i = 0; i < n; i++) x[i] += a*p[i];
          const gn = Q.map((q, i) => q*x[i]); ev++;
          let nrm = 0;
          for (let i = 0; i < n; i++) nrm += gn[i]*gn[i];
          if (nrm < 1e-18) break;
          const y = gn.map((v, i) => v - g[i]);
          let gg = 0, g2 = 0, gy = 0;
          for (let i = 0; i < n; i++) { gg += gn[i]*gn[i]; g2 += g[i]*g[i]; gy += gn[i]*y[i]; }
          const b = kind === "FR" ? gg/g2 : Math.max(0, gy/g2);
          for (let i = 0; i < n; i++) p[i] = -gn[i] + b*p[i];
          g = gn;
        }
        return [k, ev];
      };
      const fr = run("FR"), pr = run("PR+");
      output.innerHTML = '<strong>n=' + n + '</strong> · FR ' + fr[0] + ' 步/' + fr[1] +
        ' 次梯度评估 · PR+ ' + pr[0] + ' 步/' + pr[1] + ' 次梯度评估（对角二次，精确线搜索）';
    });
    if (kind === "bfgs-pd") bind(root, el => {
      const a = read(el, "a"), b = read(el, "b");
      const s = [1, 0], y = [a, b];
      const sy = a;
      const pd = sy > 1e-9;
      // With H=I the BFGS inverse update reduces to H+ = [[1/a,0],[0,1+b^2/a^2]].
      if (!pd) {
        output.innerHTML = '<strong>sᵀy = ' + fmt(sy, 2) + ' ≤ 0</strong>：曲率条件不成立，'
          + '更新分母 ρ=1/sᵀy 无效，正定性无可保证。';
      } else {
        const h11 = 1 / a, h22 = 1 + b*b/(a*a);
        const det = h11 * h22;
        // secant residual for H+y = s
        const r1 = h11 * y[0] - s[0];
        const r2 = h22 * y[1] - s[1];
        const res = Math.hypot(r1, r2);
        output.innerHTML = '<strong>sᵀy = ' + fmt(sy, 2) + ' &gt; 0</strong> · Hₖ₊₁ = diag(' +
          fmt(h11, 3) + ', ' + fmt(h22, 3) + ') · det = ' + fmt(det, 3) +
          ' &gt; 0 → 正定<br>割线残差 ‖Hₖ₊₁y − s‖ = ' + res.toExponential(1);
      }
    });
    if (kind === "bfgs-trace") {
      const f = p => 100*(p[1]-p[0]*p[0])**2 + (1-p[0])**2;
      const grad = p => [-400*p[0]*(p[1]-p[0]*p[0]) - 2*(1-p[0]), 200*(p[1]-p[0]*p[0])];
      const search = (x, p) => {
        let lo = 0, hi = 2; const gr = (Math.sqrt(5)-1)/2;
        let c = hi-gr*(hi-lo), d = lo+gr*(hi-lo);
        let fc = f([x[0]+c*p[0], x[1]+c*p[1]]), fd = f([x[0]+d*p[0], x[1]+d*p[1]]);
        for (let i = 0; i < 80; i++) {
          if (fc < fd) { hi = d; d = c; fd = fc; c = hi-gr*(hi-lo); fc = f([x[0]+c*p[0], x[1]+c*p[1]]); }
          else { lo = c; c = d; fc = fd; d = lo+gr*(hi-lo); fd = f([x[0]+d*p[0], x[1]+d*p[1]]); }
        }
        return (lo+hi)/2;
      };
      const upd = (H, s, y, rho) => {
        const Hy = [H[0][0]*y[0]+H[0][1]*y[1], H[1][0]*y[0]+H[1][1]*y[1]];
        const yHy = y[0]*Hy[0]+y[1]*Hy[1]; const out = [[0,0],[0,0]];
        for (let i = 0; i < 2; i++) for (let j = 0; j < 2; j++)
          out[i][j] = H[i][j]-rho*(s[i]*Hy[j]+Hy[i]*s[j])+rho*rho*yHy*s[i]*s[j]+rho*s[i]*s[j];
        return out;
      };
      let x = [-1.2, 1], H = [[1,0],[0,1]];
      const trace = [{ x: [-1.2, 1], f: f([-1.2,1]), g: Math.hypot(...grad([-1.2,1])), sy: null }];
      for (let it = 0; it < 14; it++) {
        const g = grad(x);
        const Hg = [H[0][0]*g[0]+H[0][1]*g[1], H[1][0]*g[0]+H[1][1]*g[1]];
        const p = [-Hg[0], -Hg[1]]; const a = search(x, p);
        const xn = [x[0]+a*p[0], x[1]+a*p[1]]; const gn = grad(xn);
        const s = [xn[0]-x[0], xn[1]-x[1]], y = [gn[0]-g[0], gn[1]-g[1]];
        const sy = s[0]*y[0]+s[1]*y[1];
        if (sy > 1e-12) H = upd(H, s, y, 1/sy);
        x = xn;
        trace.push({ x: x, f: f(x), g: Math.hypot(...grad(x)), sy: sy });
      }
      bind(root, el => {
        const k = Math.min(read(el, "k"), trace.length-1);
        const t = trace[k];
        output.innerHTML = '<strong>k = ' + k + '</strong> · xₖ = (' + fmt(t.x[0], 4) + ', ' +
          fmt(t.x[1], 4) + ') · f = ' + t.f.toExponential(2) + ' · ‖gₖ‖ = ' + t.g.toExponential(2) +
          (t.sy === null ? ' · 起始点' : ' · sᵏ⁻¹ᵀyᵏ⁻¹ = ' + fmt(t.sy, 4));
      });
    }
    if (kind === "sr1-indef") bind(root, el => {
      const a = read(el, "a"), b = read(el, "b");
      const vs = a - 1;                 // denominator (y - B0 s)^T s with B0=I, s=(1,0)
      if (Math.abs(vs) < 1e-9) {
        output.innerHTML = '<strong>(y−Bₖs)ᵀs = 0</strong>：分母为零，更新无定义，应保留旧矩阵。';
      } else {
        const det = a + b*b/vs;         // det of B1 = [[a,b],[b,1+b^2/(a-1)]]
        output.innerHTML = '<strong>(y−Bₖs)ᵀs = ' + fmt(vs, 2) + '</strong> · det Bₖ₊₁ = ' +
          fmt(det, 3) + ' → ' + (det > 0 ? '正定' : (det < 0 ? '不定' : '奇异')) +
          '<br>Bₖ₊₁ = [[' + fmt(a, 2) + ', ' + fmt(b, 2) + '], [' + fmt(b, 2) + ', ' +
          fmt(1 + b*b/vs, 2) + ']]（割线方程始终满足）';
      }
    });
    if (kind === "broyden-phi") bind(root, el => {
      const phi = read(el, "phi");
      const det = 1 + 4*phi;           // B0=I, s=(1,0), y=(1,2): det = 1 + 4 phi
      const b22 = 5 + 4*phi;
      const cls = Math.abs(det) < 1e-9 ? '奇异' : (det > 0 ? '正定' : '不定');
      output.innerHTML = '<strong>φ = ' + fmt(phi, 2) + '</strong> · B₁ = [[1, 2], [2, ' +
        fmt(b22, 2) + ']] · det = ' + fmt(det, 3) + ' → ' + cls +
        '<br>' + (phi >= 0 && phi <= 1 ? '位于 [0,1]：正定且是 BFGS/DFP 的凸组合'
                                       : '已越出 [0,1]：正定性无保证');
    });
    if (kind === "bfgs-global") bind(root, el => {
      const f = p => 100*(p[1]-p[0]*p[0])**2 + (1-p[0])**2;
      const grad = p => [-400*p[0]*(p[1]-p[0]*p[0]) - 2*(1-p[0]), 200*(p[1]-p[0]*p[0])];
      const search = (x, p) => {
        let lo = 0, hi = 2; const gr = (Math.sqrt(5)-1)/2;
        let c = hi-gr*(hi-lo), d = lo+gr*(hi-lo);
        let fc = f([x[0]+c*p[0], x[1]+c*p[1]]), fd = f([x[0]+d*p[0], x[1]+d*p[1]]);
        for (let i = 0; i < 80; i++) {
          if (fc < fd) { hi = d; d = c; fd = fc; c = hi-gr*(hi-lo); fc = f([x[0]+c*p[0], x[1]+c*p[1]]); }
          else { lo = c; c = d; fc = fd; d = lo+gr*(hi-lo); fd = f([x[0]+d*p[0], x[1]+d*p[1]]); }
        }
        return (lo+hi)/2;
      };
      const x0 = read(el, "x0");
      let x = [x0, 1], H = [[1,0],[0,1]], it = 0;
      for (; it < 100; it++) {
        const g = grad(x);
        if (Math.hypot(g[0], g[1]) < 1e-6) break;
        const Hg = [H[0][0]*g[0]+H[0][1]*g[1], H[1][0]*g[0]+H[1][1]*g[1]];
        const p = [-Hg[0], -Hg[1]]; const a = search(x, p);
        const xn = [x[0]+a*p[0], x[1]+a*p[1]]; const gn = grad(xn);
        const s = [xn[0]-x[0], xn[1]-x[1]], y = [gn[0]-g[0], gn[1]-g[1]];
        const sy = s[0]*y[0]+s[1]*y[1];
        if (sy > 1e-12) {
          const rho = 1/sy;
          const Hy = [H[0][0]*y[0]+H[0][1]*y[1], H[1][0]*y[0]+H[1][1]*y[1]];
          const yHy = y[0]*Hy[0]+y[1]*Hy[1]; const out = [[0,0],[0,0]];
          for (let i = 0; i < 2; i++) for (let j = 0; j < 2; j++)
            out[i][j] = H[i][j]-rho*(s[i]*Hy[j]+Hy[i]*s[j])+rho*rho*yHy*s[i]*s[j]+rho*s[i]*s[j];
          H = out;
        }
        x = xn;
      }
      const g = grad(x);
      output.innerHTML = '<strong>x₀ = (' + fmt(x0, 1) + ', 1)</strong> · 迭代 ' + it +
        ' 步 · 末态 x = (' + fmt(x[0], 4) + ', ' + fmt(x[1], 4) + ') · ‖g‖ = ' +
        Math.hypot(g[0], g[1]).toExponential(2) + ' · f = ' + f(x).toExponential(2);
    });
    if (kind === "bfgs-superlin") bind(root, el => {
      const f = p => 100*(p[1]-p[0]*p[0])**2 + (1-p[0])**2;
      const grad = p => [-400*p[0]*(p[1]-p[0]*p[0]) - 2*(1-p[0]), 200*(p[1]-p[0]*p[0])];
      const search = (x, p) => {
        let lo = 0, hi = 2; const gr = (Math.sqrt(5)-1)/2;
        let c = hi-gr*(hi-lo), d = lo+gr*(hi-lo);
        let fc = f([x[0]+c*p[0], x[1]+c*p[1]]), fd = f([x[0]+d*p[0], x[1]+d*p[1]]);
        for (let i = 0; i < 80; i++) {
          if (fc < fd) { hi = d; d = c; fd = fc; c = hi-gr*(hi-lo); fc = f([x[0]+c*p[0], x[1]+c*p[1]]); }
          else { lo = c; c = d; fc = fd; d = lo+gr*(hi-lo); fd = f([x[0]+d*p[0], x[1]+d*p[1]]); }
        }
        return (lo+hi)/2;
      };
      const star = [1, 1];
      const run = (x0, useBFGS) => {
        let x = [x0, 1], H = [[1,0],[0,1]], prev = null, last = null;
        const err = () => Math.hypot(x[0]-star[0], x[1]-star[1]);
        for (let it = 0; it < 80; it++) {
          const d = err();
          if (prev !== null && prev > 0) last = d/prev;
          prev = d;
          const g = grad(x);
          if (Math.hypot(g[0], g[1]) < 1e-8) break;
          const Hg = [H[0][0]*g[0]+H[0][1]*g[1], H[1][0]*g[0]+H[1][1]*g[1]];
          const p = useBFGS ? [-Hg[0], -Hg[1]] : [-g[0], -g[1]];
          const a = search(x, p);
          const xn = [x[0]+a*p[0], x[1]+a*p[1]]; const gn = grad(xn);
          if (useBFGS) {
            const s = [xn[0]-x[0], xn[1]-x[1]], y = [gn[0]-g[0], gn[1]-g[1]];
            const sy = s[0]*y[0]+s[1]*y[1];
            if (sy > 1e-12) {
              const rho = 1/sy;
              const Hy = [H[0][0]*y[0]+H[0][1]*y[1], H[1][0]*y[0]+H[1][1]*y[1]];
              const yHy = y[0]*Hy[0]+y[1]*Hy[1]; const out = [[0,0],[0,0]];
              for (let i = 0; i < 2; i++) for (let j = 0; j < 2; j++)
                out[i][j] = H[i][j]-rho*(s[i]*Hy[j]+Hy[i]*s[j])+rho*rho*yHy*s[i]*s[j]+rho*s[i]*s[j];
              H = out;
            }
          }
          x = xn;
        }
        return { ratio: last, x: x };
      };
      const x0 = read(el, "x0");
      const bf = run(x0, true), sd = run(x0, false);
      output.innerHTML = '<strong>x₀ = (' + fmt(x0, 1) + ', 1)</strong><br>BFGS 末步比率 eₖ₊₁/eₖ = ' +
        (bf.ratio === null ? '有界' : fmt(bf.ratio, 4)) + '，x = (' + fmt(bf.x[0], 4) + ', ' + fmt(bf.x[1], 4) + ')' +
        '<br>最速下降末步比率 = ' + (sd.ratio === null ? '有界' : fmt(sd.ratio, 4)) + '，x = (' + fmt(sd.x[0], 4) + ', ' + fmt(sd.x[1], 4) + ')';
    });
    if (kind === "sr1-convergence") bind(root, el => {
      const Q = [[3,1],[1,3]], b = [5,7];
      const mv = (M, v) => [M[0][0]*v[0]+M[0][1]*v[1], M[1][0]*v[0]+M[1][1]*v[1]];
      const dot = (u, v) => u[0]*v[0]+u[1]*v[1];
      const grad = x => [Q[0][0]*x[0]+Q[0][1]*x[1]-b[0], Q[1][0]*x[0]+Q[1][1]*x[1]-b[1]];
      const inv2 = M => {
        const d = M[0][0]*M[1][1]-M[0][1]*M[1][0];
        return Math.abs(d) < 1e-12 ? null : [[M[1][1]/d, -M[0][1]/d], [-M[1][0]/d, M[0][0]/d]];
      };
      const relErr = B => Math.hypot(B[0][0]-Q[0][0], B[0][1]-Q[0][1], B[1][0]-Q[1][0], B[1][1]-Q[1][1]) /
        Math.hypot(Q[0][0], Q[0][1], Q[1][0], Q[1][1]);
      const alpha = read(el, "alpha");
      let x = [0, 0], B = [[1,0],[0,1]], err = relErr(B);
      for (let it = 0; it < 12; it++) {
        const g = grad(x);
        if (Math.hypot(g[0], g[1]) < 1e-9) break;
        const Bi = inv2(B);
        if (Bi === null) break;
        const p = [-mv(Bi, g)[0], -mv(Bi, g)[1]];
        const xn = [x[0]+alpha*p[0], x[1]+alpha*p[1]]; const gn = grad(xn);
        const s = [xn[0]-x[0], xn[1]-x[1]], y = [gn[0]-g[0], gn[1]-g[1]];
        const Bs = mv(B, s); const v = [y[0]-Bs[0], y[1]-Bs[1]]; const vs = dot(v, s);
        if (Math.abs(vs) >= 1e-8*Math.hypot(s[0], s[1])*Math.hypot(v[0], v[1])) {
          B = [[B[0][0]+v[0]*v[0]/vs, B[0][1]+v[0]*v[1]/vs],
               [B[1][0]+v[1]*v[0]/vs, B[1][1]+v[1]*v[1]/vs]];
        }
        x = xn; err = relErr(B);
      }
      output.innerHTML = '<strong>α = ' + fmt(alpha, 2) + '</strong> · 末态相对偏差 ‖B−Q‖/‖Q‖ = ' +
        err.toExponential(2) + ' · 末态 x = (' + fmt(x[0], 4) + ', ' + fmt(x[1], 4) +
        ') · x* = (1, 2)';
    });
    if (kind === "qn-update") bind(root, el => {
      const a = read(el, "a"), b = read(el, "b");
      const detBFGS = a;                       // closed form for B0=I, s=(1,0), y=(a,b)
      const detDFP = a + b*b/a;
      const detSR1 = Math.abs(a - 1) < 1e-9 ? null : a + b*b/(a - 1);
      const flag = d => d === null ? '无定义' : (Math.abs(d) < 1e-9 ? '奇异' : (d > 0 ? '正定' : '不定'));
      output.innerHTML = '<strong>sᵀy = ' + fmt(a, 2) + '</strong><br>' +
        'BFGS det = ' + fmt(detBFGS, 3) + '（' + flag(detBFGS) + '）<br>' +
        'DFP det = ' + fmt(detDFP, 3) + '（' + flag(detDFP) + '）<br>' +
        'SR1 det = ' + (detSR1 === null ? '分母为 0' : fmt(detSR1, 3) + '（' + flag(detSR1) + '）');
    });
    if (kind === "qn-exercise") bind(root, el => {
      const a = read(el, "a"), b = read(el, "b");
      const detBFGS = a, detDFP = a + b*b/a, detHalf = a + 0.5*b*b/a;
      const detSR1 = Math.abs(a - 1) < 1e-9 ? null : a + b*b/(a - 1);
      const flag = d => d === null ? '无定义' : (Math.abs(d) < 1e-9 ? '奇异' : (d > 0 ? '正定' : '不定'));
      output.innerHTML = '<strong>sᵀy = ' + fmt(a, 2) + '</strong><br>' +
        'BFGS det = ' + fmt(detBFGS, 3) + '（' + flag(detBFGS) + '）<br>' +
        'DFP det = ' + fmt(detDFP, 3) + '（' + flag(detDFP) + '）<br>' +
        'φ=0.5 det = ' + fmt(detHalf, 3) + '（' + flag(detHalf) + '）<br>' +
        'SR1 det = ' + (detSR1 === null ? '分母为 0' : fmt(detSR1, 3) + '（' + flag(detSR1) + '）');
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