# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 20:43:18 2022

@author: Vineet
"""

import pandas as pd
import numpy 
import matplotlib.pyplot as plt

#creating list
Year = []
Yearly_Income = []
Yearly_Expenses = []
Annual_Returns = []
Yearly_Investments = []

#all the inputs
income = 35000     #annual income
expense = income / 2    #assuming half the income goes in expenses
interest_rate = 0.08         #taking 8% as an interest rate per year
investment = income / 2       #assuming half the income goes to investment
annual_return = investment * interest_rate #calculating the annual return
year = 2022

#append the first values to the list
Year.append(year)
Yearly_Income.append(income)
Yearly_Expenses.append(expense)
Yearly_Investments.append(investment)
Annual_Returns.append(annual_return)

#Loop for n years

invested_years = 20   #doing this for 20 years

for i in range(0,invested_years-1):
  #update the investment to the previous investment plus the previous annual return  plus half of your income
  investment = investment + annual_return + income / 2      
  #Update the annual return to the current investment time the interest rate
  annual_return = investment * interest_rate

  #append the new data to the list
  Year.append(year + i + 1 )
  Yearly_Income.append(income)
  Yearly_Expenses.append(expense)
  Yearly_Investments.append(investment)
  Annual_Returns.append(annual_return)
  
#Creating a data frame
df= pd.DataFrame()
df['Year'] = Year
df['Yearly_Income'] = Yearly_Income
df['Yearly_Expenses'] = Yearly_Expenses
df['Yearly_Investment'] = Yearly_Investments
df['Annual_Returns'] = Annual_Returns

print(df)

#visualzing the data
plt.figure(figsize=(16,6))
plt.plot(df['Year'],df['Yearly_Expenses'], label = 'Yearly_Expenses')
plt.plot(df['Year'],df['Annual_Returns'], label = 'Annual_Returns')
plt.xticks(rotation = 45)
plt.title('Retire Planning')
plt.xlabel('Years')
plt.ylabel('Rupees')
plt.xticks(df['Year'])
plt.legend()
plt.show()  


#show the year/row where you can live with returns
df[df.Yearly_Expenses <= df.Annual_Returns].head(1)