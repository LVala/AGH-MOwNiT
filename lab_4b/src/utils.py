from typing import Callable

import numpy as np

# Horner algorithm for polynomial in Newton form
def horner_newton(x_array: list[float], b_array: list[float], arg: float) -> float:
    # len(b_array) == n + 1
    prod = b_array[len(b_array)-1]  # n'th elemen
    for i in range(len(b_array)-2, -1, -1):
        prod = prod*(arg - x_array[i]) + b_array[i]
    return prod

# functions generating points (equally distributed or distributed based on Chebyshev nodes)
def gen_points_equally(func: Callable[[float], float], left_end: int, right_end: int, num_of_points: int) -> tuple[list[float], list[float]]:
    array_x = np.linspace(left_end, right_end, num_of_points)
    array_y = [func(i) for i in array_x]
    return array_x.tolist(), array_y

# accuracy calculation
def get_accuracy_sqr(func1: Callable[[float], float], func2: Callable[[float], float], left_end: int, right_end: int, points: int) -> float:
    prod = 0
    array = np.linspace(left_end, right_end, points)
    for i in array:
        prod += (func1(i) - func2(i))**2
    return prod/points

def get_accuracy_abs(func1: Callable[[float], float], func2: Callable[[float], float], left_end: int, right_end: int, points: int) -> float:
    prod = 0
    array = np.linspace(left_end, right_end, points)
    for i in array:
        temp = abs(func1(i) - func2(i))
        prod = max(prod, temp)
    return prod

# algebraic polynomial approximation
def trigpoly_approx(x_array: list[float], y_array: list[float], w_array: list[float], m: int) -> Callable[[float], float]:
    

    def func(x):
        return 1

    return func