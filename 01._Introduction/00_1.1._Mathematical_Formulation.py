"""Evaluate a small constrained optimization model by grid search.

This is a transparent teaching example, not a general-purpose optimizer.
"""
from math import isclose


def objective(x1: float, x2: float) -> float:
    return (x1 - 1.0) ** 2 + (x2 - 1.0) ** 2


def feasible(x1: float, x2: float) -> bool:
    return x1 >= 0.0 and x2 >= 0.0 and x1 + x2 >= 3.0


def grid_search(step: float = 0.05):
    candidates = []
    for i in range(81):
        for j in range(81):
            x1, x2 = i * step, j * step
            if feasible(x1, x2):
                candidates.append((objective(x1, x2), x1, x2))
    return min(candidates)


if __name__ == "__main__":
    value, x1, x2 = grid_search()
    print(f"grid minimizer: ({x1:.2f}, {x2:.2f}), f={value:.4f}")
    assert isclose(x1, 1.5, abs_tol=1e-9)
    assert isclose(x2, 1.5, abs_tol=1e-9)
    assert isclose(value, 0.5, abs_tol=1e-9)
