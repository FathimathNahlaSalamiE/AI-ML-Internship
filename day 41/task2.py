import pandas as pd

from sklearn.ensemble import RandomForestClassifier

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = RandomForestClassifier(n_estimators=45)

model.fit(X, y)

prediction = model.predict([[4]])
print(prediction)

prediction = model.predict([[2], [5], [8]])
print(prediction)