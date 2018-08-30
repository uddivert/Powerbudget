import numpy as np
from scipy.integrate import simps
from numpy import trapz

def getPower(mode, interval):
	if mode == "Cruise - Idle":
		return C2PS1(interval)
	elif mode == "Scan - Point Prep":
		return C2PS2(interval)

def C2PS1(x):
	y = np.tan(x)
	return y

def C2PS2(x):
	y = np.sin(x)/2
	return y