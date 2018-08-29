from itertools import *
import Component1
import Component2

def getInterval(line1, line2):
	startTimes = line1.split(",")[0].split(" ").pop().split(":")
	endTimes = line1.split(",")[0].split(" ").pop().split(":")
	
	for x, y in izip(startTimes, endTimes):
		x = float(x)
		y = float(y)

	print(startTimes[0])
	return startTimes

def cleanHeader(f):
	line1 = f.readline()

	while "Current Submode" not in line1:
		line1 = f.readline()

	line1 = f.readline()
	line2 = f.readline()
	return line1, line2, f

def ReadCsv():
	with open("powertestdata.csv") as f:
		line1, line2, f = cleanHeader(f)
		time = getInterval(line1, line2)

	#print("The first line is " + line1)
	#print("The second line is " + line2)
	print(time)

if __name__ == "__main__":
	ReadCsv()

