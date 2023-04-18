# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:32:12 2023

@author: Vineet
"""

import pandas as pd
import talib
import os

os.chdir('C:\\Users\\Vineet\\Downloads')
df = pd.read_csv('3131.csv',parse_dates=True,index_col=0)

data = talib.SMA(df['close'])

def get_candle_stick(df):
    return dict(
        open = df['open'],
        close = df['close'],
        high = df['high'],
        low = df['low']
        )
#integer = CDLDOJI(open, high, low, close)

df['DOJI'] = talib.CDLDOJI(**get_candle_stick(df))
df3 = df['DOJI']
print(df[df['DOJI'] !=0])