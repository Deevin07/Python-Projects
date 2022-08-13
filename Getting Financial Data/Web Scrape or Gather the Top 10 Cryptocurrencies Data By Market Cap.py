# -*- coding: utf-8 -*-
"""
Web Scrape or Gather the Top 10 Cryptocurrencies Data By Market Cap Using Python

@author: Vineet
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

#create empty list to store the data
crypto_name_list = []
crypto_market_cap_list = []
crypto_price_list = []
crypto_circulating_supply_list = []
crypto_symbol_list = []

#Create an empty dataframe to organize the data
df = pd.DataFrame()

#create a function to scrape the data
# Example https://coinmarketcap.com/historical/20220731/
def scrape(date = '20220731/'):
  #Get the URL that we want to scrape
  URL = 'https://coinmarketcap.com/historical/' + date
  #Make a request to the URL
  webpage = requests.get(URL)
  #Parse the text from the URL
  soup  = BeautifulSoup(webpage.text,'html.parser')

  #get the table row element
  tr = soup.find_all('tr',attrs = {'class':'cmc-table-row'})

  #Create a count variable for the number of crypto currencies that we want to scrape
  count = 0

  #Loop through every row and gather the info/data
  for row in tr:
    #if count is reached the break the loop
    if count == 10:
      break;
    count = count + 1    #increament by 1

    #Store the name of the crypto and convert it into variable
    #find the td element (or column) to later get the crypto currency name
    name_column = row.find('td',attrs = {'class':"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"})
    crypto_name = name_column.find('a',attrs = {'class':"cmc-table__column-name--name cmc-link"}).text.strip()
    
    #Store the coin market cap of the cryptocurrency or a coin in variable
    crypto_market_cap = row.find('td',attrs = {'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()

    #Find and store the crypto price
    crypto_price = row.find('td',attrs = {'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()
    
    #Find and store crypto supply and symbol
    crypto_ciculating_supply_and_symbol = row.find('td',attrs= {'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()

    #split the data
    crypto_circulating_supply = crypto_ciculating_supply_and_symbol.split(' ')[0]
    crypto_symbol = crypto_ciculating_supply_and_symbol.split(' ')[1]

    #Append the data to the list
    crypto_name_list.append(crypto_name)
    crypto_market_cap_list.append(crypto_market_cap)
    crypto_price_list.append(crypto_price)
    crypto_circulating_supply_list.append(crypto_circulating_supply)
    crypto_symbol_list.append(crypto_symbol)
    
    
#Rate the scrape function
#If you want to change the date from here URL = https://coinmarketcap.com/historical/   then later 
scrape(date = '20211212/')


#Store data into dataframe to help organize the data
df['Name'] = crypto_name_list
df['MarketCap'] = crypto_market_cap_list
df['Price'] = crypto_price_list
df['Cirulating Supply'] = crypto_circulating_supply_list
df['Symbol'] = crypto_symbol_list

#Show the data
print(df)

