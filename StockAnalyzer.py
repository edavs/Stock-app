"""
Eduardo Davila
StockAnalyzer.py
4/13/2019
Clase de un objeto que contiene elementos para analizar acciones usando Stocks3"""

import datetime as dt
import pandas_datareader.data as web

class StockAnalyzer:
	"""
	TODO: Descripcion
	
	-Parametros
		-Constantes
			-stockName: Nombre de la accion para analizar.
			-webSource: Donde buscare informacion del stock market.
			-endDate: Fecha para cuando terminar de evaluar.
			-startDate: Fecha para cuando empezar a analizar.
			-largeDrop: Minimo que tiene que bajar el precio de la accion para estar interesado en comprar.
			-smallRise: Minimo que tiene que subir el precio de la accion despues de largeDrop para comprar.
			-smallDrop: Minimo que tiene que bajar el precio de la accion para vender.
		-Variables
			#: Simboliza el orden en el cual se usan de pasado a futuro.
			-(1) leftPeak: El dia con el precio mas alto en la izquierdo. El precio minimo de venta en el futuro. Estamos esperando a que el precio vuelva a subir a este precio.
			-(2) valleyBottomDate: El dia con el precio mas bajo que sea 10%+ menos que el precio de leftPeak.
			-(3) buySweetSpot: El dia con el precio 1% mas alto que el precio de valleyBottomDate. Compramos a este precio.
			-(4) rightPeak: El dia con el precio mas alto el la derecha y > leftPeak. Despues de vender, este se convierte en el nuevo leftPeak.
			-(5) sellSweetSpot: El dia con el precio 1% < el precio de rightPeak. Vender a este precio.
			-currentDate: El dia presente que hay que analizar.
			-leftDate: Buscando a leftPeak."""
	
	def __init__(self, 
		stockName="IBM", 
		webSource='yahoo',
		endDate=(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day),
		startDate=(dt.datetime.now().year - 1, dt.datetime.now().month, dt.datetime.now().day),
		largeDrop=0.1, 
		smallRise=0.01,
		smallDrop=0.01,
		leftPeakDate=(dt.datetime.now().year - 1, dt.datetime.now().month, dt.datetime.now().day),
		valleyBottomDate=None,
		buySweetSpot=None,
		rightPeak=None,
		sellSweetSpot=None,
		currentDate=(dt.datetime.now().year - 1, dt.datetime.now().month, dt.datetime.now().day)):
		
		# Constant values
		self.stockName = stockName
		self.webSource = webSource
		self.endDate = dt.datetime(endDate[0], endDate[1], endDate[2])
		self.startDate = dt.datetime(startDate[0], startDate[1], startDate[2])
		self.largeDrop = largeDrop
		self.smallRise = smallRise
		self.smallDrop = smallDrop
		
		# Variable values
		self.leftPeakDate = dt.datetime(leftPeakDate[0], leftPeakDate[1], leftPeakDate[2])
		self.valleyBottomDate = valleyBottomDate
		self.buySweetSpot = buySweetSpot
		self.rightPeak = rightPeak
		self.sellSweetSpot = sellSweetSpot
		self.currentDate = dt.datetime(currentDate[0], currentDate[1], currentDate[2])
		
		self.print("StockAnalyzer initialized")
		
	# # # Debugging methods # # #
	def print(self, starterMessage):
		"""
		Print every class attribute
		"""
		print(starterMessage)
		print("StockAnalyzer")
		print("stockName:", self.stockName)
		print("webSource:", self.webSource)
		print("endDate:", self.endDate)
		print("startDate:", self.startDate)
		print("largeDrop:", self.largeDrop)
		print("smallRise:", self.smallRise)
		print("smallDrop:", self.smallDrop)
		print("leftPeakDate:", self.leftPeakDate)
		print("valleyBottomDate:", self.valleyBottomDate)
		print("buySweetSpot:", self.buySweetSpot)
		print("rightPeak:", self.rightPeak)
		print("sellSweetSpot:", self.sellSweetSpot)
		print("currentDate:", self.currentDate)
		print()
	
	# # # Methods # # #
	def incrementCurrentDate(self, incrementDays):
		"""
		Move currentDay 1 day ahead
		"""
		self.currentDate += dt.timedelta(days=incrementDays)
	
	def getDateInfo(self, date, attribute):
		"""
		Return the stock information for the current date
		"""
		df = web.DataReader(self.stockName, self.webSource, date, date)
		if attribute is None:
			return df
		else:
			try:
				return df[attribute][0]
			except:
				print("Error in StockAnalyzer.getDateInfo(...)")
				
				# Debugging
				print("df[" + attribute + "]:\n", df[attribute])
				print("df[" + attribute + "][0]:\n", df[attribute][0])

	# # # Setters & Getters # # #
	def setCurrentDate(self, newCurrentDate):
		self.currentDate = newCurrentDate
	def getCurrentDate(self):
		return self.currentDate
		
	def setLeftPeakDate(self, newLeftPeakDate):
		self.leftPeakDate = newLeftPeakDate
	def getLeftPeakDate(self):
		return self.leftPeakDate
	
	def setvalleyBottomDate(self, newvalleyBottomDate):
		self.valleyBottomDate = newvalleyBottomDate
	def getvalleyBottomDate(self):
		return self.valleyBottomDate
	
	# # # Might not be needed # # #
	"""
	def setCurrentDateDf(self, newCurrentDateDf):
		print("Cannot change currentDateDf")
	def getCurrentDateDf(self):
		return self.currentDateDf
	
	def setLeftDateDf(self, newLeftDateDf):
		print("Cannot change leftDateDf")
	def getLeftDateDf(self):
		return self.leftDateDf
	"""
	
	
	
	
	
	
	