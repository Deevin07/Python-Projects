# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:26:06 2022

@author: Vineet
"""

import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import copy

def CAGR(DF):
    "Function to create a CAGR of teh stocks"
    df = DF.copy()
    df['cum_return'] = (1 + df['mon_return']).cumprod()
    n = len(df)/12      # montly data calculating
    CAGR = (df['cum_return'].tolist()[-1]) ** (1/n) - 1
    return CAGR

def volatility(DF):
    df = DF.copy()
    vol = df['mon_return'].std() * np.sqrt(12)
    return vol

def sharpe(DF,rf):
    df = DF.copy()
    sr = (CAGR(df) - rf) / volatility(df)
    return sr

def max_dd(DF):
    df = DF.copy()
    df['cum_return'] = (1 + df['mon_return']).cumprod()
    df['cum_roll_max'] = df['cum_return'].cummax()
    df['drawdown']  = df['cum_roll_max'] - df['cum_return']
    df['drawdown_pct'] = df['drawdown'] / df['cum_roll_max']
    max_dd = df['drawdown'].max()
    return max_dd

# dowloading historical data(montly) of DJI(DOW indicator)

tickers = ["MMM","AXP","T","BA","CAT","CSCO","KO", "XOM","GE","GS","HD",
           "IBM","INTC","JNJ","JPM","MCD","MRK","MSFT","NKE","PFE","PG","TRV",
           "UNH","VZ","V","WMT","DIS"]


ohlc_mon = {}
start = dt.datetime.today() - dt.timedelta(3650) # 10 years of data
end = dt.datetime.today()

#looping 
for ticker in tickers:
    ohlc_mon[ticker] = yf.download(ticker,start,end,interval='1mo')
    ohlc_mon[ticker].dropna(how='all',inplace=True)
    
tickers = ohlc_mon.keys()     #removing tickers which have correupted data


######################################### backtesting #################################################

# calculating monthly return for each stock and consolidating return info by stock in a separate dataframe    
ohlc_dict = copy.deepcopy(ohlc_mon)
return_df = pd.DataFrame()
for ticker in tickers:
    print('calulating montly return for',ticker)
    ohlc_dict[ticker]['mon_return'] = ohlc_dict[ticker]['Adj Close'].pct_change() 
    return_df[ticker] = ohlc_dict[ticker]['mon_return']
return_df.dropna(inplace=True)

# function to calculate portfolio return iteratively

def pflio(DF,m,x):
    """Returns cumulative portfolio return
    DF = dataframe with monthly return info for all stocks
    m = number of stock in the portfolio
    x = number of underperforming stocks to be removed from portfolio monthly"""
    df = DF.copy()
    portfolio = []
    monthly_ret = [0]
    for i in range(len(df)):
        if len(portfolio)> 0:
            monthly_ret.append(df[portfolio].iloc[i,:].mean())
            bad_stocks = df[portfolio].iloc[i,:].sort_values(ascending=True)[:x].index.values.tolist()
            portfolio = [t for t in portfolio if t not in bad_stocks]
        fill = m -len(portfolio)   # number of stocks we have eariler - the number of stocks we have after the deleting of bad stocks
        new_picks = df.iloc[i,:].sort_values(ascending=False)[:fill].index.values.tolist()
        portfolio = portfolio + new_picks
        print(portfolio)
    monthly_ret_df = pd.DataFrame(np.array(monthly_ret),columns=['mon_return']) 
    return monthly_ret_df       
    
#calculating the overrall statergy

CAGR(pflio(return_df,6,3))
sharpe(pflio(return_df,6,3),0.025)
max_dd(pflio(return_df,6,3))


#calculating KPIs for Index buy and hold strategy over the same period
DJI = yf.download('^DJI',dt.date.today()-dt.timedelta(3650),dt.date.today(),interval='1mo')
DJI['mon_return'] = DJI['Adj Close'].pct_change().fillna(0)
CAGR(DJI)
sharpe(DJI,0.025)
max_dd(DJI)


#visualization

fig,ax = plt.subplots()
plt.plot((1 + pflio(return_df,6,3)).cumprod())
plt.plot((1 + DJI['mon_return'].reset_index(drop=True)).cumprod())
plt.title("Index Return vs Strategy Return")
plt.ylabel("cumulative return")
plt.xlabel("months")
ax.legend(["Strategy Return","Index Return"])

    
                    