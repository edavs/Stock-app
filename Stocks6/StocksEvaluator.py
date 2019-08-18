import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import math

# TODO: Implement the ability to see a graph for each stock of price vs date. Include data points of each purchase and sale. This will help visualize the trading strategy in action.
# TODO: Alphabetize parameters
def main():
	# Welcome the user
	print("Welcome")
	
	userInputs = initialize()
	
	strategy(userInputs=userInputs)

# Initialize the starting values
def initialize():
	# Request and handle user input
	stockSymbols = ["BK", "ED", "PFE", "DBD", "PG", "JNJ", "IBM", "BRK-B", "ABT", 'F', "XRX", 'M', "CACI", "NOC", "MU"]  # = input("List your stock symbols separated by a space(ex:STOCKA STOCKB STOCKC): ").split(' ')
	yearsBackUserInput = 2  # = int(input("Enter how many years back you would like to start collecting data(ex: 2"))). TODO: Convert user inputted start date to a datetime object.
	slants = [0.1, 0.01, 0.1, 0.01]  # = input("Enter your slants(1-4) interest rate as a decimal number separated by a space(ex:0.1 0.2 0.3 0.4 ): ").split(' ')
	initialFunds = 10000  # = int(input("Enter how much cash you wish to invest in USD(no commas, no decimals)(ex:20000): $"))
	inflationRate = 0.02  # = float(input("Enter your inflation rate as a decimal number(ex:0.5): "))
	showPurchases = False  # bool(input("Enter True if you would like to see the purchases. Enter False if you would not(ex: True): "))
	showSales = False  # bool(input("Enter True if you would like to see the sales, enter False if you would not(ex: True): "))
	showResults = False  # bool(input("Enter True if you would like to see the results, enter False if you would not(ex: True): "))
	showFinalResult = True  # bool(input("Enter True if you would like to see the final result, enter False if you would not(ex: True): "))
	
	# Let the user know the program is churning away
	print("Processing & calculating...")
	
	# Set some values
	initialStockCount = 0
	stockPriceMarker = "Adj Close"
	startDate = dt.datetime.now() - dt.timedelta(days=365*yearsBackUserInput)
	endDate = dt.datetime.now()
	
	return [stockSymbols, startDate, slants, initialFunds, inflationRate, initialStockCount, stockPriceMarker, endDate, yearsBackUserInput, showPurchases, showSales, showResults, showFinalResult]

# Apply the stock trading strategy
def strategy(userInputs):
	# Handle the parameters
	stockSymbols = userInputs[0]
	startDate = userInputs[1]
	slants = userInputs[2]
	initialFunds = userInputs[3]
	inflationRate = userInputs[4]
	initialStockCount = userInputs[5]
	stockPriceMarker = userInputs[6]
	endDate = userInputs[7]
	yearsBack = userInputs[8]
	showPurchases = userInputs[9]
	showSales = userInputs[10]
	showResults = userInputs[11]
	showFinalResult = userInputs[12]
	
	# Prepare a list of the final results
	annualInterestRatesOfReturns = []
	interestRatesOfReturns = []

	# Analyze all the stocks inputted to figure out purchase and sell dates
	for stockSymbol in stockSymbols:
		# Use user input to create the dataframe of the requested data
		df = web.DataReader(stockSymbol, 'yahoo', startDate, endDate)
		dfm = df[stockPriceMarker]  # Dataframes have a lot of stockPrice markers, only use one
		
		# Reset some values
		stockCount = initialStockCount
		funds = initialFunds
		
		# Reset the 5 points
		a = None
		b = None
		c = None
		d = None
		e = None

		# Find the 5 points by looping through the stock's stockPrices
		for i in range(len(dfm)):		
			# Get the date and stockPrice from the dataframe
			date = dfm.index[i]
			stockPrice = dfm[i]
			
			if a is None and d is None: a = stockPrice  # This should only be true in the first iteration of this loop
			elif b is None:  # Find b while adjusting a
				if stockPrice > a:  # Price went up
					a = stockPrice
				elif (a - stockPrice) / a >= slants[0]:  # Price went down
						b = stockPrice
			elif c is None:  # Find C(purchase stockPrice) while adjusting b
				if stockPrice < b:
					b = stockPrice
				elif (stockPrice - b) / b >= slants[1]:  # Purchase the stock
					c = stockPrice
					funds, stockCount = purchase(date=date, funds=funds, stockPrice=stockPrice, stockSymbol=stockSymbol, showPurchase=showPurchases)
			elif d is None:  # Find D
				if (stockPrice - c) / c >= slants[2]:
					d = stockPrice
			elif e is None:  # Find E(Sell stockPrice) while adjusting D
				if stockPrice > d:
					d = stockPrice
				elif (d - stockPrice) / d >= slants[3]:  # Sell the stock
					e = stockPrice
					funds, stockCount = sell(date=date, funds=funds, stockCount=stockCount, stockPrice=stockPrice, stockSymbol=stockSymbol, showSale=showSales)
			else:
				a = d
				b = None
				c = None
				d = None
				e = None
		
		# Handle the stock's result
		interestRateOfReturn, annualInterestRateOfReturn = stockResult(initialFunds=initialFunds, funds=funds, date=date, stockCount=stockCount, stockPrice=stockPrice, stockSymbol=stockSymbol, inflationRate=inflationRate, yearsBack=yearsBack, showResult=showResults)
		
		# Handle the averages of the stocks' results
		interestRatesOfReturns.append(interestRateOfReturn)
		annualInterestRatesOfReturns.append(annualInterestRateOfReturn)
	
	finalResult(annualInterestRatesOfReturns=annualInterestRatesOfReturns, stockSymbols=stockSymbols, showFinalResult=showFinalResult, interestRatesOfReturns=interestRatesOfReturns, yearsBack=yearsBack)

