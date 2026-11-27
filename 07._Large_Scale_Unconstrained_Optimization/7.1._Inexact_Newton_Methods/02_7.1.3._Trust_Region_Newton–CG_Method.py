"""Trust-region Newton-CG (Steihaug): boundary and negative-curvature exits."""
def matvec(M, v):
    return (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def norm(v):
    return dot(v, v) ** 0.5

def boundary_tau(z, d, Delta):
    """Smallest tau >= 0 with ||z + tau*d|| = Delta."""
    zd, dd, zz = dot(z, d), dot(d, d), dot(z, z)
    return (-zd + (zd*zd + dd*(Delta*Delta - zz)) ** 0.5) / dd

def tr_cg(H, g, Delta, eta=0.0, max_iter=10):
    """Approximately minimize m(p)=g.p+0.5 p.Hp inside ||p|| <= Delta."""
    z, r = (0.0, 0.0), (g[0], g[1])
    d, rr = (-r[0], -r[1]), dot(r, r)
    for i in range(max_iter):
        Hd = matvec(H, d)
        curvature = dot(d, Hd)
        if 0.0 >= curvature:
            tau = boundary_tau(z, d, Delta)
            return (z[0] + tau*d[0], z[1] + tau*d[1]), i + 1, "negative curvature"
        alpha = rr / curvature
        z_new = (z[0] + alpha*d[0], z[1] + alpha*d[1])
        if norm(z_new) >= Delta:
            tau = boundary_tau(z, d, Delta)
            return (z[0] + tau*d[0], z[1] + tau*d[1]), i + 1, "boundary"
        z = z_new
        r = (r[0] + alpha*Hd[0], r[1] + alpha*Hd[1])
        if eta * norm(g) >= norm(r):
            return z, i + 1, "residual tolerance"
        beta = dot(r, r) / rr
        rr = dot(r, r)
        d = (-r[0] + beta*d[0], -r[1] + beta*d[1])
    return z, max_iter, "iteration cap"

def model_decrease(H, g, p):
    return -(dot(g, p) + 0.5 * dot(p, matvec(H, p)))

def main():
    H, g = ((4.0, 1.0), (1.0, 3.0)), (-4.0, -6.0)
    small = tr_cg(H, g, 1.0)
    large = tr_cg(H, g, 5.0, eta=1e-12)
    indefinite = tr_cg(((1.0, 0.0), (0.0, -1.0)), (1.0, 1.0), 1.0)
    assert small[2] == "boundary" and abs(norm(small[0]) - 1.0) < 1e-12
    assert model_decrease(H, g, small[0]) > 0.0 and dot(g, small[0]) < 0.0
    assert large[2] == "residual tolerance" and abs(large[0][0] - 6.0/11.0) < 1e-12
    assert indefinite[2] == "negative curvature" and abs(norm(indefinite[0]) - 1.0) < 1e-12
    print("Delta=1 ->", small[1], small[2], tuple(round(v, 4) for v in small[0]), "decrease", round(model_decrease(H, g, small[0]), 4))
    print("Delta=5 ->", large[1], large[2], tuple(round(v, 4) for v in large[0]))
    print("indefinite ->", indefinite[1], indefinite[2], tuple(round(v, 4) for v in indefinite[0]))

if __name__ == "__main__":
    main()
