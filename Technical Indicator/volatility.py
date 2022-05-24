# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 20:46:40 2022

@author: Vineet
"""

import yfinance as yf
import pandas as pd
import numpy as np

tickers = ['AMZN','GOOG','MSFT']
d8 = {}


for ticker in tickers:
    temp = yf.download(ticker, period='7mo',interval='1d')
    temp.dropna(how='any',inplace=True)
    d8[ticker] = temp
    
def volatility(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    vol = df['return'].std() * np.sqrt(252)
    return vol

for ticker in d8:
    print('Volatilty of {}  = {}'.format(ticker,volatility(d8[ticker])))
