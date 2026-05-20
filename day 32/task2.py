import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
sns.lineplot(x=x, y=y)
plt.show()

sns.set_style("darkgrid")
sns.lineplot(x=x, y=y)
plt.show()