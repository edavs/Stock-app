import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import math

# TODO: Figure out why git won't let me push nor pull and fix it.
# TODO: Divide up initialFunds evenly into each stock.
def main():
	# Welcome the user
	print("Welcome")
	
	userInputs = initialize()
	
	strategy(userInputs=userInputs)

# Initialize the starting values
def initialize():
	# Request and handle user input
	stockSymbols = ["BK", "ED", "PFE", "DBD", "PG", "JNJ", "IBM", "BRK-B", "ABT", 'F', "XRX", 'M']  # = input("List your stock symbols separated by a space(ex:STOCKA STOCKB STOCKC): ").split(' ')
	yearsBackUserInput = 10  # = int(input("Enter how many years back you would like to start collecting data(ex: 2"))).
	slants = [0.1, 0.01, 0.1, 0.01]  # = input("Enter your slants(1-4) interest rate as a decimal number separated by a space(ex:0.1 0.2 0.3 0.4 ): ").split(' ')
	initialFunds = 10000  # = int(input("Enter how much cash you wish to invest in the previously listed items combined USD(no commas, no decimals)(ex:20000): $"))
	inflationRate = 0.02  # = float(input("Enter your inflation rate as a decimal number(ex:0.5): "))
	showPurchases = False  # bool(input("Enter True if you would like to see the purchases. Enter False if you would not(ex: True): "))
	showSales = False  # bool(input("Enter True if you would like to see the sales, enter False if you would not(ex: True): "))
	showResults = True  # bool(input("Enter True if you would like to see the results, enter False if you would not(ex: True): "))
	showFinalResult = True  # bool(input("Enter True if you would like to see the final result, enter False if you would not(ex: True): "))
	showGraphs = True  # bool(input("Enter True if you would like to see the graph of the stock, enter False if you would not(ex: True): "))
	purchaseLimit = 1  # float(input("Enter the maximum percent of your funds you would like to spend per purchase converted to a decimal, no percentage symbol(ex: 0.2)))"
	
	# Let the user know the program is churning away
	print("Processing & calculating...")
	
	# Set some values
	initialStockCount = 0
	priceMarker = "Adj Close"
	startDate = dt.datetime.now() - dt.timedelta(days=365*yearsBackUserInput)
	endDate = dt.datetime.now()
	
	return [endDate, initialFunds, inflationRate, initialStockCount, priceMarker, purchaseLimit, showFinalResult, showGraphs, showPurchases, showResults, showSales, slants, startDate, stockSymbols, yearsBackUserInput]

