import numpy as np

# Datatypes
# https://numpy.org/devdocs/user/basics.types.html

x = np.array([1, 2])
print(x.dtype)
x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1, 2], dtype=np.int64) # 8 bytes
print(x.dtype)

x = np.array([1, 2], dtype=np.float32) # 4 bytes
print(x.dtype)
