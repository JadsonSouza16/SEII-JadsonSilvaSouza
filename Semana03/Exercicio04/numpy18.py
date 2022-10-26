import numpy as np

data = np.loadtxt('FILE_NAME', delimiter=",",dtype=np.float32)
print(data.shape, data.dtype)

data = np.genfromtxt('FILE_NAME', delimiter=",", dtype=np.float32)
print(data.shape)
