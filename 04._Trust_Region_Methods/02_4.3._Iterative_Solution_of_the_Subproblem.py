"""Secular-equation bisection for a symmetric positive definite 2-D B."""
from math import hypot

def step(lam):
    return (-2.0/(4.0+lam),-2.0/(1.0+lam))

def solve(radius):
    if radius<=0:
        raise ValueError("radius must be positive")
    if hypot(*step(0))<=radius:
        return 0.0,step(0)
    lo,hi=0.0,1.0
    while hypot(*step(hi))>radius:
        hi*=2.0
    for _ in range(80):
        mid=(lo+hi)/2
        if hypot(*step(mid))>radius:
            lo=mid
        else:
            hi=mid
    lam=(lo+hi)/2
    return lam,step(lam)

def drop(p):
    return -(2*p[0]+2*p[1]+.5*(4*p[0]**2+p[1]**2))

if __name__=="__main__":
    lam,p=solve(1.3)
    print(lam,p,drop(p))
    assert abs(lam-0.6310945588223069)<1e-9
    assert abs(hypot(*p)-1.3)<1e-10
    assert abs(drop(p)-2.1913087311268886)<1e-9
    assert solve(2.5)[0]==0
