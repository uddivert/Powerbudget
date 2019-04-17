import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def Off(x):
	y = 0.0
	return y

def Active(x):
	y = 3.0
	return y

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Safe Mode":
		return quad(Off, 0, interval)[0]
	elif mode == "Cruise - Idle":
		return quad(Off, 0, interval)[0]
	elif mode == "Deployment - Boot":
		return quad(Off, 0, interval)[0]
	elif mode == "Deployment - Connect Prep":
		return quad(Off, 0, interval)[0]
	elif mode == "Cruise - Radiation Idle":
		return quad(Off, 0, interval)[0]
	elif mode == "Cruise - Power Generation":
		return quad(Off, 0, interval)[0]
	elif mode == "Cruise - Heat Protection Idle":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Processing - Compute Prep":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Processing - SfM":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Processing - Neural Net":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Processing - Neural Net":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Processing - Blob Detect":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Processing - Compute Exit":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Downlink - Data Prep":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Downlink - Data Transmit":
		return quad(Off, 0, interval)[0]
	elif mode == "Data Downlink - Transmit Exit":
		return quad(Off, 0, interval)[0]
	elif mode == "Scan - Point Prep":
		return quad(Active, 0, interval)[0]
	elif mode == "Scan - Target Point":
		return quad(Active, 0, interval)[0]
	elif mode == "Scan - Point Exit":
		return quad(Active, 0, interval)[0]
	elif mode == "Scan - Nadir Point":
		return quad(Active, 0, interval)[0]
	else:
		return 0