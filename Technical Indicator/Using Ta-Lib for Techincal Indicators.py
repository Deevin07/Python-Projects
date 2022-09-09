# -*- coding: utf-8 -*-
"""
Using Ta-Lib for Techincal Indicators

@author: Vineet
"""

import talib


#want to know how many indicators 
dir(talib)

#want to a specific indicator
?talib.RSI       #just add in the indicator name from the dir 

#to get the functions
talib.get_functions()

#Category of the indicators
talib.get_function_groups()

#want to apply any indicator to a stock
import talib
import yfinance as yf

data = yf.download('tsla' , start  =  '2020-01-01' ,end = '2022-09-09')
print(data)

#applying RSI indicator on the above stock data
talib.RSI(data['Close'], timeperiod = 14)

#making the data abstract so that you can use it freely
from talib import abstract

data.rename(columns={'Open':'open','Close':'close','High':'high','Low':'low','Volume':'volume'},inplace=True)
data

abstract.RSI(data)    #add indicator name after .  and then in bracket add data 

