from math import exp
from utils import *

left_end = 0.1
right_end = 1.9
n = 9
m = 25
f = lambda x: m*x*exp(-n) - m*exp(-n*x) + 1/m
d_f = lambda x: m*exp(-n) + n*m*exp(-n*x)
# h = 0.00001
# d_f = lambda x: (f(x+h) - f(x))/h

prec = 0.1

# Newton
# end = left_end
# while end < right_end:
#     print(f"[{end:.2f}, {right_end:.2f}]", end=" & ")
#     for prec in [0.01, 0.001, 0.0001, 0.00001, 0.000001]:
#         x1, iters1 = secant_roots(f, end, right_end, prec, 1)
#         x2, iters2 = secant_roots(f, end, right_end, prec, 2)
#         if prec != 0.000001:
#             print(f"{x2}", end=" & ")
#         else:
#             print(f"{x2}", end=" \\\\ \\hline\n")
#     end += 0.1

def F(X):
    ret = [0,0,0]
    ret[0] = X[0]**2 + X[1]**2 - X[2]**2 - 1
    ret[1] = X[0] - 2*(X[1]**3) + 2*(X[2]**2) + 1
    ret[2] = 2*(X[0]**2) + X[1] - 2*(X[2]**2) - 1
    return ret 

def J(X):
    ret = [[2*X[0],  2*X[1],       -2*X[2]], 
           [1,      -6*(X[1]**2),  4*X[2] ], 
           [4*X[0],  1,            -4*X[2]]]
    return ret

A = newton_matrix(F, J, [2, 2, 2], 0.01, 1)
print(F(A[0]))

for end1 in [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]:
    for end2 in [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]:
        for end3 in [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]:
            print(f"{end1:.2f}, {end2:.2f}, {end3:.2f}", end=" & ")
            for prec in [0.000001]:   #[0.01, 0.001, 0.0001, 0.00001, 0.000001]:
                x1, iters1 = newton_matrix(F, J, [end1, end2, end3], prec, 1)
                x2, iters2 = newton_matrix(F, J, [end1, end2, end3], prec, 2)
                if prec != 0.000001:
                    print(f"{x1}", end=" & ")
                else:
                    print(f"{x1}", end=" \\\\ \\hline\n")