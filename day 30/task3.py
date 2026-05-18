import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y, linestyle="--", marker="o")
plt.show()

plt.plot(x, y, label="Marks")
plt.legend()
plt.grid()
plt.show()