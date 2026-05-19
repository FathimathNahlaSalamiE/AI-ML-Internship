import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]
plt.plot(x, y1)
plt.savefig("graph.png")

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Graph 1")
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Graph 2")
plt.savefig("subplot.png")

data = [10, 20, 20, 30, 40, 40, 40]
plt.hist(data)
plt.savefig("data.png")



