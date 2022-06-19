# -*- coding: utf-8 -*-
"""
Visualizing Tech Stocks

@author: Vineet
"""

import pandas as pd
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
                                    
stocks = ['AMZN','MSFT','AAPL','GOOG','FB']           # here you can add the ticker for any stock 
start = datetime.datetime.today()-datetime.timedelta(182)           # we are getting the data of past 10 years
end = datetime.datetime.today()
cl_price = pd.DataFrame()           #getting store all data frame here
                                    
#looping through and creating a data frame and for each ticker
for ticker in stocks:
    v = yf.download(ticker,start,end)['Adj Close']
                                        
#dropping all the NAN values
cl_price.dropna(axis = 0,how = 'any',inplace=True)

#plotting the adj close price
adj_data = cl_price
adj_data.plot()
plt.title('Tech adj close price')
plt.xlabel('Date')
plt.ylabel('Price')

#calulating daily simple moving average
daily_return = adj_data.pct_change()
daily_return.plot()
plt.title("Daily Simple Rate of Return")
plt.xlabel("Date")
plt.ylabel("Rate of Return")

#creating subplots fopr better visulatization
fig = plt.figure(figsize=(20,10))
 
# Microsoft
ax1 = plt.subplot(2,3,1)
plt.plot(daily_return['MSFT'],color = 'green')
plt.title('Microsoft')
plt.xlabel('Date')
plt.ylabel('Daily Return')

#Amazon
ax2 = plt.subplot(2,3,2)
plt.plot(daily_return['AMZN'],color = 'red')
plt.title('Amazon')
plt.xlabel('Date')
plt.ylabel('Daily Return')

#Apple
ax3 = plt.subplot(2,3,3)
plt.plot(daily_return['AAPL'],color = 'blue')
plt.title('Apple')
plt.xlabel('Date')
plt.ylabel('Daily Return')


#Google
ax4 = plt.subplot(2,3,4)
plt.plot(daily_return['GOOG'],color = 'black')
plt.title('Google')
plt.xlabel('Date')
plt.ylabel('Daily Return')

#Facebook
ax5 = plt.subplot(2,3,5)
plt.plot(daily_return['FB'],color = 'violet')
plt.title('Facebook')
plt.xlabel('Date')
plt.ylabel('Daily Return')

plt.subplots_adjust(wspace=0.3,bottom = 0.1)


#calculating the mean rate of return
mean_daily_return = daily_return.mean()

#calculating the varience 
variance_daily_return = daily_return.var()

#calculating the standard deviation
stan_dev = daily_return.std()

#calculating the correlation
correlation = daily_return.corr()
