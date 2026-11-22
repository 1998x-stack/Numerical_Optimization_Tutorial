"""Spectral floor of a symmetric 2-by-2 Hessian."""
def spectral_step(delta: float):
    if delta <= 0:
        raise ValueError("delta must be positive")
    positive, negative = max(3.0, delta), max(-1.0, delta)
    b11 = (positive + negative) / 2
    b12 = (positive - negative) / 2
    determinant = positive * negative
    g = (1.0, 2.0)
    p = ((-b11*g[0]+b12*g[1])/determinant,
         (b12*g[0]-b11*g[1])/determinant)
    return (b11,b12),p,g[0]*p[0]+g[1]*p[1], max(positive,negative)/min(positive,negative)

if __name__ == "__main__":
    B,p,slope,kappa = spectral_step(1.0)
    print("B entries:",B,"direction:",p,"slope:",slope,"condition number:",kappa)
    assert B == (2.0,1.0)
    assert p == (0.0,-1.0)
    assert slope == -2.0 and kappa == 3.0
    assert spectral_step(0.5)[2] < 0.0
