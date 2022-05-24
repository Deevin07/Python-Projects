import yfinance as yf
import pandas as pd

tickers = ['AMZN','GOOG','MSFT']
d6 = {}


for ticker in tickers:
    temp = yf.download(ticker, period='7mo',interval='1d')
    temp.dropna(how='any',inplace=True)
    d6[ticker] = temp
    

def CAGR(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    df['cum_return'] = (1 + df['return']).cumprod()
    n = len(df)/252
    CAGR = (df['cum_return'][-1]) ** (1/n) - 1 
    return CAGR 

for ticker in d6:
    print('CAGR for {} = {}'.format(ticker,CAGR(d6[ticker])))
    
    
