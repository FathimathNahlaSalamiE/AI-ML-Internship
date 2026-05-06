import numpy as np

arr = np.array([10, 20, 30, 40])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))


arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

print(np.argmax(arr))
print(np.argmin(arr))

arr = np.array([1, 2, 3, 4])

print(np.cumsum(arr))