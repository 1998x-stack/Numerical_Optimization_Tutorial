"""An exact hard-case trust-region minimizer using the null space."""
from math import sqrt,hypot

def solution(radius):
    if radius <= 1/3:
        raise ValueError("the pictured hard case requires radius > 1/3")
    x=sqrt(radius**2-1/9)
    return (x,-1/3),2.0

def model(p):
    x,y=p
    return y-x*x+0.5*y*y

if __name__=="__main__":
    p,lam=solution(2.0)
    other=(-p[0],p[1])
    print(p,other,model(p))
    assert abs(hypot(*p)-2.0)<1e-12
    assert lam==2.0
    assert abs(model(p)+25/6)<1e-12
    assert abs(model(other)-model(p))<1e-12
    # Stationarity and positive semidefiniteness:
    # B+2I = diag(0,3), (B+2I)p = (0,-1) = -g.
    assert abs(3*p[1]+1)<1e-12
    for candidate in ((0,0),(0,-2),(1,-1),(-1,-1)):
        if hypot(*candidate)<=2:
            assert model(candidate)>=model(p)-1e-12
