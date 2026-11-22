"""Show floating-point step stagnation at increasing magnitude."""
import math
import sys

def probe(power: int):
    if not 0 <= power <= 18:
        raise ValueError("power out of teaching range")
    x = float(10 ** power)
    proposed_step = 1.0
    new_x = x + proposed_step
    return x, new_x, new_x == x, math.ulp(x)

if __name__ == "__main__":
    for n in (12, 14, 15, 16, 17):
        x, y, stuck, ulp = probe(n)
        print(f"10^{n}: x+1==x -> {stuck}, ULP={ulp}")
        assert math.isfinite(y)
    assert probe(12)[2] is False
    assert probe(16)[2] is True
    assert probe(17)[3] > probe(12)[3]
    assert sys.float_info.radix == 2
