"""Trust-region Newton-Lanczos: solve the subproblem in a growing Krylov subspace."""
from math import sqrt


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm(v):
    return sqrt(dot(v, v))


def lanczos(H, g, j):
    """Return orthonormal Krylov basis Q, diagonal alpha and off-diagonal beta."""
    qs, alphas, betas = [], [], []
    q = [x / norm(g) for x in g]
    q_prev, beta_prev = [0.0] * len(g), 0.0
    for _ in range(j):
        qs.append(list(q))
        z = matvec(H, q)
        alpha = dot(q, z)
        alphas.append(alpha)
        for i in range(len(g)):
            z[i] -= alpha * q[i] + beta_prev * q_prev[i]
        beta = norm(z)
        betas.append(beta)
        q_prev, q, beta_prev = list(q), [x / beta for x in z], beta
    return qs, alphas, betas


def jacobi(A, sweeps=100):
    """Eigenvalues theta and eigenvectors V (columns) of a small symmetric matrix."""
    n = len(A)
    a = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        p, q, mx = 0, 1, 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > mx:
                    mx, p, q = abs(a[i][j]), i, j
        if mx < 1e-15:
            break
        theta = 0.5 * (a[q][q] - a[p][p]) / a[p][q]
        t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + sqrt(theta * theta + 1.0))
        c, s = 1.0 / sqrt(1.0 + t * t), t / sqrt(1.0 + t * t)
        for k in range(n):
            akp, akq = a[k][p], a[k][q]
            a[k][p], a[k][q] = c * akp - s * akq, s * akp + c * akq
        for k in range(n):
            apk, aqk = a[p][k], a[q][k]
            a[p][k], a[q][k] = c * apk - s * aqk, s * apk + c * aqk
        for k in range(n):
            vkp, vkq = V[k][p], V[k][q]
            V[k][p], V[k][q] = c * vkp - s * vkq, s * vkp + c * vkq
    return [a[i][i] for i in range(n)], V


def solve_reduced(theta, V, gnorm, Delta):
    """Minimize gnorm*e1.w + 0.5 w.T.w with ||w|| <= Delta, returning (w, lambda)."""
    n = len(theta)
    c = [gnorm * V[0][i] for i in range(n)]
    sq = lambda lam: sum(c[i] * c[i] / (theta[i] + lam) ** 2 for i in range(n))
    lam = 0.0
    if sq(0.0) > Delta * Delta:
        lam = max(0.0, -min(theta)) + 1e-9
        for _ in range(100):
            f = sq(lam) - Delta * Delta
            df = -2.0 * sum(c[i] * c[i] / (theta[i] + lam) ** 3 for i in range(n))
            new = lam - f / df
            floor = max(0.0, -min(theta))
            new = 0.5 * (lam + floor) if new <= floor else new
            if abs(new - lam) < 1e-15:
                lam = new
                break
            lam = new
    y = [-c[i] / (theta[i] + lam) for i in range(n)]
    w = [sum(V[i][k] * y[k] for k in range(n)) for i in range(n)]
    return w, lam


def tr_lanczos(H, g, Delta, j):
    """Approximate solution of the trust-region subproblem in a j-dim Krylov subspace."""
    Q, alpha, beta = lanczos(H, g, j)
    T = [[0.0] * j for _ in range(j)]
    for i in range(j):
        T[i][i] = alpha[i]
        if i + 1 < j:
            T[i][i + 1] = T[i + 1][i] = beta[i]
    theta, V = jacobi(T)
    w, lam = solve_reduced(theta, V, norm(g), Delta)
    p = [sum(Q[k][i] * w[k] for k in range(j)) for i in range(len(g))]
    return p, lam, theta


def model_decrease(H, g, p):
    return -(dot(g, p) + 0.5 * dot(p, matvec(H, p)))


def main():
    H = [[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]]
    g = [1.0, 1.0, 1.0]
    decs = []
    for j in (1, 2, 3):
        p, lam, theta = tr_lanczos(H, g, 0.3, j)
        assert abs(norm(p) - 0.3) < 1e-9 and dot(g, p) < 0.0 and lam > 0.0
        decs.append(model_decrease(H, g, p))
        print("j=%d" % j, "lambda=%.6f" % lam, "Ritz=", [round(t, 4) for t in theta],
              "p=", tuple(round(x, 4) for x in p), "||p||=%.4f" % norm(p),
              "dec=%.4f" % model_decrease(H, g, p))
    assert decs[0] < decs[1] < decs[2]
    p3, lam3, _ = tr_lanczos(H, g, 10.0, 3)
    resid = matvec(H, p3)
    resid = [resid[i] + g[i] for i in range(3)]
    assert norm(resid) < 1e-10 and abs(lam3) < 1e-12
    print("full step (Delta=10):", tuple(round(x, 4) for x in p3), "residual=%.2e" % norm(resid))


if __name__ == "__main__":
    main()
