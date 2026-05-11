import numpy as np

marks = np.array([
    [85, 78, 90],
    [70, 88, 60],
    [95, 92, 89]
])

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

total = np.sum(marks, axis=1)
print(total)
top_student = np.argmax(total)
print("Top Student Index:", top_student)
