import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x_arr = np.array(x, dtype=float)
    result = (np.exp(x_arr)- np.exp(-x_arr))/(np.exp(x_arr) + np.exp(-x_arr))
    return result