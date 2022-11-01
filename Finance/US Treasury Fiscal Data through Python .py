# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:16:57 2022

@author: Vineet
"""

import requests
import pandas as pd

endpoint = 'v2/accounting/od/avg_interest_rates'

api_url = f'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/{endpoint}'

#getting the data
data = requests.get(api_url).json()

#converting the data in dataframe
Data = pd.DataFrame(data['data'])

#wanting the data from 2020 and adding filters
apiurl =  f'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/{endpoint}?fields=record_date,security_desc,avg_interest_rate_amt&filter=record_date:eq:2022-09-30'
data2 = requests.get(apiurl).json()
Data2 = pd.DataFrame(data2['data'])
