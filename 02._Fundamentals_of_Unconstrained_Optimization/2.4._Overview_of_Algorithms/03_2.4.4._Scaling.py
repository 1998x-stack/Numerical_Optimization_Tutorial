"""Show how diagonal variable scaling changes a quadratic condition number."""
from math import isclose

def condition_number_diagonal(a: float, b: float) -> float:
    if a <= 0.0 or b <= 0.0:
        raise ValueError("this example requires positive eigenvalues")
    return max(a, b) / min(a, b)

def scaled_condition(scale_x: float) -> float:
    # x = D z, D = diag(scale_x, 1), H = diag(100, 1).
    return condition_number_diagonal(100.0 * scale_x ** 2, 1.0)

if __name__ == "__main__":
    print("original condition number:", condition_number_diagonal(100.0, 1.0))
    for scale in (1.0, 0.5, 0.2, 0.1, 0.05):
        print(f"scale_x={scale:.2f} -> condition={scaled_condition(scale):.3f}")
    assert isclose(condition_number_diagonal(100.0, 1.0), 100.0)
    assert isclose(scaled_condition(0.1), 1.0)
    assert isclose(scaled_condition(0.2), 4.0)
