import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr + 100)
print(arr * 100)
print((arr - arr.min()) / (arr.max() - arr.min()))