import pandas_datareader.data as web
import datetime as dt

"""
-Start with the price of the first day in leftDay and the tenth day in rightDay.
-Keep moving forward with both one day at a time until rightDay price is 10% < leftDay.
	-Once the 10% threshold is reached, store the price of rightDay in possiblePurchaseDay(ppd).
	-Keep moving leftDay and rightDay one day at a time. Each time compare them both to ppd. If rightDay is 1% > than ppd then purchase at rightDay price.
	-Else if rightDay is < ppd then move ppd to rightDay price.
-Once the stock is purchased, move leftDay to ppd and anchor it there until the stock is sold.
-Now increase increment rightDay one day at a time until rightDay is 10% > leftDay in which case, sell, move leftDay to rightDay, move rightDay 10 days ahead, and restart the process.
"""

startDate = dt.datetime(2018,5,11)
endDate = dt.datetime(2019,5,11)
df = web.DataReader('IBM', 'yahoo', startDate, endDate)
leftDay = web.DataReader('IBM', 'yahoo', startDate, startDate)
rightDay = web.DataReader('IBM', 'yahoo', startDate, endDate, startDate + dt.timedelta(days=10))

while True:
    if rightDay > leftDay*1.1:
        #
    else:
        
