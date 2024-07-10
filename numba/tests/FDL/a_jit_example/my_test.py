import numpy as np
import numba
from numba import jit
import sys
print(numba.__version__)
print(sys.version)

@jit(nopython=True)
def go_fast(a): # Function is compiled to machine code when called the first time
    trace = 0.0
    # assuming square input matrix
    for i in range(a.shape[0]):   # Numba likes loops
        trace += np.tanh(a[i, i]) # Numba likes NumPy functions
    return a + trace              # Numba likes NumPy broadcasting


x = np.arange(100).reshape(10, 10)
go_fast(x)
