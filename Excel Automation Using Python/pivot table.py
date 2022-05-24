"""

@author: Vineet Dusa
@linked in = https://www.linkedin.com/in/vineet-dusa-a266321b5/
"""

import os
import pandas as pd
import glob
import numpy as np

os.chdir('C:\\Users\\Vineet\\.spyder-py3')

cwd = os.getcwd()

filenames = glob.glob(cwd+'\\*\\*.xlsx')

consolidated = pd.DataFrame(pd.read_excel(filenames[0]).columns)

for file in filenames:
    temp = pd.read_excel(file)
    consolidated = consolidated.append(temp,ignore_index=True)
    
########################### pandas pivot method ##############################    

pd.pivot_table(consolidated,values = 'Profit',
               index = ['Segment','Category','Sub-Category'],  
               columns = 'Region',
               aggfunc= np.sum)           # here the index is the row and 
                                          # by default aggfunc is mean so you should mention what function 
                                          # do you need to apply
                                      

########################### one method ######################################
#getting all the relevant data we need and converting it in what we need
columns =  ['Region']
rows = ['Segment','Category','Sub-Category'] 
values = ['Profit']

relevant_data = consolidated.loc[:,columns+rows+values]

#converting the data into pivot table
pivot_table =relevant_data.groupby(rows+columns).sum().unstack()   

#exporting the data to excel
pivot_table.to_excel('pivot_table.xlsx')
pivot_table.to_