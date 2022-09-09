# -*- coding: utf-8 -*-
"""
using machine learning to simple trading/ investment stratergies
@author: Vineet
"""
#!pip install pytest-warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
plt.style.use('fivethirtyeight')
warnings.filterwarnings('ignore')
import os

#Set the working directory
os.chdir('C:\\Users\\Vineet\\Downloads')

#getting the data
df = pd.read_csv('niftycsv.csv')
df = df.dropna()
#show the data
print(df)

#set the date column as index
df.index = pd.to_datetime(df['Date'])

#Drop the date column
df = df.drop(['Date'] , axis = 'columns')

#Create Independent variable
df['High-Low'] = df['High'] - df['Low']
df['Open-Close'] = df['Open'] - df['Close']

#Store the independent variables in a variables called X
X = df[['High-Low','Open-Close','Close']]

#getting the first 5 of the data
X.head()

#Store the target variable into a variable called 'y'
#If tommorrows close price is greater than todays then 1 other wise 0
y = np.where(df.Close.shift(-1) > df.Close , 1, 0) 

#Get the percentage to split the data (90% train data set and 10% test data set)
percetage_split = 0.9
row = int(df.shape[0] * percetage_split)

#create the train data set
x_train = X[:row]
y_train  = y[:row]

# Create the test data set
x_test = X[row:]
y_test = y[row:]

#import the library from the machine learning model called support vector classifier (SVC)
from sklearn.svm import SVC

#Create the model
model = SVC()

#Train the model
model.fit(x_train[['Open-Close','High-Low']],y_train) 

#Check the score of the model on the test data set
model.score(x_test[['Open-Close','High-Low']],y_test)
   
#make and show the model predictions
df['Predictions'] = model.predict(X[['Open-Close','High-Low']])
df['Predictions']

#calculate the daily returns
df['Returns'] = df['Close'].pct_change()
df['Returns']

#calculate the stratergy returns
df['Strat_Returns'] = df['Predictions'].shift(1) * df['Returns']
df['Strat_Returns']

#Calculate the cummulative returns
df['Cumul_Ret'] = df['Returns'].cumsum()
df['Cumul_Strat'] = df['Strat_Returns'].cumsum()

#Visulizing and showing the data
plt.figure(figsize=(16,8))
plt.title('Returns')
plt.plot(df['Cumul_Ret'],color ='orange' , label = 'Stock Return')
plt.plot(df['Cumul_Strat'],color = 'red', label = 'Stratergy Returns')
plt.xticks(rotation = 45)
plt.legend()
plt.show()

#Print the returns
print('The stock gives a return of = ',df['Cumul_Ret'][-1]*100,'%')
print('The stratergy gives a return of = ',df['Cumul_Strat'][-1]*100,'%')
