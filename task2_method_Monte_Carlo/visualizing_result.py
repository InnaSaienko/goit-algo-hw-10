from typing import Callable, Union

import matplotlib.pyplot as plt
import numpy as np


def visualizing_result(function: Callable[[Union[float, np.ndarray]], np.ndarray], a: float, b: float, number_points: int) -> None:
    """Plot function and points"""

    x_inside, y_inside = [], []  # points under curve
    x_outside, y_outside = [], []  # points above curve
    y_max = np.max(function(np.linspace(a, b, 400))) # limiting the vertical range of random points

    for _ in range(number_points):
        x = np.random.uniform(a, b)
        y = np.random.uniform(0, y_max)
        if y <= function(x):
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    fig, ax = plt.subplots()

    # Create plot curve
    x_line = np.linspace(a, b, 400)
    y_line = function(x_line)
    ax.plot(x_line, y_line, color="blue", linewidth=2, label="f(x)")


    # Draw points
    ax.scatter(x_inside, y_inside, color="green", s=10, label="Points below curve")
    ax.scatter(x_outside, y_outside, color="red", s=10, label="Points above curve")

    ax.legend()
    print(f"Points below curve: {len(x_inside)}, above curve: {len(x_outside)}")
    plt.show()
