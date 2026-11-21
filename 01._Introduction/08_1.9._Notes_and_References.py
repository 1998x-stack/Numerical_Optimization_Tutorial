"""Independent derivative check with a central finite difference.

Demonstrates the tradeoff between truncation and floating-point error.
"""
from math import isclose

def f(x: float) -> float:
    return (x - 2.0) ** 2 + 1.0

def analytic_derivative(x: float) -> float:
    return 2.0 * (x - 2.0)

def central_difference(x: float, h: float) -> float:
    return (f(x + h) - f(x - h)) / (2.0 * h)

if __name__ == "__main__":
    x = 1.25
    exact = analytic_derivative(x)
    print(f"analytic derivative = {exact:.12f}")
    for k in (1, 3, 5, 7, 9, 11):
        h = 10.0 ** (-k)
        estimate = central_difference(x, h)
        print(f"h=1e-{k:02d}: estimate={estimate:.12f}, abs_error={abs(estimate-exact):.3e}")
    assert isclose(exact, -1.5)
    assert abs(central_difference(x, 1e-3) - exact) < 1e-9
    assert abs(central_difference(x, 1e-1) - exact) < 1e-12
