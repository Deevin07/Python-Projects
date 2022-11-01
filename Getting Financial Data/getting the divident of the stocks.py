# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:12:02 2022

@author: Vineet
"""

import pandas as pd
import os

os.chdir('C:\\Users\\Vineet\\Downloads')

divd = pd.read_csv('Corporate_Actions (1).csv')

divd.columns = divd.columns.str.strip()

divd.columns
#removing the uncessory data
divd.drop (labels = ['Record Date', 'BC Start Date', 'BC End Date', 'ND Start Date',
 'ND End Date', 'Actual Payment Date'],inplace = True,axis = 1)

#getting the div value
divd['div_value'] = divd.apply(lambda x : x['Purpose'].split('-')[-1].strip(),axis=1) 

#saving it in excel
divd.to_csv('div_data.csv')

