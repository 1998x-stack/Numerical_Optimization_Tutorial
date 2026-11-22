"""Compare Q-linear, Q-superlinear and Q-quadratic error recurrences."""
def sequence(update, initial: float = 0.5, steps: int = 8):
    values = [initial]
    for _ in range(steps):
        values.append(update(values[-1]))
    return values

if __name__ == "__main__":
    linear = sequence(lambda e: 0.5 * e)
    superlinear = sequence(lambda e: e ** 1.5)
    quadratic = sequence(lambda e: e ** 2)
    print("k=4 errors:", linear[4], superlinear[4], quadratic[4])
    print("superlinear ratio:", superlinear[5] / superlinear[4])
    print("quadratic ratio:", quadratic[5] / (quadratic[4] ** 2))
    assert linear[4] == 0.03125
    assert superlinear[5] / superlinear[4] < superlinear[2] / superlinear[1]
    assert abs(quadratic[5] / (quadratic[4] ** 2) - 1.0) < 1e-12
