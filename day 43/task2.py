import pandas as pd
from sklearn.svm import SVC

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = SVC()

model.fit(X, y)

prediction = model.predict([[5]])

print("Prediction:", prediction)