"""Compare a deterministic forecast with a finite-scenario stochastic objective.

Uses the exact three equally likely scenarios (1, 2, 4); no external solver.
"""
from math import isclose
from random import Random

SCENARIOS = (1.0, 2.0, 4.0)

def loss(x: float, demand: float) -> float:
    return (x - demand) ** 2

def scenario_risk(x: float) -> float:
    return sum(loss(x, d) for d in SCENARIOS) / len(SCENARIOS)

def monte_carlo_mean(seed: int = 2026, size: int = 1000) -> float:
    rng = Random(seed)
    return sum(rng.choice(SCENARIOS) for _ in range(size)) / size

if __name__ == "__main__":
    deterministic = 2.0
    stochastic = sum(SCENARIOS) / len(SCENARIOS)
    theoretical_risk = 14.0 / 9.0
    print(f"fixed forecast decision: {deterministic:.6f}")
    print(f"mean-squared-loss decision: {stochastic:.6f}")
    print(f"minimum scenario risk: {scenario_risk(stochastic):.6f}")
    print(f"fixed-seed Monte Carlo sample mean: {monte_carlo_mean():.6f}")
    assert isclose(stochastic, 7.0 / 3.0)
    assert isclose(scenario_risk(stochastic), theoretical_risk)
    assert scenario_risk(stochastic) <= scenario_risk(deterministic)
    assert scenario_risk(stochastic) <= scenario_risk(stochastic + 0.5)
    assert 1.0 <= monte_carlo_mean() <= 4.0
