# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 17:17:27 2023

@author: Vineet
"""

import pandas as pd
import os
import datetime as dt

os.chdir('C:\\Users\\Vineet\\Downloads')

df = pd.read_csv('nifty.csv',parse_dates=True,index_col=0)

df['year'] = df.index.strftime('%Y')


df['year'] = df['year'].astype(float)

df_yoy = df.resample('Y').last().pct_change()


print(df_yoy)


