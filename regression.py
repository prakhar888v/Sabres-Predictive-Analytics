import statsmodels.api as sm
from sklearn import datasets
import pandas as pd
from sklearn import linear_model

data = datasets.load_boston()

df = pd.DataFrame(data.data, columns=data.feature_names)
target = pd.DataFrame(data.target, columns=['MEDV'])

# Using OLS in statsmodels.api
X = df[['RM', 'LSTAT']]
print(X)
y = target['MEDV']
# X = sm.add_constant(X)
model = sm.OLS(y,X).fit()
predictions = model.predict(X)

print(predictions)
print(target)
print(model.summary())

# Using sklearn
X = df
y = target['MEDV']

lm = linear_model.LinearRegression()
model = lm.fit(X,y)
predictions = lm.predict(X)
print(predictions)
print('score is ',lm.score(X,y))

