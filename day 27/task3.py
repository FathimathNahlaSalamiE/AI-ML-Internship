import pandas as pd

df = pd.read_csv("students.csv")

print(df)

print(df.head())

print(df.tail())

print(df.shape)

print(df["name"])

print(df[["name", "marks"]])
