"""Scale a 2D SPD trust-region model using q=D*p."""
from math import hypot,sqrt

def solve(d,delta=1.0):
    if d<=0 or delta<=0: raise ValueError("positive scale and radius")
    grad=(10.0/d,1.0)
    curv=(100.0/d**2,1.0)
    def scaled(lam):
        return (-grad[0]/(curv[0]+lam),-grad[1]/(curv[1]+lam))
    if hypot(*scaled(0))<=delta:
        lam=0.0
    else:
        lo,hi=0.,1.
        while hypot(*scaled(hi))>delta: hi*=2
        for _ in range(80):
            mid=(lo+hi)/2
            if hypot(*scaled(mid))>delta: lo=mid
            else: hi=mid
        lam=(lo+hi)/2
    q=scaled(lam)
    p=(q[0]/d,q[1])
    drop=-(10*p[0]+p[1]+.5*(100*p[0]**2+p[1]**2))
    return q,p,drop,lam

if __name__=="__main__":
    q,p,drop,lam=solve(10)
    print(q,p,drop,lam)
    assert abs(q[0]+1/sqrt(2))<1e-12
    assert abs(q[1]+1/sqrt(2))<1e-12
    assert abs(hypot(10*p[0],p[1])-1)<1e-12
    assert abs(drop-(sqrt(2)-.5))<1e-12
    assert abs(lam-(sqrt(2)-1))<1e-12
    for d in (1,2,5,10):
        _,p,drop,_=solve(d)
        assert hypot(d*p[0],p[1])<=1+1e-10
        assert drop>0
