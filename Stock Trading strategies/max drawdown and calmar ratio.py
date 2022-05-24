# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:52:40 2022

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
    
def CAGR(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    df['cum_return'] = (1 + df['return']).cumprod()
    n = len(df)/252
    CAGR = (df['cum_return'][-1]) ** (1/n) - 1 
    return CAGR 

def max_dd(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    df['cum_return'] = (1 + df['return']).cumprod()
    df['cum_roll_max'] = df['cum_return'].cummax()
    df['drawdown'] = df['cum_roll_max'] - df['cum_return']
    return (df['drawdown']/df['cum_roll_max']).max()

def calmar(DF):
    return (CAGR(DF) / max_dd(DF))

for ticker in d8:
    print('max dd for {} = {}'.format(ticker,max_dd(d8[ticker])))
    print('calmar ratio for {} = {}'.format(ticker,calmar(d8[ticker])))