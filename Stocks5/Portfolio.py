import Record, Investment, ValleyStrategy

# A Portfolio holds data on the user's fund allocations
class Portfolio(Record):
	totalValue = 0
	cashValue = 0
	stocksValue = 0
	investments = [Investment.Investment()]
	valleyStrategies = [ValleyStrategy.ValleyStrategy()]
	
	# Parameterized constructor
	def __init__(self, totalValue=0, cashValue=0, stocksValue=0, investments=[Investment.Investment()], valleyStrategies=[ValleyStrategy.ValleyStrategy()]):
		self.totalValue = totalValue
		self.cashValue = cashValue
		self.stocksValue = stocksValue
		self.investments = investments
		self.valleyStrategies = valleyStrategies
	
	# Write to the output file
	def outputToFile(self, message):
		# Append the available data to the output file in a json string
		f = open(self.outputFilePath, 'a')
		f.write("\n--------------------\nPortfolio\n")
		info = {"date": str(self.date)}  # Initialize the json that will be used to display the data in the output file
		if self.value is not None: info["value"] = '$' + str(self.value)
		if self.stock is not None: info["stock"] = self.stock  # TODO: Decide if I want to use a list or json for this
		if self.cash is not None: info["cash"] = '$' + str(self.cash)
		if message is not None: info["message"] = message
		f.write(json.dumps(info, indent=2))
		f.write("\n--------------------\n")
		f.close()
	
	# Getters and setters
	def getCashValue(self):
		return self.cashValue
	def setCashValue(self, newCashValue):
		self.cashValueV = newCashValue
	
	def getTotalValue(self):
		return self.totalValue
	def setTotalValue(self, newTotalValue):
		self.totalValue = newTotalValue
	
	def getStocksValue(self):
		return self.stocksValue
	def setStocksValue(self, newStocksValue):
		self.stocksValue = newStocksValue
		
	def getInvestments(self):
		return self.investments
	def setInvestments(self, newInvestments):
		self.investments = newInvestments

	def getValleyStrategies(self):
		return self.valleyStrategies
	def setValleyStrategies(self, newValleyStrategies):
		self.valleyStrategies = newValleyStrategies
	