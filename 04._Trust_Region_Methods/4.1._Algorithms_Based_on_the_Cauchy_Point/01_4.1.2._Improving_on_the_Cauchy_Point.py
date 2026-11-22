"""Compare feasible Cauchy and curvature-aware steps on one sphere."""
from math import sqrt, sin, cos, radians

def reduction(p):
    x,y = p
    return -(2*x+2*y+0.5*(4*x*x+y*y))

def cauchy():
    return (-1/sqrt(2),-1/sqrt(2))

def candidate(degrees):
    theta = radians(degrees)
    return (-cos(theta),-sin(theta))

if __name__ == "__main__":
    c = cauchy()
    better = candidate(60)
    print("Cauchy drop:", reduction(c))
    print("60-degree candidate:", reduction(better))
    assert abs(sum(t*t for t in better)-1)<1e-12
    assert abs(reduction(c)-1.57842712474619)<1e-10
    assert abs(reduction(better)-1.8570508075688772)<1e-10
    assert reduction(better)>reduction(c)
