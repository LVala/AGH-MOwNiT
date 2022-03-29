import numpy as np

from utils import gen_points_chebyshev, gen_points_equally, newton_intpol, lagrange_intpol, get_accuracy_sqr, get_accuracy_abs
from plotting import plot_from_func

# function
k = 0.5
m = 4
left_end = -6
right_end = 6
f = lambda x: x**2 - m*np.cos((np.pi*x)/k)
