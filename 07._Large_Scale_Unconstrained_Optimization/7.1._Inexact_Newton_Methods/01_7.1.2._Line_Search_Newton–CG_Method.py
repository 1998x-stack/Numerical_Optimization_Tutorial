"""Truncated Newton-CG on a 2D quadratic, plus a negative-curvature stop guard."""
def matvec(M, v):
    return (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def norm(v):
    return dot(v, v) ** 0.5

def newton_cg(H, g, eta, max_iter=10):
    """Approximately solve H p = -g; stop when ||r|| <= eta*||g|| or curvature <= 0."""
    z, r = (0.0, 0.0), (g[0], g[1])
    d, rr, tol = (-r[0], -r[1]), dot(r, r), eta * norm(g)
    for i in range(max_iter):
        Hd = matvec(H, d)
        curvature = dot(d, Hd)
        if 0.0 >= curvature:
            return (z if i > 0 else (-g[0], -g[1])), i, "negative curvature"
        alpha = rr / curvature
        z = (z[0] + alpha*d[0], z[1] + alpha*d[1])
        r = (r[0] + alpha*Hd[0], r[1] + alpha*Hd[1])
        if tol >= norm(r):
            return z, i + 1, "residual tolerance"
        beta = dot(r, r) / rr
        rr = dot(r, r)
        d = (-r[0] + beta*d[0], -r[1] + beta*d[1])
    return z, max_iter, "iteration cap"

def main():
    H, g = ((4.0, 1.0), (1.0, 3.0)), (-4.0, -6.0)
    loose = newton_cg(H, g, 0.5)
    tight = newton_cg(H, g, 0.01)
    indefinite = newton_cg(((1.0, 0.0), (0.0, -1.0)), (1.0, 1.0), 0.3)
    assert loose[1] == 1 and loose[2] == "residual tolerance"
    assert dot(g, loose[0]) < 0.0
    assert tight[1] == 2 and abs(tight[0][0] - 6.0/11.0) < 1e-12
    assert indefinite[2] == "negative curvature" and indefinite[0] == (-1.0, -1.0)
    print("eta=0.50 -> steps", loose[1], loose[2], "p", tuple(round(v, 4) for v in loose[0]), "g.p", round(dot(g, loose[0]), 3))
    print("eta=0.01 -> steps", tight[1], tight[2], "p", tuple(round(v, 4) for v in tight[0]))
    print("indefinite -> steps", indefinite[1], indefinite[2], "p", indefinite[0])

if __name__ == "__main__":
    main()
