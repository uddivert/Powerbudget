import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def Off(x):
	y = 0.0
	return y

def RX(x):
	y = 0.221
	return y

def TxhalfW(x):
	y = 2.5
	return y

def TX1W(x):
	y = 2.8562
	return y

def TX2W(x):
	y = 5.1
	return y

def Beacon(x):
	y = 0.8717
	return y

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Scan - Point Prep":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Scan - Target Point":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Scan - Point Exit":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Scan - Nadir Point":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Deployment - Boot":
		return quad(RX, 0, interval)[0]
	elif mode == "Deployment - Connect Prep":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Data Processing - Compute Prep":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Data Processing - SfM":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Data Processing - Neural Net":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Data Processing - Neural Net":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Data Processing - Blob Detect":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Data Processing - Compute Exit":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Data Downlink - Data Prep":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Downlink - Data Transmit":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Data Downlink - Transmit Exit":
		return quad(TX2W, 0, interval)[0]
	elif mode == "Safe Mode":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Cruise - Idle":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Cruise - Radiation Idle":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Cruise - Power Generation":
		return quad(Beacon, 0, interval)[0]
	elif mode == "Cruise - Heat Protection Idle":
		return quad(Beacon, 0, interval)[0]
	else:
		return 0