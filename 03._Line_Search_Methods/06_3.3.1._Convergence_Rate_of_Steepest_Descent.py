"""Exact-line-search steepest descent on a 2-D SPD quadratic."""
def objective(x, kappa):
    return 0.5 * (x[0] ** 2 + kappa * x[1] ** 2)

def steepest_descent(kappa: float, steps: int = 10):
    if kappa < 1.0 or steps < 1:
        raise ValueError("require kappa >= 1 and steps >= 1")
    x = (1.0, 1.0)
    history = [objective(x, kappa)]
    for _ in range(steps):
        g = (x[0], kappa * x[1])
        numerator = g[0] ** 2 + g[1] ** 2
        if numerator < 1e-28:
            break
        denominator = g[0] ** 2 + kappa * g[1] ** 2
        alpha = numerator / denominator
        x = (x[0] - alpha * g[0], x[1] - alpha * g[1])
        history.append(objective(x, kappa))
    return x, history

if __name__ == "__main__":
    kappa = 25.0
    x, history = steepest_descent(kappa, 10)
    factor = ((kappa - 1.0) / (kappa + 1.0)) ** 2
    ratios = [history[i + 1] / history[i] for i in range(len(history) - 1)]
    print("x after iterations:", x)
    print("objective:", history[-1])
    print("worst-case factor:", factor)
    print("largest observed ratio:", max(ratios))
    assert all(r <= factor + 1e-12 for r in ratios)
    assert history[-1] < history[0]
