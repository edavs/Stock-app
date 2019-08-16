"""
-Eduardo Davila
-08/15/2019
-ValleyRecord.py
-TODO: Describe the file
"""

import datetime as dt
import Record

# TODO: Describe the class
# TODO: Figure out how to tie the ValleyRecord and the Investment together. Perhaps by an id.
# TODO: Consider changing class name to InvestingRecord
class ValleyRecord(Record.Record):
	## Properties ##
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	itemUnitPrice = 0
	
	## Constructors ##
	# Parameterized constructor
	def __init__(self, id=0, date=dt.datetime.now(), a=0, b=0, c=0, d=0, e=0, itemUnitPrice=0, outputDestination="./ValleyRecord.txt"):
		super(ValleyRecord, self).__init__(id, date)
		
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
		self.itemUnitPrice = itemUnitPrice
		outputDestination = outputDestination
	
	## Methods ##
	# Write to the output file. Output the data as a json string
	def outputToDestination(self, message):
		
		# Update the message
		if message is not None: self.message = message
	
		f = open(self.outputDestination, 'a')  # Open the output file to be appended
		f.write('\n' + self.__class.__name__ + '\n')
		info = {}  # Dictionary to hold all the data that will be outputted
		# This is the data to be outputted
		if self.id is not None: info["Id"] = str(self.id)
		if self.date is not None: info["Date"] = '$' + str(self.date)
		if self.a is not None: info["a"] = '$' + str(self.a)
		if self.b is not None: info["b"] = '$' + str(self.b)
		if self.c is not None: info["c"] = '$' + str(self.c)
		if self.d is not None: info["d"] = '$' + str(self.d)
		if self.e is not None: info["e"] = '$' + str(self.e)
		if self.itemUnitPrice is not None: info["Item unit price"] = '$' + str(self.itemUnitPrice)
		if self.message is not None: info["Message"] = self.message
		f.write(json.dumps(info, indent=2))  # Convert the dictionary into a json string
		f.write('\n')
		f.close()  # Close the output file
	
	## Getters and setters ##
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
	
	def getItemUnitPrice(self):
		return self.itemUnitPrice
	def setItemUnitPrice(self, newItemUnitPrice):
		self.itemUnitPrice = newItemUnitPrice