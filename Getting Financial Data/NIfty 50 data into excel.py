# -*- coding: utf-8 -*-
"""
NIfty 50 data into excel

@author: Vineet
"""

import pandas as pd
import yfinance as yf
import datetime
import os

os.chdir('C:\\Users\\Vineet\\Downloads')    #give the path where you want to save

#getting the nifty 50 stocks data
stocks = ['ITC.NS','ADANIPORTS.NS','HDFC.NS','LT.NS','KOTAKBANK.NS','AXISBANK.NS','NTPC.NS',
          'HDFCBANK.NS','APOLLOHOSP.NS','EICHERMOT.NS','TECHM.NS','SBIN.NS','M&M.NS',
          'BAJFINANCE.NS','HDFCLIFE.NS','JSWSTEEL.NS','HCLTECH.NS','TCS.NS','BHARTIARTL.NS',
          'HINDUNILVR.NS','DIVISLAB.NS','TITAN.NS','SUNPHARMA.NS','ICICIBANK.NS','COALINDIA.NS',
          'BAJAJFINSV.BO','BRITANNIA.NS','DRREDDY.NS','ASIANPAINT.BO','WIPRO.NS','CIPLA.NS',
          'POWERGRID.NS','TATASTEEL.NS','INFY.NS','NESTLEIND.NS','TATACONSUM.NS','SBILIFE.NS',
          'ULTRACEMCO.NS','INDUSINDBK.NS','BAJAJ-AUTO.NS','TATAMOTORS.NS','RELIANCE.NS',
          'MARUTI.NS','UPL.NS','ONGC.NS','HEROMOTOCO.NS','HINDALCO.NS','SHREECEM.NS','BPCL.NS','^NSEI']

#srart and end date
start = datetime.datetime.today() - datetime.timedelta(1825)   #days to years 1825 days = 5 years
end = datetime.datetime.today()

#Creatiing a dataframe
cl_price = pd.DataFrame()

#Looping all the tickers
for tickers in stocks:
    cl_price[tickers] = yf.download(tickers,start,end)['Adj Close']

#converting dataframe data into csv file
cl_price.to_csv('nifty.csv')  
