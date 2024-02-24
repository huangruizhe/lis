import ctypes
import numpy as np

# Load the shared library
_liblis = ctypes.CDLL('./liblis.so')  # Change the path if necessary

# Define function prototypes
_liblis.longestIncreasingSubsequence.restype = ctypes.POINTER(ctypes.c_int)
_liblis.longestIncreasingSubsequence.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32), ctypes.c_int]

def longest_increasing_subsequence(X):
    # Convert Python list to NumPy array
    X_np = np.array(X, dtype=np.int32)
    N = len(X)
    
    # Call the C/C++ function
    result_ptr = _liblis.longestIncreasingSubsequence(X_np, N)
    
    # Convert the result from C pointer to Python list
    result = [result_ptr[i] for i in range(N)]
    
    # Free the memory allocated in C/C++ side
    _liblis.free(result_ptr)
    
    return result