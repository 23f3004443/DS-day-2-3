from sklearn.datasets  import load_iris
from sklearn.ensemble import RandomForestClassifier

import joblib

iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.20, random_state=42)

model=RandomForestClassifier()

model.fit(Xtr, ytr)

y_pred = model.predict(Xte)

from sklearn.metrics import accuracy_score

print(accuracy_score(yte, y_pred))

joblib.dump(model, "model.pkl")

print(iris.target_names[model.predict([[7.2, 2.9, 3.8, 1]])])

print(iris.target_names)