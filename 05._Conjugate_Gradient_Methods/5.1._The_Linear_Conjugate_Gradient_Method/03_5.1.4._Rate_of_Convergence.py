"""Compare CG energy-norm error with the kappa bound (Theorem 5.3)."""
from math import sqrt

def diag_problem(kappa, n=20):
    lam = [1.0 + (kappa - 1.0)*i/(n - 1) for i in range(n)]
    return lam, list(lam)               # x* = ones, so b = Q x* = eigenvalues

def energy_error(lam, x):
    return sqrt(sum(lam[i]*(x[i] - 1.0)**2 for i in range(len(lam))))

def run(lam, b, steps):
    n = len(lam)
    x = [0.0]*n
    g = [-b[i] for i in range(n)]
    p = [-g[i] for i in range(n)]
    gn = sum(v*v for v in g)
    hist = [energy_error(lam, x)]
    for _ in range(steps):
        if sqrt(gn) <= 1e-14:
            break
        Qp = [lam[i]*p[i] for i in range(n)]
        alpha = gn / sum(p[i]*Qp[i] for i in range(n))
        x = [x[i] + alpha*p[i] for i in range(n)]
        g = [g[i] + alpha*Qp[i] for i in range(n)]
        gn_new = sum(v*v for v in g)
        beta = gn_new / gn
        p = [-g[i] + beta*p[i] for i in range(n)]
        gn = gn_new
        hist.append(energy_error(lam, x))
    return hist

if __name__ == "__main__":
    lam, b = diag_problem(10)
    hist = run(lam, b, 5)
    rho = (sqrt(10) - 1)/(sqrt(10) + 1)
    bound = 2*rho**5*hist[0]
    assert hist[-1] <= bound
    assert hist[-1] < hist[0]
    print("rho =", round(rho, 4), "| bound =", round(bound, 6), "| actual =", round(hist[-1], 6))
