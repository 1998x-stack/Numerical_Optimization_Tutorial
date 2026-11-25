"""Fletcher-Reeves nonlinear conjugate gradient on a 2x2 quadratic."""
from fractions import Fraction

Q = ((3, 1), (1, 3))
b = (5, 7)

def matvec(M, v):
    return (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def gradient(x):
    q = matvec(Q, x)
    return (q[0] - b[0], q[1] - b[1])

def fletcher_reeves(x0, max_iter=10):
    x, g = x0, gradient(x0)
    p = (-g[0], -g[1])
    trace = []
    for k in range(max_iter):
        alpha = -dot(g, p) / dot(p, matvec(Q, p))
        x = (x[0] + alpha*p[0], x[1] + alpha*p[1])
        g_next = gradient(x)
        beta = dot(g_next, g_next) / dot(g, g)
        trace.append((k, alpha, beta, x))
        if dot(g_next, g_next) < Fraction(1, 10**12):
            break
        p = (-g_next[0] + beta*p[0], -g_next[1] + beta*p[1])
        g = g_next
    return x, trace

if __name__ == "__main__":
    x_star, trace = fletcher_reeves((Fraction(0), Fraction(0)))
    assert trace[0][1] == Fraction(37, 146)
    assert trace[0][2] == Fraction(36, 5329)
    assert trace[1][1] == Fraction(73, 148)
    assert trace[1][2] == 0
    assert x_star == (Fraction(1), Fraction(2))
    print("x* =", x_star, "beta =", [str(t[2]) for t in trace])
