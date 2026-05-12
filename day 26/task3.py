import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)

data["Age"] = [19,19,20]
df = pd.DataFrame(data)
print(df)
