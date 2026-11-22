"""Hessian modification: a direction can be non-descent before correction."""
def direction(tau: float):
    g = (2.0, -2.0)
    h = (2.0 + tau, -2.0 + tau)
    if abs(h[0]) < 1e-12 or abs(h[1]) < 1e-12:
        raise ValueError("singular modified Hessian")
    p = (-g[0] / h[0], -g[1] / h[1])
    return p, sum(g[i] * p[i] for i in range(2))

if __name__ == "__main__":
    p0, slope0 = direction(0.0)
    p, slope = direction(3.0)
    print("raw Newton:", p0, "directional derivative:", slope0)
    print("modified Newton:", p, "directional derivative:", slope)
    assert p0 == (-1.0, -1.0) and slope0 == 0.0
    assert p == (-0.4, 2.0)
    assert abs(slope + 4.8) < 1e-12
