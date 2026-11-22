"""Local Newton convergence and an indefinite-Hessian non-descent example."""
def f(x: float) -> float:
    return 0.5 * x**2 + 0.25 * x**4

def grad(x: float) -> float:
    return x + x**3

def hess(x: float) -> float:
    return 1.0 + 3.0 * x**2

def newton(x: float, steps: int = 6):
    history = [x]
    for _ in range(steps):
        x = x - grad(x) / hess(x)
        history.append(x)
    return history

if __name__ == "__main__":
    history = newton(1.0)
    errors = [abs(x) for x in history]
    ratios = [errors[k + 1] / (errors[k] ** 2) for k in range(3)]
    print("Newton iterates:", history[:5])
    print("e[k+1] / e[k]^2:", ratios)
    assert errors[1] < errors[0]
    assert errors[3] < 0.02
    assert ratios[-1] < ratios[0]

    x = 0.1
    g = 4.0 * x**3 - 2.0 * x
    h = 12.0 * x**2 - 2.0
    p = -g / h
    assert h < 0.0
    assert g * p > 0.0  # Newton direction is not a descent direction.
