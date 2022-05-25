# -*- coding: utf-8 -*-
"""

@author: Vineet
"""


import os 
import pandas as pd

os.chdir('C:\\Users\\Vineet\\.spyder-py3')

sales_data = pd.read_excel('sales_data.xlsx',index_col='Row ID')

#count if
sales_data[sales_data['Quantity']>5]

len(sales_data[sales_data['Quantity']>5])

sales_data[sales_data['Quantity']>5].shape[0]

#count if

len(sales_data[(sales_data['State']=='Kentucky') &(sales_data['Quantity']>5)])

#sum if
sales_data[sales_data['City'].str[:4] == 'Fort']['Profit'].sum()
sales_data.loc[sales_data['City'].str[:4] == 'Fort','Profit'].sum()

#sums ifs
sales_data[(sales_data['City'].str[:4] == 'Fort') & (sales_data['Quantity']>5)]['Profit'].sum()
