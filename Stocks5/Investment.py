import Record, ValleyRecord

class Investment(Record):
	totalValue = 0
	cashValue = 0
	stockValue = 0
	stockSymbol = ""
	stockCount = 0
	valleyRecords = [ValleyRecord.ValleyRecord()]
	
	# Parameterized constructor
	def __init__(self, totalValue=0, cashValue=0, stockValue=0, stockSymbol="", stockCount, valleyRecords):
		self.totalValue = totalValue
		self.cashValue = cashValue
		self.stockValue = stockValue
		self.stockSymbol = stockSymbol
		self.stockCount = stockCount
		self.valleyRecords = valleyRecords
	
	# Getters & setters	
	def setTotalValue(self, newTotalValue):
		self.totalValue = newTotalValue
	def getTotalValue(self):
		return self.totalValue
	
	def setCashValue(self, newCashValue):
		self.cashValue = newCashValue
	def getCashValue(self):
		return self.cashValue
	
	def getStockValue(self):
		return self.stockValue
	def setStockValue(self, newStockValue):
		self.stockValue = newStockValue
	
	def setStockSymbol(self, newStockSymbol):
		self.stockSymbol = newStockSymbol
	def getStockSymbol(self):
		return self.stockSymbol
	
	def setStockCount(self, newStockCount):
		self.stockCount = newStockCount
	def getStockCount(self):
		return self.stockCount
	
	def getValleyRecords(self):
		return self.valleyRecords
	def setValleyRecords(self, newValleyRecords):
		self.valleyRecords = newValleyRecords