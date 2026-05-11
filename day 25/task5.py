import numpy as np

arr = np.arange(12)

arr2d = arr.reshape(3, 4)
print(arr2d)

arr1d = arr2d.reshape(-1)
print(arr1d)

arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr3d)
print(arr3d.shape)