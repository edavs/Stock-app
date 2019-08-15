"""
Eduardo Davila
Stocks3.py
4/13/2019
Algoritmo simple para comprar y vender acciones.
"""

import sys, StockAnalyzer, FSM

"""
Algoritmo: [TODO: Nombrar el algoritmo]
[TODO: Describir el algoritmo]

-Proceso	
	-Estado: waitingForTheComeback
		-if currentDay >= leftPeak:
			-rightPeak = currentDay
			-nextState = waitingToSell
		-elif currentDay < valleyBottom:
			-valleyBottom = currentDay
			-nextState = waitingToBuy
		-else:
			-nextState = waitingForTheComeback
		-A~adir 1 dia a currentDay.
		-Ir a nextState
	
	-Estado: waitingToSell
		-if currentDay es smallDrop(1%) < rightPeak:
			-sellSweetSpot = currentDay
			-Vender al precio de sellSweetSpot.
			-leftDate = rightPeak
			-nextState = waitingForTheFall
		-else:
			-if currentDay > rightPeak:
				-rightPeak = currentDay
			-nextState = waitingToSell
		-A~adir 1 dia a currentDay.
		-Ir a nextState
"""

FSM.fsm("initialize", sys.argv[1:])









