# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:33:06 2022

@author: Vineet
"""

import os 
import pandas as pd

os.chdir('C:\\Users\\Vineet\\.spyder-py3')

sales_data = pd.read_excel('sales_data.xlsx')

# extract subtring from a text column left right and mid
sales_data['Order ID'].str[3:7]   # mid function
sales_data['Order ID'].str[:2]    # left fucntion
sales_data['Order ID'].str[-6:]   # right function
sales_data['Order ID'].str.split('-').str[0]         # 0,1,2 for left mid and reight respectively

#trim trailing and stoploss  
sales_data['Order ID'].str.strip()

#concatenate
sales_data['State']+'_'+sales_data['City']

#captilize
sales_data['State'].str.upper() # for upper case
sales_data['State'].str.lower() # for lower case

#find a string
sales_data['City'].str.find('Fort') # if find then zero if not then -1