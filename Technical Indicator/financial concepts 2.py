# -*- coding: utf-8 -*-
"""
financial concepts

@author: Vineet
"""

"""
PRESENT VALUE

The present value of an investment which will yield $10,000 15 years from now at an 
inflation rate of 3% per year and assign it to investment_1.

"""
#!pip install numpy-financial
import numpy as np
import numpy_financial as npf

#note that the present value will return negative so we have to multilpy by -1
investment_1 = npf.pv(rate = 0.03 , nper = 15 , pmt = 0 , fv = 10000)

print("Investment 1 is worth:" + str(round( -investment_1,2)) + 'in todays value')

#caluclating the second investment
investment_2 = npf.pv(rate = 0.06 , nper = 15 , pmt = 0 , fv = 10000)
print("Investment 1 is worth:" + str(round( -investment_2,2)) + 'in todays value')


"""
FUTURE VALUE

The present value of the investment It is important to note that in this function call, 
you must pass a negative value into the pv parameter if it represents a negative cash flow (cash going out). 
In other words, if you were to compute the future value of an investment, requiring an up-front cash payment, 
you would need to pass a negative value to the pv parameter in the .fv() function.

"""

"""
calculating the future value of a $10,000 investment returning 5% per year's
for 15 years and assign it to investment_3.

Calculating the future value of a $10,000 investment returning 8% per year
for 15 years and assign it to investment_4.
"""

investment_3 = npf.fv(rate = 0.05, nper = 15 , pmt = 0 ,pv = -10000)
print("Investment 3 will yield a total of $" + str(round(investment_3,2)) + ' in 15 years')

investment_3_discounted = npf.pv(rate=0.03, nper=10, pmt=0, fv=investment_3)
print("After adjusting for inflation, investment 1 is worth $" + str(round(-investment_3_discounted, 2)) + " in today's dollars")

