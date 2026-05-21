import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}
df = pd.DataFrame(data)
sns.scatterplot(x="StudyHours", y="Marks", data=df)
plt.show()