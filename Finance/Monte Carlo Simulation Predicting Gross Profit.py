# -*- coding: utf-8 -*-
"""
Monte Carlo Simulation Predicting Gross Profit

@author: Vineet
"""
import numpy as np
import matplotlib.pyplot as plt

rev_m = 170              #assuming revenue of 170million dollars
rev_stddev = 20             #and standard deviation is 20 million dollars
iterations = 1000        #assuming 1000 possible outcomes of these

rev = np.random.normal(rev_m, rev_stddev ,iterations)       #predicting future revenues

plt.figure(figsize = (15,6))
plt.plot(rev)

COGS = - (rev * np.random.normal(0.6,0.1))    #assuming cogs amount 60% of the revenue
                                            # and having a standard deviation of 10% 
                                            #COGS is money spend so minus
plt.figure(figsize = (15,6))
plt.plot(COGS)

# caclulating mean and Standard deviation

COGS.mean()
COGS.std()

#difference between revenue and cogs gives us gross profit

Gross_Profit = rev + COGS          #adding here because we have used minus while calculating COGS
Gross_Profit


plt.figure(figsize = (15,6))
plt.plot(Gross_Profit)

max(Gross_Profit)
min(Gross_Profit)

Gross_Profit.mean()
Gross_Profit.std()

plt.figure(figsize = (10,6))
plt.hist(Gross_Profit,bins = 20)