# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:32:36 2022

@author: Vineet
"""

import nsepy as nse
from datetime import date

"""
Here the expiry dates are very important, before adding the dates see the expiry dates of the 
futures and then add and also see that the expiry data is in between the start and the end date

"""
#getting futures data fro stock
stock_fut = nse.get_history(symbol = 'SBIN',index = False, start= date(2022,7,30), end = date(2022,9,30),
                            futures=True ,expiry_date= date(2022,9,29))

print(stock_fut)

#getting the index futures
index_fut = nse.get_history(symbol = 'NIFTY',index = True, start= date(2022,7,30), end = date(2022,9,30),
                            futures=True ,expiry_date= date(2022,9,29))

print(index_fut)

#getting future chain table
future_chain  = nse.live.get_futures_chain_table(symbol='SBIN')
print(future_chain)

#getting the expiry dates
expiry_dates = nse.derivatives.get_expiry_date(year = 2022, month = 10)
print(expiry_dates)

#getting stock option data "CE"
stock_opt_CE =nse.get_history(symbol = 'SBIN', start = date(2022,7,30),end = date(2022,9,30),index = False,option_type = 'CE'
                           ,strike_price = 500,expiry_date= date(2022,9,29))

print(stock_opt_CE)

#getting stock option data "PE"
stock_opt_PE =nse.get_history(symbol = 'SBIN', start = date(2022,7,30),end = date(2022,9,30),index = False,
                            option_type = 'PE',
                           strike_price = 500,expiry_date= date(2022,9,29))

print(stock_opt_PE)

#getting index option data "CE"
stock_opt_CE =nse.get_history(symbol = 'NIFTY', start = date(2022,7,30),end = date(2022,9,30),index = True,option_type = 'CE'
                           ,strike_price = 17500,expiry_date= date(2022,9,29))

print(stock_opt_CE)

#getting stock option data "PE"
stock_opt_PE =nse.get_history(symbol = 'NIFTY', start = date(2022,7,30),end = date(2022,9,30),index = True,option_type = 'PE'
                           ,strike_price = 17500,expiry_date= date(2022,9,29))

print(stock_opt_PE)
