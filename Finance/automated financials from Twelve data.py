# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:19:06 2022

@author: Vineet
""" 
import requests
import pandas as pd
import numpy as np

api_key = '190ad362175b43638975eac8e2dcad84'
data_type = input("Data type- time series or tech indicator: ")
def inputs():
  symbol = input('Enter ticker/forex/crypto/ETF/Index: ')
  interval = input('Interval- 1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 8h, 1day, 1week, 1month: ')
  order = input('Order-asc, desc: ')
  start_date = input('Start Date(yyyy-mm-dd): ')
  end_date = input('End Date(yyyy-mm-dd): ')
  return symbol,interval,order,start_date,end_date

if data_type == 'time series':
  print('\nTicker eg.: AAPL, MSFT\nForex eg.: USD/JPY, USD/EUR\nCrypro eg.:BTC/USD, ETH/USD\nETF eg.:SPY, VTI\nIndex eg.:IXIC, SPX\n')
  inputs1 = inputs()
  api_url = f'https://api.twelvedata.com/time_series?symbol={inputs1[0]}&start_date={inputs1[3]}&end_date={inputs1[4]}&interval={inputs1[1]}&order={inputs1[2]}&apikey={api_key}'
elif data_type == 'tech indicator':
  tech_indi_json = requests.get('https://api.twelvedata.com/technical_indicators').json()
  print("\nList of Technical Indicators: "+str(np.array(pd.DataFrame(tech_indi_json['data']).columns))+"\n")
  tech_indi = input("Enter Tech Indicator exactly as mentioned above: ")
  print('\nTicker eg.: AAPL, MSFT, etc.\nForex eg.: USD/JPY, USD/EUR, etc.\nCrypro eg.:BTC/USD, ETH/USD, etc.\nETF eg.:SPY, VTI, etc.\nIndex eg.:IXIC, SPX, etc.\n')
  inputs1 = inputs()
  api_url = f'https://api.twelvedata.com/{tech_indi}?symbol={inputs1[0]}&start_date={inputs1[3]}&end_date={inputs1[4]}&interval={inputs1[1]}&include_ohlc=true&order={inputs1[2]}&apikey={api_key}'
else:
  print('Wrong Entry')
  
data = requests.get(api_url).json()
data_final = pd.DataFrame(data['values'])
data_final