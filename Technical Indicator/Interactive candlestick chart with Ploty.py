# -*- coding: utf-8 -*-
"""
Interactive candlestick chart with Ploty 

@author: Vineet
"""

import plotly.graph_objects as go
import pandas as pd
import os

os.chdir('C:\\Users\\Vineet\\Downloads')

df = pd.read_csv('niftycsv.csv')
df = df.set_index(pd.DatetimeIndex(df['Date'].values))
print(df)

#creating an interactive candlestick chart
figure = go.Figure(
        data = [
               go.Candlestick(
                   x = df.index,
                   low = df['Low'],
                   high = df['High'],
                   close = df['Close'],
                   open = df['Open'],
                   increasing_line_color = 'green',
                   decreasing_line_color  = ' red',
                   
                   )             
            ]
    )
figure.show()