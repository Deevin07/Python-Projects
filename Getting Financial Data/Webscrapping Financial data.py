# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:24:12 2022

@author: Vineet
"""

import requests 
from bs4 import BeautifulSoup
import pandas as pd

tickers = ['AAPL','MSFT']            # add the ticker you want the financial data for
financial_dr = {}

#getting the balance sheet from the yahoo finance
 
for ticker in tickers:
    
    temp_dir = {}
    #getting the income statement from the yahoo finance
    url = 'https://finance.yahoo.com/quote/'+ticker+'/financials?p='+ticker
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url,headers = headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,'html.parser')
    tabl = soup.find_all('div',{'class':'M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)'})
    for t in tabl:
        rows = t.find_all('div',{'class':'D(tbr) fi-row Bgc($hoverBgColor):h'})
        for row in rows:
            temp_dir[row.get_text(separator='/').split('/')[0]]=row.get_text(separator='/').split('/')[1]
            
    #getting balance sheet from yahoo finance
    url = 'https://finance.yahoo.com/quote/'+ticker+'/balance-sheet?p='+ticker
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url,headers = headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,'html.parser')
    tabl = soup.find_all('div',{'class':'M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)'})
    for t in tabl:
        rows = t.find_all('div',{'class':'D(tbr) fi-row Bgc($hoverBgColor):h'})
        for row in rows:
            temp_dir[row.get_text(separator='/').split('/')[0]]=row.get_text(separator='/').split('/')[1]
    
    #getting the cash flow statement
    url = 'https://finance.yahoo.com/quote/'+ticker+'/cash-flow?p='+ticker
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url,headers = headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,'html.parser')
    tabl = soup.find_all('div',{'class':'M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)'})
    for t in tabl:
        rows = t.find_all('div',{'class':'D(tbr) fi-row Bgc($hoverBgColor):h'})
        for row in rows:
            temp_dir[row.get_text(separator='/').split('/')[0]]=row.get_text(separator='/').split('/')[1]
    
    #getting key stastical of income statement data
    url = 'https://finance.yahoo.com/quote/'+ticker+'/key-statistics?p='+ticker
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url,headers = headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,'html.parser')
    tabl = soup.find_all('table',{'class':'W(100%) Bdcl(c) '})
    for t in tabl:
        rows = t.find_all('tr')
        for row in rows:
            if len(row.get_text(seperator='/').split('/')[0:2]>0):
                temp_dir[row.get_text(separator='/').split('/')[0]] = row.get_text(seperator='/').split('/')[1]
     
    #combining all extracted data to ticker            
    financial_dr[ticker] = temp_dir

#storing data in pandas dataframe
combined_financials = pd.DataFrame(financial_dr)
tickers = combined_financials.columns
for ticker in tickers:
    combined_financials = combined_financials[~combined_financials[ticker].str.contains('a-z').fillna(False)]
            

data = pd.DataFrame(financial_dr)

data.astype(float)
data1 =data.iloc[[1,2,3,4,5,6,7,8,10,9]]

revenue = data.iloc[1,0] // data.iloc[1,1]  