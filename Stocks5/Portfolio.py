"""
-Eduardo Davila
-08/15/2019
-Portfolio.py
-TODO: Describe the file
"""

import datetime as dt
import Record, Investment, ValleyStrategy

# A Portfolio holds data on the user's fund allocations
class Portfolio(Record.Record):
	## Properties ##
	cashValue = 0
	itemsValue = 0  # TODO: Actually make it possible to track the value of more than 1 item
	totalValue = cashValue + itemsValue  # Also the sum of all Investments' total value
	investment = Investment.Investment()  # TODO: Implement 1+ Investments per Portfolio
	valleyStrategy = ValleyStrategy.ValleyStrategy()  # TODO: Tie the ValleyStrategy and the Portfolio together, perhaps by an id.  # TODO: Implement 1+ ValleyStrategys per Portfolio
	
	## Constructors ##
	# Parameterized constructor
	def __init__(self, id=0, date=dt.datetime.now(), cashValue=0, itemsValue=0, totalValue=cashValue+itemsValue, investment=Investment.Investment(), valleyStrategy=ValleyStrategy.ValleyStrategy(), outputDestination="./Portfolio.txt"):
		super(Portfolio, self).__init__(id, date)
		
		self.totalValue = totalValue
		self.cashValue = cashValue
		self.itemsValue = itemsValue
		self.investment = investment
		self.valleyStrategy = valleyStrategy
		self.outputDestination = outputDestination
	
	## Methods ##
	def updateTotalValue(self):
		self.setTotalValue(self.cashValue + self.itemsValue)
	
	# Write to the output file. Output the data as a json string
	# TODO: Output a Portfolio graph
	# TODO: Output the first and last Portfolio total values along with their difference in $ and %
	def outputToDestination(self, message):
		
		# Update the message
		if message is not None: self.message = message
	
		f = open(self.outputDestination, 'a')  # Open the output file to be appended
		f.write('\n' + self.__class.__name__ + '\n')
		info = {}  # Dictionary to hold all the data that will be outputted
		# This is the data to be outputted
		if self.id is not None: info["Id"] = str(self.id)
		if self.date is not None: info["Date"] = '$' + str(self.date)
		if self.totalValue is not None: info["Total value"] = '$' + str(self.totalValue)
		if self.cashValue is not None: info["Cash value"] = '$' + str(self.cashValue)
		if self.itemsValue is not None: info["Items value"] = '$' + str(self.itemsValue)
		if self.message is not None: info["Message"] = self.message
		f.write(json.dumps(info, indent=2))  # Convert the dictionary into a json string
		f.write('\n')
		f.close()  # Close the output file
	
	## Getters and setters ##
	def getTotalValue(self):
		return self.totalValue
	def setTotalValue(self, newTotalValue):
		self.totalValue = newTotalValue
	
	def getCashValue(self):
		return self.cashValue
	def setCashValue(self, newCashValue):
		self.cashValueV = newCashValue
		self.updateTotalValue()
	
	def getItemsValue(self):
		return self.stocksValue
	def setItemsValue(self, newStocksValue):
		self.stocksValue = newStocksValue
		self.updateTotalValue()
		
	def getInvestment(self):
		return self.investment
	def setInvestment(self, newInvestment):
		self.investment = newInvestment

	def getValleyStrategy(self):
		return self.valleyStrategy
	def setValleyStrategy(self, newValleyStrategy):
		self.valleyStrategy = newValleyStrategy
	