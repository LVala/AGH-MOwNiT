from utils import gen_points_equally, get_accuracy_abs, get_accuracy_sqr, trigpoly_approx
from plotting import plot_from_func

import numpy as np

# function
k = 0.5
m = 4
left_end = -6
right_end = 6
f = lambda x: x**2 - m*np.cos((np.pi*x)/k)

for num_of_points in range(51,60):
    eql_x, eql_y = gen_points_equally(f, left_end, right_end, num_of_points)
    weights = [1]*num_of_points
    degree = 20
    tri = trigpoly_approx(eql_x, eql_y, weights, degree)

    plot_from_func([f, tri], ["f", "approximation with trigonometric polynomials of 20th degree"], left_end, right_end, 2000, (eql_x, eql_y), f"{num_of_points} Points")
    # print(f"{num_of_points} points | SQR = {get_accuracy_sqr(f, tri, left_end, right_end, 1000):.3f}, ABS = {get_accuracy_abs(f, tri, left_end, right_end, 1000):.3f}")