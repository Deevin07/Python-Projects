# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:03:35 2022

@author: Vineet
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import datetime as dt
"""
AAPL = Apple
Meta = Meta
C = Citigroup Inc. (C)
DIS = The Walt Disney Company 
F = Ford Motor Company 
MSFT = Microfoft
MS = Morgan Stanley
GME = GameStop Corp
TSLA = Tesla
AMZN = Amazon

"""

tickers = ['AAPL','META','C','DIS','F','MSFT','MS','GME','TSLA','AMZN']
weights = np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

start=  dt.datetime(2020,1,1)
end = dt.datetime.now()
df = yf.download(tickers,start,end)['Adj Close']

#calculating the returns
returns = df.pct_change()

#coveriance return
cov_matrix = returns.cov()

#Expected returns
avg_returns = returns.mean()

counts = df.count()

#portfolio mean
port_mean = avg_returns @ weights

#standard deviation of the portfolio
port_stan = np.sqrt(weights.T @ cov_matrix  @ weights)

#plotting
x = np.arange(-0.05, 0.055 , 0.001)
norm_dist = norm.pdf(x, port_mean, port_stan)

plt.plot(x,norm_dist,color = 'r')
plt.show()

confidence_level = 0.05
VaR = norm.ppf(confidence_level,port_mean,port_stan)
    