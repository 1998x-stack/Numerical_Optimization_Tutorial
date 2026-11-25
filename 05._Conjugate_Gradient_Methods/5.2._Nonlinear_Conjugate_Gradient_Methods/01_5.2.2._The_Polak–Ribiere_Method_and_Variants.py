"""Polak-Ribiere, Hestenes-Stiefel and Fletcher-Reeves beta on a 2x2 quadratic."""
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

def substep(x, p, c):
    alpha = -dot(gradient(x), p) / dot(p, matvec(Q, p))
    return (x[0] + c*alpha*p[0], x[1] + c*alpha*p[1])

def betas(g_prev, g_now, p_prev):
    y = (g_now[0] - g_prev[0], g_now[1] - g_prev[1])
    num = dot(g_now, y)
    return (dot(g_now, g_now) / dot(g_prev, g_prev),
            num / dot(g_prev, g_prev),
            num / dot(p_prev, y))

if __name__ == "__main__":
    x = (Fraction(0), Fraction(0))
    g0 = gradient(x)
    p0 = (-g0[0], -g0[1])
    x1 = substep(x, p0, Fraction(1))
    g1 = gradient(x1)
    fr1 = dot(g1, g1) / dot(g0, g0)
    p1 = (-g1[0] + fr1*p0[0], -g1[1] + fr1*p0[1])
    x2 = substep(x1, p1, Fraction(3, 5))
    fr, pr, hs = betas(g1, gradient(x2), p1)
    assert (fr, pr, hs) == (Fraction(4, 25), Fraction(-6, 25), Fraction(-2, 5))
    exact = betas(g1, gradient(substep(x1, p1, Fraction(1))), p1)
    assert exact == (Fraction(0), Fraction(0), Fraction(0))
    print("inexact c=3/5 -> FR, PR, HS =", fr, pr, hs, "| PR+ =", max(Fraction(0), pr))
