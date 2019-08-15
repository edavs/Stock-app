import datetime as dt
import json

# Abstract class. Parent class to all the other classes
class Record:
	id = 0
	date = dt.datetime.now()
	message = ""
	outputFilePath = "Output.txt"
	
	# Parameterized constructor
	def __init__(self, id=0, date=dt.datetime.now(), message="", outputFilePath="Output.txt"):
		self.id = id
		self.date = date
		self.message = message
		self.outputFilePath = outputFilePath
		
		# Clear the output file
		open(self.outputFilePath, 'w').close()
	
	# Output data to a file. This function should be virtual and implemented by each child
	def outputToFile(self, message):		
		# Append the available data to the output file in a json string
		f = open(self.outputFilePath, 'a')
		f.write("\n--------------------\nrecord\n")
		info = {"date": str(self.date)}
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
	
	def getMessage(self):
		return self.message
	
	def setMessage(self, newMessage):
		self.message = newMessage

	def getOutputFilePath(self):
		return self.outputFilePath
	
	def setOutputFilePath(self, newOutputFilePath):
		self.outputFilePath = newOutputFilePath