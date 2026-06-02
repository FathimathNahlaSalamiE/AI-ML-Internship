import pandas as pd

from sklearn.linear_model import LogisticRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)
X = df[["Hours"]]
y = df["Result"]
model = LogisticRegression()
model.fit(X, y)
prediction = model.predict([[5]])
print(prediction)
prediction = model.predict([[2], [4], [7]])
print(prediction)

a=model.predict_proba([[5]])
print(a)