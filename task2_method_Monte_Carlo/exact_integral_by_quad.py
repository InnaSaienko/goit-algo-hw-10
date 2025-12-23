from typing import Callable

import scipy.integrate as spi


def exact_integral(function: Callable[[float], float], a: float, b: float) -> float:
    """Compute exact integral value by quadrature rule"""

    result, _ = spi.quad(function, a, b)

    return result
