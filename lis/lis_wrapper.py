import ctypes
import numpy as np
import os
import glob
import sys
import platform

# Get the directory of the current file
file_dir = os.path.dirname(os.path.abspath(__file__))

# Attempt to dynamically find the .so file compiled for the current Python version
python_tag = f"cpython-{sys.version_info.major}{sys.version_info.minor}"
machine = platform.machine().lower()

# Wildcard pattern to match expected .so file format
pattern = os.path.join(file_dir, f"_liblis.{python_tag}*.so")
matches = glob.glob(pattern)

if not matches:
    # Fallback: just grab any .so file (in case exact match not found)
    matches = glob.glob(os.path.join(file_dir, "_liblis*.so"))
    if not matches:
        raise FileNotFoundError(f"No suitable shared object (.so) file found in {file_dir}")

so_file = matches[0]  # use the first match

# Load the shared object file
_liblis = ctypes.CDLL(so_file)

# Define function prototypes
_liblis.longestIncreasingSubsequence.restype = ctypes.POINTER(ctypes.c_int)
_liblis.longestIncreasingSubsequence.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32), ctypes.c_int]

def longestIncreasingSubsequence(X):
    # Convert Python list to NumPy array
    X_np = np.array(X, dtype=np.int32)
    N = len(X)
    L = ctypes.c_int()
    
    # Call the C/C++ function
    result_ptr = _liblis.longestIncreasingSubsequence(X_np, N, ctypes.byref(L))
    
    # Convert the result from C pointer to Python list
    result = [result_ptr[i] for i in range(L.value)]
    
    # Free the memory allocated in C/C++ side
    _liblis.free(result_ptr)
    
    return result

# Expose the function under the lis module
lis = {
    'longestIncreasingSubsequence': longestIncreasingSubsequence
}
