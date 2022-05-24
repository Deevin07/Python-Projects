import os
import pandas as pd

os.chdir('C:\\Users\\Vineet\\.spyder-py3')

cwd = os.getcwd()

sales = pd.read_excel('sales_data.xlsx') # importing left data frame

zip_income =  pd.read_csv('zipcode_income.csv',engine='python',encoding='ISO-8859-1') #importing right data frame

temp = sales.merge(zip_income.loc[:,['Zip_Code','Mean']].rename(columns = {'Zip_Code':'Postal Code','Mean':'Mean Income'}) 
                   ,how='left',on='Postal Code') #merging left and right with relevent data frames


temp.drop_duplicates(subset=['Row ID'], inplace=True,keep = 'first') # dropping all the duplicates 



def vlookup(left_df,right_df,left_key,right_key,right_val):
    left = pd.read_excel(left_df)
    left.reset_index(inplace=True)
    right = pd.read_csv(right_df,engine='python',encoding='ISO-8859-1')
    right = right.loc[:,[right_key,right_val]].rename(columns = {right_key:left_key})
    temp = left.merge(right,how='left',on = left_key)
    temp.drop_duplicates(subset=['index'], inplace=True,keep = 'first') # dropping all the duplicates 
    return temp.set_index('index')

vlookup('sales_data.xlsx', 'zipcode_income.csv','Postal Code' ,'Zip_Code' ,'Mean')