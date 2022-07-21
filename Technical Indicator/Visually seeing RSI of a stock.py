# -*- coding: utf-8 -*-
"""
Visually seeing RSI of a stock

@author: Vineet
"""

#Using RSI and python to determine where the stock is over bought or over sold

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import os


os.chdir('C:\\Users\\Vineet\\Downloads')

#store the data
meta = pd.read_csv('META.csv')

#set the date as the index
meta = meta.set_index(pd.DatetimeIndex(meta['Date'].values))

#visually show the price
plt.figure(figsize=(16,8))
plt.plot(meta.index,meta['Adj Close'], label = 'Adj Close Price')
plt.title('Adj Close price history')
plt.xlabel('5 Years of data',fontsize = 12  )
plt.ylabel('Adj Close price', fontsize = 12)

#prepare the data for RSI
#get the difference in price
delta = meta['Adj Close'].diff(1)

#get rid of NAN
delta = delta.dropna()

#get the postive gains (up) and negative gains (down)

up = delta.copy()
down = delta.copy()

up[up < 0] = 0
down[down > 0] = 0

#get the time period
period = 14

#Calculate the avg gain and the avg loss
avg_gain = up.rolling(window = period).mean()
avg_loss = abs(down.rolling(window=period).mean())

#calulate the RSI


#calulate the relative strength(RS)
RS = avg_gain / avg_loss

#calulate the relative strenght index
RSI = 100.0 - (100.0 / (1.0 + RS))

#show the rsi visually
plt.figure(figsize = (15.2,10.5))
RSI.plot()
plt.show()

#putting all together

#create a new dataframe
new_df = pd.DataFrame()
new_df['Adj Close Price']  = meta['Adj Close']
new_df['RSI'] = RSI

#visuallty show the adj close price

#plot the adjusted close price

plt.figure(figsize=(15,10))
plt.plot(new_df.index,new_df['Adj Close Price'])
plt.title('Adj Close Price')
plt.legend(new_df.columns.values, loc= 'upper left')
plt.show()

#plotting the correspondance RSI values and the significant  levels
plt.figure(figsize=(15,10))
plt.title('RSI plot')
plt.plot(new_df.index, new_df['RSI'])
plt.axhline(0,linestyle='--', alpha = 0.5, color = 'gray')
plt.axhline(10,linestyle='--', alpha = 0.5, color = 'orange')
plt.axhline(20,linestyle='--', alpha = 0.5, color = 'green')
plt.axhline(30,linestyle='--', alpha = 0.5, color = 'red')
plt.axhline(70,linestyle='--', alpha = 0.5, color = 'red')
plt.axhline(80,linestyle='--', alpha = 0.5, color = 'green')
plt.axhline(90,linestyle='--', alpha = 0.5, color = 'orange')
plt.axhline(100,linestyle='--', alpha = 0.5, color = 'gray')
