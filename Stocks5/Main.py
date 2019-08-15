import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import Record
import math
import Portfolio

# Welcome the user
print("Welcome")

# Take in user input
userName = "test"  # = input("Enter your name: ")
print("Welcome, " + userName)
stockSymbols = ['BK']  # = input("List your stock symbols separated by a space(ex: STOCKA STOCKB STOCKC): ").split(' ')
startYear = 2018  # = int(input("Enter your start year: "))
endYear = 2018  # = int(input("Enter your end year: "))
slant1 = 0.1  # = float(input("Enter your slant1 interest rate as a decimal number(ex:0.5): "))
slant2 = 0.01  # = float(input("Enter your slant2 interest rate as a decimal number(ex:0.5): "))
slant3 = 0.1  # = float(input("Enter your slant3 interest rate as a decimal number(ex:0.5): "))
slant4 = 0.01  # = float(input("Enter your slant4 interest rate as a decimal number(ex:0.5): "))
funds = 1000  # = int(input("Enter how much cash you wish to invest in USD(no commas, no decimals)(ex: 20000): $"))
inflationRate = 0.02  # = float(input("Enter your inflation rate as a decimal number(ex:0.5): "))
priceMeasurement = "Adj Close"  # = input("Enter the price measurement you would like to use (options: High, Low, Open, Close, Adj Close): ")

# Pick the start and end dates
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=730)

# Create the user's portfolio
cash = funds
p = Portfolio.Portfolio(cash=cash, date=startDate, outputFilePath="Portfolio.txt")

# Analyze all the stocks inputted
for stockSymbol in stockSymbols:
	# Use user input to create the dataframe of the requested data
	df = web.DataReader(stockSymbol, 'yahoo', startDate, endDate)
	dfm = df[priceMeasurement]  # Dataframes have a lot of prices, only use one
	
	firstPrice = dfm[0].round(2)
	r = Record.Record(a=firstPrice, date=startDate, funds=funds, moneyInvested=0, numStocksOwned=0, outputFilePath="./"+stockSymbol+".txt", price=firstPrice, stockSymbol=stockSymbol);
	
	# Output first record and portfolio to their output files
	r.outputToFile("First record")
	p.outputToFile("First portfolio")

	# Find the 5 points
	for i in range(len(dfm)):		
		# Update the record
		r.setDate(dfm.index[i])
		r.setPrice(round(dfm[i], 2))
		recordOutputted = False
		
		if r.getB() is None:  # Find B
			if r.getPrice() > r.getA():
				r.setA(r.getPrice())
			elif (r.getA() - r.getPrice()) / r.getA() >= slant1:
					r.setB(r.getPrice())
		elif r.getC() is None:  # Find C(purchase price)
			if r.getPrice() < r.getB():
				r.setB(r.getPrice())
			elif (r.getPrice() - r.getB()) / r.getB() >= slant2:  # Purchase
					# TODO: Perhaps create a function to handle a purchase
					r.setC(r.getPrice())
					maxStocksAfford = math.floor(p.getCash() / r.getC())
					stockValue = round(maxStocksAfford * r.getPrice(), 2)
					p.setStock(key="Count", newValue=maxStocksAfford)
					p.setCash(newCash=round(p.getCash() - p.getStock("Value"), 2))
					
					r.outputToFile("purchase transaction")  # Save the purchase record to the output file
					recordOutputted = True
		elif r.getD() is None:  # Find D
			if (r.getPrice() - r.getC()) / r.getC() >= slant3:
				r.setD(r.getPrice())
		elif r.getE() is None:  # Find E(Sell price)
			if r.getPrice() > r.getD():
				r.setD(r.getPrice())
			elif (r.getD() - r.getPrice()) / r.getD() >= slant4:  # Sell
				# TODO: Perhaps create a function to handle a sale
				r.setE(r.getPrice())
				p.setCash(newCash=round(p.getCash() + p.getStock("Value"), 2))
				p.setStock(key="Count", newValue=0)
				
				"""r.setFunds(round(r.getFunds() + (r.getE() * r.numStocksOwned), 2))
				r.setNumStocksOwned(0)
				r.setMoneyInvested(0)"""
				r.outputToFile("sale transaction")  # Save the sale r to the output file
				recordOutputted = True
		else:
			r.setA(newA=r.getD())
			r.setB(newB=None)
			r.setC(newC=None)
			r.setD(newD=None)
			r.setE(newE=None)
		
		# Update the portfolio
		p.setDate(r.getDate())
		stockValue = p.getStock(key="Count") * r.getPrice()
		p.setStock(key="Value", newValue=stockValue)
		p.setValue(newValue=p.getCash() + p.getStock(key="Value"))
		
		# Output the record and the portfolio to their output files
		if recordOutputted is False: r.outputToFile()
		p.outputToFile()

	# Save the last record and portfolio to their output files
	r.outputToFile("Final record")
	p.outputToFile("Final portfolio")