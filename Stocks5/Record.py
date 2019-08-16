"""
-Eduardo Davila
-08/15/2019
-Record.py
-TODO: Describe the file
"""

import datetime as dt
import json

# Abstract class.
# Parent class to all the other classes
class Record:
	## Properties ##
	id = 0
	date = dt.datetime.now()
	message = ""
	outputDestination = "./Output.txt"
		
	## Constructors ##
	# Parameterized constructor
	def __init__(self, id=0, date=dt.datetime.now(), outputDestination="./Record.txt", message=""):
		self.id = id
		self.date = date
		self.outputDestination = outputDestination
		self.message = message
		
		# Clear the output file
		open(self.outputDestination, 'w').close()
	
	## Methods ##
	# Write to the output file. Output the data as a json string
	# TODO: Figure out if there is a simpler way to handle the output because all the output functions in each class seem too similar, perhaps by implementing a class that handles output.
	def outputToDestination(self, message):
		pass

	## Getters and setters ##
	def getId(self):
		return self.id
	def setId(self, newId):
		self.id = newId
		
	def getDate(self):
		return self.date
	def setDate(self, newDate):
		self.date = newDate	

	def getOutputDestination(self):
		return self.outputDestination
	def setOutputDestination(self, newOutputDestination):
		self.outputDestination = newOutputDestination
	
	def getMessage(self):
		return self.message
	def setMessage(self, newMessage):
		self.message = newMessage