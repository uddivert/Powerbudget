import numpy as np
from scipy.integrate import simps
from numpy import trapz

def getPower(mode, interval):
	if mode == "Cruise - Idle":
		return C1PS1(interval)
	elif mode == "Scan - Point Prep":
		return C1PS2(interval)

def C1PS1(x):
	y = np.sin(x)/x
	return y

def C1PS2(x):
	y = np.cos(x)/x
	return y