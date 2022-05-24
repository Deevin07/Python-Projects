# -*- coding: utf-8 -*-
"""
Created on Sat May 21 18:20:11 2022

@author: Vineet
"""

import os
import glob 
import pandas as pd

os.chdir('C:\\Users\\Vineet\\.spyder-py3\\excel dump')

cwd = os.getcwd()

filenames = glob.glob(cwd+"\\*\\*.xlsx")
 
consolidated = pd.DataFrame(columns = pd.read_excel(filenames[0]).columns)
for file in filenames:
    temp = pd.read_excel(file)
    consolidated = consolidated.append(temp,ignore_index=True)
    
consolidated.to_excel('consolidated.xlsx')