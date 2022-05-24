# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:23:07 2022

@author: Vineet
"""

import yfinance as yf
import pandas as pd
import numpy as np

tickers = ['AMZN','GOOG','MSFT']
d7 = {}

for ticker in tickers:
    temp = yf.download(ticker, period='7mo',interval='1d')
    temp.dropna(how='any',inplace=True)
    d7[ticker] = temp

def CAGR(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    df['cum_return'] = (1 + df['return']).cumprod()
    n = len(df)/252
    CAGR = (df['cum_return'][-1]) ** (1/n) - 1 
    return CAGR 


def volatility(DF):
    df = DF.copy()
    df['return'] = DF['Adj Close'].pct_change()
    vol = df['return'].std() * np.sqrt(252)
    return vol

def sharpe(DF, rf):
    df = DF.copy()
    return (CAGR(df) - rf) / volatility(df)
 
def sortino(DF, rf):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    neg_return = np.where(df['return']>0,0,df['return'])
    neg_vol = pd.Series(neg_return[neg_return!=0]).std() * np.sqrt(252)
    return (CAGR(df) - rf) / neg_vol 

for ticker in d7:
    print('Sharpe for {} = {}'.format(ticker,sharpe(d7[ticker],0.03)))
    print('Sharpe for {} = {}'.format(ticker,sortino(d7[ticker],0.03)))