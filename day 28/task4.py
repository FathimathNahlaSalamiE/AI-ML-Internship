import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}

df = pd.DataFrame(data)

print(df)

print(df.fillna("Unknown"))

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)
