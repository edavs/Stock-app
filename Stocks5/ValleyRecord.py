import Record

# A Valley holds the points and slants that implement the trading strategy
class ValleyRecord(Record):
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	
	# Parameterized constructor
	def __init__(self, a=0, b=0, c=0, d=0, e=0):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
	
	# Getters and setters
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