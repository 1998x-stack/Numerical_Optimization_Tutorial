"""Correct a single indefinite symmetric 2-by-2 block."""
def modify_block(delta: float):
    if delta <= 0.0:
        raise ValueError("delta must be positive")
    a = (2.0+delta)/2.0
    b = (2.0-delta)/2.0
    det = a*a-b*b
    p = (-1.0/delta, 1.0/delta)
    slope = p[0]-p[1]
    return (a,b,a), det, p, slope

if __name__ == "__main__":
    B,det,p,slope = modify_block(1.0)
    print("B:",B,"det:",det,"p:",p,"slope:",slope)
    assert B == (1.5,0.5,1.5) and det == 2.0
    assert p == (-1.0,1.0) and slope == -2.0
    for delta in (0.25,0.5,1.0,2.0):
        B,det,p,slope = modify_block(delta)
        assert det > 0.0 and slope < 0.0
    # Adding just I to the original H leaves a negative eigenvalue.
    assert 1.0-2.0 < 0.0
