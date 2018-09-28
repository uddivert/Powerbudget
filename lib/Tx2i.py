import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def Off(x):
	y = 0
	return y/3600

def Idle(x):
	y = 4.104
	return y/3600

def Load(x):
	y = 4.74
	return y/3600

def Max(x):
	y = 5.28
	return y/3600

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Safe Mode":
		return quad(Off, 0, interval)[1]
	elif mode == "Cruise - Idle":
		return quad(Off, 0, interval)[1]
	elif mode == "Scan - Point Prep":
		return (quad(Max, 0, interval)[1])*.5
	elif mode == "Scan - Target Point":
		return (quad(Max, 0, interval)[1])*.15
	elif mode == "Scan - Point Exit":
		return (quad(Max, 0, interval)[1])*.25
	elif mode == "Scan - Nadir Point":
		return (quad(Max, 0, interval)[1])*.15
	elif mode == "Deployment - Boot":
		return quad(Off, 0, interval)[1]
	elif mode == "Deployment - Connect Prep":
		return quad(Off, 0, interval)[1]
	elif mode == "Cruise - Radiation Idle":
		return quad(Off, 0, interval)[1]
	elif mode == "Cruise - Power Generation":
		return quad(Off, 0, interval)[1]
	elif mode == "Cruise - Heat Protection Idle":
		return quad(Off, 0, interval)[1]
	elif mode == "Data Processing - Compute Prep":
		return quad(Load, 0, interval)[1]
	elif mode == "Data Processing - SfM":
		return quad(Load, 0, interval)[1]
	elif mode == "Data Processing - Neural Net":
		return quad(Load, 0, interval)[1]
	elif mode == "Data Processing - Blob Detect":
		return quad(Load, 0, interval)[1]
	elif mode == "Data Processing - Compute Exit":
		return quad(Load, 0, interval)[1]
	elif mode == "Data Downlink - Data Prep":
		return quad(Load, 0, interval)[1]
	elif mode == "Data Downlink - Data Transmit":
		return quad(Load, 0, interval)[1]
	elif mode == "Data Downlink - Transmit Exit": 
		return quad(Off, 0, interval)[1]
	else:
		return 0