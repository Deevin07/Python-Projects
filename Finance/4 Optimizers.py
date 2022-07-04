# -*- coding: utf-8 -*-
"""
4 Optimizers

@author: Vineet
"""

from empyrial import empyrial ,Engine

#Global Efficient Frontier

portfolio = Engine(
            start_date  = "2018-06-09",
            portfolio = ['TCS.NS','RELIANCE.NS'],
            weights = [0.5,0.5],
            benchmark = ['^NSEI'],
            optimizer  = "EF"
)

empyrial(portfolio)

portfolio.weights


#mean varience
portfolio = Engine(
            start_date  = "2018-06-09",
            portfolio = ['TCS.NS','RELIANCE.NS'],
            weights = [0.5,0.5],
            benchmark = ['^NSEI'],
            optimizer  = "MEANVAR",
            max_vol = 0.25
)

empyrial(portfolio)

#Hierarchical Risk Parity
portfolio = Engine(
            start_date  = "2018-06-09",
            portfolio = ['TCS.NS','RELIANCE.NS'],
            weights = [0.5,0.5],
            benchmark = ['^NSEI'],
            optimizer  = "HRP",
            
)

empyrial(portfolio)


#Minimum - Varience 
portfolio = Engine(
            start_date  = "2018-06-09",
            portfolio = ['TCS.NS','RELIANCE.NS'],
            weights = [0.5,0.5],
            benchmark = ['^NSEI'],
            optimizer  = "MINIVAR",
            
)

empyrial(portfolio)
