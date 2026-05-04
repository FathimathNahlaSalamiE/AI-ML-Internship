import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr[arr > 25])
print(arr[(arr > 10) & (arr < 40)])
arr[arr>25] = 100
print(arr)