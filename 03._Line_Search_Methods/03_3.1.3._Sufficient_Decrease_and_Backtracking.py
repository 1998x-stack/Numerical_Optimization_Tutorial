"""Armijo backtracking with a finite iteration guard."""
def phi(alpha: float) -> float:
    return (4.0 * alpha - 2.0) ** 2

def dphi0() -> float:
    return -16.0

def armijo(alpha: float, c: float = 1e-4) -> bool:
    return phi(alpha) <= phi(0.0) + c * alpha * dphi0()

def backtracking(alpha0: float = 1.0, rho: float = 0.5,
                 c: float = 1e-4, max_trials: int = 100):
    if alpha0 <= 0.0 or not (0.0 < rho < 1.0) or not (0.0 < c < 1.0):
        raise ValueError("require alpha0 > 0 and rho,c in (0,1)")
    alpha = alpha0
    for trials in range(1, max_trials + 1):
        if armijo(alpha, c):
            return alpha, trials
        alpha *= rho
    raise RuntimeError("backtracking exceeded max_trials")

if __name__ == "__main__":
    alpha, trials = backtracking()
    print(f"accepted alpha={alpha:.6f} after {trials} trials")
    print(f"phi(alpha)={phi(alpha):.6f}")
    assert alpha == 0.5
    assert trials == 2
    assert armijo(alpha)
    assert not armijo(1.0)
