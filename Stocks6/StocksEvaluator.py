import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import math

# TODO: Implement the ability to see a graph for each stock of price vs date. Include data points of each purchase and sale. This will help visualize the trading strategy in action.
# TODO: Alphabetize parameters.
# TODO: Figure out why git won't let me push nor pull and fix it.
def main():
	# Welcome the user
	print("Welcome")
	
	userInputs = initialize()
	
	strategy(userInputs=userInputs)

# Initialize the starting values
def initialize():
	# Request and handle user input
	stockSymbols = ["BK", "ED"]  # = input("List your stock symbols separated by a space(ex:STOCKA STOCKB STOCKC): ").split(' ')
	yearsBackUserInput = 10  # = int(input("Enter how many years back you would like to start collecting data(ex: 2"))). TODO: Convert user inputted start date to a datetime object.
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
	priceMarker = "Adj Close"
	startDate = dt.datetime.now() - dt.timedelta(days=365*yearsBackUserInput)
	endDate = dt.datetime.now()
	
	return [stockSymbols, startDate, slants, initialFunds, inflationRate, initialStockCount, priceMarker, endDate, yearsBackUserInput, showPurchases, showSales, showResults, showFinalResult]

# Apply the stock trading strategy
def strategy(userInputs):
	# Handle the parameters
	stockSymbols = userInputs[0]
	startDate = userInputs[1]
	slants = userInputs[2]
	initialFunds = userInputs[3]
	inflationRate = userInputs[4]
	initialStockCount = userInputs[5]
	priceMarker = userInputs[6]
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
		dfm = df[priceMarker]  # Dataframes have a lot of price markers, only use one
		
		# Reset some values
		stockCount = initialStockCount
		funds = initialFunds
		
		# Reset values for the graph
		dates = [dt.datetime.now()]
		prices = [0]
		labels = ['']
		
		# Reset the 5 points
		# TODO: Consider renaming these or making them uppercase
		a = None
		b = None
		c = None
		d = None
		e = None

		# Find the 5 points by looping through the stock's prices
		for i in range(len(dfm)):		
			# Get the date and price from the dataframe
			date = dfm.index[i]
			price = dfm[i]
			
			if a is None and d is None: a = price  # This should only be true in the first iteration of this loop
			elif b is None:  # Find b while adjusting a
				if price > a:  # Price went up; therefore, adjust a
					a = price
					
					# Graphing values
					# TODO: Move these lines into a function since they get repeated a lot
					dates[-1] = date
					prices[-1] = price
					labels[-1] = 'A'
				elif (a - price) / a >= slants[0]:  # Price went down significantly
					b = price
					
					# Graphing values
					# TODO: Move these lines into a function since they get repeated a lot
					dates.append(date)
					prices.append(price)
					labels.append('B')
			elif c is None:  # Find C(purchase price) while adjusting b
				if price < b:
					b = price
					
					# Graphing values
					dates[-1] = date
					prices[-1] = price
					labels[-1] = 'B'
				elif (price - b) / b >= slants[1]:  # Purchase the stock
					c = price
					funds, stockCount = purchase(date=date, funds=funds, price=price, stockSymbol=stockSymbol, showPurchase=showPurchases)
					
					# Graphing values
					dates.append(date)
					prices.append(price)
					labels.append('C')
			elif d is None:  # Find D
				if (price - c) / c >= slants[2]:
					d = price
					
					# Graphing values
					dates.append(date)
					prices.append(price)
					labels.append('D')
			elif e is None:  # Find E(Sell price) while adjusting D
				if price > d:
					d = price
					
					# Graphing values
					dates[-1] = date
					prices[-1] = price
					labels[-1] = 'D'
				elif (d - price) / d >= slants[3]:  # Sell the stock
					e = price
					funds, stockCount = sell(date=date, funds=funds, stockCount=stockCount, price=price, stockSymbol=stockSymbol, showSale=showSales)
					
					# Graphing values
					dates.append(date)
					prices.append(price)
					labels.append('E')
			else:
				a = d
				b = None
				c = None
				d = None
				e = None
				
				# Graphing values
				dates.append(date)
				prices.append(price)
				labels.append('A')
		
		# Show the stock's result
		interestRateOfReturn, annualInterestRateOfReturn = stockResult(initialFunds=initialFunds, funds=funds, date=date, stockCount=stockCount, price=price, stockSymbol=stockSymbol, inflationRate=inflationRate, yearsBack=yearsBack, showResult=showResults)
		
		# Save the averages of the stocks' results for future use
		interestRatesOfReturns.append(interestRateOfReturn)
		annualInterestRatesOfReturns.append(annualInterestRateOfReturn)
		
		# Graph of the prices, purchase prices, and sale prices
		# TODO: Move all this graphing code to a function. Including the graphing lines in the loops
		dfm.plot(label="Price")
		plt.plot(dates, prices, marker='o')
		plt.title(stockSymbol + " stock")
		plt.xlabel("Date")
		plt.ylabel(priceMarker + " price")
		plt.legend()		
		# zip joins x and y coordinates in pairs
		for date, price, label in zip(dates, prices, labels):
			label = label.format(price)

			plt.annotate(label, # this is the text
						 (date, price), # this is the point to label
						 textcoords="offset points", # how to position the text
						 xytext=(0,10), # distance from text to points (x,y)
						 ha='center') # horizontal alignment can be left, right or center

		plt.show()
	
	finalResult(annualInterestRatesOfReturns=annualInterestRatesOfReturns, interestRatesOfReturns=interestRatesOfReturns, showFinalResult=showFinalResult, stockSymbols=stockSymbols, yearsBack=yearsBack)

