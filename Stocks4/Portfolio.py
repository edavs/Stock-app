import json

# A portfolio holds data on the user's fund allocations
class Portfolio:
	cash = None
	date = None
	outputFilePath = None
	stock = {
		"Symbol": "",
		"Count": 0,
		"Value": 0
		}
	value = None
	
	# Parameterized constructor
	def __init__(self, cash=0, date=None, outputFilePath=None, stock=stock, value=0):
		self.cash = cash
		self.date = date
		self.outputFilePath = outputFilePath
		self.stock = stock
		self.value = value
		
		# Clear the output file
		open(self.outputFilePath, 'w').close()
	
	# Write to the output file
	def outputToFile(self, message=None):
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
	def getCash(self):
		return self.cash
	
	def setCash(self, newCash):
		self.cash = newCash
	
	def getDate(self):
		return self.date
	
	def setDate(self, newDate):
		self.date = newDate
	
	def getOutputFilePath(self):
		return self.outputFilePath
	
	def setOutputFilePath(self, newOutputFilePath):
		self.outputFilePath = newOutputFilePath
	
	def getStock(self, key=None):
		if key is not None:
			return self.stock[key]
		else:
			return self.stock
	
	def setStock(self, key=None, newValue=None, newStock=None):
		if key is not None:
			self.stock[key] = newValue
		else:
			self.stock = newStock
	
	def getValue(self):
		return self.value
	
	def setValue(self, newValue):
		self.value = newValue