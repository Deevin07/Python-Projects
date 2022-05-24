# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:31:29 2022

@author: Vineet
"""

import pandas as pd

data = pd.read_excel('sales_data.xlsx', sheet_name = 'Orders', index_col='Row ID')

data['month_year'] = data['Order Date'].dt.strftime('%m-%Y')
data.columns

od_data = data.groupby('month_year')

od_data.groups


ls = []
for df in od_data.groups:
    ls.append(od_data.get_group(df))
    
for df in ls:
    file_name = df['month_year'].iloc[0]
    df.to_excel('{}.xlsx'.format(file_name),index = False)