"""Compare weak and strong Wolfe conditions on a one-dimensional line."""
def phi(alpha: float) -> float:
    return (4.0 * alpha - 2.0) ** 2

def dphi(alpha: float) -> float:
    return 32.0 * alpha - 16.0

def conditions(alpha: float, c1: float = 1e-4, c2: float = 0.9):
    if not (0.0 < c1 < c2 < 1.0):
        raise ValueError("require 0 < c1 < c2 < 1")
    f0, slope0 = phi(0.0), dphi(0.0)
    armijo = phi(alpha) <= f0 + c1 * alpha * slope0
    weak = armijo and dphi(alpha) >= c2 * slope0
    strong = armijo and abs(dphi(alpha)) <= c2 * abs(slope0)
    return armijo, weak, strong

if __name__ == "__main__":
    at_minimum = conditions(0.50)
    overshot = conditions(0.99)
    print("alpha=0.50:", at_minimum, "phi' =", dphi(0.50))
    print("alpha=0.99:", overshot, "phi' =", dphi(0.99))
    assert at_minimum == (True, True, True)
    assert overshot == (True, True, False)
    assert abs(dphi(0.99)) > 0.9 * abs(dphi(0.0))
