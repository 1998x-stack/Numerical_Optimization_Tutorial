"""Compare no-fill preconditioners on the 1D Laplacian via closed-form spectra."""
from math import cos, pi, tan

def laplacian_eigs(n):
    return [2 - 2*cos(k*pi/(n + 1)) for k in range(1, n + 1)]

def condition(eigs):
    return max(eigs) / min(eigs)

if __name__ == "__main__":
    n = 10
    eigs = laplacian_eigs(n)
    kappa_q = condition(eigs)
    # Jacobi: M = 2I, so M^{-1}Q = Q/2 and the condition number is unchanged.
    kappa_jacobi = condition([e/2 for e in eigs])
    # Exact tridiagonal factorization keeps the pattern, so M = Q and kappa = 1.
    kappa_exact = 1.0
    assert abs(kappa_q - 1/tan(pi/(2*(n + 1)))**2) < 1e-9
    assert abs(kappa_jacobi - kappa_q) < 1e-9
    assert kappa_exact == 1.0
    print("kappa(Q) =", round(kappa_q, 4), "| Jacobi =", round(kappa_jacobi, 4), "| exact =", kappa_exact)
