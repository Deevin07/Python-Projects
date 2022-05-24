# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:45:38 2022

@author: Vineet

MACD 
"""

import yfinance as yf

tickers = {'AMZN','GOOG','MSFT'}
data = {}

for ticker in tickers:
    temp = yf.download(ticker, period  = '1mo', interval='15m')
    temp.dropna(how='any',inplace=True)
    data[ticker] = temp
    
def MACD(DF, a = 12 , b = 26 , c = 9):
    df = DF.copy()
    df['ma_fast'] = df['Adj Close'].ewm(a, min_periods= a).mean()
    df['ma_slow'] = df['Adj Close'].ewm(b,min_periods= b).mean()
    df['macd'] = df['ma_fast'] - df['ma_slow']
    df['signal'] = df['macd'].ewm(c).mean()
    return df.loc[:,['macd','signal']]
                  
for ticker in data:
    data[ticker][['MACD','SINAL']] = MACD(data[ticker])
                                         
                  
                  
    