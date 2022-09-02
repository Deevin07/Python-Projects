# -*- coding: utf-8 -*-
"""
Getting financial data and then converting it into CSV files

@author: Vineet
"""

import pandas as pd
import yfinance as yf
import datetime
import os

os.chdir('C:\\Users\\Vineet\\Downloads')    #give the path where you want to save

#getting the stocks data
stocks = ['AMZN','MSFT','INTC','GOOG','INFY.NS','META']
start = datetime.datetime.today() - datetime.timedelta(3650)   #days to years 3650 days = 10 years
end = datetime.datetime.today()

#Creatiing a dataframe
cl_price = pd.DataFrame()

#Looping all the tickers
for tickers in stocks:
    cl_price[tickers] = yf.download(tickers,start,end)['Adj Close']


#converting dataframe data into csv file
cl_price.to_csv('Stockdata.csv')  