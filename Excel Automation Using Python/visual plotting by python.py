# -*- coding: utf-8 -*-
"""

@author: Vineet Dusa

@linked in = https://www.linkedin.com/in/vineet-dusa-a266321b5/

"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as trk

os.chdir('C:\\Users\\Vineet\\.spyder-py3')

sales_data = pd.read_excel('sales_data.xlsx')


fig = plt.figure()
fig.suptitle('City Level Performance',x=0,y=1)

def newticks(x,pos):
    return "${}.K".format(round(x/1000))


ax1 = fig.add_axes([0,0,1,0.89])
ax1.set_title('Top Cities')
ax1.yaxis.label.set_visible(False)
ax1.set_xlabel('Sales')
ax1.axvline(x=100000,color = 'black',ls='--')
ax1.xaxis.set_major_formatter(trk.FuncFormatter(newticks))

ax2 = fig.add_axes([0.6,0.56,0.25,0.25])
ax2.set_title('Lagger  Cities')
ax2.xaxis.label.set_visible(False)

sales_data.groupby('City')['Sales'].sum().sort_values(ascending = False).iloc[:15].plot(kind = 'barh',ax =ax1, color = 'green')
sales_data.groupby('City')['Sales'].sum().sort_values(ascending = True).iloc[:5].plot(kind = 'bar',ax =ax2,color= 'red')