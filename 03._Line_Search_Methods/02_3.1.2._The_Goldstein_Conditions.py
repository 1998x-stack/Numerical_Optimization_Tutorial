"""Goldstein interval and an example whose exact line minimizer is excluded."""
def phi(alpha: float) -> float:
    return 19.0 * alpha**3 - 28.0 * alpha**2 - alpha

def dphi(alpha: float) -> float:
    return 57.0 * alpha**2 - 56.0 * alpha - 1.0

def goldstein(alpha: float, c: float = 0.2) -> tuple[bool, float, float]:
    if not (0.0 < c < 0.5) or alpha <= 0.0:
        raise ValueError("require 0 < c < 0.5 and alpha > 0")
    slope0 = dphi(0.0)
    lower = phi(0.0) + (1.0 - c) * alpha * slope0
    upper = phi(0.0) + c * alpha * slope0
    return lower <= phi(alpha) <= upper, lower, upper

if __name__ == "__main__":
    accepted, lower, upper = goldstein(0.5)
    minimizer_ok, min_lower, min_upper = goldstein(1.0)
    print("alpha=0.5:", accepted, "interval =", (lower, upper), "phi =", phi(0.5))
    print("alpha=1.0:", minimizer_ok, "interval =", (min_lower, min_upper), "phi =", phi(1.0))
    assert dphi(0.0) == -1.0
    assert dphi(1.0) == 0.0
    assert phi(1.0) == -10.0
    assert not minimizer_ok
    assert phi(1.0) < min_lower
