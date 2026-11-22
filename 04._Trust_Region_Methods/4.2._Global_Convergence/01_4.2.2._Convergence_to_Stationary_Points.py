"""Trust ratio for a nonquadratic, strongly convex teaching objective."""
def f(x):
    t=x-1.0
    return 0.5*t*t+0.1*t**4

def gradient(x):
    t=x-1.0
    return t+0.4*t**3

def hessian(x):
    t=x-1.0
    return 1.0+1.2*t*t

def trial(x, radius):
    if radius <= 0:
        raise ValueError("radius must be positive")
    g, h=gradient(x), hessian(x)
    p=max(-radius,min(radius,-g/h))
    predicted=-g*p-0.5*h*p*p
    if predicted <= 0:
        raise RuntimeError("nonpositive predicted decrease")
    actual=f(x)-f(x+p)
    return p,predicted,actual,actual/predicted

if __name__ == "__main__":
    p,pred,actual,rho=trial(2.0,0.5)
    print("step",p,"pred",pred,"actual",actual,"rho",rho)
    assert p == -0.5
    assert abs(pred-0.425)<1e-12
    assert abs(actual-0.46875)<1e-12
    assert abs(rho-0.46875/0.425)<1e-12
    assert trial(2.0,0.2)[3]>0
