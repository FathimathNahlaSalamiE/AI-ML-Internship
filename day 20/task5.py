import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr[:, 1:3])

arr2 = np.array([10, 20, 30, 40, 50])
print(arr2[::2])  # [10, 30, 50]

