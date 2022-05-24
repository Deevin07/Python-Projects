# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:19:42 2022

@author: Vineet
"""

import numpy as np
import datetime
import pandas_datareader.data as web


ticker = 'AAPL'
ohlc_data = web.get_data_yahoo(ticker,datetime.date.today() - datetime.timedelta(364),datetime.date.today())

DF = ohlc_data.copy()

def OBV(DF):
    fg = DF.copy()
    fg['daily_ret'] = fg['Adj Close'].pct_change()
    fg['direction'] = np.where(fg['daily_return']>=0,1,-1)
    fg['direction'][0] = 0
    fg['vol_adj'] = fg['Volume'] * fg['direction']
    fg['obv'] = fg['vol_adj'].cumsum()
    return fg['obv']