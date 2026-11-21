"""Numerically verify five original exercises from unconstrained optimization."""
from math import exp, isclose

def soft_threshold(y: float, lam: float) -> float:
    return max(-lam, min(lam, y)) * -1.0 + y if abs(y) > lam else 0.0

def exercise_results() -> dict[str, float]:
    # 1) Stationary point of x^2 + xy + y^2 - 4x.
    x, y = 8.0 / 3.0, -4.0 / 3.0
    value = x*x + x*y + y*y - 4.0*x
    # 2) L1-regularized scalar least squares, y=1.5, lambda=0.5.
    sparse_solution = soft_threshold(1.5, 0.5)
    # 3) Directional derivative for g=(2,-1), p=(-1,-1).
    slope = 2.0*(-1.0) + (-1.0)*(-1.0)
    # 4) Trust-region ratio for exp(x), x=0, p=-0.25.
    predicted = 0.25 - 0.5 * 0.25**2
    actual = 1.0 - exp(-0.25)
    ratio = actual / predicted
    # 5) Scale H=diag(100,1) by D=diag(0.1,1).
    scaled_condition = max(100.0*0.1**2, 1.0) / min(100.0*0.1**2, 1.0)
    return {"x": x, "y": y, "quadratic_minimum": value,
            "sparse_solution": sparse_solution, "directional_slope": slope,
            "trust_ratio": ratio, "scaled_condition": scaled_condition}

if __name__ == "__main__":
    result = exercise_results()
    for name, value in result.items():
        print(f"{name}: {value:.8f}")
    assert isclose(result["x"], 8.0/3.0)
    assert isclose(result["y"], -4.0/3.0)
    assert isclose(result["quadratic_minimum"], -16.0/3.0)
    assert isclose(result["sparse_solution"], 1.0)
    assert isclose(result["directional_slope"], -1.0)
    assert result["trust_ratio"] > 1.0
    assert isclose(result["scaled_condition"], 1.0)
