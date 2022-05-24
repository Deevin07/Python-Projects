# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:48:31 2022

@author: Vineet
"""

import yfinance as yf

tickers = {'AMZN','GOOG','MSFT'}     # here you can add the ticker for any stock
d2 = {}

for ticker in tickers:
    temp = yf.download(ticker, period  = '1mo', interval='5m')
    temp.dropna(how='any',inplace=True)
    d2[ticker] = temp
    
    
def ATR(DF, n=14 ):
    df = DF.copy()
    df['H-L'] = df['High'] - df['Low']
    df['H-PC'] = df['High'] - df['Adj Close'].shift(1)
    df['L-PC'] = df['Low'] - df['Adj Close'].shift(1)
    df['TR'] = df[['H-L','H-PC','L-PC']].max(axis=1,skipna = False)
    df['ATR'] = df['TR'].ewm(com=n,min_periods = n).mean()
    return df['ATR']

for ticker in tickers:
    d2[ticker]['ATR'] = ATR(d2[ticker])