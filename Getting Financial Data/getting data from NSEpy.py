# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:52:24 2022

@author: Vineet
"""

import nsepy as nse
from datetime import date
"""
date format is yyyy,mm,dd
"""


#getting particular stock data
stock_data = nse.get_history(symbol='INFY',index = False, start= date(2022,7,1), end = date(2022,10,1))
print(stock_data)

#getting index price
index_data = nse.get_history(symbol= 'NIFTY',index = True, start = date(2022,7,1), end = date(2022,10,1))
print(index_data)

#getting vix data
vix_data = nse.get_history(symbol = 'INDIAVIX',index = True, start = date(2022,7,1), end = date(2022,10,1))
print(vix_data)

#getting nifty pe
nifty_pe = nse.get_index_pe_history(symbol = 'NIFTY', start = date(2022,7,1), end = date(2022,10,1))
print(nifty_pe)

#getting forex data
forex = nse.get_rbi_ref_history(start= date(2022,7,1), end = date(2022,10,1))
print(forex)

#bhav copy
from nsepy.history import get_price_list
bhav_copy = get_price_list(dt=date(2022,10,20))
bhav_copy.shape[0]

#real time data # mention the symbole
quote = nse.live.get_quote(symbol='INFY')
print(quote)

#getting the indepth data
quote['data']

#converting it into DataFrame
import pandas as pd

Data  = pd.DataFrame(quote['data']).T