# Apply the stock trading strategy
def strategy(userInputs):
	# Handle the parameters	
	endDate = userInputs[0]
	initialFunds = userInputs[1]
	inflationRate = userInputs[2]
	initialStockCount = userInputs[3]
	priceMarker = userInputs[4]
	purchaseLimit = userInputs[5]
	showFinalResult = userInputs[6]
	showGraphs = userInputs[7]
	showPurchases = userInputs[8]
	showResults = userInputs[9]
	showSales = userInputs[10]
	slants = userInputs[11]
	startDate = userInputs[12]
	stockSymbols = userInputs[13]
	yearsBack = userInputs[14]
	
	# Prepare a list of the final results
	annualInterestRatesOfReturns = []
	interestRatesOfReturns = []

	# Analyze all the stocks inputted to figure out purchase and sell dates
	for stockSymbol in stockSymbols:
		# Use user input to create the dataframe of the requested data
		df = web.DataReader(stockSymbol, 'yahoo', startDate, endDate)
		dfm = df[priceMarker]  # Dataframes have a lot of price markers, only use one
		
		# Reset some values
		stockCount = initialStockCount
		funds = initialFunds
		
		# Reset values for the graph
		dates = [dt.datetime.now()]
		prices = [0]
		labels = [""]
		
		# TODO: Consider not limiting the trading strategy to just 2 purchases. 
		# TODO: Consider having an extra funds account for extra purchases when the price continues to drop
		# Reset the 5 points
		pricePoints = {"a1": None, "b1": None, "c1": None, "a2": None, "b2": None, "c2": None, 'd': None, 	'e': None}
		
		# Find the price points by looping through the stock's prices
		for i in range(len(dfm)):		
			# Get the date and price from the dataframe
			date = dfm.index[i]
			price = dfm[i]
			
			if pricePoints["a1"] is None and pricePoints["d"] is None:  # This should only be true in the first iteration of this loop
				pricePoints["a1"] = price
				dates, labels, prices = updateGraphValues(append=False, date=date, dates=dates, label="A1", labels=labels, price=price, prices=prices, replace=True)
			elif pricePoints["b1"] is None:  # Find pricePoints["b1"] while adjusting pricePoints["a1"]
				if price > pricePoints["a1"]:  # Price went up; therefore, adjust pricePoints["a1"]
					pricePoints["a1"] = price
					dates, labels, prices = updateGraphValues(append=False, date=date, dates=dates, label="A1", labels=labels, price=price, prices=prices, replace=True)				
				elif (pricePoints["a1"] - price) / pricePoints["a1"] >= slants[0]:  # Price went down significantly; therefore assign b1
					pricePoints["b1"] = price
					dates, labels, prices = updateGraphValues(append=True, date=date, dates=dates, label="B1", labels=labels, price=price, prices=prices, replace=False)	
			elif pricePoints["c1"] is None:  # Find purchase price while adjusting pricePoints["b1"]
				if price < pricePoints["b1"]:
					pricePoints["b1"] = price
					dates, labels, prices = updateGraphValues(append=False, date=date, dates=dates, label="B1", labels=labels, price=price, prices=prices, replace=True)	
				elif (price - pricePoints["b1"]) / pricePoints["b1"] >= slants[1]:  # The price went up slightly; therefore, purchase the stock
					pricePoints["c1"] = price
					dates, labels, prices = updateGraphValues(append=True, date=date, dates=dates, label="C1", labels=labels, price=price, prices=prices, replace=False)
					
					funds, stockCount = purchase(date=date, funds=funds, price=price, purchaseLimit=purchaseLimit, stockSymbol=stockSymbol, stockCount=stockCount, showPurchase=showPurchases)	
			elif pricePoints['d'] is None:  # Find pricePoints["d1"] while considering a second purchase					
				if (price - pricePoints["c1"]) / pricePoints["c1"] >= slants[2]:  # Price went up significantly; therefore assign pricePoints["d1"] and forget about a second purchase
					pricePoints['d'] = price
					dates, labels, prices = updateGraphValues(append=True, date=date, dates=dates, label="D", labels=labels, price=price, prices=prices, replace=False)
				elif pricePoints["b2"] is None:  # Find a potential second purchase
					# TODO: Update the graphs to include the 3 new points
					if (pricePoints["c1"] - price) / pricePoints["c1"] >= slants[0]:  # Price dropped significantly again; therefore, assign pricePoints["a2"] and pricePoints["b2"]
						"""pricePoints["a2"] = pricePoints["c1"]
						dates, labels, prices = updateGraphValues(append=True, date=date, dates=dates, label="A2", labels=labels, price=price, prices=prices, replace=False)"""
						
						pricePoints["b2"] = price
						dates, labels, prices = updateGraphValues(append=True, date=date, dates=dates, label="B2", labels=labels, price=price, prices=prices, replace=False)
				elif pricePoints["c2"] is None:  # Look for the new purchasing price
					if (price - pricePoints["b2"]) / pricePoints["b2"] >= slants[1]:  # Price went up slightly; therefore, purchase the stock again
						pricePoints["c2"] = price
						dates, labels, prices = updateGraphValues(append=True, date=date, dates=dates, label="C2", labels=labels, price=price, prices=prices, replace=False)
						
						funds, stockCount = purchase(date=date, funds=funds, price=price, purchaseLimit=purchaseLimit, stockSymbol=stockSymbol, stockCount=stockCount, showPurchase=showPurchases)
			elif pricePoints['e'] is None:  # Find the selling price while adjusting the highest price
				if price > pricePoints['d']:
					pricePoints['d'] = price
					dates, labels, prices = updateGraphValues(append=False, date=date, dates=dates, label="D", labels=labels, price=price, prices=prices, replace=True)	
				elif (pricePoints['d'] - price) / pricePoints["d"] >= slants[3]:  # Sell the stock
					pricePoints['e'] = price
					dates, labels, prices = updateGraphValues(append=True, date=date, dates=dates, label="E", labels=labels, price=price, prices=prices, replace=False)
					
					funds, stockCount = sell(date=date, funds=funds, stockCount=stockCount, price=price, stockSymbol=stockSymbol, showSale=showSales)
			else:
				pricePoints["a1"] = pricePoints["d"]
				pricePoints["b1"] = None
				pricePoints["c1"] = None
				pricePoints["a2"] = None
				pricePoints["b2"] = None
				pricePoints["c2"] = None
				pricePoints['d'] = None
				pricePoints['e'] = None
				
				dates, labels, prices = updateGraphValues(append=True, date=date, dates=dates, label="A1", labels=labels, price=price, prices=prices, replace=False)
		
		# Show the stock's result		
		annualInterestRateOfReturn, interestRateOfReturn = stockResult(date=date, funds=funds, inflationRate=inflationRate, initialFunds=initialFunds, price=price, showResult=showResults, stockCount=stockCount, stockSymbol=stockSymbol, yearsBack=yearsBack)
		
		# Save the averages of the stocks' results for future use
		interestRatesOfReturns.append(interestRateOfReturn)
		annualInterestRatesOfReturns.append(annualInterestRateOfReturn)
		
		# Graph the analysis
		if showGraphs:
			# Alphabetize these parameters			
			graphAnalysis(dates=dates, dfm=dfm, labels=labels, prices=prices, priceMarker=priceMarker, stockSymbol=stockSymbol)
	
	finalResult(annualInterestRatesOfReturns=annualInterestRatesOfReturns, interestRatesOfReturns=interestRatesOfReturns, showFinalResult=showFinalResult, stockSymbols=stockSymbols, yearsBack=yearsBack)

