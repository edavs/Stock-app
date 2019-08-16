"""
-Eduardo Davila
-08/15/2019
-Investment.py
-TODO: Describe the file
"""

import datetime as dt
import Record, ValleyRecord, Portfolio

# TODO: Describe the class
class Investment(Record.Record):
	## Properties ##
	cashValue = 0
	itemValue = 0  # TODO: Implement a way to update this value each time the price changes
	totalValue = cashValue + itemValue  # TODO: Implement a way to update this value each time self.itemValue changes
	itemName = ""
	itemCount = 0
	valleyRecord = ValleyRecord.ValleyRecord()  # TODO: Tie the ValleyRecord and the Investment together, perhaps by an id.
	
	## Constructors ##
	# Parameterized constructor
	def __init__(self, id=0, date=dt.datetime.now(), cashValue=0, itemValue=0, totalValue=cashValue+itemValue, itemName="", itemCount=0, valleyRecord=ValleyRecord.ValleyRecord(), outputDestination="./Investment.txt"):
		super(Investment, self).__init__(id, date)
	
		self.cashValue = cashValue
		self.itemValue = itemValue
		self.totalValue = self.cashValue + self.itemValue
		self.itemName = itemName
		self.itemCount = itemCount
		self.valleyRecord = valleyRecord
		outputDestination = outputDestination
	
	## Methods ##
	def updateTotalValue(self):
		self.setTotalValue(self.cashValue + self.itemValue)
	
	def purchase(self):
		
	
	def sell(self):
		
	
	# Write to the output file. Output the data as a json string
	def outputToDestination(self, message):
		
		# Update the message
		if message is not None: self.message = message
	
		f = open(self.outputDestination, 'a')  # Open the output file to be appended
		f.write('\n' + self.__class.__name__ + '\n')
		info = {}  # Dictionary to hold all the data that will be outputted
		# This is the data to be outputted
		if self.id is not None: info["Id"] = str(self.id)
		if self.date is not None: info["Date"] = str(self.date)
		if self.totalValue is not None: info["Total value"] = '$' + str(self.totalValue)
		if self.cashValue is not None: info["Cash value"] = '$' + str(self.cashValue)
		if self.itemValue is not None: info["Item value"] = '$' + str(self.itemValue)
		if self.itemCount is not None: info["Item count"] = str(self.itemCount)
		if self.itemName is not None: info["Item name"] = str(self.itemName)
		if self.message is not None: info["Message"] = self.message
		f.write(json.dumps(info, indent=2))  # Convert the dictionary into a json string
		f.write('\n')
		f.close()  # Close the output file
	
	## Getters & setters ##
	def getTotalValue(self):
		return self.totalValue
	def setTotalValue(self, newTotalValue):
		self.totalValue = newTotalValue
	
	def getCashValue(self):
		return self.cashValue
	def setCashValue(self, newCashValue):
		self.cashValue = newCashValue
		self.updateTotalValue()
	
	def getItemValue(self):
		return self.itemValue
	def setItemValue(self, newItemValue):
		self.itemValue = newItemValue
		self.updateTotalValue()
	
	def getItemName(self):
		return self.itemName
	def setItemName(self, newItemName):
		self.itemName = newItemName
	
	def getItemCount(self):
		return self.itemCount
	def setItemCount(self, newItemCount):
		self.itemCount = newItemCount
	
	def getValleyRecord(self):
		return self.valleyRecord
	def setValleyRecord(self, newValleyRecord):
		self.valleyRecord = newValleyRecord