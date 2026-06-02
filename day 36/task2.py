import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
result = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})
print(result)
score = model.score(X_test, y_test)
print("Accuracy:", score)