"""
Markowitz Portfolio Optimazation

@author: Vineet
"""

import pandas as pd 
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt

assets = ['PG','^GSPC']             #ticker you want
pf_data  = pd.DataFrame()

for a in assets:
    pf_data[a] = web.DataReader(a,'yahoo',start= '2012-1-1')['Adj Close'] #getting data of past 10 years
    
log_return = np.log(pf_data / pf_data.shift(1))

num_assets = len(assets)   #number of assets 

#now we will consider 1000 combination of the assets we have

pfolio_return = []
pfolio_volatilty= []

for x in range(1000):
    weights  = np.random.random(num_assets)            # here we re getting the 1 or 100% because portfolios are consider 
    weights /= np.sum(weights)                         # 100%
    pfolio_return.append(np.sum(weights * log_return.mean()) * 250)  #Expected portfolio return
    pfolio_volatilty.append(np.sqrt(np.dot(weights.T,np.dot(log_return.cov() * 250,weights)))) 

pfolio_return = np.array(pfolio_return)
pfolio_volatilty = np.array(pfolio_volatilty) 

#plotting the data

portfolio = pd.DataFrame({'Return':pfolio_return,'Volatility':pfolio_volatilty})

portfolio.plot(x = 'Volatility' , y = 'Return', kind = 'scatter' , figsize= (10,6))
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
                      