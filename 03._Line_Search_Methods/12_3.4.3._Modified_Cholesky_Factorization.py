"""Two-dimensional pivot modification: pedagogical LDL^T example."""
def modified_ldl(delta: float):
    if delta <= 0:
        raise ValueError("delta must be positive")
    d1 = max(1.0, delta)
    l21 = 2.0/d1
    raw2 = 1.0-l21*l21*d1
    d2 = max(raw2, delta)
    b11, b12, b22 = d1, l21*d1, l21*l21*d1+d2
    det = b11*b22-b12*b12
    p = ((-b22+b12)/det,(b12-b11)/det)
    return (d1,d2), (b11,b12,b22), p, sum(p)

if __name__ == "__main__":
    D,B,p,slope = modified_ldl(0.5)
    print("D:",D,"B:",B,"p:",p,"slope:",slope)
    assert D == (1.0,0.5)
    assert B == (1.0,2.0,4.5)
    assert p == (-5.0,2.0)
    assert slope == -3.0
    for delta in (0.25,1.0,2.0):
        d,b,p,slope = modified_ldl(delta)
        assert d[0]>0 and d[1]>0 and b[0]*b[2]-b[1]**2>0
        assert slope<0
