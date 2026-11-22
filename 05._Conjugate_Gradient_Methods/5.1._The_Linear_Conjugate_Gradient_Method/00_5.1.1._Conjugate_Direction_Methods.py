"""Conjugate direction method on a 2x2 positive definite quadratic."""
from math import sqrt

Q = ((3.0, 1.0), (1.0, 3.0))
b = (5.0, 7.0)

def matvec(M, v):
    return (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def gradient(x):
    qx = matvec(Q, x)
    return (qx[0] - b[0], qx[1] - b[1])

def exact_step(x, p):
    return -dot(gradient(x), p) / dot(p, matvec(Q, p))

def run(x0, directions):
    x = x0
    alphas = []
    for p in directions:
        a = exact_step(x, p)
        alphas.append(a)
        x = (x[0] + a*p[0], x[1] + a*p[1])
    return x, alphas

if __name__ == "__main__":
    p0, p1 = (1.0, 0.0), (1.0, -3.0)
    assert abs(dot(p0, matvec(Q, p1))) < 1e-12
    assert abs(dot(p0, p1) - 1.0) < 1e-12
    x_star, alphas = run((0.0, 0.0), (p0, p1))
    assert sqrt((x_star[0]-1.0)**2 + (x_star[1]-2.0)**2) < 1e-12
    assert abs(alphas[0] - 5/3) < 1e-12
    assert abs(alphas[1] + 2/3) < 1e-12
    print("x* =", x_star, "alpha =", [round(a, 6) for a in alphas])
