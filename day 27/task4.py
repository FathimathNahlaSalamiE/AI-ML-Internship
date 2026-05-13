import pandas as pd

df = pd.read_csv("students.csv")

print(df)

print(df.loc[0])

print(df.iloc[1])

print(df.loc[0, "name"])

print(df.iloc[1, 2])

print(df[0:2])

print(df.loc[:, ["name", "city"]])
