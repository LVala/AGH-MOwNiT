from utils import gen_points_equally, cubic_spline, quadratic_spline
from plotting import plot_from_func

import numpy as np

# function
k = 0.5
m = 4
left_end = -6
right_end = 6
f = lambda x: x**2 - m*np.cos((np.pi*x)/k)

for num_of_points in range(4,51):
    eql_x, eql_y = gen_points_equally(f, left_end, right_end, num_of_points)
    cubic = cubic_spline(eql_x, eql_y, 1)
    quadratic = quadratic_spline(eql_x, eql_y, 1)
    plot_from_func([f, cubic, quadratic], ["f", "cubic spline", "quadratic spline"], left_end, right_end, 2000, (eql_x, eql_y), f"{num_of_points} Points")

# cubic = quadratic_spline([1,2,3,4], [1,2,3,4], 1)