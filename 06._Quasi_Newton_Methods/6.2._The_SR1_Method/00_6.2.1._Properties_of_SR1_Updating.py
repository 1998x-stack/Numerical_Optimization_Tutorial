"""SR1 (symmetric rank-one) Hessian update: secant equation and indefiniteness."""


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def sr1(B, s, y):
    """B+ = B + v v^T / (v^T s) with v = y - B s. Returns None if v^T s ~ 0."""
    v = (y[0] - (B[0][0] * s[0] + B[0][1] * s[1]),
         y[1] - (B[1][0] * s[0] + B[1][1] * s[1]))
    vs = dot(v, s)
    if abs(vs) < 1e-12:
        return None
    return [[B[i][j] + v[i] * v[j] / vs for j in range(2)] for i in range(2)]


def det(B):
    return B[0][0] * B[1][1] - B[0][1] * B[1][0]


if __name__ == "__main__":
    B0, s = [[1.0, 0.0], [0.0, 1.0]], (1.0, 0.0)
    B1 = sr1(B0, s, (3.0, 1.0))
    assert abs(B1[0][0] * s[0] + B1[0][1] * s[1] - 3.0) < 1e-12   # secant equation
    assert det(B1) > 0                                            # positive definite
    B2 = sr1(B0, s, (0.9, 2.0))
    assert abs(B2[0][0] * s[0] + B2[0][1] * s[1] - 0.9) < 1e-12
    assert det(B2) < 0                                            # indefinite
    assert sr1(B0, s, (1.0, 2.0)) is None                         # zero denominator
    print("B1 det =", det(B1))
    print("B2 det =", det(B2))
