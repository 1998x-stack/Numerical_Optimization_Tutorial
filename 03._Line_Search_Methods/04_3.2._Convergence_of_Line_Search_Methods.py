"""Illustrate why the angle lower bound matters in Zoutendijk's condition."""
def partial_sum_angle_bounded(n: int, delta: float) -> float:
    # cos(theta_k)=delta and ||g_k||=1/(k+1).
    return sum((delta ** 2) / ((k + 1) ** 2) for k in range(n))

def partial_sum_vanishing_angle(n: int) -> float:
    # ||g_k||=1 while cos(theta_k)=1/(k+1).
    return sum(1.0 / ((k + 1) ** 2) for k in range(n))

if __name__ == "__main__":
    n, delta = 100, 0.5
    bounded = partial_sum_angle_bounded(n, delta)
    vanishing = partial_sum_vanishing_angle(n)
    print("angle bounded: weighted sum =", bounded, "; gradient -> 0")
    print("angle vanishes: weighted sum =", vanishing, "; gradient stays 1")
    assert bounded < 1.0
    assert vanishing < 2.0
    assert abs(partial_sum_angle_bounded(n, delta) -
               delta ** 2 * partial_sum_vanishing_angle(n)) < 1e-12
