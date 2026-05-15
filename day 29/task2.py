import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

print(df)

print(df.sort_values("Salary"))

print(df.sort_values("Salary", ascending=False))

print(df.sort_values(["Department", "Salary"]))
