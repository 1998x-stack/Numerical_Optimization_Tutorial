"""Fletcher-Reeves with the Powell restart test on a 2x2 quadratic."""
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

def powell_ratio(g_prev, g_now):
    return abs(dot(g_now, g_prev)) / dot(g_now, g_now)

if __name__ == "__main__":
    x = (Fraction(0), Fraction(0))
    g0 = gradient(x)
    p0 = (-g0[0], -g0[1])
    x1 = substep(x, p0, Fraction(1))
    g1 = gradient(x1)
    fr1 = dot(g1, g1) / dot(g0, g0)
    p1 = (-g1[0] + fr1*p0[0], -g1[1] + fr1*p0[1])
    x_exact = substep(x1, p1, Fraction(1))
    assert gradient(x_exact) == (Fraction(0), Fraction(0))
    x2 = substep(x1, p1, Fraction(3, 5))
    g2 = gradient(x2)
    ratio = powell_ratio(g1, g2)
    assert ratio == Fraction(5, 2)
    restart = ratio >= Fraction(1, 10)
    assert dot(g2, (-g2[0], -g2[1])) < 0
    print("exact step: g =", gradient(x_exact), "| powell ratio =", ratio, "restart:", restart)
