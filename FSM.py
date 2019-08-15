"""
Eduardo Davila
FSM.py
4/13/2019
Estados para el algoritmo de Stocks3
"""

import StockAnalyzer as sa
import pandas_datareader.data as web
import os

def initialize(stockAnalyzerParameters):
	"""
	-Estado: initialize
		-currentDay = startDate. Igual para leftPeakDate.
		-El resto de los variables pueden ser null.
		-A~adir 1 dia a currentDay.
		-nextState = waitingForTheFall
		-Ir a nextState"""
	print("state: initialize")

	mySA = sa.StockAnalyzer(stockAnalyzerParameters)
	
	mySA.incrementCurrentDate(1)
	nextState = "waitingForTheFall"
	fsm(nextState, mySA)
 
def waitingForTheFall(mySA):
	"""
	-Estado: waitingForTheFall
		-if currentDate precio es largeDrop(10%) < leftPeakDate precio:
			-valleyBottom = currentDay
			-nextState = waitingToBuy
		-else:
			-if currentDate precio >= leftPeakDate precio:
				-leftPeakDate = currentDate
			-nextState = waitingForTheFall
		-A~adir 1 dia a currentDay.
		-Ir a nextState"""
	print("state: waitingForTheFall")
	mySA.print("StockAnalyzer in waitingForTheFall")  # Debugging
	Error is here in line 43. It won't let me call index 0(StockAnalyzer.py line 105)
	if mySA.getDateInfo(mySA.currentDate, "Open") <= mySA.getDateInfo(mySA.leftPeakDate, "Open") * 0.9:
		mySA.setValleyBottom(mySA.getCurrentDate())
		nextState = "waitingToBuy"
	elif mySA.getDateInfo(mySA.getCurrentDate(), "Open") >= mySA.getDateInfo(mySA.leftPeakDate, "Open"):
		mySA.setLeftPeakDate(mySA.getCurrentDate())
		nextState = "waitingForTheFall"
	
	mySA.incrementCurrentDate(1)
	fsm(nextState, mySA)
			 
def waitingToBuy(mySA):	
	"""
	-Estado: waitingToBuy
		-if currentDay es smallRise(1%) > valleyBottom:
			-buySweetSpot = currentDay
			-Comprar la accion al precio de buySweetSpot.
			-nextState = waitingForTheComeback
		-else:
			-if currentDay < valleyBottom:
				-valleyBottom = currentDay
			-nextState = waitingToBuy
		-A~adir 1 dia a currentDay.
		-Ir a nextState
	"""
	print("state: waitingToBuy")
	
	#if mySA.getDateInfo(mySA.getCurrentDate(), "Open") > mySA.getDateInfo(mySA.getValleyBottomDate(), "Open") * 1.01:
 
def waitingForTheComeback(mySA):
    print("state: waitingForTheComeback")
 
def waitingToSell(mySA):
    print("state: waitingToSell")
 
def fsm(state, argument):
	"""
	-Estados: Para evitar tantas declaraciones de if, mantener estos estados.
	#: Simboliza el orden de dias de pasado a futuro.
	-(1) initialize: Preparar los variables.
	-(2) waitingForTheFall: Esperando por una caida de 10% en el precio de la accion.
	-(3) waitingToBuy: Esperando un aumento de 1% en el precio de la accion para comprar.
	-(4) waitingForTheComeback: Esperando que el precio de la accion vuelva a subir a leftPeakDate.
	-(5) waitingToSell: Esperando que el precio de la accion baje por 1% para vender.
	"""
	
	switcher = {
		"initialize": initialize,
		"waitingForTheFall": waitingForTheFall,
		"waitingToBuy": waitingToBuy,
		"waitingForTheComeback": waitingForTheComeback,
		"waitingToSell": waitingToSell}
	
	# Get the function from switcher dictionary
	stateFunc = switcher.get(state, lambda: "Invalid state")

	# Execute the state function
	stateFunc(argument)