import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def Off(x):
	y = 0
	return y

def Heater(x):
	y = .6
	return y

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Safe Mode":
		return quad(Heater, 0, interval)[0]
	elif mode == "Cruise - Idle":
		return quad(Heater, 0, interval)[0]
	elif mode == "Scan - Point Prep":
		return quad(Heater, 0, interval)[0]
	elif mode == "Scan - Target Point":
		return quad(Heater, 0, interval)[0]
	elif mode == "Scan - Point Exit":
		return quad(Heater, 0, interval)[0]
	elif mode == "Scan - Nadir Point":
		return quad(Heater, 0, interval)[0]
	elif mode == "Deployment - Boot":
		return quad(Heater, 0, interval)[0]
	elif mode == "Deployment - Connect Prep":
		return quad(Heater, 0, interval)[0]
	elif mode == "Cruise - Radiation Idle":
		return quad(Heater, 0, interval)[0]
	elif mode == "Cruise - Power Generation":
		return quad(Heater, 0, interval)[0]
	elif mode == "Cruise - Heat Protection Idle":
		return quad(Heater, 0, interval)[0]
	elif mode == "Data Processing - Compute Prep":
		return quad(Heater, 0, interval)[0]
	elif mode == "Data Processing - SfM":
		return quad(Heater, 0, interval)[0]
	elif mode == "Data Processing - Neural Net":
		return quad(Heater, 0, interval)[0]
	elif mode == "Data Processing - Blob Detect":
		return quad(Heater, 0, interval)[0]
	elif mode == "Data Processing - Compute Exit":
		return quad(Heater, 0, interval)[0]
	elif mode == "Data Downlink - Data Prep":
		return quad(Heater, 0, interval)[0]
	elif mode == "Data Downlink - Data Transmit":
		return quad(Heater, 0, interval)[0]
	elif mode == "Data Downlink - Transmit Exit": 
		return quad(Heater, 0, interval)[0]
	else:
		return 0