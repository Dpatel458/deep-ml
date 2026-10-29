import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.

    Args:
        A: Square matrix as a list of lists

    Returns:
        tuple: (L, U) where L is lower triangular with 1s on diagonal,
               U is upper triangular, and A = L @ U
    """
    a = np.asarray(A, dtype=float)
    n = a.shape[0]

    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        # Calculate elements of U
        for j in range(i, n):
            U[i, j] = a[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

        # Calculate elements of L
        for j in range(i + 1, n):
            if U[i, i] == 0:
                raise ValueError("LU decomposition cannot proceed with a zero pivot.")

            L[j, i] = (a[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

    return L,U
