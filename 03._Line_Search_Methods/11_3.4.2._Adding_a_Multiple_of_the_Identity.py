"""Shift a symmetric Hessian by tau times the identity."""
def shifted(tau: float):
    return (-1.0 + tau, 3.0 + tau)

def shifted_step(tau: float):
    a, b = shifted(tau)
    if a <= 0 or b <= 0:
        raise ValueError("H+tau*I is not positive definite")
    p = (-1.0 / a, -2.0 / b)
    slope = p[0] + 2.0*p[1]
    return p, slope, max(a,b)/min(a,b)

if __name__ == "__main__":
    tau = 1.5
    assert shifted(tau) == (0.5, 4.5)
    p, slope, kappa = shifted_step(tau)
    print("modified direction:",p,"slope:",slope,"condition:",kappa)
    assert abs(slope + 26.0/9.0) < 1e-12
    assert kappa == 9.0
    assert (3.0/0.5) == 6.0  # spectral clipping comparison
    try:
        shifted_step(0.5)
        raise AssertionError("indefinite matrix should be rejected")
    except ValueError:
        pass
