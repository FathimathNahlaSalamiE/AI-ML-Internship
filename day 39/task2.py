import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)
X = df[["Hours"]]
y = df["Result"]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
prediction = model.predict([[4]])
print(prediction)
prediction = model.predict([[2], [4], [8]])
print(prediction)