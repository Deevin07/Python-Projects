# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:23:46 2022

@author: Vineet
"""

S = 100 #spot price
T = 1 #time is 1 year
r = 0.07    #discount rate
sigma =0.2      #volatility
Nsimulations  = 5000 #number of simulations
nsteps = 250
k = 100   #strike price

dt = T/nsteps

#using Brownian Motion
import numpy as np

drift = (r - (sigma**2)/2)*dt
a = sigma * np.sqrt(dt)
x = np.random.normal(0,1,(Nsimulations,nsteps))

smat = np.zeros((Nsimulations,nsteps))
smat[:,0]+=S

#implementing brownian motion

for i in range(1,nsteps):
    smat[:,i] += smat[:,i-1] * np.exp(drift + a * x[:,i])

"""
q = pay off for call
p = pay off for put 
"""
#call 
q =  smat[:,-1] - k

for i in range(len(q)):
    if q[i] < 0:
        q[i] = 0
    else:
        q[i] = q[i]

#put option

p =  k - smat[:,-1]  

for i in range(len(p)):
    if p[i] < 0:
        p[i] = 0
    else:
        p[i] = p[i]
        
payoff_call = np.mean(q)
payoff_put = np.mean(p)

call = payoff_call * np.exp(-r/T)
put = payoff_put * np.exp(-r/T)

            