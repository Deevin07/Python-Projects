import requests
from bs4 import BeautifulSoup
import pandas as pd
tickers = ["AXP","AAPL","BA","CAT","CVX","CSCO","DIS","DOW", "XOM",
           "HD","IBM","INTC","JNJ","KO","MCD","MMM","MRK","MSFT",
           "NKE","PFE","PG","UNH","VZ","V","WMT","WBA"]

#list of tickers whose financial data needs to be extracted
financial_dir = {}

for ticker in tickers:
    try:
        print("scraping financial statement data for ",ticker)
        #getting balance sheet data
        url = "https://stockrow.com/api/companies/{}/financials.xlsx?dimension=A&section=Balance%20Sheet&sort=desc".format(ticker)
        df1 = pd.read_excel(url)
        #getting income statement data
        url = "https://stockrow.com/api/companies/{}/financials.xlsx?dimension=A&section=Income%20Statement&sort=desc".format(ticker)
        df2 = pd.read_excel(url)
        #getting cashflow statement data
        url = "https://stockrow.com/api/companies/{}/financials.xlsx?dimension=A&section=Cash%20Flow&sort=desc".format(ticker)
        df3 = pd.read_excel(url)
        
        #getting key statistics data from yahoo finance for the given ticker
        temp_dir = {}
        url = 'https://finance.yahoo.com/quote/'+ticker+'/key-statistics?p='+ticker
        headers={'User-Agent': "Mozilla/5.0"}
        page = requests.get(url, headers=headers)
        page_content = page.content
        soup = BeautifulSoup(page_content,'html.parser')
        tabl = soup.findAll("table", {"class": "W(100%) Bdcl(c) "}) # try to remove the leading space if the code breaks "class": "W(100%) Bdcl(c)"
        for t in tabl:
            rows = t.find_all("tr")
            for row in rows:
                if len(row.get_text(separator='|').split("|")[0:2])>0:
                    temp_dir[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[-1]
                    
        url = 'https://finance.yahoo.com/quote/'+ticker+'?p='+ticker
        headers={'User-Agent': "Mozilla/5.0"}
        page = requests.get(url, headers=headers)
        page_content = page.content
        soup = BeautifulSoup(page_content,'html.parser')
        tabl = soup.findAll("table", {"class": "W(100%) M(0) Bdcl(c)"}) # try to remove the leading space if the code breaks "class": "W(100%) Bdcl(c)"
        for t in tabl:
            rows = t.find_all("tr")
            for row in rows:
                if len(row.get_text(separator='|').split("|")[0:2])>0:
                    temp_dir[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[-1]
                    
        df4 = pd.DataFrame(temp_dir.items(),columns=df3.columns[0:2])
        df4.iloc[:,1] = df4.iloc[:,1].replace({'M': 'E+03','B': 'E+06','T': 'E+09','%': 'E-02'}, regex=True)
        df4.iloc[:,1] = pd.to_numeric(df4.iloc[:,1],errors="coerce")
        df4 = df4[df4["Unnamed: 0"].isin(["Market Cap","Forward Annual Dividend Yield"])]
        
        #combining all extracted information with the corresponding ticker
        df = pd.concat([df1,df2,df3,df4]).iloc[:,[0,1]]
        columns = df.columns.values
        for i in range(len(columns)):
            if columns[i] == "Unnamed: 0":
                columns[i] = "heading"
            else:
                columns[i] = columns[i].strftime("%Y-%m-%d")
        df.columns = columns
        df.set_index("heading",inplace=True)
        financial_dir[ticker] = df
    except Exception as e:
        print(ticker,":", e)


# creating dataframe with relevant financial information for each stock using fundamental data
stats = ["EBITDA",
         "Depreciation & Amortization",
         "Market Cap",
         "Net Income Common",
         "Operating Cash Flow",
         "Capital expenditures",
         "Total current assets",
         "Total current liabilities",
         "Property, Plant, Equpment (Net)",
         "Shareholders Equity (Total)",
         "Long Term Debt (Total)",
         "Forward Annual Dividend Yield"] # change as required

indx = ["EBITDA","D&A","MarketCap","NetIncome","CashFlowOps","Capex","CurrAsset",
        "CurrLiab","PPE","BookValue","TotDebt","DivYield"]

def info_filter(df,stats,indx):
    """function to filter relevant financial information
       df = dataframe to be filtered
       stats = headings to filter
       indx = rename long headings
       lookback = number of years of data to be retained"""
    for stat in stats:
        if stat not in df.index:
            return
    df_new = df.loc[stats,:]
    df_new.rename(dict(zip(stats,indx)),inplace=True)
    return df_new

#applying filtering to the finacials and calculating relevant financial metrics for each stock
transformed_df = {}
for ticker in financial_dir:
    transformed_df[ticker] = info_filter(financial_dir[ticker],stats,indx)
    if transformed_df[ticker] is None:
        del transformed_df[ticker]
        continue
    transformed_df[ticker].loc["EBIT",:] = transformed_df[ticker].loc["EBITDA",:] - transformed_df[ticker].loc["D&A",:]
    transformed_df[ticker].loc["TEV",:] =  transformed_df[ticker].loc["MarketCap",:] + \
                                           transformed_df[ticker].loc["TotDebt",:] - \
                                           (transformed_df[ticker].loc["CurrAsset",:]-transformed_df[ticker].loc["CurrLiab",:])
    transformed_df[ticker].loc["EarningYield",:] =  transformed_df[ticker].loc["EBIT",:]/transformed_df[ticker].loc["TEV",:]
    transformed_df[ticker].loc["FCFYield",:] = (transformed_df[ticker].loc["CashFlowOps",:]-transformed_df[ticker].loc["Capex",:])/transformed_df[ticker].loc["MarketCap",:]
    transformed_df[ticker].loc["ROC",:]  = (transformed_df[ticker].loc["EBITDA",:] - transformed_df[ticker].loc["D&A",:])/(transformed_df[ticker].loc["PPE",:]+transformed_df[ticker].loc["CurrAsset",:]-transformed_df[ticker].loc["CurrLiab",:])
    transformed_df[ticker].loc["BookToMkt",:] = transformed_df[ticker].loc["BookValue",:]/transformed_df[ticker].loc["MarketCap",:]

################################Output Dataframes##############################
final_stats_val_df = pd.DataFrame(columns=transformed_df.keys())
for key in transformed_df:
    final_stats_val_df[key] = transformed_df[key].values.flatten()
final_stats_val_df.set_index(transformed_df[key].index,inplace=True)


# finding value stocks based on Magic Formula
final_stats_val_df.loc["CombRank",:] = final_stats_val_df.loc["EarningYield",:].rank(ascending=False,na_option='bottom')+final_stats_val_df.loc["ROC",:].rank(ascending=False,na_option='bottom')
final_stats_val_df.loc["MagicFormulaRank",:] = final_stats_val_df.loc["CombRank",:].rank(method='first')
value_stocks = final_stats_val_df.loc["MagicFormulaRank",:].sort_values()
print("------------------------------------------------")
print("Value stocks based on Greenblatt's Magic Formula")
print(value_stocks)


# finding highest dividend yield stocks
high_dividend_stocks = final_stats_val_df.loc["DivYield",:].sort_values(ascending=False)
print("------------------------------------------------")
print("Highest dividend paying stocks")
print(high_dividend_stocks)