"""Inexact Newton on f(x)=x^2/2+x^3/6: the forcing term sets the convergence order."""
def grad(x):
    return x + x * x / 2

def hess(x):
    return 1.0 + x

def inexact_newton(x0, eta, steps):
    """eta(k, g) returns the residual factor; the step satisfies h*p + g = eta*g."""
    x, errors = x0, []
    for k in range(steps):
        gk, hk = grad(x), hess(x)
        x += -(1.0 - eta(k, gk)) * gk / hk
        errors.append(abs(x))
    return errors

def ratios(errors):
    return [errors[i + 1] / errors[i] for i in range(len(errors) - 1) if errors[i] > 1e-16]

constant = inexact_newton(0.5, lambda k, gk: 0.5, 7)
vanishing = inexact_newton(0.5, lambda k, gk: 0.5 ** (k + 1), 7)
quadratic = inexact_newton(0.5, lambda k, gk: 0.5 * abs(gk), 6)

if __name__ == "__main__":
    assert 0.55 > ratios(constant)[-1] > 0.45
    assert 0.02 > ratios(vanishing)[-1]
    assert all(1.1 * quadratic[i] ** 2 >= quadratic[i + 1] for i in range(1, 5))
    assert 1e-15 > quadratic[-1]
    print("constant  eta=0.5        ratios", [round(r, 3) for r in ratios(constant)])
    print("vanishing eta=0.5^(k+1)  ratios", [round(r, 4) for r in ratios(vanishing)])
    print("quadratic eta=0.5|g|     ratios", [f"{r:.2e}" for r in ratios(quadratic)])
    print("quadratic e[k+1]/e[k]^2 ", [round(quadratic[i + 1] / quadratic[i] ** 2, 3) for i in range(1, 5)])
