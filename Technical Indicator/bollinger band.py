# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:24:42 2022

@author: Vineet
"""

import yfinance as yf

tickers = {'AMZN','GOOG','MSFT'} # here you can add the ticker for any stock 
d1 = {}

for ticker in tickers:
    temp = yf.download(ticker, period  = '1mo', interval='5m')
    temp.dropna(how='any',inplace=True)
    d1[ticker] = temp
    
def Bol_band(DF,n=14):
    df = DF.copy()
    df['MB'] = df['Adj Close'].rolling(n).mean()
    df['UB'] = df['MB'] + 2 * df['Adj Close'].rolling(n).std(ddof=0)
    df['LB'] = df['MB'] - 2 * df['Adj Close'].rolling(n).std(ddof=0)
    df['BB'] = df['UB'] - df['LB']
    return df[['MB','UB','LB','BB']]

for ticker in d1:
    d1[ticker][['MB','UB','LB','BB']] = Bol_band(d1[ticker],20)    
    
