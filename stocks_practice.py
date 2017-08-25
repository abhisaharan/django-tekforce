from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

enter_stocks = input("Enter a list of the stocks you want to see separated by space: ")
splitting_stocks_to_list = enter_stocks.split()
data_source = 'google'

start_date_input_user = input("Enter the start date in format YEAR-MONTH-DATE: ")
print(start_date_input_user)
start_date = start_date_input_user
end_date_input_user = input("Enter the End date in format YEAR-MONTH-DATE: ")
end_date = end_date_input_user

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader(splitting_stocks_to_list, data_source, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data.ix['Close']

all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

#print(close.head(10))