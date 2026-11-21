"""Classify stationary points with exact 2x2 Hessian eigenvalues.

A Hessian test is a local test. A semidefinite Hessian alone is inconclusive.
"""
from math import sqrt, isclose

def eigenvalues_symmetric_2x2(a: float, b: float, c: float) -> tuple[float, float]:
    """Eigenvalues of [[a,b],[b,c]], returned in ascending order."""
    radius = sqrt((a - c) ** 2 + 4.0 * b ** 2)
    return ((a + c - radius) / 2.0, (a + c + radius) / 2.0)

def classify_hessian(a: float, b: float, c: float, tol: float = 1e-10) -> str:
    lo, hi = eigenvalues_symmetric_2x2(a, b, c)
    if lo > tol:
        return "positive definite: strict local minimum is certified"
    if hi < -tol:
        return "negative definite: strict local maximum is certified"
    if lo < -tol and hi > tol:
        return "indefinite: saddle point is certified"
    return "semidefinite or nearly singular: second-order test is inconclusive"

if __name__ == "__main__":
    cases = {
        "x^2+y^2": (2.0, 0.0, 2.0),
        "x^4+y^2 at the origin": (0.0, 0.0, 2.0),
        "x^2-y^2": (2.0, 0.0, -2.0),
        "-x^2-y^2": (-2.0, 0.0, -2.0),
    }
    for name, hessian in cases.items():
        print(name, "->", classify_hessian(*hessian))
    assert classify_hessian(2.0, 0.0, 2.0).startswith("positive definite")
    assert classify_hessian(0.0, 0.0, 2.0).startswith("semidefinite")
    assert classify_hessian(2.0, 0.0, -2.0).startswith("indefinite")
    assert classify_hessian(-2.0, 0.0, -2.0).startswith("negative definite")
    assert isclose(eigenvalues_symmetric_2x2(2.0, 1.0, 2.0)[0], 1.0)
