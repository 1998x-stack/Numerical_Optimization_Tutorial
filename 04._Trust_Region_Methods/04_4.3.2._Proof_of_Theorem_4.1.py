"""Verify an exact global trust-region certificate and its identity."""
from math import sqrt,cos,sin,pi,hypot

DELTA=2.0
LAM=2.0
STAR=(sqrt(35)/3,-1/3)

def q(p):
    x,y=p
    return y-x*x+.5*y*y

def gap_identity(v):
    d=(v[0]-STAR[0],v[1]-STAR[1])
    first=.5*3*d[1]*d[1] # B+lambda I = diag(0,3)
    second=.5*LAM*(DELTA**2-v[0]**2-v[1]**2)
    return first+second

if __name__=="__main__":
    assert abs(hypot(*STAR)-DELTA)<1e-12
    assert abs(3*STAR[1]+1)<1e-12
    for radius in (0.0,.5,1.0,2.0):
        for angle in range(0,360,15):
            t=angle*pi/180
            v=(radius*cos(t),radius*sin(t))
            observed=q(v)-q(STAR)
            predicted=gap_identity(v)
            assert abs(observed-predicted)<1e-11
            assert observed>=-1e-11
    print("certificate passed; model optimum:",q(STAR))
    assert abs(q(STAR)+25/6)<1e-12
