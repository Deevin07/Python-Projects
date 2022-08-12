# -*- coding: utf-8 -*-
"""
Daily Simple Return Using Python

@author: Vineet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import os

os.chdir('C:\\Users\\Vineet\\Downloads')

#load the data
df = pd.read_csv('niftycsv.csv')
df = df.set_index(pd.DatetimeIndex(df['Date'].values))
df.drop(['Date'],axis=1,inplace = True)
print(df)

#plotting the stock price
plt.Figure(figsize=(12,6))
plt.title('Close Price')
plt.plot(df['Close'])
plt.xlabel('Date')
plt.ylabel('Price')

#Calculating the simple Daily return
DSR = df['Close'].pct_change()

#Getting some statical data on DSR
DSR.describe()

#plotting the daily simple return
plt.Figure(figsize=(12,6))
plt.title('Daily Simple Return')
plt.plot(DSR.index,DSR, label = 'DSR',lw = 2, alpha=0.8)
plt.xlabel('Date')
plt.ylabel('Percentage')
plt.xticks(rotation=45)

#putting both the charts togerther 
top = plt.subplot2grid((4,4),(0,0),rowspan=3,colspan=4)
top.plot(df.index,df['Close'],label = 'Close')
plt.title('Close Price')
plt.legend(loc='best')

bottom = plt.subplot2grid((4,4),(3,0), rowspan=1,colspan=4)
plt.title('DSR')
bottom.plot(DSR.index, DSR)
plt.subplots_adjust(hspace=0.75)
plt.gcf().set_size_inches(15,8)