import numpy as np

def jacobi_method(A: np.ndarray, B: np.ndarray, X: np.ndarray, mode: int, eps: float):
    # matrix A must be diagonal dominant
    D_inv = np.linalg.inv(np.diag(A))

    while True:
        X_new = X + D_inv @ (B - (A @ X))
        if mode == 1:
            if np.linalg.norm(X_new - X) < eps:
                return X_new
        else:
            if np.linalg.norm(A @ X_new - B) < eps:
                return X_new
        X = X_new

    return X