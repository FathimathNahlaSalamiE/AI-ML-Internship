import pandas as pd

data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}
df = pd.DataFrame(data)
print(df)
print(df.corr())