# Buy the stock
# TODO: Update purchase(...) to account for the buying limit
def purchase(date=dt.datetime.now(), funds=0, price=0, purchaseLimit=0.1, showPurchase=True, stockCount=0, stockSymbol=""):
	# Calculate the pruchase price and how it will affect other values
	purchaseCount = math.floor(funds * purchaseLimit / price)
	stockCount += purchaseCount
	purchaseCost = purchaseCount * price
	funds -= purchaseCost
	
	# Output
	if showPurchase:
		print("----------------------------------------")
		print("Purchase of " + stockSymbol + " stock")
		print("Date: " + str(date))
		print("Purchase count: " + str(purchaseCount) + " shares")
		print("Price: $" + str(round(price, 2)) + " per share")
		print("Cost: $" + str(round(purchaseCost, 2)))
		print("Funds left: $" + str(round(funds, 2)))
	
	return funds, stockCount

# Sell the stock
def sell(date=dt.datetime.now(), funds=0, stockCount=0, price=0, showSale=True, stockSymbol=""):
	# Calculate the sale earnings and how it will affect other values
	saleEarnings = stockCount * price
	funds += saleEarnings
	
	# Output
	if showSale:
		print("----------------------------------------")
		print("Sale of " + stockSymbol + " stock")
		print("Date: " + str(date))
		print("Sale count: " + str(stockCount) + " shares")
		print("Price: $" + str(round(price, 2)) + " per share")
		print("Earnings: $" + str(round(saleEarnings, 2)))
		print("Funds left: $" + str(round(funds, 2)))
	
	stockCount = 0
	
	return funds, stockCount

