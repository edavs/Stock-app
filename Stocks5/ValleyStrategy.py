import Record

class ValleyStrategy(Record):
	# properties
	slant1 = 0.9
	slant2 = 0.9
	slant3 = 0.9
	slant4 = 0.9
	
	# Parameterized constructor
	def __init__(self, slant1=0.9, slant2=0.9, slant3=0.9, slant4=0.9):
		self.slant1 = slant1
		self.slant2 = slant2
		self.slant3 = slant3
		self.slant4 = slant4	
	
	# Getters & setters
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