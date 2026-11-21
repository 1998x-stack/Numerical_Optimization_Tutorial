"""Subgradients and the exact soft-threshold solution of a 1-D L1 model."""
from math import isclose

def subgradient_abs(x: float) -> tuple[float, float]:
    if x < 0.0:
        return (-1.0, -1.0)
    if x > 0.0:
        return (1.0, 1.0)
    return (-1.0, 1.0)

def soft_threshold(y: float, lam: float) -> float:
    if lam < 0.0:
        raise ValueError("lambda must be nonnegative")
    if y > lam:
        return y - lam
    if y < -lam:
        return y + lam
    return 0.0

def objective(x: float, y: float, lam: float) -> float:
    return 0.5 * (x - y) ** 2 + lam * abs(x)

if __name__ == "__main__":
    lam = 0.5
    cases = (-2.0, -0.25, 0.25, 2.0)
    for y in cases:
        x = soft_threshold(y, lam)
        print(f"y={y:5.2f} -> x*={x:5.2f}, objective={objective(x, y, lam):.4f}")
    assert subgradient_abs(0.0) == (-1.0, 1.0)
    assert isclose(soft_threshold(2.0, 0.5), 1.5)
    assert isclose(soft_threshold(-2.0, 0.5), -1.5)
    assert isclose(soft_threshold(0.25, 0.5), 0.0)
    for y in (-3.0, -1.0, 0.0, 1.0, 3.0):
        x_star = soft_threshold(y, lam)
        for candidate in (x_star - 0.1, x_star, x_star + 0.1):
            assert objective(x_star, y, lam) <= objective(candidate, y, lam) + 1e-12
