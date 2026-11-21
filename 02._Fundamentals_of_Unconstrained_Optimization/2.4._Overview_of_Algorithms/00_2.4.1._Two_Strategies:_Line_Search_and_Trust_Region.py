"""Compare line search and a 1-D trust-region subproblem on one quadratic."""
from math import isclose

def f(x: float) -> float:
    return 4.0 * x * x

def model(x: float, p: float) -> float:
    # Exact quadratic model at x for this objective.
    gradient = 8.0 * x
    hessian = 8.0
    return f(x) + gradient * p + 0.5 * hessian * p * p

if __name__ == "__main__":
    x0 = 1.0
    gradient = 8.0
    direction = -gradient
    exact_line_alpha = 1.0 / 8.0
    line_step = exact_line_alpha * direction
    radius = 0.4
    trust_step = max(-radius, min(radius, -1.0))
    print(f"line search: alpha={exact_line_alpha:.3f}, displacement={line_step:.3f}, f={f(x0+line_step):.3f}")
    print(f"trust region: radius={radius:.3f}, displacement={trust_step:.3f}, f={f(x0+trust_step):.3f}")
    assert isclose(line_step, -1.0)
    assert isclose(f(x0 + line_step), 0.0)
    assert isclose(trust_step, -0.4)
    assert isclose(model(x0, trust_step), f(x0 + trust_step))
    assert abs(trust_step) <= radius
