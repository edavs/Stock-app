
class Stock:
	id = None
	date = None
	outputFilePath = None
	price = None
	symbol = None
	
	def __init__(self, id, date, outputFilePath, price, symbol):
		# Parameterized constructor
		self.id = id
		self.date = date
		self.price = price
		self.symbol = symbol
	
	