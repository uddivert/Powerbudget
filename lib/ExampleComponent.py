import numpy as np
from scipy.integrate import quad
from numpy import trapz
from math import *

#defines the mathematical functions associated with each power state
def C2PState1(x):
	y = sin(x)
	return y

def C2PState2(x):
	y = cos(x)
	return y

#calls the appropriate power state given the submode
def getPower(mode, interval):
	if mode == "Cruise - Idle":
		return quad(C2PState1, 0, interval)[0]
	elif mode == "Scan - Point Prep":
		return quad(C2PState2, 0, interval)[0]
	else:
		return 0