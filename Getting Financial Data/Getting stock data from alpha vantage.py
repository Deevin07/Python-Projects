# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:52:24 2022

@author: Vineet
"""

from alpha_vantage.timeseries import TimeSeries
Api_key = '7398IW3YVLO8TTYE' 

ts = TimeSeries(key=Api_key, output_format='pandas')

#getting montly adjusted data
data = ts.get_monthly_adjusted('AAPL')
data[0]

#getting daily data
data1 = ts.get_daily('AAPL')

#intraday data
"""
5min , 10min , 15min
"""
data2 = ts.get_intraday('AAPL',interval='15min')

#INPUT THE TICKER AND GET THE DATA


from alpha_vantage.timeseries import TimeSeries
Api_key = '7398IW3YVLO8TTYE' 
outputsize = 'compact'
ts = TimeSeries(key=Api_key, output_format='pandas')
symbol = input('ticker:')
typ = input('Data Type- "daily" , "weekly","monthly","interval :"')

if typ == 'daily':
    state = ts.get_daily(symbol,outputsize=outputsize)[0]
elif typ == 'weekly':
    state = ts.get_weekly(symbol,outputsize=outputsize)[0]
elif typ == 'montly':
    state  = ts.get_monthly(symbol,outputsize=outputsize)[0]
elif  typ == 'interval':
    interval = input('Interval- 1min , 5min , 15 min , 30min ,60min :')
    state = ts.get_intraday(symbol,outputsize=outputsize,interval = interval)[0]
else:
    print('Wrong Input')
state


