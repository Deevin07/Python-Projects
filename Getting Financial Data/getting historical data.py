import pandas as pd
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
                                    
stocks = ['AMZN','MSFT','INTC','GOOG','INFY.NS','FB']           # here you can add the ticker for any stock 
start = datetime.datetime.today()-datetime.timedelta(3650)           # we are getting the data of past 10 years
end = datetime.datetime.today()
cl_price = pd.DataFrame()           #getting store all data frame here
                                    
#looping through and creating a data frame and for each ticker
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)['Adj Close']
                                        
#dropping all the NAN values
cl_price.dropna(axis = 0,how = 'any',inplace=True) 

#Calculating the return
daily_return =  cl_price.pct_change() # Creates dataframe with daily return for each stocks

#plotting the data
cl_price.plot(title='Title')

#plotting daily return
daily_return.plot(title='Daily Return', grid=True,subplots = True, layout =(3,3))

#cumulative return
(1+daily_return).cumprod().plot()

#Visualization

plt.style.use('ggplot')
plt.bar(x=daily_return.columns , height=daily_return.mean())