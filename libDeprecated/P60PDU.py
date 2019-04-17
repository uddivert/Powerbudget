import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def Off(x):
	y = 0
	return y

def Vcc(x):
	y = .165
	return y

def Vbat(x):
	y = .08
	return y

def Standby(x):
	y = .6
	return y

def StandbyPlus(x):
	y = .845
	return y

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Safe Mode":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Cruise - Idle":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Scan - Point Prep":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Scan - Target Point":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Scan - Point Exit":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Scan - Nadir Point":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Deployment - Boot":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Deployment - Connect Prep":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Cruise - Radiation Idle":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Cruise - Power Generation":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Cruise - Heat Protection Idle":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Data Processing - Compute Prep":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Data Processing - SfM":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Data Processing - Neural Net":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Data Processing - Blob Detect":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Data Processing - Compute Exit":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Data Downlink - Data Prep":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Data Downlink - Data Transmit":
		return quad(StandbyPlus, 0, interval)[0]
	elif mode == "Data Downlink - Transmit Exit": 
		return quad(StandbyPlus, 0, interval)[0]
	else:
		return 0