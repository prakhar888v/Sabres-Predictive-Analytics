import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from matplotlib import pyplot as plt

columns = 'age sex bmi map tc ldl hdl tch ltg glu'.split()
diabetes = datasets.load_diabetes()

df = pd.DataFrame(diabetes.data, columns=columns)
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

lm = linear_model.LinearRegression()
model = lm.fit(X_train,y_train)
predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.show()

print(model.score(X_test, y_test))

# Cross Validaiton
from sklearn import metrics

scores = cross_val_score(model, df, y, cv=6)
print(scores)
predictions = cross_val_predict(model, df, y, cv=6)
plt.scatter(y, predictions)
plt.show()

print(metrics.r2_score(y,predictions))