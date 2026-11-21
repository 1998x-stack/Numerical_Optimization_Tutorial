"""Evaluate a trust-region quadratic model and its actual/predicted ratio."""
from math import exp, isclose

def objective(x: float) -> float:
    return exp(x)

def model(p: float) -> float:
    # Second-order Taylor model at x=0: f(0) + f'(0)p + 1/2 f''(0)p^2.
    return 1.0 + p + 0.5 * p * p

def trust_step(radius: float) -> float:
    # The unconstrained model minimizer is -1; project it onto [-radius, radius].
    return -min(radius, 1.0)

def reduction_ratio(radius: float) -> float:
    p = trust_step(radius)
    predicted = model(0.0) - model(p)
    actual = objective(0.0) - objective(p)
    if predicted <= 0.0:
        raise ValueError("the model step must predict positive reduction")
    return actual / predicted

if __name__ == "__main__":
    for radius in (0.1, 0.25, 0.5, 1.0, 1.5):
        p = trust_step(radius)
        print(f"Delta={radius:.2f}, p={p:.2f}, rho={reduction_ratio(radius):.6f}")
        assert abs(p) <= radius
        assert reduction_ratio(radius) > 0.0
    assert isclose(trust_step(0.25), -0.25)
    assert isclose(trust_step(1.5), -1.0)
    assert reduction_ratio(0.5) > 1.0
