"""Show why a constrained optimum can lie on a boundary."""
def objective(x: float) -> float:
    return (x - 2.0) ** 2


def feasible(x: float) -> bool:
    return 0.0 <= x <= 1.0


if __name__ == "__main__":
    unconstrained_x = 2.0
    constrained_x = 1.0
    multiplier = 2.0
    gradient_at_boundary = 2.0 * (constrained_x - 2.0)

    print("unconstrained:", unconstrained_x, objective(unconstrained_x))
    print("constrained:  ", constrained_x, objective(constrained_x))
    print("boundary gradient:", gradient_at_boundary)
    print("KKT multiplier:", multiplier)

    assert not feasible(unconstrained_x)
    assert feasible(constrained_x)
    assert objective(constrained_x) == 1.0
    assert gradient_at_boundary + multiplier == 0.0
    assert multiplier >= 0.0
