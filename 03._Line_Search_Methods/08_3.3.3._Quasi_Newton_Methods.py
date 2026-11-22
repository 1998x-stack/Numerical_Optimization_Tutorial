"""A small 2-D BFGS experiment with exact line search on a quadratic."""
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def matvec(A, x):
    return (A[0][0] * x[0] + A[0][1] * x[1],
            A[1][0] * x[0] + A[1][1] * x[1])

def solve2(A, b):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if det <= 0.0:
        raise ValueError("B must remain positive definite")
    return ((A[1][1] * b[0] - A[0][1] * b[1]) / det,
            (-A[1][0] * b[0] + A[0][0] * b[1]) / det)

def bfgs_demo(scale: float = 1.0):
    Q = ((4.0, 1.0), (1.0, 3.0))
    B = [[scale, 0.0], [0.0, 1.0]]
    x = (2.0, -1.0)
    records = []
    for _ in range(5):
        g = matvec(Q, x)
        if (dot(g, g) ** 0.5) < 1e-10:
            break
        p = solve2(B, (-g[0], -g[1]))
        alpha = -dot(g, p) / dot(p, matvec(Q, p))
        s = (alpha * p[0], alpha * p[1])
        x_new = (x[0] + s[0], x[1] + s[1])
        g_new = matvec(Q, x_new)
        y = (g_new[0] - g[0], g_new[1] - g[1])
        Bs = matvec(B, s)
        sBs, ys = dot(s, Bs), dot(y, s)
        if sBs <= 0.0 or ys <= 0.0:
            raise ArithmeticError("BFGS curvature condition failed")
        B_new = [[B[i][j] - Bs[i] * Bs[j] / sBs + y[i] * y[j] / ys
                  for j in range(2)] for i in range(2)]
        residual = matvec(B_new, s)
        secant_error = max(abs(residual[i] - y[i]) for i in range(2))
        det = B_new[0][0] * B_new[1][1] - B_new[0][1] * B_new[1][0]
        records.append((ys, secant_error, B_new[0][0], det))
        B, x = B_new, x_new
    return x, records

if __name__ == "__main__":
    x, records = bfgs_demo()
    print("final x:", x)
    print("curvature y^T s:", [r[0] for r in records])
    print("secant residuals:", [r[1] for r in records])
    assert len(records) >= 2
    assert all(r[0] > 0.0 for r in records)
    assert all(r[1] < 1e-10 for r in records)
    assert all(r[2] > 0.0 and r[3] > 0.0 for r in records)
