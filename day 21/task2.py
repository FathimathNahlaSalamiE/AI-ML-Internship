import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped1 = arr.reshape(2, 3)
print(reshaped1)

reshaped2 = arr.reshape(1, 2, 3)
print(reshaped2)

reshaped3 = arr.reshape(2,3,3)