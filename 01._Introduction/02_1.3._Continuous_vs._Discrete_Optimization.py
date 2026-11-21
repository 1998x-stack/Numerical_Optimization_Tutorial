"""Compare a continuous optimum with an integer-constrained optimum."""
def objective(x: float) -> float:
    return (x - 2.4) ** 2


if __name__ == "__main__":
    continuous_x = 2.4
    integer_x = min(range(6), key=objective)
    print(f"continuous: x={continuous_x:.1f}, f={objective(continuous_x):.2f}")
    print(f"integer:    x={integer_x}, f={objective(integer_x):.2f}")
    assert objective(continuous_x) == 0.0
    assert integer_x == 2
    assert abs(objective(integer_x) - 0.16) < 1e-12
