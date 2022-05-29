from utils import jacobi_method, get_spectral_radius
import numpy as np
import time

k = 8
m = 3

for n in range(3,101):
    print(f"{n}", end=" & ")
    for index, prec in enumerate([0.01, 0.001, 0.0001, 0.00001, 0.000001]):
        A = np.array([[k if i == j else 1/(abs(i-j)+m) for i in range(1,n+1)] for j in range(1,n+1)])
        X_known = np.array([1 if i%2==0 else -1 for i in range(n)])
        B = A @ X_known
        X_start = np.array([0 for _ in range(n)])
        start = time.time()
        X, iters = jacobi_method(A, B, X_start, 2, prec)
        stop = time.time()
        calc_time = stop-start
        norm = np.linalg.norm(X_known-X)
        if prec != 0.000001:
            print(f"{norm:.5e}", end=" & ")  # error
            # print(f"{calc_time:.7f}", end=" & ")  # time
            # print(f"{iters}", end=" & ")  # iterations
        else: 
            print(f"{norm:.5e}", end=" \\\\ \\hline\n")  # error
            # print(f"{calc_time:.7f}", end=" \\\\ \\hline\n")  # time
            # print(f"{iters}", end=" \\\\ \\hline\n")  # iterations
