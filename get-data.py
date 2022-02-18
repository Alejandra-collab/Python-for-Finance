# Let's see how to download data from Yahoo Finance with Python

import pandas_datareader.data as web #to collect data
import datetime as dt #to specify start and end dates

# Start date data yyy, mm, dd
start = dt.datetime(2020, 1, 1)

# End date data yyy, mm, dd
end = dt.datetime(2020, 9, 7)

tickers = ['GOOG', 'AMZN', 'AAPL']
cc = 'BTC-USD' # We can replace 'tickers' in the following
               # lines of code for 'cc' andthe data that 
               # the code will download will be the cc 
               # (cryptocurrency) data

for ticker in tickers:
    data = web.DataReader(ticker, 'yahoo', start, end)
    data.to_csv('{}.csv'.format(ticker)) # the {} will be replaced 
                                     # with whatever the ticker
                                     #  is
                                     #