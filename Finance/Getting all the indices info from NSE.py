# -*- coding: utf-8 -*-
"""
Getting all the indices info from NSE

@author: Vineet
"""


from nsetools import Nse
import pandas  as pd, numpy as np

nse = Nse()
print(nse)


index_info = pd.DataFrame(nse.get_advances_declines())

lastPrice , change , pChange = [], [] , []

for i in list(index_info['indice']):
    try:
        temp = nse.get_index_quote(i) 
        lastPrice.append(temp['lastPrice'])
        change.append(temp['change'])
        pChange.append(temp['pChange'])
    except:
        lastPrice.append(np.NAN)
        change.append(np.NAN)
        pChange.append(np.NaN)
        
index_info['lastPrice']  = lastPrice
index_info['change']  = change
index_info['pChange'] = pChange

print(index_info)