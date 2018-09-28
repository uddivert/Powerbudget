import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def C1PState1(x):
	y = cos(x)/2
	return y

def C1PState2(x):
	y = 2*sin(x)
	return y

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Cruise - Idle":
		return quad(C1PState1, 0, interval)[1]
	elif mode == "Scan - Point Prep":
		return quad(C1PState2, 0, interval)[1]
	else:
		return 0