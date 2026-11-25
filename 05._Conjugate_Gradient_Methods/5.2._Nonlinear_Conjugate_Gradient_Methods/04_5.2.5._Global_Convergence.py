"""Zoutendijk implication: the angle bound decides whether the sum stays finite."""
import math
from fractions import Fraction

def series(angle2, grad2, n):
    return sum(angle2(k) * grad2(k) for k in range(1, n + 1))

if __name__ == "__main__":
    n = 1000
    vanish = series(lambda k: Fraction(1, 4), lambda k: Fraction(9, 10)**(2*k), n)
    limit = Fraction(81, 76)
    assert vanish < limit
    flat = series(lambda k: Fraction(1, 4), lambda k: Fraction(1), n)
    assert flat == Fraction(n, 4)
    slow = series(lambda k: Fraction(1, k), lambda k: Fraction(1), n)
    assert math.log(n + 1) < float(slow) < 1 + math.log(n)
    print("vanishing gradient sum", round(float(vanish), 4), "< limit", float(limit))
    print("flat gradient sum", int(flat), "| slowly-vanishing angle sum", round(float(slow), 4))
