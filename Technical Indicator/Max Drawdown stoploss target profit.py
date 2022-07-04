# -*- coding: utf-8 -*-
"""
Max Drawdown
Stop loss
Take Profit

@author: Vineet
"""

#Max Drawdown
from empyrial import empyrial, Engine
portfolio = Engine(
      start_date = "2018-01-01",
      portfolio= ["RELIANCE.NS", "TCS.NS", "TATAMOTORS.NS", "DEEPAKNTR.NS","ITC.NS"],
      benchmark  = ['^NSEI'],
      risk_manager = {'Max Drawdown': - 0.2}                               #max draw down of 20%
)
empyrial(portfolio)


#Take Profit
from empyrial import empyrial, Engine
portfolio = Engine(
      start_date = "2018-01-01",
      portfolio= ["RELIANCE.NS", "TCS.NS", "TATAMOTORS.NS", "DEEPAKNTR.NS","ITC.NS"],
      benchmark  = ['^NSEI'],
      optimizer= 'EF',
      rebalance = '1y',
      risk_manager = {'Stop Loss': - 0.2}   #Stop the investment when the loss becomes superior to 20%
)
empyrial(portfolio)

#take Profit
from empyrial import empyrial, Engine
portfolio = Engine(
      start_date = "2018-01-01",
      portfolio= ["RELIANCE.NS", "TCS.NS", "TATAMOTORS.NS", "DEEPAKNTR.NS","ITC.NS"],
      benchmark  = ['^NSEI'],
      optimizer= 'EF',
      rebalance = '1y',
      risk_manager = {'Take Proftit': 0.25}   #Stop the investment when the loss becomes superior to 20%
)
empyrial(portfolio)