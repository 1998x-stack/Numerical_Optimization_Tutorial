"""Gradient descent and Newton steps on one strictly convex quadratic."""
from math import isclose

def f(x: float) -> float:
    return (x - 3.0) ** 2 + 1.0

def gradient(x: float) -> float:
    return 2.0 * (x - 3.0)

def hessian(x: float) -> float:
    return 2.0

def gradient_descent(x: float, step: float, count: int) -> float:
    for _ in range(count):
        x -= step * gradient(x)
    return x

def newton_step(x: float) -> float:
    return x - gradient(x) / hessian(x)

if __name__ == "__main__":
    x0 = 0.0
    gd_first = gradient_descent(x0, 0.2, 1)
    gd_tenth = gradient_descent(x0, 0.2, 10)
    newton_first = newton_step(x0)
    unstable = gradient_descent(x0, 1.05, 10)
    print(f"GD (1 step) = {gd_first:.6f}")
    print(f"GD (10 steps) = {gd_tenth:.6f}")
    print(f"Newton (1 step) = {newton_first:.6f}")
    assert isclose(gd_first, 1.2)
    assert isclose(gd_tenth, 3.0 * (1.0 - 0.6 ** 10))
    assert isclose(newton_first, 3.0)
    assert isclose(f(newton_first), 1.0)
    assert abs(unstable - 3.0) > abs(x0 - 3.0)
