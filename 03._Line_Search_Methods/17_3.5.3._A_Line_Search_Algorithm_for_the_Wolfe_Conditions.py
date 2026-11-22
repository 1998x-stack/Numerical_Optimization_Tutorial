"""Strong Wolfe search with safeguarded bisection-based zoom."""
def phi(a):
    return (a - 2.0) ** 2

def dphi(a):
    return 2.0 * (a - 2.0)

def wolfe_search(initial=4.0, c1=1e-4, c2=0.1, maximum=16.0):
    if not (0.0 < c1 < c2 < 1.0 and 0.0 < initial < maximum):
        raise ValueError("invalid Wolfe parameters or step bound")
    f0, g0 = phi(0.0), dphi(0.0)
    if g0 >= 0.0:
        raise ValueError("direction is not descending")
    trace = []
    def sufficient(a):
        return phi(a) <= f0 + c1 * a * g0
    def zoom(lo, hi):
        for _ in range(60):
            a = (lo + hi) / 2.0
            trace.append(("zoom", a))
            if abs(hi - lo) < 1e-12:
                raise RuntimeError("zoom stagnated")
            if not sufficient(a) or phi(a) >= phi(lo):
                hi = a
            else:
                ga = dphi(a)
                if abs(ga) <= -c2 * g0:
                    return a, trace
                if ga * (hi - lo) >= 0.0:
                    hi = lo
                lo = a
        raise RuntimeError("zoom iteration limit")
    prev, a = 0.0, initial
    for i in range(60):
        trace.append(("expand", a))
        if not sufficient(a) or (i > 0 and phi(a) >= phi(prev)):
            return zoom(prev, a)
        ga = dphi(a)
        if abs(ga) <= -c2 * g0:
            return a, trace
        if ga >= 0.0:
            return zoom(a, prev)
        prev, a = a, min(2.0 * a, maximum)
        if a == prev:
            raise RuntimeError("maximum step reached")
    raise RuntimeError("search iteration limit")

if __name__ == "__main__":
    for start in (0.5, 1.0, 3.0, 4.0):
        alpha, history = wolfe_search(initial=start)
        print(start, alpha, history)
        assert phi(alpha) <= phi(0) + 1e-4 * alpha * dphi(0)
        assert abs(dphi(alpha)) <= 0.1 * abs(dphi(0))
    assert wolfe_search(4.0)[0] == 2.0
    assert wolfe_search(0.5)[0] == 2.0
