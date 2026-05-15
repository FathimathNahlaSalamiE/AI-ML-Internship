import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)
print(df)

print(df.groupby("Department")["Salary"].agg(["mean", "max", "min"]))
