# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:07:29 2022

@author: Vineet
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime as dt
import pandas_datareader.data as web


start = dt.datetime(2019,1,1)
end = dt.datetime.now()

stocks = web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 'yahoo', start, end)
stocks_close = pd.DataFrame(web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 'yahoo', start, end)['Close'])


candlestick= go.Figure(data = [go.Candlestick(x =stocks.index,
                                              open = stocks[('Open', 'AMZN')],
                                              high = stocks[('High','AMZN')],
                                              low = stocks[('Low','AMZN')],
                                              close = stocks[('Close','AMZN')]
                                              )])

candlestick.update_layout(xaxis_rangeslider_visible = False, title = "AMAZON SHARE PRICE(2019-2022)")
candlestick.update_xaxes(title_text = 'Date')
candlestick.update_yaxes(title_text = 'AMZN PRICE', tickprefix= "$")

candlestick.show()

#customize candlestick

# Customized Candlestick

c_candlestick = go.Figure(data = [go.Candlestick(x = stocks.index, 
                                               open = stocks[('Open',    'AMZN')], 
                                               high = stocks[('High',    'AMZN')], 
                                               low = stocks[('Low',    'AMZN')], 
                                               close = stocks[('Close',    'AMZN')])])

c_candlestick.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

c_candlestick.update_layout(
    title = {
        'text': 'AMAZON SHARE PRICE (2013-2020)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

c_candlestick.update_yaxes(title_text = 'AMZN Close Price', tickprefix = '$')
c_candlestick.show()