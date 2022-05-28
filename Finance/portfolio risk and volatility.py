# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:25:35 2022

@author: Vineet
"""
import pandas as pd
import numpy as np
import pandas_datareader.data as web




tickers  = ['PG','BEI.DE']          # the tickers you want 
sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = web.DataReader(t,'yahoo',start='2007-1-1')['Adj Close']     #mention the data you want data from 
    

sec_data.tail()                                       #checking the data

sec_return  = np.log(sec_data / sec_data.shift(1))     #daily change in return
sec_return

weights = np.array([0.5,0.5])                         # Assuming equal weights of two stocks

port_var = np.dot(weights.T,np.dot(sec_return.cov() * 250, weights ))        #portfolio variance

port_vol = np.dot(weights.T,np.dot(sec_return.cov() * 250, weights )) ** 0.5   #portfolio volatility

print (str(round(port_vol,5)*100)+'%')                                   