"""Quadratic interpolation from phi(0), phi'(0), phi(alpha0)."""
from math import sqrt

def phi(alpha: float, eps: float):
    return (alpha-2.0)**2 + eps*alpha**3

def candidate(alpha0: float, eps: float):
    slope0 = -4.0
    denom = 2.0*(phi(alpha0,eps)-phi(0.0,eps)-slope0*alpha0)
    if alpha0 <= 0.0 or denom <= 1e-12:
        raise ValueError("invalid interpolation curvature")
    return -slope0*alpha0**2/denom

def optimum(eps: float):
    if eps == 0.0:
        return 2.0
    return (-2.0 + sqrt(4.0 + 48.0*eps))/(6.0*eps)

if __name__ == "__main__":
    assert candidate(1.0,0.0) == 2.0
    a = candidate(1.0,0.25)
    exact = optimum(0.25)
    print("candidate:",a,"stationary point:",exact)
    assert abs(a-1.6)<1e-12
    assert abs(exact-4.0/3.0)<1e-12
    assert phi(a,0.25)<phi(0.0,0.25)
    assert abs(a-exact)>0.1
