import pandas as pd 
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}
df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print("Predicted Marks:", prediction)