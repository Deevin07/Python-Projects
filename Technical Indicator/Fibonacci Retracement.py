# -*- coding: utf-8 -*-
"""
Fibonacci Retracement

@author: Vineet
"""
#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import os

#the file path where the csv file is
os.chdir('C:\\Users\\Vineet\\Downloads')

#store the data
df = pd.read_csv('nifty50.csv')

#setting the date as index
df.set_index(pd.DatetimeIndex(df['Date'].values))

#plotting the close price 
plt.figure(figsize = (16,6))
plt.plot(df.Close,color = 'black')
plt.title('Nifty Close price')
plt.xlabel('Date')
plt.ylabel('Price')

#calculate the Fibonacci Retracement level price with non-Fibonacci Level/Ratio of 0.5 or 50%
#fibonachi ratio are 0.236 , 0.382 and 0.618
#example  1,1,2,3,5,8,13,21,34,55,89,144  ====> 89/144 = 0.618
#To get 0.382 take any number in the Fibonacci sequence and divide it by the next number in the sequence 
#example 34/89 ===> 0.236


#first ge the max and min from the time period
maximum_price = df['Close'].max()
minimum_price = df['Close'].min()

difference = maximum_price - minimum_price

first_level = maximum_price - difference * 0.236
second_level = maximum_price - difference * 0.382
third_level = maximum_price - difference * 0.5
fourth_level = maximum_price - difference  * 0.618

#print the price at each level
print('Level\nPercentage       Price')
print('00.0\t\t',maximum_price)
print('23.6%\t\t',first_level)
print('38.2%\t\t',second_level)
print('50.0%\t\t',third_level)
print('61.8%\t\t',fourth_level)
print('100.0%\t\t',minimum_price)

#plot the fibonacci level price along withe the close price
new_df = df
plt.figure(figsize = (12,6))
plt.title('Fibonacci Retracement')
plt.plot(new_df.index,new_df['Close'])

plt.axhline(maximum_price,linestyle = '--',alpha= 0.5, color = 'red')
plt.axhline(first_level,linestyle = '--',alpha= 0.5, color = 'orange')
plt.axhline(second_level,linestyle = '--',alpha= 0.5, color = 'yellow')
plt.axhline(third_level,linestyle = '--',alpha= 0.5, color = 'green')
plt.axhline(fourth_level,linestyle = '--',alpha= 0.5, color = 'blue')
plt.axhline(minimum_price,linestyle = '--',alpha= 0.5, color = 'purple')
plt.xlabel('Date')
plt.ylabel('Price') 