from itertools import *
import Component1
import Component2

def getInterval(line1, line2):
	'''defunct-----------------
	startTimes = line1.split(",")[0].split(" ").pop().split(":")
	endTimes = line1.split(",")[0].split(" ").pop().split(":")

	for x, y in izip(startTimes, endTimes):
		x = float(x)
		y = float(y)

	(endTimes[1] - startTimes[1]) * 60 + (endTimes[2] - startTimes[2])
	print(startTimes[0])-------------'''
	#just define the interval time here
	interval = 30
	return interval

def scrapeInfo(line):
	#this may get more complex later
	lineInfo = line.split(",")
	lineInfo[-1] = lineInfo[-1].replace("\n", "")
	return lineInfo

def cleanHeader(f):
	#cleaning the csv so just the data is left and the first two lines are set
	line1 = f.readline()

	while "Current Submode" not in line1:
		line1 = f.readline()

	line1 = f.readline()
	line2 = f.readline()
	return line1, line2, f

def ReadCsv():
	#opens the timeline csv and scrapes the info from each line
	with open("powertestdata.csv") as f:
		line1, line2, f = cleanHeader(f)
		interval = getInterval(line1, line2)
		line1Info = scrapeInfo(line1)
		line2Info = scrapeInfo(line2)
		while line2 != '':
			pow1 = Component1.getPower(line1Info[-1], interval)
			print(pow1)
			#pow2 = Component2.getPower(line1Info[-1], interval)
		line1Info = line2Info
		line2Info = scrapeInfo(f.readline())

	#print("The first line is " + line1)
	#print("The second line is " + line2)
	#print(time)

if __name__ == "__main__":
	ReadCsv()

