"""Check the convexity inequality for a quadratic teaching example."""
from math import isclose

def f(x: float) -> float:
    return (x - 1.0) ** 2

def chord_gap(theta: float, a: float = 0.0, b: float = 4.0) -> float:
    x = theta * a + (1.0 - theta) * b
    return theta * f(a) + (1.0 - theta) * f(b) - f(x)

if __name__ == "__main__":
    theta = 0.25
    x = theta * 0.0 + (1.0 - theta) * 4.0
    lhs = f(x)
    rhs = theta * f(0.0) + (1.0 - theta) * f(4.0)
    print(f"x={x:.2f}, curve={lhs:.2f}, chord={rhs:.2f}, gap={rhs-lhs:.2f}")
    assert isclose(x, 3.0)
    assert isclose(lhs, 4.0)
    assert isclose(rhs, 7.0)
    for i in range(101):
        assert chord_gap(i / 100.0) >= -1e-12
    assert isclose(chord_gap(0.0), 0.0)
    assert isclose(chord_gap(1.0), 0.0)
