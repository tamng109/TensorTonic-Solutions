import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x, y = np.array(x,dtype=float), np.array(y, dtype=float)
    result = np.sum(np.abs(x - y))
    return result