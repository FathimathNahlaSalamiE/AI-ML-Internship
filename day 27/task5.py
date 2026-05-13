
import pandas as pd

df = pd.read_csv("students.csv")

print(df)

print(df[df["marks"] > 80])

print(df[df['city'] == 'kollam'])

print([(df['marks'] > 80) & (df['city'] == 'Mumbai')])