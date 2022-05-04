from cProfile import label
from typing import Callable

def secant_roots(f: Callable[[float], float], a: int, b: int, epsilon: int, max_iter: int) -> float:
    for _ in range(max_iter):
        if not f(a)*f(b) < 0:
            print("Error: points take the same sign")
            exit(1)
        a, b = b, (f(b)*a - f(a)*b)/(f(b)-f(a))
        if abs(b) < epsilon: return b

    print("Error: maxiumu number of iterations exceeded")
    return None

def newton_roots(f: Callable[[float], float], d_f: Callable[[float], float], x: int, epsilon: int, max_iter: int) -> float:
    for _ in range(max_iter):
        x = x - f(x)/d_f(x)
        if abs(x) < epsilon: return x

    print("Error: maxiumu number of iterations exceeded")
    return None
