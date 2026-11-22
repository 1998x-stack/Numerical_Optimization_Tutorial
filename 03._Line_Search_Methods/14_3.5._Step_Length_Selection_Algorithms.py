"""Derivative-sign bisection on a strictly convex quadratic."""
def dphi(alpha):
    return 2.0*(alpha-2.0)

def bracket(steps=4):
    left, right = 0.0, 5.0
    if not (dphi(left) < 0 and dphi(right) > 0):
        raise ValueError("the bracket must straddle a stationary point")
    history = []
    for _ in range(steps):
        midpoint = (left+right)/2.0
        history.append(midpoint)
        if dphi(midpoint) > 0:
            right = midpoint
        elif dphi(midpoint) < 0:
            left = midpoint
        else:
            left = right = midpoint
            break
    return (left,right),history

if __name__ == "__main__":
    interval, trials = bracket(4)
    print("candidates:",trials,"bracket:",interval)
    assert trials == [2.5,1.25,1.875,2.1875]
    assert interval == (1.875,2.1875)
    assert interval[0] < 2.0 < interval[1]
