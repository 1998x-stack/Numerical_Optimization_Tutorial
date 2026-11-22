"""Exact trust-region solution for an SPD two-dimensional model."""
from math import hypot

def norm_at(lam):
    return hypot(2/(4+lam),2/(1+lam))

def solve(radius):
    if radius<=0:
        raise ValueError("radius must be positive")
    if norm_at(0)<=radius:
        return (-0.5,-2.0),0.0
    lo,hi=0.0,1.0
    while norm_at(hi)>radius:
        hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if norm_at(mid)>radius: lo=mid
        else: hi=mid
    lam=(lo+hi)/2
    return (-2/(4+lam),-2/(1+lam)),lam

def reduction(p):
    x,y=p
    return -(2*x+2*y+0.5*(4*x*x+y*y))

if __name__ == "__main__":
    for radius in (0.5,1.3,2.5):
        p,lam=solve(radius)
        print(radius,lam,p,reduction(p))
        assert hypot(*p)<=radius+1e-10 and lam>=0
    p,lam=solve(1.3)
    assert abs(lam-0.6310945588223069)<1e-8
    assert abs(reduction(p)-2.1913087311268886)<1e-8
    assert reduction(p)>1.9650065164267754
