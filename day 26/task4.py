import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)

print(df["Name"])

print(df[["Name", "Marks"]])

print(df.head())