"""Exact-arithmetic conjugate gradient on a 2x2 positive definite quadratic."""
from fractions import Fraction as F

Q = ((F(3), F(1)), (F(1), F(3)))
b = (F(5), F(7))
xstar = (F(1), F(2))

def matvec(v):
    return (Q[0][0]*v[0] + Q[0][1]*v[1], Q[1][0]*v[0] + Q[1][1]*v[1])

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def gradient(x):
    q = matvec(x)
    return (q[0] - b[0], q[1] - b[1])

def run(x0, steps):
    x, g = x0, gradient(x0)
    p = (-g[0], -g[1])
    grads = [g]
    for _ in range(steps):
        alpha = -dot(g, p) / dot(p, matvec(p))
        x = (x[0] + alpha*p[0], x[1] + alpha*p[1])
        g_next = gradient(x)
        beta = dot(g_next, g_next) / dot(g, g)
        p = (-g_next[0] + beta*p[0], -g_next[1] + beta*p[1])
        g, grads = g_next, grads + [g_next]
    return x, grads

if __name__ == "__main__":
    x2, grads = run((F(0), F(0)), 2)
    assert dot(grads[0], grads[1]) == 0
    assert dot(grads[0], grads[2]) == 0
    assert x2 == xstar
    assert matvec(x2) == b
    print("x2 =", tuple(str(c) for c in x2), "| g0.g1 =", dot(grads[0], grads[1]))
