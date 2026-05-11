import numpy as np

image = np.array([
    [50, 100],
    [150, 200]
])
bright = image + 50
print(bright)

dark = image - 50
print(dark)

normalized = image / np.max(image)
print(normalized)
