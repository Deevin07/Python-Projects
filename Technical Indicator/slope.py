# -*- coding: utf-8 -*-
"""
Created on Sun May 1 15:56:52 2022

@author: Vineet
"""
import yfinance as yf
import statsmodels.api as sm
import datetime as dt
import numpy as np

ticker = 'AAPL'
ohlc = yf.download(ticker,dt.date.today() - dt.timedelta(365),dt.datetime.today())

def slope(ser,n):
    ser = (ser - ser.min()) / (ser.max() - ser.min())
    x = np.array(range(len(ser)))
    x = (x- x.min()) / (x.max() - x.min())
    slopes = [i*0 for i in range(n-1)]
    for i in range(n,len(ser)+1):
        y_scaled = ser[i-1:i]
        x_scaled = ser[x:n]
        x_scaled = sm.add_constant(x_scaled)
        model = sm.OLS(y_scaled,x_scaled)
        results  = model.fit()
        slopes.append(results.params[-1])
    slope_angle = (np.rad2deg(np.arctan(np.array(slopes))))
    return np.array(slope_angle)

ohlc['close_slope']  = slope(ohlc['Adj Close'], 5)

df = ohlc.copy()
df['slope'] = slope(ohlc['Adj Close'],5)


df.iloc[:,[4,6]].plot(subplots=True , layout= (2,1))