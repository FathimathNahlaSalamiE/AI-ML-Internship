import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000],
    "City": ["A","B","C","D"],
    "Category": [1,2,3,4]
}

df = pd.DataFrame(data)

print(df)

print(df.groupby("Department"))
print(df.groupby("City"))
print(df.groupby("Category"))
