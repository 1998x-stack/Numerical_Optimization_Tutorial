"""Practical linear conjugate gradient (Algorithm 5.2) on a small quadratic."""
from math import sqrt

def cg(Q, b, x0, tol=1e-12, max_iter=10):
    n = len(b)
    mv = lambda v: [sum(Q[i][j]*v[j] for j in range(n)) for i in range(n)]
    dot = lambda u, v: sum(u[i]*v[i] for i in range(n))
    x = list(x0)
    g = [mv(x)[i] - b[i] for i in range(n)]
    p = [-g[i] for i in range(n)]
    gnorm = dot(g, g)
    for k in range(max_iter):
        if sqrt(gnorm) <= tol:
            return x, k
        Qp = mv(p)
        alpha = gnorm / dot(p, Qp)
        x = [x[i] + alpha*p[i] for i in range(n)]
        g = [g[i] + alpha*Qp[i] for i in range(n)]
        gnorm_new = dot(g, g)
        beta = gnorm_new / gnorm
        p = [-g[i] + beta*p[i] for i in range(n)]
        gnorm = gnorm_new
    return x, max_iter

if __name__ == "__main__":
    Q = [[3.0, 1.0], [1.0, 3.0]]
    b = [5.0, 7.0]
    x, iters = cg(Q, b, [0.0, 0.0])
    assert iters == 2
    assert abs(x[0] - 1.0) < 1e-9 and abs(x[1] - 2.0) < 1e-9
    print("x =", [round(v, 6) for v in x], "iterations =", iters)
