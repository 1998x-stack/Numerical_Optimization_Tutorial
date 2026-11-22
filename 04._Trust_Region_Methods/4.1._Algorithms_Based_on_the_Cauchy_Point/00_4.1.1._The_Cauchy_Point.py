"""Compute Cauchy steps for a simple two-dimensional quadratic model."""
from math import hypot

def cauchy(radius):
    if radius <= 0:
        raise ValueError("radius must be positive")
    g = (2.0, 0.0)
    norm = hypot(*g)
    gg = norm**2
    gBg = 4.0*g[0]**2 + g[1]**2
    t = min(gg/gBg, radius/norm) if gBg > 0 else radius/norm
    p = (-t*g[0], -t*g[1])
    reduction = -(2*p[0] + 0.5*(4*p[0]**2+p[1]**2))
    return p, reduction

if __name__ == "__main__":
    p, decrease = cauchy(1.0)
    print("delta=1:", p, decrease)
    assert p == (-0.5, 0.0) and abs(decrease-0.5)<1e-12
    p, decrease = cauchy(0.2)
    assert abs(p[0]+0.2)<1e-12
    assert abs(decrease-0.32)<1e-12
