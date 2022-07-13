# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 19:46:13 2022

@author: Vineet
"""

#!pip install scikit-learn
#!pip install keras
#!pip install --upgrade pandas-datareader

import pandas as pd
import math
import pandas_datareader as web
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential 
from keras.layers import Dense ,LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


#getting the stock data
df = web.DataReader('AAPL',data_source = 'yahoo',start='2012-01-01',end = '2019-12-17')                   #yyyy-mm-dd

#show the data
print(df)

#visualizing the data
plt.figure(figsize=(16,8))
plt.title('Closing price of Apple')
plt.plot(df['Close'])
plt.xlabel('Date',fontsize=18)
plt.ylabel('Closing Price in INR',fontsize=18)
plt.show()

#Creating a dataframe for closing price
data = df.filter(['Close'])

#converting dataframe into a numpy array
dataset = data.values

#getting the rows to train for the lstm model
training_data_len = math.ceil(len(dataset)*.8)

print(training_data_len)

#Scale the data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

print(scaled_data)

#Crating the training data set
# 1. Creating the scaled training data set

train_data = scaled_data[0:training_data_len, :]  #getting all the 1603 data set i.e 80% of the data

#splitting the data into x_train and y_train

x_train = []
y_train = []

for i in range(60,len(train_data)):
  x_train.append(train_data[i-60:i,0])   #first 60 values from position 1 to 59
  y_train.append(train_data[i,0])        # contains the value at position 60
  if i<=61:
    print(x_train)            #printing the first 60 
    print(y_train)            # printing the 60th number
    print()
    
#conerting the x_train and y_train in np array
x_train , y_train = np.array(x_train) , np.array(y_train)

#reshaping the data from 2D to 3D bcoz the LSTm model needs 3D data set
x_train = np.reshape(x_train , (x_train.shape[0],x_train.shape[1],1))
print(x_train.shape)

#Building the LSTM model
model = Sequential()

model.add(LSTM(50,return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(50,return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

#compile the model
model.compile(optimizer='adam',loss='mean_squared_error')

#train the model
model.fit(x_train,y_train, batch_size=1,epochs = 1)

#Creating the dataset
#Creating the new array containing scaled values from 1543 to 2003
test_data = scaled_data[training_data_len - 60: , :]

#creating the datasets x_test and y_test

x_test = []
y_test = dataset[training_data_len:,:]

for i in range(60,len(test_data)):
  x_test.append(test_data[i-60:i,0])
  
#Converting the data into numpy array
x_test =  np.array(x_test)

#reshaping the data
x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

#getting the model to predicted price value
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

#getting the root mean square error(RMSE)
rmse = np.sqrt( np.mean( predictions - y_test)**2)
print(rmse)

#plotting the data
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions

#visualizing the data
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date',fontsize = 18)
plt.ylabel('Close Price', fontsize = 18)
plt.plot(train['Close'])
plt.plot(valid[['Close','Predictions']])
plt.legend(['Train','Actual Value','Predictions'])
plt.show()

#show the valid and predicted prices
print(valid)



#get the quote
apple_quote = web.DataReader('AAPL',data_source = 'yahoo',start = '2012-01-01',end='2019-12-17')

#Create a new dataframe 
new_df = apple_quote.filter(['Close'])

#get the last 60 days closing value and convert them in an array
last_60_days = new_df[-60:].values              #.values se array mai convert ho rha hai

#scale the data from 0 to 1 
last_60_days_scaled =  scaler.transform(last_60_days)

#creating an empty list
X_test = []

#append the past 60 days value
X_test.append(last_60_days_scaled)

#comverting the X_test data into numpy array
X_test = np.array(X_test)

#reshape the data
X_test = np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

#predicted scaled price
pred_price = model.predict(X_test)

#undo the scaling
pred_price = scaler.inverse_transform(pred_price)

print(pred_price)             #predicing the price next to the end date

#checking the data
apple_quote2 = web.DataReader('AAPL',data_source = 'yahoo',start = '2012-01-01',end='2019-12-18')
apple_quote2.tail()



