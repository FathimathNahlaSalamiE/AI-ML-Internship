import numpy as np


arr = np.array([[1, 2], [3, 4]])
print(np.sum(arr, axis=0))  #column wise
print(np.sum(arr, axis=1))  #row wise

# arr = np.array([10, 20, 30])
# print(arr > 15)
# print(arr[arr > 15])