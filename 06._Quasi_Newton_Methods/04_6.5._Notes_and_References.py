"""One observation, three quasi-Newton updates: secant consistency and determinants."""


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def mv(B, v):
    return [B[0][0] * v[0] + B[0][1] * v[1], B[1][0] * v[0] + B[1][1] * v[1]]


def det(B):
    return B[0][0] * B[1][1] - B[0][1] * B[1][0]


def broyden(B, s, y, phi):
    """phi=0 -> BFGS, phi=1 -> DFP."""
    Bs = mv(B, s); sBs = dot(s, Bs); ys = dot(y, s)
    v = [y[i] / ys - Bs[i] / sBs for i in range(2)]
    return [[B[i][j] - Bs[i] * Bs[j] / sBs + y[i] * y[j] / ys + phi * sBs * v[i] * v[j]
             for j in range(2)] for i in range(2)]


def sr1(B, s, y):
    Bs = mv(B, s)
    v = [y[i] - Bs[i] for i in range(2)]
    vs = dot(v, s)
    if abs(vs) < 1e-12:
        return None
    return [[B[i][j] + v[i] * v[j] / vs for j in range(2)] for i in range(2)]


if __name__ == "__main__":
    B0, s, y = [[1.0, 0.0], [0.0, 1.0]], (1.0, 0.0), (0.9, 2.0)
    updates = {"BFGS": broyden(B0, s, y, 0.0), "DFP": broyden(B0, s, y, 1.0),
               "SR1": sr1(B0, s, y)}
    for name, B1 in updates.items():
        assert abs(B1[0][0] * s[0] + B1[0][1] * s[1] - y[0]) < 1e-12   # secant
        print(name, "B1 =", B1, "det =", round(det(B1), 4))
    assert det(updates["BFGS"]) > 0 and det(updates["DFP"]) > 0
    assert det(updates["SR1"]) < 0          # SR1 is not positive definite
