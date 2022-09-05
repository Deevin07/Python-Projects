# -*- coding: utf-8 -*-
"""
Getting info of all companies from NSE 

@author: Vineet
"""


from nsetools import Nse
import pandas  as pd, numpy as np

nse = Nse()
print(nse)

stock_data = pd.DataFrame()

tickers  = ['infy' , 'tcs' , 'reliance' , 'yesbank' , 'KOTAKBANK']  #add the list of stock names you want info of

for i in tickers:
    s = nse.get_quote(i)
    stock_data[s['companyName']] = pd.Series(s)

print(stock_data)