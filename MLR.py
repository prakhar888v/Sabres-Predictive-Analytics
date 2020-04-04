import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import cross_val_score, cross_val_predict
from matplotlib import pyplot as plt

data_path = 'C:\\Users\\prakh\\OneDrive\\Documents\\Sabres project\\Buffalo Sabres data\\sabres_aggregated_data2.csv'
df = pd.read_csv(data_path)

X = df['Streak(cont)']
y = df['Attendance']
X = sm.add_constant(X)

model = sm.OLS(y,X).fit()
predictions = model.predict(X)

print(model.summary())

# from sklearn import metrics
#
# scores = cross_val_score(model, X, y, cv=6)
# print(scores)
# predictions = cross_val_predict(model, X, y, cv=6)
x_axis = [n+1 for n in range(len(predictions))]

plt.plot(x_axis,y, color = 'blue')
plt.plot(x_axis,predictions, color = 'orange')
plt.show()

# print(metrics.r2_score(y,predictions))

