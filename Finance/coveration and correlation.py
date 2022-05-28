# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:15:34 2022

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

sec_return  = np.log(sec_data / sec_data.shift(1))
sec_return

sec_return[['PG','BEI.DE']].mean() * 250 * 0.5    # change the tickers you want data from 


#calculating covariance and correlation

cov_matrix_a = sec_return.cov() * 250         #calculating coveration of two stocks annually
print (cov_matrix_a)   

corr_matrix = sec_return.corr()               # correlation
print(corr_matrix)