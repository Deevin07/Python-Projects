# -*- coding: utf-8 -*-
"""
Getting the data from NSE

@author: Vineet
"""

from nsetools import Nse
import pandas  as pd, numpy as np

nse = Nse()
print(nse)

#getting the information about a Indian Stock Listed Company
info = nse.get_quote('infy')      #add the symbol of the company you want data of
print(info)

#want to get all the stock codes/ticker/symbol
code = pd.Series(nse.get_stock_codes())

#get to know how many companies of an index have changed 
adv_dec = pd.DataFrame(nse.get_advances_declines())

#want to get the list of all the indexes 
index = pd.Series(nse.get_index_list())

#want to get info about particular index
index_info = nse.get_index_quote('Nifty 50')  #just add the index name 

#get top gainers 
top_gainers = pd.DataFrame(nse.get_top_gainers()) 

#get top lossers
top_lossers = pd.DataFrame(nse.get_top_losers())

#get pre open nifty 
pre_open = pd.DataFrame(nse.get_preopen_nifty())

#get pre open bank nifty
pre_open_bank = pd.DataFrame(nse.get_preopen_niftybank())





