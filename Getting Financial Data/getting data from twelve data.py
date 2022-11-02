# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:11:53 2022

@author: Vineet
"""

import requests
import pandas as pd

api_key = '190ad362175b43638975eac8e2dcad84'
symbol = 'USD/JPY'
interval = '1min'

api_url = f'https://api.twelvedata.com/time_series?symbol={symbol}&start_date=2019-08-09&end_date=2022-01-01&interval={interval}&apikey={api_key}'

data2 = requests.get(api_url).json()

data2 = pd.DataFrame(data2['values'])

