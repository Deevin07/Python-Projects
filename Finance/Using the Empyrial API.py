# -*- coding: utf-8 -*-
"""
Using the Empyrial API

@author: Vineet
"""

from empyrial import empyrial ,Engine

#usage
portfolio = Engine(
            start_date  = "2018-06-09",
            portfolio = ['TCS.NS','RELIANCE.NS'],
            weights = [0.5,0.5],
            benchmark = ['^NSEI']

)

empyrial(portfolio)

#Calender Rebalancing 

portfolio_1 = Engine(
            start_date  = "2018-06-09",
            portfolio = ['TCS.NS','RELIANCE.NS'],
            weights = [0.5,0.5],
            benchmark = ['^NSEI'],
            rebalance = '1y'                               #periods available for rebalancing are 2y , 1y , 6mo , quaterly , monthly
            )

empyrial(portfolio_1)

#Optimizer
from empyrial import empyrial, Engine
portfolio = Engine(
      start_date = "2018-01-01",
      portfolio= ["RELIANCE.NS", "TCS.NS", "TATAMOTORS.NS", "DEEPAKNTR.NS","ITC.NS"], 
      weights = [0.1, 0.3, 0.15, 0.25, 0.2], #custom weights
      rebalance = "1y" , #rebalance every year,
      benchmark  = ['^NSEI']
)
empyrial(portfolio)