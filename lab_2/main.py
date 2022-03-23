import numpy as np

from utils import gen_points_chebyshev, gen_points_equally, newton_intpol, lagrange_intpol
from plotting import plot_from_func

def get_accuracy_sqr(func1, func2, left_end, right_end, points):
    prod = 0
    array = np.linspace(left_end, right_end, points)
    for i in array:
        prod += (func1(i) - func2(i))**2
    return prod

def get_accuracy_abs(func1, func2, left_end, right_end, points):
    prod = 0
    array = np.linspace(left_end, right_end, points)
    for i in array:
        prod += abs(func1(i) - func2(i))
    return prod


f = lambda x: x**2 - 4*np.cos((np.pi*x)/0.5)
left_end = -6
right_end = 6

num_of_points = 50

cheb_x, cheb_y = gen_points_chebyshev(f, left_end, right_end, num_of_points)
eql_x, eql_y = gen_points_equally(f, left_end, right_end, num_of_points)

newt_cheb = newton_intpol(cheb_x, cheb_y)
newt_eql = newton_intpol(eql_x, eql_y)
lagr_cheb = lagrange_intpol(cheb_x, cheb_y)
lagr_eql = lagrange_intpol(eql_x, eql_y)

print("ACCURACY CHEB", get_accuracy_sqr(f, newt_cheb, left_end, right_end, 1000))
print("ACCURACY EQL", get_accuracy_sqr(f, newt_eql, left_end, right_end, 1000))


# plot_from_func([f, newt_cheb, newt_eql], ["f", "newton chebyshev", "newton equally"], left_end, right_end, 2000, [(cheb_x, cheb_y), (eql_x, eql_y)])
plot_from_func([f, lagr_cheb], ["f", "lagrange chebyshev"], left_end, right_end, 2000, [(cheb_x, cheb_y), (eql_x, eql_y)])


best_poly = 1
best_poly_acc = float('inf')
# for i in range(1, 100):
#     x, y = gen_points_chebyshev(f, left_end, right_end, i)
#     newt = newton_intpol(x, y)
#     acc = get_accuracy_sqr(f, newt, left_end, right_end, 10000)
#     if (acc < best_poly_acc):
#         best_poly = i
#         best_poly_acc = acc

print(best_poly)
best_x, best_y = gen_points_chebyshev(f, left_end, right_end, 40)
best_newt = lagrange_intpol(best_x, best_y)
# plot_from_func([best_newt], [f"najlepszy newton, dla {best_poly} pkt"], left_end, right_end, 2000)