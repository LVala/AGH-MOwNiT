import numpy as np

def jacobi_method(A: np.ndarray, B: np.ndarray, X: np.ndarray, mode: int, eps: float):
    # matrix A must be diagonal dominant
    D = np.diag(A)
    R = A - np.diagflat(D)
    iter_num = 0
    while True:
        X_new = (B - (R @ X)) / D
        iter_num += 1;
        if mode == 1:
            if np.linalg.norm(X_new - X) < eps:
                return X_new, iter_num
        else:
            if np.linalg.norm(A @ X_new - B) < eps:
                return X_new, iter_num
        X = X_new

def get_spectral_radius(A: np.ndarray):
    D = np.diag(A)
    R = A - np.diagflat(D)
    S = R / D
    eigvals = np.linalg.eigvals(S)
    return max(abs(i) for i in eigvals)

def jacobi_2(A: np.ndarray, B: np.ndarray, X: np.ndarray, mode: int, eps: float):
    n = len(X)
    iter_num = 0
    while True:
        X_old = np.copy(X)
        for i in range(n):
            cos = 0
            for j in range(n):
                if i != j:
                    cos += A[i,j]*X[j]

            X[i] = (B[i]-cos)/A[i,i]

        iter_num += 1;
        if mode == 1:
            if np.linalg.norm(X_old - X) < eps:
                return X, iter_num
        else:
            if np.linalg.norm(A @ X - B) < eps:
                return X, iter_num
