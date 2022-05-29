"""

@author: Vineet
"""

import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os

os.chdir('C:\\Users\\Vineet\\Downloads')

data = pd.read_excel('Housing.xlsx')

data[['House Price','House Size (sq.ft.)']]

#Univariate regression

x = data['House Size (sq.ft.)']
y = data['House Price']

#plotting the scatter graph

plt.scatter(x,y)
plt.axis([0,2500,0,1500000])       #on x axis go till 2500 and on y axis go till 1500000
plt.xlabel('House Size (sq.ft.)')
plt.ylabel('House Price')

#Computing alpha beta and R sqaure 
x1  = sm.add_constant(x)
reg  = sm.OLS(y,x1).fit()

reg.summary()

260800 + 402 * 1000
# you will get 662800

