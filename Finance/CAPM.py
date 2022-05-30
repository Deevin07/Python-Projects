# -*- coding: utf-8 -*-
"""
CAPM

@author: Vineet
"""
# -*- coding: utf-8 -*-
"""
Calculating Beta

@author: Vineet
"""

import numpy as np
import pandas as pd
import pandas_datareader.data as web

assets = ['^NSEI','RELIANCE.NS']                 # add your ticker
data = pd.DataFrame()

for a in assets:
    data[a] = web.DataReader(a,'yahoo',start = '2012-1-1' , end = '2016-12-31')['Adj Close'] # getting 5 years of data
    

sec_returns = np.log(data /data.shift(1))

cov = sec_returns.cov() * 250

cov_with_market = cov.iloc[0,1]

market_var = sec_returns['^NSEI'].var() * 250

beta = cov_with_market  / market_var

#risk_free_rate  = 2.75 = 2.75/100 = 0.0275
#equity_risk_premium_today = 6.42 = 0.062

CAPM = 0.0275 + beta * 0.062 


