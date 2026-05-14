import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Anu", "Arjun", None,'Rahul'],
    "Marks": [85, np.nan, 78, 90,85],
    "City": ["Kochi", "Trivandrum", None, "Kollam",'Kochi']
}

df = pd.DataFrame(data)

print(df)


print(df.duplicated())

print(df.drop_duplicates())

