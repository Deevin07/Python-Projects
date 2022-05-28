# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:29:02 2022

@author: Vineet
"""

import pandas as pd
import numpy as np 
import pandas_datareader.data as web

tickers = {'AAPL','MSFT','F','GE'}     # add the tickers you want to add 

my_data = pd.DataFrame()

for t in tickers:
    my_data[t] = web.DataReader(t,'yahoo',start = '2012-1-1')['Adj Close']     #getting data from past 10 years from 
                                                                                #yahoo finaance
    
my_data.tail()


### calculating the return of the portfolio

returns= (my_data / my_data.shift(1)) - 1   #returns 

weights = np.array([0.25,0.25,0.25,0.25])  # assuming that there is a equal weightage of stocks in the portfolio

annual_return  = returns.mean() * 250    # we have 250 trading days in a 

np.dot(annual_return,weights)            #calculating the dot product

port_01 = str(round(np.dot(annual_return,weights),5) * 100) + '%'
print(port_01)

weights_2 = ([0.4,0.4,0.15,0.05])             # assuming different weights of stocksin the portfolio
port_02 = str(round(np.dot(annual_return,weights_2),5) * 100) + '%'
print(port_02)


 