# Buy the stock
def purchase(date, funds, price, stockSymbol, showPurchase):
	# Calculate the pruchase price and how it will affect other values
	stockCount = math.floor(funds / price)
	purchaseCost = stockCount * price
	funds -= purchaseCost
	
	# Output
	if showPurchase:
		print("----------------------------------------")
		print("Purchase of " + stockSymbol + " stock")
		print("Date: " + str(date))
		print("Count: $" + str(stockCount) + " shares")
		print("Price: $" + str(round(price, 2)) + " per share")
		print("Cost: $" + str(round(purchaseCost, 2)))
		print("Funds: " + str(round(funds, 2)))
	
	return funds, stockCount

# Sell the stock
def sell(date, funds, stockCount, price, stockSymbol, showSale):
	# Calculate the sale earnings and how it will affect other values
	saleEarnings = stockCount * price
	funds += saleEarnings
	
	# Output
	if showSale:
		print("----------------------------------------")
		print("Sale of " + stockSymbol + " stock")
		print("Date: " + str(date))
		print("Count: $" + str(stockCount) + " shares")
		print("Price: $" + str(round(price, 2)) + " per share")
		print("Earnings: $" + str(round(saleEarnings, 2)))
		print("Funds: " + str(round(funds, 2)))
	
	stockCount = 0
	
	return funds, stockCount

# Show the changes in funds comparing initial funds with final funds
def stockResult(date, funds, initialFunds, stockCount, price, stockSymbol, inflationRate, yearsBack, showResult):
	# Calculate the final statistics
	finalValue = funds + price * stockCount
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
# Calculate & display the overall results of all the stocks evaluated
def finalResult(annualInterestRatesOfReturns, interestRatesOfReturns, showFinalResult, stockSymbols, yearsBack):
	# Find the average of the results
	averageInterestRateOfReturn = sum(interestRatesOfReturns) / len(interestRatesOfReturns)
	averageAnnualInterestRateOfReturn = sum(annualInterestRatesOfReturns) / len(annualInterestRatesOfReturns)
	
	# Output
	if showFinalResult:
		print("----------------------------------------")
		print("Final result of " + str(stockSymbols))
		print("Average interest rate of return: " + str(round(averageInterestRateOfReturn * 100, 2)) + "% in " + str(yearsBack) + "years.")
		print("Average annual interest rate of return: " + str(round(averageAnnualInterestRateOfReturn * 100, 2)) + '%')

main()