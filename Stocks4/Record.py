import datetime as dt
import json

# A Record holds information on daily data from the stock market
class Record:	
	date = None
	funds = None
	price = None
	stockSymbol = None
	numStocksOwned = None
	moneyInvested = None
	a = None
	b = None
	c = None
	d = None
	e = None
	message = None
	outputFilePath = None
	
	# Parameterized constructor
	def __init__(self, a=None, b=None, c=None, d=None, date=None, e=None, funds=0, message=None, moneyInvested=0, numStocksOwned=0, outputFilePath=None, price=0, stockSymbol=None):
		self.date = date
		self.funds = funds
		self.price = price
		self.stockSymbol = stockSymbol
		self.numStocksOwned = numStocksOwned
		self.moneyInvested = moneyInvested
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
		self.message = message
		self.outputFilePath = outputFilePath
		
		# Clear the output file
		open(self.outputFilePath, 'w').close()
	
	# Output data to a file
	def outputToFile(self, message=None):		
		# Append the available data to the output file in a json string
		f = open(self.outputFilePath, 'a')
		f.write("\n--------------------\nrecord\n")
		info = {"date": str(self.date)}
		if self.funds is not None: info["funds"] = "$" + str(self.funds)
		if self.price is not None: info["price"] = "$" + str(self.price)
		if self.stockSymbol is not None: info["stockSymbol"] = self.stockSymbol
		if self.numStocksOwned is not None: info["numStocksOwned"] = self.numStocksOwned
		if self.moneyInvested is not None: info["moneyInvested"] = "$" + str(self.moneyInvested)
		if self.a is not None: info["a"] = "$" + str(self.a)
		if self.b is not None: info["b"] = "$" + str(self.b)
		if self.c is not None: info["c"] = "$" + str(self.c)
		if self.d is not None: info["d"] = "$" + str(self.d)
		if self.e is not None: info["e"] = "$" + str(self.e)
		if message is not None: info["message"] = message
		f.write(json.dumps(info, indent=2))
		f.write("\n--------------------\n")
		f.close()
	
	# Getters and setters
	def getDate(self):
		return self.date
	
	def setDate(self, newDate):
		self.date = newDate
		
	def getFunds(self):
		return self.funds
	
	def setFunds(self, newFunds):
		self.funds = newFunds
	
	def getPrice(self):
		return self.price
	
	def setPrice(self, newPrice):
		self.price = newPrice

	def getStockSymbol(self):
		return self.stockSymbol
	
	def setStockSymbol(self, newStockSymbol):
		self.stockSymbol = newStockSymbol
	
	def getNumStocksOwned(self):
		return self.numStocksOwned
	
	def setNumStocksOwned(self, newNumStocksOwned):
		self.numStocksOwned = newNumStocksOwned
	
	def getMoneyInvested(self):
		return self.moneyInvested
	
	def setMoneyInvested(self, newMoneyInvested):
		self.moneyInvested = newMoneyInvested
	
	def getA(self):
		return self.a
	
	def setA(self, newA):
		self.a = newA
	
	def getB(self):
		return self.b
	
	def setB(self, newB):
		self.b = newB
	
	def getC(self):
		return self.c
	
	def setC(self, newC):
		self.c = newC
	
	def getD(self):
		return self.d
	
	def setD(self, newD):
		self.d = newD
	
	def getE(self):
		return self.e
	
	def setE(self, newE):
		self.e = newE
	
	def getMessage(self):
		return self.message
	
	def setMessage(self, newMessage):
		self.message = newMessage

	def getOutputFilePath(self):
		return self.outputFilePath
	
	def setOutputFilePath(self, newOutputFilePath):
		self.outputFilePath = newOutputFilePath