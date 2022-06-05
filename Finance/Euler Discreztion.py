# -*- coding: utf-8 -*-
"""
Euler Discretization

@author: Vineet
"""

import numpy as np
import pandas as pd
import pandas_datareader.data as web
from scipy.stats import norm
import matplotlib.pyplot as plt


ticker = 'PG'
data = pd.DataFrame()
data[ticker] = web.DataReader(ticker,'yahoo',start='2012-1-1')['Adj Close']

log_return = np.log(1 + data.pct_change())

r = 0.025          #risk free return

stdev = log_return.std() * 250 ** 0.5
print('Standard dev',stdev)

stdev = stdev.values      #cnverting it to np array

T = 1.0                            #time horizon
t_intervals = 250
delta_t = T / t_intervals 

iteration = 10000

Z = np.random.standard_normal((t_intervals + 1, iteration))
S = np.zeros_like(Z)
S0 = data.iloc[-1]
S[0] = S0

for t in range(1,t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])
    
print(S)

plt.figure(figsize = (15,6))
plt.plot(S[:,:10])