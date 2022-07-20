# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:25:41 2022

@author: Vineet
"""

from sklearn.svm  import SVR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight') 
import os

os.chdir('C:\\Users\\Vineet\\Downloads')
df = pd.read_csv('GOOGLE.csv')

#show and store the last row of data
actual_price = df.tail(1)

#getting all the data except the last row
df = df.head(len(df)-1)

#creating empty list
days = list()
adj_close_prices = list()

#get the dates and adjusted close prices
df_days = df.loc[:,'Date']
df_adj_close = df.loc[:,'Adj Close']

 #Create the independent data set(dates)
for day in df_days:
  days.append([int(day.split('-')[2])])

#creating the dependent data set (adj Close price)
for adj_close_price in df_adj_close:
  adj_close_prices.append(float(adj_close_price))
  
#Create 3 models
lin_svr = SVR(kernel = 'linear', C = 1000.0)
lin_svr.fit(days,adj_close_prices)

poly_svr = SVR(kernel = 'poly', C = 1000.0, degree = 2)
poly_svr.fit(days,adj_close_prices)

rbf_svr = SVR(kernel = 'rbf', C = 1000.0 , gamma=0.85)
rbf_svr.fit(days,adj_close_prices)

#plot the model
plt.figure(figsize = (16,8))
plt.scatter(days,adj_close_prices,color='black',label = 'Data')
plt.plot(days,rbf_svr.predict(days),color='green',label = 'RBF Model')
plt.plot(days,poly_svr.predict(days),color='orange',label = 'Polymonial Model')
plt.plot(days,lin_svr.predict(days),color='blue',label = 'Linear Model')
plt.xlabel('Days')
plt.ylabel('Adj Close Price')
plt.legend()
plt.show()
