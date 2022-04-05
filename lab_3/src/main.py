from utils import gen_points_equally, gen_points_chebyshev, cubic_spline
from plotting import plot_from_func

import numpy as np

# function
k = 0.5
m = 4
left_end = -6
right_end = 6
f = lambda x: x**2 - m*np.cos((np.pi*x)/k)

num_of_points = 50

eql_x, eql_y = gen_points_equally(f, left_end, right_end, num_of_points)
cheb_x, cheb_y = gen_points_chebyshev(f, left_end, right_end, num_of_points)

cubic = cubic_spline(eql_x, eql_y, 1)

plot_from_func([f, cubic], ["f", "cubic spline"], left_end, right_end, 2000, [(cheb_x, cheb_y), (eql_x, eql_y)], f"{num_of_points} Points")