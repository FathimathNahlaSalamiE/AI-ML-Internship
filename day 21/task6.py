import numpy as np



arr = np.array([1, 2, 3, 4])
print(np.split(arr, 2))

matrix = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

rows_split = np.split(matrix, 2, axis=0)
print(rows_split)