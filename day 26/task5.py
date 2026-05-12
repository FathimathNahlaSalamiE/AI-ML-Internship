import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)

print(df.head())

print(df.tail())

print(df.info())