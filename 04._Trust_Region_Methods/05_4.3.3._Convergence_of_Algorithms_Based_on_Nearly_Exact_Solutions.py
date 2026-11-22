"""Test near-exact trust-region model reduction in an exact 2-D case."""
from math import hypot,sqrt
OPTIMAL=25.0/6.0
def trial(t):
    p=(t,-1.0/3.0)
    if hypot(*p)>2.0+1e-12:
        raise ValueError("infeasible trust-region step")
    reduction=t*t+5.0/18.0
    return p,reduction,reduction/OPTIMAL
if __name__=="__main__":
    for t in (0.5,1.0,1.5,sqrt(35)/3):
        p,d,r=trial(t)
        print(t,p,d,r)
        assert 0<r<=1+1e-12
    assert trial(1.5)[2]>=.6
    assert trial(.5)[2]<.6
    assert abs(trial(sqrt(35)/3)[2]-1)<1e-12
    # With g=0, B=diag(-2,1), p=(2,0) reduces the model by 4.
    assert -0.5*(-2*2**2)==4.0
