# -*- coding: utf-8 -*-
"""

@author: Vineet

@linked in = https://www.linkedin.com/in/vineet-dusa-a266321b5/

"""

import os
import pandas as pd
import numpy as np

os.chdir('C:\\Users\\Vineet\\.spyder-py3')

sales_data = pd.read_excel('sales_data.xlsx')

sales_data['Profit Net Tax'] = np.where(sales_data['Category']=='Furniture',0.8*sales_data['Profit'],
                                        np.where(sales_data['Category']=='Office Supplies',0.7*sales_data['Profit'],
                                                 np.where(sales_data['Category']=='Technology',0.6*sales_data['Profit'],0)))