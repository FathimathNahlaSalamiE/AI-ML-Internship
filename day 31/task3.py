import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]

plt.figure(figsize=(8, 5))
plt.plot(x, y1)
plt.title("Custom Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()
