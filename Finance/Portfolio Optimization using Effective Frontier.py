# -*- coding: utf-8 -*-
"""
This program attempts to optimise a user portfolio by using the Efficient Frontier & Python

@author: Vineet
"""
#!pip install PyPortfolioOpt
#Import the libaries
from pandas_datareader import data as web 
import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from datetime import datetime
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


#get the stock tickers
#using the FAANG as user portfolio 

assets = ['ITC.BO','RELIANCE.NS','TATAMOTORS.NS','DEEPAKNTR.NS','BHARTIARTL.NS']

#assing weights to the stocks
weights = np.array([0.2,0.2,0.2,0.2,0.2])

#get the stock/portfolio stsrting date
stockStartDate = '2015-01-01'

#Get the stocks ending date
today = datetime.today().strftime('%Y-%m-%d')

#Create a dataframe to store the adjusted close price of the stocks
df = pd.DataFrame()

#store the adjusted close price of the stocks into the df
for stock in assets:
  df[stock] = web.DataReader(stock, 'yahoo',start = '2015-01-01' ,end = today)['Adj Close']
  
print(df)

#visually show the stocks / portfolio
title = 'Portfolio Adj Close price History'

#get the stock
my_stocks  = df

#create and plot 
for c in my_stocks.columns.values:
  plt.plot(my_stocks[c],label = c)

plt.title(title)
plt.xlabel('Date', fontsize = 18)
plt.ylabel("Adj close Price", fontsize = 18)
plt.legend(my_stocks.columns.values)
plt.show()

#daily simple returns
returns = df.pct_change()

#annualized coovarince matrix
cov_matrix_annual = returns.cov() * 252

#calculate  the portfolio varience
port_var = np.dot(weights.T,np.dot(cov_matrix_annual,weights))

#calciulate the portfolio volatility
port_volatility = np.sqrt(port_var)

#annual portfilo return
portfolio_return = np.sum(returns.mean() * weights ) * 252

#expected annual return , volatility , varience

percent_var = str(round(port_var,2)*100) + '%'
percent_vola = str(round(port_volatility,2)*100) + '%'
percent_return = str(round(portfolio_return,2)*100) + '%'
print('Expected annual return ',percent_return)
print('Annual volatility /risk:',percent_vola)
print('Annual varience ',percent_var)

#Portfolio Optimization

#caluclted the expected return and the annualized sample covarance matrix of assset

mu = expected_returns.mean_historical_return(df)
s = risk_models.sample_cov(df)

#optimize for max sharpe ratio
ef = EfficientFrontier(mu,s)
weights = ef.max_sharpe()
clean_weights = ef.clean_weights()
print(clean_weights)
ef.portfolio_performance(verbose=True)   

#get the discreate  allocation of each share per stock

#This will show you at this point of time how many stock you can buy with the limit money and leftover money

from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

latest_prices = get_latest_prices(df)
weights = clean_weights
da = DiscreteAllocation(weights,latest_prices,total_portfolio_value = 100000)

allocation , leftover = da.lp_portfolio()
print('Discreate allocation', allocation)
print('Funds Remaining: Rupees: {:.2f}'.format(leftover))