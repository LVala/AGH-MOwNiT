import numpy as np

def gaussian_elimination(A: np.ndarray, B: np.ndarray):
    n = np.shape(A)[0]
    if np.shape(B)[0] != n:
        print("Invalid B vector size")
        exit(1)
    
    C = np.hstack([A, B.reshape((n,1))]).astype(np.float64)

    for i in range(n):
        pivot = C[i, i]
        for j in range(i+1, n):
            base = C[j, i] / pivot          
            C[j] = C[j] - (base * C[i])

    X = C[:, n]
    X[n-1] /= C[n-1, n-1]
    for i in range(n-2, -1, -1):
        pivot = C[i,i]
        X[i] -= (C[i, i+1:n] * X[i+1:n]).sum()
        X[i] /= pivot

    return X
