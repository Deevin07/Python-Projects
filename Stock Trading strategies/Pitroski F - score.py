import pandas as pd

tickers = ["AXP","AAPL","BA","CAT","CVX","CSCO","DIS","DOW", "XOM",
           "HD","IBM","INTC","JNJ","KO","MCD","MMM","MRK","MSFT",
           "NKE","PFE","PG","UNH","VZ","V","WMT","WBA"]           #stocks list

#list of tickers whose financial data needs to be extracted
financial_dir = {} #directory to store financial information for each ticker

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
        #combining all extracted information with the corresponding ticker
        df = pd.concat([df1,df2,df3])
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


# selecting relevant financial information for each stock using fundamental data
stats = ["Net Income Common",
         "Total Assets",
         "Operating Cash Flow",
         "Long Term Debt (Total)",
         "Total non-current liabilities",
         "Total current assets",
         "Total current liabilities",
         "Common Equity (Total)",
         "Revenue",
         "Gross Profit"] # change as required

indx = ["NetIncome","TotAssets","CashFlowOps","LTDebt","TotLTLiab",
        "CurrAssets","CurrLiab","CommStock","TotRevenue","GrossProfit"]


def info_filter(df,stats,indx,lookback):
    """function to filter relevant financial information
       df = dataframe to be filtered
       stats = headings to filter
       indx = rename long headings
       lookback = number of years of data to be retained"""
    df_new = df.loc[stats,df.columns[:3]]
    df_new.rename(dict(zip(stats,indx)),inplace=True)
    df_new.loc["OtherLTDebt",:] = df_new.loc["TotLTLiab",:] - df_new.loc["LTDebt",:]
    return df_new

#applying filtering to the finacials
transformed_df = {}
for ticker in financial_dir:
    transformed_df[ticker] = info_filter(financial_dir[ticker],stats,indx,3)


def piotroski_f(df_dict):
    """function to calculate f score of each stock and output information as dataframe"""
    f_score = {}
    for ticker in df_dict:
        columns = df_dict[ticker].columns
        #return on assets  # if true it will return 1 and false 0 therefore greater than zero
        ROA_FS = int(df_dict[ticker].loc["NetIncome",columns[0]]/((df_dict[ticker].loc["TotAssets",columns[0]] + df_dict[ticker].loc["TotAssets",columns[1]])/2) > 0)
        
        #cash flow from opertation
        CFO_FS = int(df_dict[ticker].loc["CashFlowOps",columns[0]] > 0)
        
        #return on assets delta
        ROA_D_FS = int((df_dict[ticker].loc["NetIncome",columns[0]]/((df_dict[ticker].loc["TotAssets",columns[0]] + df_dict[ticker].loc["TotAssets",columns[1]])/2)) > (df_dict[ticker].loc["NetIncome",columns[1]]/((df_dict[ticker].loc["TotAssets",columns[1]] + df_dict[ticker].loc["TotAssets",columns[2]])/2)))
        
        #cashflow from operation divided by average assets and ROA
        CFO_ROA_FS = int(df_dict[ticker].loc["CashFlowOps",columns[0]]/df_dict[ticker].loc["TotAssets",columns[0]] > df_dict[ticker].loc["NetIncome",columns[0]]/((df_dict[ticker].loc["TotAssets",columns[0]] + df_dict[ticker].loc["TotAssets",columns[1]])/2))
        
        #long term debt and other liability here the debt should less than the previous year
        LTD_FS = int((df_dict[ticker].loc["LTDebt",columns[0]] + df_dict[ticker].loc["OtherLTDebt",columns[0]]) < (df_dict[ticker].loc["LTDebt",columns[1]] + df_dict[ticker].loc["OtherLTDebt",columns[1]]))
        
        #Current Ratio should be greater than the previous year
        CR_FS = int((df_dict[ticker].loc["CurrAssets",columns[0]] / df_dict[ticker].loc["CurrLiab",columns[0]]) > (df_dict[ticker].loc["CurrAssets",columns[1]] / df_dict[ticker].loc["CurrLiab",columns[1]]))
        
        #Dilustion of shares 
        DILUTION_FS = int(df_dict[ticker].loc["CommStock",columns[0]] <= df_dict[ticker].loc["CommStock",columns[1]])
        
        #Gross margin should be greater than the previous day
        GM_FS = int((df_dict[ticker].loc["GrossProfit",columns[0]]/df_dict[ticker].loc["TotRevenue",columns[0]]) > (df_dict[ticker].loc["GrossProfit",columns[1]]/df_dict[ticker].loc["TotRevenue",columns[1]]))
        
        #Asset turn over  average of two years should be greater than previous year
        ATO_FS = int((df_dict[ticker].loc["TotRevenue",columns[0]]/((df_dict[ticker].loc["TotAssets",columns[0]] + df_dict[ticker].loc["TotAssets",columns[1]])/2)) > (df_dict[ticker].loc["TotRevenue",columns[1]]/((df_dict[ticker].loc["TotAssets",columns[1]] + df_dict[ticker].loc["TotAssets",columns[2]])/2)))
      
        f_score[ticker] = [ROA_FS,CFO_FS,ROA_D_FS,CFO_ROA_FS,LTD_FS,CR_FS,DILUTION_FS,GM_FS,ATO_FS]
    f_score_df = pd.DataFrame(f_score,index=["PosROA","PosCFO","ROAChange","Accruals","Leverage","Liquidity","Dilution","GM","ATO"])
    return f_score_df

# sorting stocks with highest Piotroski f score to lowest
f_score_df = piotroski_f(transformed_df)
f_score_df.sum().sort_values(ascending=False)