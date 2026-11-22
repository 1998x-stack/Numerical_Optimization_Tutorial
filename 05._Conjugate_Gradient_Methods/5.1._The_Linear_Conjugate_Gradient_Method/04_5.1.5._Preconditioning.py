"""Preconditioned CG on a diagonal problem with M = diag(lam**p)."""
from math import sqrt

def pcg(lam, p, tol=1e-10, max_iter=10):
    n = len(lam)
    m = [l**p for l in lam]
    x = [0.0]*n
    g = [-l for l in lam]                  # b = lam since x* = ones
    z = [g[i]/m[i] for i in range(n)]
    pdir = [-z[i] for i in range(n)]
    gz = sum(g[i]*z[i] for i in range(n))
    for k in range(max_iter):
        if sqrt(sum(v*v for v in g)) <= tol:
            return x, k
        Qp = [lam[i]*pdir[i] for i in range(n)]
        alpha = gz / sum(pdir[i]*Qp[i] for i in range(n))
        x = [x[i] + alpha*pdir[i] for i in range(n)]
        g = [g[i] + alpha*Qp[i] for i in range(n)]
        z = [g[i]/m[i] for i in range(n)]
        gz_new = sum(g[i]*z[i] for i in range(n))
        beta = gz_new / gz
        pdir = [-z[i] + beta*pdir[i] for i in range(n)]
        gz = gz_new
    return x, max_iter

if __name__ == "__main__":
    lam = [1.0, 4.0, 16.0, 64.0]
    x1, it1 = pcg(lam, 1.0)                 # M = Q: exact in one step
    assert it1 == 1
    assert abs(x1[0] - 1.0) < 1e-9 and abs(x1[3] - 1.0) < 1e-9
    _, it0 = pcg(lam, 0.0)                  # M = I: plain CG
    assert it0 >= it1
    print("p=1 iterations:", it1, "| p=0 iterations:", it0)
