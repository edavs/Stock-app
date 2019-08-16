"""
-Eduardo Davila
-08/15/2019
-ValleyStrategy.py
-TODO: Describe the file
"""

# TODO: Describe the class
# TODO: Figure out how to tie the ValleyStrategy and the Portfolio together. Perhaps by an id.
# TODO: Consider changing class name to InvestingStrategy
class ValleyStrategy():
	## Properties ##
	# TODO: Consider consolidating all slants into 1 list
	slant1 = 0.9
	slant2 = 0.9
	slant3 = 0.9
	slant4 = 0.9
	# TODO: Implement other aspects of an investing strategy such as a time limit on HODL, a high and low price limit, and continouos buying as item price per unit falls.
	
	## Constructors ##
	# Parameterized constructor
	def __init__(self, slant1=0.9, slant2=0.9, slant3=0.9, slant4=0.9):
		self.slant1 = slant1
		self.slant2 = slant2
		self.slant3 = slant3
		self.slant4 = slant4	
	
	## Getters & setters ##
	def getSlant1(self):
		return self.slant1
	def setSlant1(self, newSlant1):
		self.slant1 = newSlant1
	
	def getSlant2(self):
		return self.slant2
	def setSlant2(self, newSlant2):
		self.slant2 = newSlant2
	
	def getSlant3(self):
		return self.slant3
	def setSlant3(self, newSlant3):
		self.slant3 = newSlant3
	
	def getSlant4(self):
		return self.slant4
	def setSlant4(self, newSlant4):
		self.slant4 = newSlant4