# Show the changes in funds comparing initial funds with final funds
def stockResult(date=dt.datetime.now(), funds=0.0, inflationRate=0.0, initialFunds=0.0, price=0.0, showResult=True, stockCount=0, stockSymbol="", yearsBack=0):
	# Calculate the final statistics
	moneyStillInvested = price * stockCount
	finalValue = funds + moneyStillInvested
	changeInValue = finalValue - initialFunds
	interestRateOfReturn = changeInValue / initialFunds
	annualInterestRateOfReturn = interestRateOfReturn / yearsBack
	
	# TODO: Include initial date, final date, time passed
	
	# Output
	if showResult:
		print("----------------------------------------")
		print("Result of " + stockSymbol + " stock")
		print("Date: " + str(date))
		print("Initial funds: $" + str(round(initialFunds, 2)))
		print("Money still invested: $" + str(round(moneyStillInvested, 2)))
		print("Funds left: $" + str(round(funds, 2)))
		print("Final value: $" + str(round(finalValue, 2)))
		print("Change in value: $" + str(round(changeInValue, 2)))
		print("Interest rate of return: " + str(round(interestRateOfReturn * 100, 2)) + "% in " + str(yearsBack) + "years.")
		print("Annual interest rate of return: " + str(round(annualInterestRateOfReturn * 100, 2)) + str('%'))
	
	# Return information for the final results
	return annualInterestRateOfReturn, interestRateOfReturn

# TODO: Find a way to implement the stockResults function but to calculate the average results with all the stocks put together.
# Calculate & display the overall results of all the stocks evaluated
def finalResult(annualInterestRatesOfReturns, interestRatesOfReturns, showFinalResult, stockSymbols, yearsBack):
	# TODO: Implement moneyStillInvested and fundsLeft like in stockResult(...)
	# Find the average of the results
	averageInterestRateOfReturn = sum(interestRatesOfReturns) / len(interestRatesOfReturns)
	averageAnnualInterestRateOfReturn = sum(annualInterestRatesOfReturns) / len(annualInterestRatesOfReturns)
	
	# Output
	if showFinalResult:
		print("----------------------------------------")
		print("Final result of " + str(stockSymbols))
		print("Average interest rate of return: " + str(round(averageInterestRateOfReturn * 100, 2)) + "% in " + str(yearsBack) + "years.")
		print("Average annual interest rate of return: " + str(round(averageAnnualInterestRateOfReturn * 100, 2)) + '%')

# Update the lists that will be used to make the graph
def updateGraphValues(append=False, date=dt.datetime.now(), dates=[dt.datetime.now()], label="label", labels=["labels"], price=0, prices=[0], replace=False):
	if append:
		dates.append(date)
		prices.append(price)
		labels.append(label)
	elif replace:
		dates[-1] = date
		prices[-1] = price
		labels[-1] = label
	
	return dates, labels, prices

# Create and display the graph
def graphAnalysis(dates=[dt.datetime.now()], dfm=None, labels=["labels"], prices=[0], priceMarker="Adj Close", stockSymbol="Stock symbol"):
	# Graph of the prices, purchase prices, and sale prices
	dfm.plot(label="Price")
	plt.plot(dates, prices, marker='o')
	plt.title(stockSymbol + " stock")
	plt.xlabel("Date")
	plt.ylabel(priceMarker + " price")
	plt.legend()		
	for date, price, label in zip(dates, prices, labels):  # zip joins x and y coordinates in pairs
		label = label.format(price)

		plt.annotate(label, # this is the text
					 (date, price), # this is the point to label
					 textcoords="offset points", # how to position the text
					 xytext=(0,10), # distance from text to points (x,y)
					 ha='center') # horizontal alignment can be left, right or center

	plt.show()

main()