import pandas as pd
from sklearn.linear_model import LinearRegression

student = {
    'id':[101,102,103],
    'mark':[80,70,80]
}
df = pd.DataFrame(student)
X=df[['id']]
y=df['mark']
model= LinearRegression()
model.fit(X,y)
prediction = model.predict([[104]])
print(prediction)

employee = {
    'hours':[8,7,9],
    'salary':[10,12,11]
}
df = pd.DataFrame(employee)
X=df[['hours']]
y=df['salary']
model= LinearRegression()
model.fit(X,y)
prediction = model.predict([[10]])
print(prediction)