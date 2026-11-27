"""Preconditioned trust-region Newton-CG: p=Cv turns the ball into an M-ellipsoid."""
from math import sqrt


def matvec(M, v):
    return (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])


def times(C, v):
    return (C[0][0]*v[0] + C[0][1]*v[1], C[1][0]*v[0] + C[1][1]*v[1])


def transpose_times(C, v):
    return (C[0][0]*v[0] + C[1][0]*v[1], C[0][1]*v[0] + C[1][1]*v[1])


def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]


def norm(v):
    return sqrt(dot(v, v))


def m_norm(M, v):
    return sqrt(dot(v, matvec(M, v)))


def boundary_tau(z, d, M, Delta):
    """Smallest tau >= 0 with ||z + tau*d||_M = Delta."""
    zd, dd, zz = dot(z, matvec(M, d)), dot(d, matvec(M, d)), dot(z, matvec(M, z))
    return (-zd + sqrt(zd*zd + dd*(Delta*Delta - zz))) / dd


def precond_tr_cg(H, g, M, C, Delta, eta=0.0, max_iter=10):
    """Minimize m(p)=g.p+0.5 p.Hp with ||p||<=Delta, preconditioned by M=C C^T."""
    ghat = transpose_times(C, g)
    hess = lambda v: transpose_times(C, matvec(H, times(C, v)))
    z, r = (0.0, 0.0), ghat
    d, rr = (-r[0], -r[1]), dot(r, r)
    for i in range(max_iter):
        Hd = hess(d)
        curvature = dot(d, Hd)
        if 0.0 >= curvature:
            t = boundary_tau(z, d, M, Delta)
            return (z[0] + t*d[0], z[1] + t*d[1]), i + 1, "negative curvature"
        alpha = rr / curvature
        z_new = (z[0] + alpha*d[0], z[1] + alpha*d[1])
        if m_norm(M, z_new) >= Delta:
            t = boundary_tau(z, d, M, Delta)
            return (z[0] + t*d[0], z[1] + t*d[1]), i + 1, "boundary"
        z = z_new
        r = (r[0] + alpha*Hd[0], r[1] + alpha*Hd[1])
        if eta * norm(ghat) >= norm(r):
            return z, i + 1, "residual tolerance"
        beta = dot(r, r) / rr
        rr = dot(r, r)
        d = (-r[0] + beta*d[0], -r[1] + beta*d[1])
    return z, max_iter, "iteration cap"


def model_decrease(H, g, p):
    return -(dot(g, p) + 0.5 * dot(p, matvec(H, p)))


def main():
    H, g = ((4.0, 1.0), (1.0, 3.0)), (-4.0, -6.0)
    I = ((1.0, 0.0), (0.0, 1.0))
    M = ((4.0, 0.0), (0.0, 3.0))
    C = ((2.0, 0.0), (0.0, 3.0 ** 0.5))
    v0, i0, why0 = precond_tr_cg(H, g, I, I, 1.0)
    p0 = times(I, v0)
    v1, i1, why1 = precond_tr_cg(H, g, M, C, 1.0)
    p1 = times(C, v1)
    v2, i2, why2 = precond_tr_cg(H, g, M, C, 50.0, eta=1e-14)
    p2 = times(C, v2)
    assert why0 == "boundary" and abs(norm(p0) - 1.0) < 1e-12 and dot(g, p0) < 0.0
    assert why1 == "boundary" and abs(norm(p1) - 1.0) < 1e-12 and dot(g, p1) < 0.0
    assert why2 == "residual tolerance" and abs(p2[0] - 6.0/11.0) < 1e-9
    print("no precond Delta=1 ->", i0, why0, tuple(round(v, 4) for v in p0),
          "||p||", round(norm(p0), 4), "dec", round(model_decrease(H, g, p0), 4))
    print("precond    Delta=1 ->", i1, why1, tuple(round(v, 4) for v in p1),
          "||p||", round(norm(p1), 4), "dec", round(model_decrease(H, g, p1), 4))
    print("precond    Delta=50 ->", i2, why2, tuple(round(v, 4) for v in p2))


if __name__ == "__main__":
    main()
