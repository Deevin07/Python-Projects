# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:48:21 2022

@author: Vineet
"""

from alpha_vantage.fundamentaldata import FundamentalData
Api_key = 'ENTER YOU API KEY' 

fd = FundamentalData(key=Api_key, output_format='pandas')

#getting company overview 
data3 = fd.get_company_overview('AAPL')
data3[0].T

#getting the earnings
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=Api_key'
r = requests.get(url)
data_earnings = r.json()

print(data_earnings)
