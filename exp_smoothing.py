from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

colnames = ['Date','Attendance']
data = pd.read_csv('Sabres home games_csv.csv',usecols=colnames)

# data['Date'] = pd.to_datetime(data["Date"])
# print(data['Date'])
# model = SimpleExpSmoothing(data)

data = data['Attendance']
data = list(data)
data = [int(n.replace(',','')) for n in data ]
index= pd.date_range(start='2000', end='2164', freq='A')
att_data = pd.Series(data, index)

ax=att_data.plot()
ax.set_xlabel("Year")
ax.set_ylabel("Attendance")
plt.show()
print("Attendance")
print(att_data)


# # Simple Exponential Smoothing
# fit1 = SimpleExpSmoothing(data).fit(smoothing_level=0.2,optimized=False)
# fcast1 = fit1.forecast(12).rename(r'$\alpha=0.2$')
# # plot
# fcast1.plot(marker='o', color='blue', legend=True)
# fit1.fittedvalues.plot(marker='o',  color='blue')
#
# fit2 = SimpleExpSmoothing(data).fit(smoothing_level=0.6,optimized=False)
# fcast2 = fit2.forecast(12).rename(r'$\alpha=0.6$')
# # plot
# fcast2.plot(marker='o', color='red', legend=True)
# fit2.fittedvalues.plot(marker='o', color='red')


# fit3 = SimpleExpSmoothing(data).fit()
# fcast3 = fit3.forecast(12).rename(r'$\alpha=%s$'%fit3.model.params['smoothing_level'])
# # plot
# fcast3.plot(marker='o', color='green', legend=True)
# fit3.fittedvalues.plot(marker='o', color='green')
#


