"""Numerically check the Cauchy decrease lower bound."""
def example(radius):
    if radius <= 0:
        raise ValueError("radius must be positive")
    norm_g, norm_B = 2.0, 4.0
    t = min(0.25, radius/norm_g)
    x = -2.0*t
    reduction = -2*x - 2*x*x
    lower_bound = 0.5*norm_g*min(radius,norm_g/norm_B)
    return x,reduction,lower_bound

if __name__ == "__main__":
    for r in (0.1,0.2,0.5,0.8,1.0,1.5):
        x,actual,bound=example(r)
        print(r,x,actual,bound)
        assert abs(x)<=r+1e-12
        assert actual>=bound-1e-12
    _,actual,bound=example(0.2)
    assert abs(actual-0.32)<1e-12 and abs(bound-0.2)<1e-12
    _,actual,bound=example(1.0)
    assert abs(actual-0.5)<1e-12 and abs(bound-0.5)<1e-12
