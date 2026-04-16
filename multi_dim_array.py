import numpy as np

a1 = np.array([1, 2, 3, 4, 5, 6])
a2 = np.array([[1, 2, 3], [4, 5, 6]])
a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

a2.shape = (3, 2)

print(a2)

print(a1.size)
print(a2.size)
print(a3.size)

print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)