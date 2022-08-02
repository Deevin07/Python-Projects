# -*- coding: utf-8 -*-
"""
Determine the worst and the best dates for the Nifty 50

@author: Vineet
"""

#importing the libaries
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import os
import calendar

#changing the path where the csv file is located
os.chdir('C:\\Users\\Vineet\\Downloads')

#create lists to store the daily simple returns for each day
Mon = []
Tues = []
Wed = []
Thur = []
Fri = []
Sat = []
Sun = []

#Create a function to get the daily simple return for each day and append it to corresponding day
def get_dsr(day,dsr):
    
    if day == 'Monday':
        Mon.append(float(dsr))
    elif day == 'Tuesday':
        Tues.append(float(dsr))
    elif day == 'Wednesday':
        Wed.append(float(dsr))
    elif day == 'Thursday':
        Thur.append(float(dsr))
    elif day == 'Friday':
        Fri.append(float(dsr))
    elif day == 'Saturday':
        Sat.append(float(dsr))
    elif day == 'Sunday':
        Sun.append(float(dsr))
    else:
        print('Something is wrong with the input of the day')
        
#load the data
df = pd.read_csv('niftycsv.csv')

#set the date as the index
df = df.set_index(pd.DatetimeIndex(df['Date'].values))

#calulate the daily simple return
DSR = df['Close'].pct_change()
df['DSR'] = DSR

#getting rid of the first row
df = df[1:]

#create a loop to gather the daily simple return of each day from the data set
for i in range(0,len(df)):
    df_date = str(df.index[i])      #get the current date and casting it as a string
    df_dsr = df['DSR'][i]           #get the current daily simple return
    df_month = df_date.split('-')   #get the current month
    curr_date = df.index[i]         #get the current date
    df_weekday = calendar.day_name[curr_date.weekday()]  #get the weekday

    #add the daily simple return to the curresponding list of the day
    get_dsr(df_weekday,df_dsr)


#create a function to average the returns of each weekday
def AVG(day):
    if not day:  #if true then the list is empty so return a list containing 0
        return [0]
    else:
        return [sum(day) / len(day)]

#create a new dataframe and set the index to the days of the week
df_returns = pd.DataFrame(index = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])

#Get the average for the weekday and add the values under the column called AVG
df_returns['AVG'] = AVG(Mon) + AVG(Tues) + AVG(Wed) + AVG(Thur) + AVG(Fri) + AVG(Sat) + AVG(Sun)

#plotting the AVG daily return
df_returns.plot.bar()           #run this particular line to see the graph


"""
Interpretation from the graph

Monday is the best day to buy and wednesday is best day to sell

"""