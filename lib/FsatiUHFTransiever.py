import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def Off(x):
	y = 0
	return y

def RXOnly(x):
	y = .2213
	return y

def TXHalfW(x):
	y = 2.4795
	return y

def TX1W(x):
	y = 3.3295
	return y

def TX2W(x):
	y = 5.1295
	return y

def TXandRX(x):
	y = .4426
	return y

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Safe Mode":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Cruise - Idle":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Scan - Point Prep":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Scan - Target Point":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Scan - Point Exit":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Scan - Nadir Point":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Deployment - Boot":
		return quad(RXOnly, 0, interval)[0]
	elif mode == "Deployment - Connect Prep":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Cruise - Radiation Idle":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Cruise - Power Generation":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Cruise - Heat Protection Idle":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Processing - Compute Prep":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Processing - SfM":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Processing - Neural Net":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Processing - Blob Detect":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Processing - Compute Exit":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Downlink - Data Prep":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Downlink - Data Transmit":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Downlink - Transmit Exit": 
		return quad(TX2W, 0, interval)[0]
	else:
		return 0