import random

from typing import Callable


def monte_carlo_worker(function: Callable[[float], float], a: float, b: float, n: int) -> float:
    """Estimate integral using Monte Carlo method."""

    values = [function(random.uniform(a, b)) for _ in range(n)] # list random points between a and b
    estimate = (b - a) * sum(values) / n # average integral approximation
    return estimate
