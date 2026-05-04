import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr[0, 1])   # 2
print(arr[1, 2])   # 6
print(arr[0])   # First row
print(arr[1])   # Second row
print(arr[:, 1])  # all columns