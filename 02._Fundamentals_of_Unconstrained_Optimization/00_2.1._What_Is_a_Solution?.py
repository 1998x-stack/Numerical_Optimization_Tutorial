"""Separate an attained minimum, a stationary non-minimum, and an infimum."""
from math import exp, isclose

def quadratic(x: float) -> float:
    return (x - 2.0) ** 2 + 0.5

def quadratic_gradient(x: float) -> float:
    return 2.0 * (x - 2.0)

def cubic(x: float) -> float:
    return x ** 3

def cubic_gradient(x: float) -> float:
    return 3.0 * x ** 2

if __name__ == "__main__":
    minimizer = 2.0
    print("quadratic minimizer:", minimizer, "minimum value:", quadratic(minimizer))
    print("cubic stationary derivative at zero:", cubic_gradient(0.0))
    print("exp(-1), exp(-5), exp(-10):", exp(-1), exp(-5), exp(-10))
    assert isclose(quadratic(minimizer), 0.5)
    for x in (-3.0, 0.0, 1.0, 2.0, 3.5):
        assert quadratic(x) >= quadratic(minimizer)
    assert isclose(quadratic_gradient(minimizer), 0.0)
    assert isclose(cubic_gradient(0.0), 0.0)
    assert cubic(-0.1) < cubic(0.0) < cubic(0.1)
    assert exp(-10) < exp(-5) < exp(-1)
    assert exp(-10) > 0.0
