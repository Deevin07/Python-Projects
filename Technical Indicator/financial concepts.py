# -*- coding: utf-8 -*-
"""
Introducing financial concept

@author: Vineet
"""

"""
At first we are calulating growth and rate of return

Calculate the future value (cumulative return) of a $100 investment
which grows at a rate of 6% per year for 30 years in a row and assign it to future_value.

"""
#calulating the future value and printing it out

initial_investment_1 = 100
rate_of_return_1 = 0.06
time_1 = 30

future_value = initial_investment_1 * (1 + rate_of_return_1) ** time_1
print('Future Value of Investment is: ' +   str(round(future_value,2)))

#calulating COMPOUND INTEREST

initial_investment_2 = 100
growth_period = 30
growth_rate  = 0.06

#calculating the value for the investment compounded once per year
compound_periods_1 = 1  

investemt_1 = initial_investment_2 * (1 + growth_rate / compound_periods_1) ** (compound_periods_1 * growth_period)
print('Investemt 1: ' + str(round(investemt_1,2)))

#calculating the value for the investment compounded quaterly
compound_periods_2 = 4  

investemt_2 = initial_investment_2 * (1 + growth_rate / compound_periods_2) ** (compound_periods_2 * growth_period)
print('Investemt 1: ' + str(round(investemt_1,2)))
print('Investemt 2: ' + str(round(investemt_2,2)))