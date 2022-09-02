# -*- coding: utf-8 -*-
"""
Get assests that gave a greater anualized return than NIFTY 50

@author: Vineet
"""


import pandas as pd
import os

os.chdir('C:\\Users\\Vineet\\Downloads')    #give the path where you have saved the excel file

#getting the data
assets = pd.read_csv('nifty.csv') #this consists of nifty 50 close price data

#Set date as index
assets = assets.set_index(pd.DatetimeIndex(assets['Date'].values))

#remove or drop the date column
assets.drop(['Date'],inplace=True, axis= 1)

#removing the nan values
assets.fillna(0)

#get the simple daily return
daily_simple_return = assets.pct_change()

#get the annualized return
annual_return = daily_simple_return.mean() * 252

#show the annualized return for Nifty 50 
annual_return['^NSEI']


print('NIFTY 50  :' , annual_return['^NSEI'])

#Show all the assets that have given a higher annualized return than Nifty 50
for i in range(0 , len(annual_return)):
               if annual_return[i] > annual_return['^NSEI']:
                   print(annual_return.index[i], ":", annual_return[i])
                   