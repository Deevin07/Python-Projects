# -*- coding: utf-8 -*-
"""
Created on Fri May 20 23:19:00 2022

@author: Vineet
"""

import pandas as pd
import numpy as np

commute = pd.read_excel('commute.xlsx',sheet_name='Sales',index_col='Date')

commute.replace(['Yes','No'],[1,0], inplace= True)             # replacing yes no with 1 and zero


x = np.array(commute)         # converting daily data to 2D array
y =  np.array([8,3,0.5,12])   # converting pricing into 1D array

daily_expense = x.dot(y)      #calculating the dot product

daily_expense.sum()        # calculating the overall expense of the month

max_expense = daily_expense.argmax()       # index with the highest expense

commute['daily expenses'] = daily_expense

commute.index[daily_expense.argmax()].strftime('%Y-%m-%d') # getting the data with highest expense of the month 