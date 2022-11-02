# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:42:08 2022

@author: Vineet
"""

import pandas as pd
import requests
import numpy as np
import datetime as dt
import warnings
import matplotlib.pyplot as plt


warnings.filterwarnings('ignore')

api_key = '190ad362175b43638975eac8e2dcad84'
symbol = 'BTC/USD'
interval = '5min'
order = 'asc'
end_date = dt.datetime(2021,7,14)
start_date = end_date - dt.timedelta(days=15)

api_url = f'https://api.twelvedata.com/time_series?symbol={symbol}&start_date={start_date}&end_date={end_date}&interval={interval}&order={order}&apikey={api_key}'

data = requests.get(api_url).json()
print(data)

data_final = pd.DataFrame(data['values'])
data_final['close'] = pd.to_numeric(data_final['close'],errors='coerce')
data_final.set_index('datetime',inplace = True)

window = 24*12

roll_max = data_final['close'].rolling(window, min_periods = 1).max() 
dd = data_final['close'] / roll_max - 1

max_draw = dd.rolling(window,min_periods = 1).min()


"""
blue is the daily draw down
and the yellow is the max drawdown

""" 
dd.plot()
max_draw.plot()
plt.show()

#analysizing the drawdown
max_draw.min()
max_draw.mean()
max_draw.median()

#converting it into dataframe
max_draw_df = pd.DataFrame(columns = ['Drawdown'])
max_draw_df['Drawdown']  = max_draw 

max_draw_df.describe()
