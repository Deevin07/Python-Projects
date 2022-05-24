# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:13:51 2022

@author: Vineet
"""

import glob
import os

os.chdir('C:\\Users\\Vineet\\.spyder-py3\\excel dump')

cwd = os.getcwd()


filename = glob.glob("*.xlsx")

for file in filename:
    year = file.split('.')[0][3:]
    try:
        int(year)
    except:
        print(' there is a string so cannot copy and paste')
        continue
    if os.path.isdir(year) ==  False:
        os.mkdir(year)
        
    os.rename(file,os.path.join(cwd,year,file))    