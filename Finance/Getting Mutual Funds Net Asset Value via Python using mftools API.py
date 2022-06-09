import pandas as pd
from mftool import Mftool
import datetime

mf = Mftool()
scheme_codes = mf.get_scheme_codes()
print(scheme_codes)


scheme_code_list = [x for x in scheme_codes.keys()]  #getting only the list we have
print(scheme_code_list)

nav_data = mf.get_scheme_historical_nav('119551','01-01-2021','11-05-2021')
print(nav_data)

def HistoricalNav(scheme_code_list, start_date, end_date):
  assert (isinstance(scheme_code_list, list) is True), "Arguement scheme_code_list should be a list" 
  assert (isinstance(start_date, str) is True), "start_date must be a str in %d-%m-%Y format" 
  assert (isinstance(end_date, str) is True), "end_date must be a str in %d-%m-%Y format" 

  main_df = pd.DataFrame() #empty dataframe

  for schemes in scheme_code_list:
    data = mf.get_scheme_historical_nav_for_dates(schemes, start_date, end_date) # requesting NAV data from the api.

    df = pd.DataFrame(data['data']) 
    df['scheme_code'] = pd.Series([data['scheme_code'] for x in range(len(df.index))]) 
    df['scheme_name'] = pd.Series([data['scheme_name'] for x in range(len(df.index))]) 

    df = df.sort_values(by = 'date')

    main_df = main_df.append(df) # appending the data in the main_df dataframe.

  main_df = main_df[['scheme_code', 'scheme_name', 'date', 'nav']] #creating names of dataframe columns 
  main_df.reset_index(drop = True, inplace = True) 

  return main_df #Returning the required Dataframe.

def NAV_Data(start,end):
  try:
    values_df = HistoricalNav(scheme_code_list = scheme_code_list[0:5],start_date = start , end_date = end)
    return values_df

  except KeyError:
    start = datetime.strptime(start,'%d-%m-%Y') - timedelta(1)
    return NAV_Data(star.strftime('%d-%m-%Y'),end)


# Calling the function and saving the output in a variable.
# To get the latest NAV set the start_date and end_date as the last traded date in 'dd/mm/yyyy' format.
# Note:- To get data of a particular date, enter same start_date and end_date. 
start_date= "01-05-2021" # enter the date in "dd-mm-yyyy" format
end_date = "10-05-2021" # enter the date in "dd-mm-yyyy" format
values_df = NAV_Data(start_date,end_date) #calling function NAV_Data
print(values_df)

