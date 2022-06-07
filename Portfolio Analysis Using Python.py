# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:57:07 2022

@author: Vineet
"""
   # !pip install nsepy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import datetime 
from nsepy import get_history as gh
plt.style.use('fivethirtyeight')

stocksymbols = ['TATAMOTORS','DABUR', 'ICICIBANK','WIPRO','BPCL','IRCTC','INFY','RELIANCE'] # add your assets 
 
startdate = datetime.date(2021,1,1)
end_date = datetime.date.today()
print(end_date)
print(f" You have {len (stocksymbols)}assets in your portfolio")


df = pd.DataFrame()

for i in range(len(stocksymbols)):
    data = gh(symbol = stocksymbols[i],start=startdate , end = (end_date))[['Symbol','Close']]
    data.rename(columns = {'Close':data['Symbol'][0]}, inplace =True)
    data.drop(['Symbol'],axis = 1 , inplace = True)
    if i == 0:
        df = data
    if i != 0:
        df = df.join(data)
        
print(df)

fig, ax = plt.subplots(figsize = (15,6))

for i in df.columns.values:
    ax.plot(df[i], label = i)

ax.set_title = ('Portfolio Closing Price')
ax.set_xlabel('Date', fontsize = 18)
ax.set_ylabel('Close Price INR',fontsize = 18)
ax.legend(df.columns.values)
plt.show(fig)


#correaltion matrix
correlation_matrix = df.corr(method = 'pearson')

#plotting the correlation matrix
fig1 = plt.figure()
sb.heatmap(correlation_matrix, xticklabels = correlation_matrix.columns , yticklabels= correlation_matrix.columns, 
               cmap = 'YlGnBu', annot = True, linewidth = 0.5)

#risk and return
daily_return = df.pct_change(1)
print(daily_return)

#plotting daily return
daily_return.plot(figsize =  (15,6), xlabel = 'Date',title = ' Volatility of Daily Simple average', ylabel='Daily Simple Average')

#average daily index
Avg_daily = daily_return.mean()
print(Avg_daily * 100)

#plotting risk using daily return
daily_return.plot(kind = "box",figsize = (20,10), title = "Risk Box Plot")

print('Annualized Standard Deviation (Volatality(%), 252 trading days) of individual stocks in your portfolio on the basis of daily simple returns.')
print(daily_return.std() * np.sqrt(252) * 100)


#return per unit of risk
Avg_daily / (daily_return.std() * np.sqrt(252)) * 100


#daily cummulative return
daily_cum_return = (daily_return + 1 ).cumprod()

#plotting daily cummulative return

daily_cum_return.plot(figsize = (15,6), xlabel = 'Date', ylabel = 'Growth of investment of 1 re',title = 'Cummulative Daily return')

