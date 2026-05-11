import numpy as np

arr = np.array([10, 25, 30, 5, 60])
filtered = arr[arr > 20]
print(filtered)

replaced = np.where(arr < 20, 0, arr)
print(replaced)

count = np.sum(arr > 20)
print(count)