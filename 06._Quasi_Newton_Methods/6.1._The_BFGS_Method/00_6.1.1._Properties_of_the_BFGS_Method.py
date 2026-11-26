"""BFGS inverse update on a 2x2 positive definite quadratic.

Verifies the secant equation H y = s, positive definiteness of the updated
inverse Hessian, and two-step termination on a fixed teaching problem.
"""
Q = ((3.0, 1.0), (1.0, 3.0))


def matvec(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def bfgs_H(H, s, y):
    """H+ = (I - rho*s*y^T) H (I - rho*y*s^T) + rho*s*s^T, expanded. Needs s'y > 0."""
    rho = 1.0 / dot(s, y)
    Hy = matvec(H, y)
    yHy = dot(y, Hy)
    out = [[0.0, 0.0], [0.0, 0.0]]
    for i in range(2):
        for j in range(2):
            out[i][j] = (H[i][j] - rho * (s[i] * Hy[j] + Hy[i] * s[j])
                         + rho * rho * yHy * s[i] * s[j] + rho * s[i] * s[j])
    return out


def run():
    x, H = (1.0, 0.0), [[1.0, 0.0], [0.0, 1.0]]
    H1 = None
    for k in range(2):
        g = matvec(Q, x)
        Hg = matvec(H, g)
        p = (-Hg[0], -Hg[1])
        a = -dot(g, p) / dot(p, matvec(Q, p))   # exact line search
        x_new = (x[0] + a * p[0], x[1] + a * p[1])
        g_new = matvec(Q, x_new)
        s, y = sub(x_new, x), sub(g_new, g)
        if dot(s, y) > 1e-12:
            H = bfgs_H(H, s, y)
            if k == 0:
                H1 = H
        x = x_new
    return x, H1


if __name__ == "__main__":
    x_star, H1 = run()
    assert abs(x_star[0]) < 1e-12 and abs(x_star[1]) < 1e-12
    det = H1[0][0] * H1[1][1] - H1[0][1] * H1[1][0]
    assert abs(det - 0.2777777777) < 1e-6
    print("x* =", x_star, "det H1 =", det)
