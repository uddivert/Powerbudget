import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def Off(x):
	y = 0.0
	return y

def Load(x):
	y = 4.74
	return y

def Idle(x):
	y = 4.104
	return y

def Max(x):
	y = 5.28
	return y

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == Safe Mode:
		return quad(Safe Mode, 0, interval)[0]
	elif mode == Cruise - Idle:
		return quad(Cruise - Idle, 0, interval)[0]
	elif mode == Deployment - Boot:
		return quad(Deployment - Boot, 0, interval)[0]
	elif mode == Deployment - Connect Prep:
		return quad(Deployment - Connect Prep, 0, interval)[0]
	elif mode == Cruise - Radiation Idle:
		return quad(Cruise - Radiation Idle, 0, interval)[0]
	elif mode == Cruise - Power Generation:
		return quad(Cruise - Power Generation, 0, interval)[0]
	elif mode == Cruise - Heat Protection Idle:
		return quad(Cruise - Heat Protection Idle, 0, interval)[0]
	elif mode == Data Processing - Compute Prep:
		return quad(Data Processing - Compute Prep, 0, interval)[0]
	elif mode == Data Downlink - Transmit Exit:
		return quad(Data Downlink - Transmit Exit, 0, interval)[0]
	elif mode == Data Processing - Compute Prep:
		return quad(Data Processing - Compute Prep, 0, interval)[0]
	elif mode == Data Processing - Neural Net:
		return quad(Data Processing - Neural Net, 0, interval)[0]
	elif mode == Data Processing - SfM:
		return quad(Data Processing - SfM, 0, interval)[0]
	elif mode == Data Processing - Blob Detect:
		return quad(Data Processing - Blob Detect, 0, interval)[0]
	elif mode == Data Processing - Compute Exit:
		return quad(Data Processing - Compute Exit, 0, interval)[0]
	elif mode == Data Downlink - Data Prep:
		return quad(Data Downlink - Data Prep, 0, interval)[0]
	elif mode == Data Downlink - Data Transmit:
		return quad(Data Downlink - Data Transmit, 0, interval)[0]
	elif mode == Scan - Target Point:
		return quad(Scan - Target Point, 0, interval)[0]
	elif mode == Scan - Point Prep:
		return quad(Scan - Point Prep, 0, interval)[0]
	elif mode == Scan - Point Exit:
		return quad(Scan - Point Exit, 0, interval)[0]
	elif mode == Scan - Nadir Point:
		return quad(Scan - Nadir Point, 0, interval)[0]
	else:
		return 0