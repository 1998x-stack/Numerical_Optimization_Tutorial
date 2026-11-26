"""SR1 recovers the true Hessian on a 2-D quadratic (teaching example)."""
import math


def mv(M, v):
    return [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def inv2(M):
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    if abs(d) < 1e-12:
        return None
    return [[M[1][1] / d, -M[0][1] / d], [-M[1][0] / d, M[0][0] / d]]


Q = [[3.0, 1.0], [1.0, 3.0]]
b = [5.0, 7.0]


def grad(x):
    return [Q[0][0] * x[0] + Q[0][1] * x[1] - b[0], Q[1][0] * x[0] + Q[1][1] * x[1] - b[1]]


def rel_err(B):
    num = math.sqrt(sum((B[i][j] - Q[i][j]) ** 2 for i in range(2) for j in range(2)))
    den = math.sqrt(sum(Q[i][j] ** 2 for i in range(2) for j in range(2)))
    return num / den


if __name__ == "__main__":
    x = [0.0, 0.0]; B = [[1.0, 0.0], [0.0, 1.0]]; alpha = 0.3
    errs = [rel_err(B)]
    for _ in range(12):
        g = grad(x)
        if math.hypot(*g) < 1e-9:
            break
        Bi = inv2(B)
        if Bi is None:
            break
        p = [-v for v in mv(Bi, g)]
        xn = [x[i] + alpha * p[i] for i in range(2)]
        gn = grad(xn)
        s = [xn[i] - x[i] for i in range(2)]
        y = [gn[i] - g[i] for i in range(2)]
        Bs = mv(B, s)
        v = [y[i] - Bs[i] for i in range(2)]
        vs = dot(v, s)
        if abs(vs) >= 1e-8 * math.hypot(*s) * math.hypot(*v):   # skip rule
            B = [[B[i][j] + v[i] * v[j] / vs for j in range(2)] for i in range(2)]
        x = xn
        errs.append(rel_err(B))
    print("rel err sequence:", [round(e, 4) for e in errs[:4]])
    assert errs[2] < 1e-8          # Hessian recovered after two updates
    assert math.hypot(x[0] - 1.0, x[1] - 2.0) < 1e-2
