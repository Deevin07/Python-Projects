# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:11:09 2022

@author: Vineet
"""

#!pip install pycaret
#!pip install markupsafe==2.0.1
#!pip install jinja2
"""
did this project in google colab

"""

import jinja2
from pycaret.regression import *
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from google.colab import files
files.upload()

# read the data
asset = pd.read_csv('niftycsv.csv')

#setting the date as index
asset = asset.set_index(pd.DatetimeIndex(asset['Date'].values))

#show the data
asset

#making a copy of the data
df3  = asset.copy()

#Store the data in the feature data and the set 'X' and add in the target column
#here we are taking the date and open as features and close as the target
X = np.array(df3[['Date','Open','Close']])

#store the close price in the variable 'y' as set that as target
y = df3['Close'].values

#spliting the data into 85% training and remaining 15% for testing
x_train, x_test , y_train , y_test  = train_test_split(X, y, test_size = 0.15 , random_state = 0 , shuffle = False)

#get the train data and transform it to dataframe 
train_data = pd.DataFrame(x_train , columns = ['Date', 'Open' , 'Close'])

#show the first 7 rows of data
train_data.head(7)

#get the test data and transform it to dataframe 
test_data = pd.DataFrame(x_test , columns = ['Date', 'Open' , 'Close'])

#show the first 7 rows of data
test_data.head(7)

#initialize the setup
s = setup(data = train_data ,target=  'Close' ,session_id = 123 , use_gpu = True)

#train on multiple models
#lower the mean squre error the better
compare_models(sort = 'MSE')

#Create the model
par = create_model('par')

#getting the predictions
predict_model(par , data =test_data.drop(['Close'],axis = 1)) 

 #show the actual values
test_data['Close']

#creating a 2 model
en = create_model('en')

predict_model(en , data =test_data.drop(['Close'],axis = 1)) 