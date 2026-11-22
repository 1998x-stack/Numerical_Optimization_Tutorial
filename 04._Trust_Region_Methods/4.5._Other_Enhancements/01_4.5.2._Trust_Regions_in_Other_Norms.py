"""Compare L1/L2/Linf radii with a nonnegative-variable box QP."""
from math import hypot,sqrt
X=(0.2,0.3)
P=(-0.2,-0.3)
def norms(p):
    return abs(p[0])+abs(p[1]),hypot(*p),max(abs(p[0]),abs(p[1]))
def boxed(delta):
    if delta<=0: raise ValueError("radius must be positive")
    low=(-min(X[0],delta),-min(X[1],delta))
    unconstrained=(-0.5,-0.5)
    p=tuple(max(low[i],min(delta,unconstrained[i])) for i in range(2))
    model=p[0]+2*p[1]+p[0]**2+2*p[1]**2
    return p,-model
if __name__=="__main__":
    n1,n2,ninf=norms(P)
    print("norms",n1,n2,ninf)
    assert abs(n1-0.5)<1e-12
    assert abs(n2-sqrt(.13))<1e-12
    assert ninf==.3 and n2>.3 and n1>.3
    p,drop=boxed(.3)
    assert p==P and abs(drop-.58)<1e-12
    for delta in (.1,.3,.6):
        p,drop=boxed(delta)
        assert max(abs(z) for z in p)<=delta+1e-12
        assert all(X[i]+p[i]>=-1e-12 for i in (0,1))
        assert drop>0
