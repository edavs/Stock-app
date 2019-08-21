"""
-Eduardo Davila
-08/15/2019
-Main.py
-TODO: Describe the file
"""

# TODO: Consider using a database system to avoid having to update so many variables each time something changes.

import datetime as dt
import mongo as mdb
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import Record, Portfolio, Investment, ValleyStrategy, ValleyRecord
import math

# Welcome the user
print("Welcome")

# Take in user input.
# TODO: Consider making a class to handle user input and maybe output as well.
userNameUserInput = "test"  # = input("Enter your name: ")
print("Welcome, " + userNameUserInput)
itemNamesUserInput = ['BK']  # = input("List the names of items you want to invest in separated by a space(ex: STOCKA STOCKB STOCKC): ").split(' ')
# TODO: Implement the ability for the user to enter an exact date then the program convert the user's input into a datetime value
startYearUserInput = 2018  # = int(input("Enter your start year: "))
endYearUserInput = 2019  # = int(input("Enter your end year: "))
slant1UserInput = 0.1  # = float(input("Enter your slant1 interest rate as a decimal number(ex:0.5): "))
slant2UserInput = 0.01  # = float(input("Enter your slant2 interest rate as a decimal number(ex:0.5): "))
slant3UserInput = 0.1  # = float(input("Enter your slant3 interest rate as a decimal number(ex:0.5): "))
slant4UserInput = 0.01  # = float(input("Enter your slant4 interest rate as a decimal number(ex:0.5): "))
fundsUserInput = 1000  # = int(input("Enter how much funds you wish to invest (USD, no commas, no decimals)(ex: 20000): $"))
# TODO: Implement the inflation rate
inflationRateUserInput = 0.02  # = float(input("Enter your inflation rate as a decimal number(ex:0.5): "))
priceMeasurementUserInput = "Adj Close"  # = input("Enter the price measurement you would like to use (options: High, Low, Open, Close, Adj Close): ")

# TODO: Think of a better and safer way of implementing id generation
global_id = 0
def generateNewId(id=global_id):
	id += 1
	return id

## Initializations based on the inputs ##
# Formulate the start and end dates based on the date inputs
endDate = dt.datetime.now()  # dt.datetime(endYear, 12, 31)
startDate = endDate - dt.timedelta(days=730)  # dt.datetime(startYear, 1, 1)
# ValleyStrategy
vs = ValleyStrategy.ValleyStrategy(slant1=slant1UserInput, slant2=slant2UserInput, slant3=slant3UserInput, slant4=slant4UserInput)
# ValleyRecord
vr = ValleyRecord.ValleyRecord(id=generateNewId(), date=startDate)
# Investment
# TODO: Loop over itemNamesUserInput to create 1 investment per item
inv = Investment.Investment(id=generateNewId(), date=startDate, cashValue=fundsUserInput, itemValue=0, itemName=itemNamesUserInput[0], itemCount=0, valleyRecord=vr)
# Portfolio
p = Portfolio.Portfolio(id=generateNewId(), date=startDate, cashValue=fundsUserInput, itemsValue=0, investment=inv, valleyStrategy=vs)
print("Reached here")

"""
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
"""