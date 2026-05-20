import seaborn as sns
import matplotlib.pyplot as plt

students = ["A", "B", "C"]
marks = [85, 90, 78]
sns.barplot(x=students, y=marks)
plt.show()

