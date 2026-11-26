"""BFGS (Algorithm 6.1) on the 2-D Rosenbrock function."""
import math


def f(p):
    return 100.0 * (p[1] - p[0] ** 2) ** 2 + (1.0 - p[0]) ** 2


def grad(p):
    return (-400.0 * p[0] * (p[1] - p[0] ** 2) - 2.0 * (1.0 - p[0]),
            200.0 * (p[1] - p[0] ** 2))


def exact_search(x, p):
    """Golden-section minimiser of phi(a) = f(x + a*p) on [0, 2]."""
    lo, hi = 0.0, 2.0
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c, d = hi - gr * (hi - lo), lo + gr * (hi - lo)
    fc, fd = f((x[0] + c * p[0], x[1] + c * p[1])), f((x[0] + d * p[0], x[1] + d * p[1]))
    for _ in range(80):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi - gr * (hi - lo); fc = f((x[0] + c * p[0], x[1] + c * p[1]))
        else:
            lo, c, fc = c, d, fd
            d = lo + gr * (hi - lo); fd = f((x[0] + d * p[0], x[1] + d * p[1]))
    return 0.5 * (lo + hi)


def bfgs(x0, tol=1e-6, maxit=200):
    n = len(x0); x = list(x0)
    H = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for it in range(1, maxit + 1):
        g = grad(x)
        if math.hypot(*g) < tol:
            return it - 1, x
        Hg = [sum(H[i][j] * g[j] for j in range(n)) for i in range(n)]
        p = [-v for v in Hg]
        a = exact_search(x, p)
        xn = [x[i] + a * p[i] for i in range(n)]; gn = grad(xn)
        s = [xn[i] - x[i] for i in range(n)]; y = [gn[i] - g[i] for i in range(n)]
        sy = sum(s[i] * y[i] for i in range(n))
        if sy > 1e-12:                     # curvature safeguard
            rho = 1.0 / sy
            Hy = [sum(H[i][j] * y[j] for j in range(n)) for i in range(n)]
            yHy = sum(y[i] * Hy[i] for i in range(n))
            H = [[H[i][j] - rho * (s[i] * Hy[j] + Hy[i] * s[j])
                  + rho * rho * yHy * s[i] * s[j] + rho * s[i] * s[j]
                  for j in range(n)] for i in range(n)]
        x = xn
    return maxit, x


if __name__ == "__main__":
    it, x = bfgs([-1.2, 1.0])
    assert math.hypot(*grad(x)) < 1e-6
    print("iterations =", it, "x =", x, "f =", f(x))
