import numpy as np

colors = ["red", "blue", "green"]
print(np.random.choice(colors))

print(np.random.choice(colors, size=5))

names = ['riya','miya','george']
print(np.random.choice(names,size=(3, 3)))