# Buy the stock
def purchase(date, funds, stockPrice, stockSymbol, showPurchase):
	# Calculate the pruchase price and how it will affect other values
	stockCount = math.floor(funds / stockPrice)
	purchaseCost = stockCount * stockPrice
	funds -= purchaseCost
	
	# Output
	if showPurchase:
		print("----------------------------------------")
		print("Purchase of " + stockSymbol + " stock")
		print("Date: " + str(date))
		print("Count: $" + str(stockCount) + " shares")
		print("Price: $" + str(round(stockPrice, 2)) + " per share")
		print("Cost: $" + str(round(purchaseCost, 2)))
		print("Funds: " + str(round(funds, 2)))
	
	return funds, stockCount

# Sell the stock
def sell(date, funds, stockCount, stockPrice, stockSymbol, showSale):
	# Calculate the sale earnings and how it will affect other values
	saleEarnings = stockCount * stockPrice
	funds += saleEarnings
	
	# Output
	if showSale:
		print("----------------------------------------")
		print("Sale of " + stockSymbol + " stock")
		print("Date: " + str(date))
		print("Count: $" + str(stockCount) + " shares")
		print("Price: $" + str(round(stockPrice, 2)) + " per share")
		print("Earnings: $" + str(round(saleEarnings, 2)))
		print("Funds: " + str(round(funds, 2)))
	
	stockCount = 0
	
	return funds, stockCount

# Show the changes in funds comparing initial funds with final funds
def stockResult(date, funds, initialFunds, stockCount, stockPrice, stockSymbol, inflationRate, yearsBack, showResult):
	# Calculate the final statistics
	finalValue = funds + stockPrice * stockCount
	changeInValue = finalValue - initialFunds
	interestRateOfReturn = changeInValue / initialFunds
	annualInterestRateOfReturn = interestRateOfReturn / yearsBack
	
	# TODO: Include initial date, final date, time passed, overall irr(interest rate of return) and annual irr.
	
	# Output
	if showResult:
		print("----------------------------------------")
		print("Result of " + stockSymbol + " stock")
		print("Date: " + str(date))
		print("Initial funds: $" + str(initialFunds))
		print("Final value: $" + str(round(finalValue, 2)))
		print("Change in value: $" + str(round(changeInValue, 2)))
		print("Interest rate of return: " + str(round(interestRateOfReturn * 100, 2)) + "% in " + str(yearsBack) + "years.")
		print("Annual interest rate of return: " + str(round(annualInterestRateOfReturn * 100, 2)) + str('%'))
	
	# Return information for the final results
	return interestRateOfReturn, annualInterestRateOfReturn

# TODO: Find a way to implement the stockResults function but to calculate the average results with all the stocks put together.
def finalResult(annualInterestRatesOfReturns, stockSymbols, showFinalResult, interestRatesOfReturns, yearsBack):
	# Find the average of the results
	averageAnnualInterestRateOfReturn = sum(annualInterestRatesOfReturns) / len(annualInterestRatesOfReturns)
	averageInterestRateOfReturn = sum(interestRatesOfReturns) / len(interestRatesOfReturns)
	
	# Output
	if showFinalResult:
		print("----------------------------------------")
		print("Final result of " + str(stockSymbols))
		print("Average interest rate of return: " + str(round(averageInterestRateOfReturn, 2)) + "% in " + str(yearsBack) + "years.")
		print("Average annual interest rate of return: " + str(round(averageAnnualInterestRateOfReturn, 2)) + '%')

main()