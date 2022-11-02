# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:39:20 2022

@author: Vineet
"""

from nsepy import get_history
from datetime import date
import pandas as pd
import numpy as np
import talib
import datetime

scrip = 'HDFCAMC'


stock_df = get_history(symbol=scrip,
                    start=date(2021,1,1), 
                    end=date(2021,12,31)) 

pd.set_option('display.width', 10000)
print(f"Stock data size:{stock_df.shape}")
print(stock_df.head(2))
print(stock_df.tail(2))


import plotly.graph_objects as go

candlestick = go.Candlestick(x=stock_df.index, 
                             open=stock_df['Open'],  
                             high=stock_df['High'], 
                             low=stock_df['Low'], 
                             close=stock_df['Close'])

fig = go.Figure(data=[candlestick])
fig.layout.xaxis.type = 'category' 
fig.show()

def plot_candle(df, title):
    candlestick = go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])

    # Plot only the last month's data
    fig = go.Figure(data=[candlestick],
                    layout=go.Layout(title=go.layout.Title(text=title)))
    fig.layout.xaxis.type = 'category' 
    fig.show()



# Identify the engulfing candles in the dataset
stock_df['engulf'] = talib.CDLENGULFING(stock_df['Open'], stock_df['High'], stock_df['Low'], stock_df['Close'])

# Subset dataframe for only the doji candles
stock_df['next_is_engulf'] = stock_df['engulf'].shift(-1)
engulf_candles = stock_df[(stock_df['engulf'] != 0) | (stock_df['next_is_engulf'] != 0)]
print(engulf_candles[['Open','Close','engulf']].head(10))


# Plot the candlestick chart
plot_candle(engulf_candles, title = f"Engulfing Candlestick Pattern - {scrip}")