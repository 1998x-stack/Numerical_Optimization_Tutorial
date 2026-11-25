"""Count gradient and function evaluations for FR, PR+ and HS on a convex quadratic."""
from fractions import Fraction as F

n = 10
Q = [F(i + 1) for i in range(n)]

def grad(x):
    return [Q[i]*x[i] for i in range(n)]

def dot(u, v):
    return sum(a*b for a, b in zip(u, v))

def run(kind, maxit=200):
    x = [F(1)]*n
    g = grad(x)
    p = [-v for v in g]
    grad_evals = 0
    for k in range(maxit):
        denom = dot(p, [Q[i]*p[i] for i in range(n)])
        a = -dot(g, p) / denom
        x = [x[i] + a*p[i] for i in range(n)]
        gn = grad(x)
        grad_evals += 1
        if dot(gn, gn) < F(1, 10**18):
            break
        y = [gn[i] - g[i] for i in range(n)]
        if kind == "FR":
            b = dot(gn, gn) / dot(g, g)
        elif kind == "PR+":
            b = max(F(0), dot(gn, y) / dot(g, g))
        else:
            b = dot(gn, y) / dot(p, y)
        p = [-gn[i] + b*p[i] for i in range(n)]
        g = gn
    return k, grad_evals, dot(gn, gn)

if __name__ == "__main__":
    for kind in ("FR", "PR+", "HS"):
        k, evals, norm = run(kind)
        print(kind, "iters", k, "grad evals", evals, "final |g|^2", norm)
        assert norm < F(1, 10**18)
