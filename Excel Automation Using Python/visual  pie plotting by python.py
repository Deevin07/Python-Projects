# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:36:18 2022

@author: Vineet
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\Vineet\\.spyder-py3')

sales_data = pd.read_excel('sales_data.xlsx')

fig , (ax1,ax2) = plt.subplots(nrows = 1, ncols = 2)
fig.suptitle('Sales Breakdown by Category & Segments')


def fmt_wdges(data):
    def fmt_values(pct):
        total = sum(data)
        abs_value = round(pct*total/100000,1)
        return '${}K'.format(abs_value)
    return fmt_values

ax1.set_title('Category Level Sales \n Breakdown')
data = sales_data.groupby('Category')['Sales'].sum().to_list()
labels = sales_data.groupby('Category')['Sales'].sum().index
explode =  [0 if x!=max(data) else 0.1 for x in data]
ax1.pie(data,labels = labels , autopct = fmt_wdges(data),explode = explode)


ax2.set_title('Segment Level Sales \n Breakdown')
data = sales_data.groupby('Segment')['Sales'].sum().to_list()
labels = sales_data.groupby('Segment')['Sales'].sum().index
explode = [0 if x!=max(data) else 0.1 for x in data]
ax2.pie(data,labels = labels,autopct = '%.2f%%',explode = explode)
ax2.legend(labels, bbox_to_anchor = (1,0,1,0.5))
