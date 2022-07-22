# -*- coding: utf-8 -*-
"""
Stock price prediction with linear regression 

@author: Vineet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
plt.style.use('fivethirtyeight')
import os

os.chdir('C:\\Users\\Vineet\\Downloads')

df = pd.read_csv('nifty.csv')
df = df.set_index(pd.DatetimeIndex(df['Date'].values))
df.drop(['Date'], axis =1, inplace=True)

#plot the linear regression line and the close price

#making a copy
df3 = df.copy()

#create a new column called'NUMBERS' that ranges from 0 to the length of the data set
df3['Numbers'] = list(range(0,len(df3)))

#store the 'Number' column into a variable called 'X' as an array
x = np.array(df3[['Numbers']])

#storing the close price as an array in a variable 'Y'
y = df3['Close'].values

#creating a linear model
lin_model = LinearRegression().fit(x,y)
print('Intercept',lin_model.intercept_)
print('Slope:', lin_model.coef_)

#prepare the data for visualization
#Get the prediction prices from the model and store them into a variable called y_pred
y_pred =lin_model.coef_ * x + lin_model.intercept_     #y = mx + b

#store the predict value in a new column called 'Pred'
df3['Pred'] = y_pred

#plot the data
df3['Pred'].plot()
df3['Close'].plot()
plt.title('Close Price title')

#how good is the model using the co-efficience of determination
r2_score(df3['Close'],df3['Pred'])

#Show the posssible price for the next day based on the model
price_prediction = lin_model.coef_ * len(df3)+1 + lin_model.intercept_
print("Price Prediction is:",price_prediction)