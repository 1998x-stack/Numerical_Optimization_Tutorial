"""Illustrate two attraction basins for a nonconvex objective."""
def objective(x: float) -> float:
    return (x * x - 1.0) ** 2 + 0.4 * x


def gradient(x: float) -> float:
    return 4.0 * x * (x * x - 1.0) + 0.4


def gradient_descent(start: float, step: float = 0.01, iterations: int = 5000):
    x = start
    for _ in range(iterations):
        next_x = x - step * gradient(x)
        if abs(next_x - x) < 1e-11:
            x = next_x
            break
        x = next_x
    return x


if __name__ == "__main__":
    left = gradient_descent(-1.5)
    right = gradient_descent(1.5)
    print(f"start -1.5 -> x={left:.6f}, f={objective(left):.6f}")
    print(f"start +1.5 -> x={right:.6f}, f={objective(right):.6f}")
    assert abs(left - (-1.04668)) < 1e-3
    assert abs(right - 0.94565) < 1e-3
    assert objective(left) < objective(right)
