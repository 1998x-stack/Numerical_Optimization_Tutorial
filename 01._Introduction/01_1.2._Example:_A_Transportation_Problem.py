"""Enumerate a small integer transportation instance.

The algebraic argument in the article proves the continuous LP optimum.
This finite enumeration independently checks the displayed integral plan.
"""
SUPPLY = (35, 25)
DEMAND = (20, 25, 15)
COST = ((4, 6, 8), (5, 4, 3))


def best_integer_plan():
    best = None
    for ax in range(DEMAND[0] + 1):
        for ay in range(DEMAND[1] + 1):
            az = SUPPLY[0] - ax - ay
            if not 0 <= az <= DEMAND[2]:
                continue

            bx = DEMAND[0] - ax
            by = DEMAND[1] - ay
            bz = DEMAND[2] - az
            if min(bx, by, bz) < 0 or bx + by + bz != SUPPLY[1]:
                continue

            plan = ((ax, ay, az), (bx, by, bz))
            cost = sum(plan[i][j] * COST[i][j]
                       for i in range(2) for j in range(3))
            if best is None or cost < best[0]:
                best = (cost, plan)
    return best


if __name__ == "__main__":
    cost, plan = best_integer_plan()
    print("minimum cost:", cost)
    print("factory A:", plan[0])
    print("factory B:", plan[1])
    assert cost == 255
    assert plan == ((20, 15, 0), (0, 10, 15))
    assert sum(plan[0]) == SUPPLY[0]
    assert sum(plan[1]) == SUPPLY[1]
    assert tuple(plan[0][j] + plan[1][j] for j in range(3)) == DEMAND
