import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def Off(x):
	y = 0
	return y/3600

def Quiescent(x):
	y = .2339
	return y/3600

def HouseKeeping(x):
	y = .3644
	return y/3600

def Intensive(x):
	y = 1.0393
	return y/3600

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Safe Mode":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Cruise - Idle":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Scan - Point Prep":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Scan - Target Point":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Scan - Point Exit":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Scan - Nadir Point":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Deployment - Boot":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Deployment - Connect Prep":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Cruise - Radiation Idle":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Cruise - Power Generation":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Cruise - Heat Protection Idle":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Data Processing - Compute Prep":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Data Processing - SfM":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Data Processing - Neural Net":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Data Processing - Blob Detect":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Data Processing - Compute Exit":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Data Downlink - Data Prep":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Data Downlink - Data Transmit":
		return quad(Quiescent, 0, interval)[1]
	elif mode == "Data Downlink - Transmit Exit": 
		return quad(Quiescent, 0, interval)[1]
	else:
		return 0