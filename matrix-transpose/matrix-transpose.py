import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A, dtype=float)
    new_col, new_row = A.shape
    result = np.zeros((new_row, new_col))
    for i in range(new_row):
        for j in range(new_col):
            result[i,j] = A[j, i]
    return result
    
