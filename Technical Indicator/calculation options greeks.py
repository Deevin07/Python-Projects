# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 20:04:03 2022

@author: Vineet

here we are trying to find the option greeks

all we need is [Underlying Price, Call / Put Strike Price, Interest Rate, Days To Expiration], Call / Put Volatility)

formula for caluclating the option greeks

mibian.BS([Underlying Price, Strike Price, Interest Rate, Daystoexpiration], Call Price, Put Price, volatility)


underlying_price = 8572
call_strike = 8700
put_strike = 8500
call_price = 616.05
put_price = 654.05
interest_rate = 0% (as we are taking futures prices as underlying)
days_to_expiry = 31

"""
 
import mibian
call = mibian.BS([8572,8700,0,31], callPrice = 616.05)
print(f'the volality for call option = {call.impliedVolatility}')

put = mibian.BS([8572,8500,0,31], putPrice = 654.05)
print(f'the volality for put option = {put.impliedVolatility}')

call_greek = mibian.BS([8572, 8700, 0, 31], volatility = 67.65)
print(f'price = {call_greek.callPrice}')
print(f'delta = {call_greek.callDelta}')
print(f'Theta  = {call_greek.callTheta}')
print(f'vega = {call_greek.vega}')
print(f'gamma = {call_greek.gamma}')


#put greeks
p = mibian.BS([8572, 8500, 0, 31], volatility = 69.60)
print(p.callPrice)
print(p.callDelta)
print(p.callTheta)
print(p.vega)
print(p.gamma)