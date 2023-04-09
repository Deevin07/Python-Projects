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

# =============================================================================
# initial_value = df['Close'].iloc[0]
# final_value = df['Close'].iloc[-1]
# overall_pct_change = (final_value / initial_value - 1) * 100
# 
# # Print the result
# print('Overall % change: {:.2f}%'.format(overall_pct_change))
# 
# 
# =============================================================================

