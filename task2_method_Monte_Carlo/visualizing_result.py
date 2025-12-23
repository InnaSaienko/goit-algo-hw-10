from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def visualizing_result(function: Callable[[float], float], a: float, b: float) -> None:
    """Plot function and shaded area"""

    x = np.linspace(a - 0.5, b + 0.5, 400) #  list of points on axis X
    y = function(x) # list of point on axis Y

    fig, ax = plt.subplots() # new canvas for drawing
    ax.plot(x, y, linewidth=2) #  draw a curve

    points_on_segment_a_b = np.linspace(a, b, 200) # 200 -> number of points to under curve area
    ax.fill_between(points_on_segment_a_b, function(points_on_segment_a_b), alpha=0.3) # alpha value used for blending

    ax.axvline(a, linestyle='dashed') #draw vertical lines on the integration limits [a, b]
    ax.axvline(b, linestyle='dashed')

    ax.grid()
    plt.show()