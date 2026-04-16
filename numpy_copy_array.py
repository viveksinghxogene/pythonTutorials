import numpy as np

a1 = np.arange(1, 10)
a2 = a1.copy()

print('a1:', a1)
print('a2:', a2)

a2[3] = 40

print('after modification')
print('a1:', a1)
print('a2:', a2)