from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def plot_from_array(array_x: list[float], array_y: list[list[float]], names: list[str]) -> None:
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    plt.xlabel("y")
    plt.ylabel("x")

    for arr, name, mcolor in zip(array_y, names, mcolors.BASE_COLORS.keys()):
        ax.plot(array_x, arr, color=mcolor, label=name,)
        ax.legend()

    plt.show()
