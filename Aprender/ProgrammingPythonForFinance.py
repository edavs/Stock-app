import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

##start = dt.datetime(2000, 1, 1)
##end = dt.datetime(2016, 12, 31)
##
##df = web.DataReader('TSLA', 'yahoo', start, end)
##df.to_csv('tsla.csv')
##df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
##
##print(df.head())
##
##print(df[['Open', 'High']].head())
##
##df['Adj Close'].plot()
##plt.show()

###################################################################
start1 = dt.datetime(2018, 1, 1)
end1 = dt.datetime(2018, 12, 31)
df1 = web.DataReader('F', 'yahoo', start1, end1)

##price1 = df1['Adj Close'][0]
##price2 = df1['Adj Close'][1]
##print("price1: " + str(price1))
##print("price1 round(2): " + str(price1.round(2)))
##print("price1 type: " + str(type(price1)))
##print("price2: " + str(price2))
##print("difference: " + str(price1 - price2))











