"""Dogleg solution for B=diag(4,1), g=(2,2)."""
from math import sqrt, hypot
U=(-0.8,-0.8)
P=(-0.5,-2.0)

def reduction(p):
    x,y=p
    return -(2*x+2*y+0.5*(4*x*x+y*y))

def dogleg(radius):
    if radius <= 0:
        raise ValueError("radius must be positive")
    nu,nb=hypot(*U),hypot(*P)
    if radius <= nu:
        return (-radius/sqrt(2),-radius/sqrt(2)), "first"
    if radius >= nb:
        return P,"Newton"
    d=(P[0]-U[0],P[1]-U[1])
    A=d[0]**2+d[1]**2
    B=2*(U[0]*d[0]+U[1]*d[1])
    C=U[0]**2+U[1]**2-radius**2
    t=(-B+sqrt(B**2-4*A*C))/(2*A)
    assert 0 <= t <= 1
    return (U[0]+t*d[0],U[1]+t*d[1]),"second"

if __name__ == "__main__":
    for r in (0.8,1.3,2.5):
        p,phase=dogleg(r)
        print(r,phase,p,reduction(p))
        assert hypot(*p)<=r+1e-10 and reduction(p)>0
    p,phase=dogleg(1.3)
    assert phase=="second"
    assert abs(reduction(p)-1.9650065164267754)<1e-9
