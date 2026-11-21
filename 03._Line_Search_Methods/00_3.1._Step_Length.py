"""Armijo, weak/strong Wolfe, Goldstein and backtracking on a scalar line."""
from math import isclose

def f(x: float) -> float:
    return (x - 2.0) ** 2

def phi(alpha: float) -> float:
    # x0=0 and descent direction p=4.
    return f(4.0 * alpha)

def phi_prime(alpha: float) -> float:
    return 32.0 * alpha - 16.0

def armijo(alpha: float, c1: float = 1e-4) -> bool:
    return phi(alpha) <= phi(0.0) + c1 * alpha * phi_prime(0.0)

def weak_wolfe(alpha: float, c1: float = 1e-4, c2: float = 0.9) -> bool:
    return armijo(alpha, c1) and phi_prime(alpha) >= c2 * phi_prime(0.0)

def strong_wolfe(alpha: float, c1: float = 1e-4, c2: float = 0.9) -> bool:
    return armijo(alpha, c1) and abs(phi_prime(alpha)) <= c2 * abs(phi_prime(0.0))

def goldstein(alpha: float, c: float = 0.2) -> bool:
    lower = phi(0.0) + (1.0 - c) * alpha * phi_prime(0.0)
    upper = phi(0.0) + c * alpha * phi_prime(0.0)
    return lower <= phi(alpha) <= upper

def backtracking(alpha0: float = 1.0, rho: float = 0.5, c1: float = 1e-4) -> float:
    if alpha0 <= 0.0 or not 0.0 < rho < 1.0 or not 0.0 < c1 < 1.0:
        raise ValueError("require alpha0>0 and rho,c1 in (0,1)")
    alpha = alpha0
    for _ in range(100):
        if armijo(alpha, c1):
            return alpha
        alpha *= rho
    raise RuntimeError("Armijo backtracking did not terminate within 100 trials")

if __name__ == "__main__":
    selected = backtracking()
    print("alpha=1 Armijo:", armijo(1.0))
    print(f"backtracking selected alpha={selected:.6f}, phi={phi(selected):.6f}")
    print("weak Wolfe at alpha=0.5:", weak_wolfe(0.5))
    print("strong Wolfe at alpha=0.5:", strong_wolfe(0.5))
    print("Goldstein at alpha=0.5:", goldstein(0.5))
    assert not armijo(1.0)
    assert isclose(selected, 0.5)
    assert armijo(selected)
    assert weak_wolfe(0.5)
    assert strong_wolfe(0.5)
    assert goldstein(0.5)
