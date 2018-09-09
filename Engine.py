from itertools import *
import Component1
import Component2

test = True
interval = 0

def getInterval():
	'''defunct-----------------
	startTimes = line1.split(",")[0].split(" ").pop().split(":")
	endTimes = line1.split(",")[0].split(" ").pop().split(":")

	for x, y in izip(startTimes, endTimes):
		x = float(x)
		y = float(y)

	(endTimes[1] - startTimes[1]) * 60 + (endTimes[2] - startTimes[2])
	print(startTimes[0])-------------'''
	#just define the interval time IN SECONDS here
	interval = 30
	return interval

def scrapeInfo(line):
	#this may get more complex later
	lineInfo = line.split(",")
	lineInfo[-1] = lineInfo[-1].replace("\n", "")

	#this if will only occur at the end of the file and helps exit cleanly
	if lineInfo[0] == '':
		return lineInfo[0], lineInfo[1], lineInfo[2], lineInfo[3]
	return lineInfo[0], float(lineInfo[1]), float(lineInfo[2]), lineInfo[3]

def cleanHeader(f):
	#cleaning the csv so just the data is left and the first two lines are set
	line1 = f.readline()

	while "Current Submode" not in line1:
		line1 = f.readline()

	line1 = f.readline()
	line2 = f.readline()
	return line1, line2, f

def convertItoA(arg):
	arg = (float(arg)/3600)*getInterval()
	return float(arg)

def ReadCsv():
	#opens the timeline csv and scrapes the info from each line
	with open("powertestdata.csv") as f:
		totalPower = 0
		curLine, nextLine, f = cleanHeader(f)
		interval = getInterval()

		#sperating the elements(cloumns of the STK.csv) This is done for readability
		curLineTime, curLinePowGain, curLineSol, curLineMode = scrapeInfo(curLine)
		nextLineTime, nextLinePowGain, nextLineSol, nextLineMode = scrapeInfo(nextLine)

		g = open("engineOutput.csv", "w+")
		g.write("Time,Submode,Power Generated (W),Power Consumed (W),Battery Level(W)\n")

		while nextLineTime != '':
			#plugs in the submode info to each component (line#Info[-1])
			powConsp1 = Component1.getPower(curLineMode, interval)
			powConsp2 = Component2.getPower(curLineMode, interval)
			#converts the instatanious data to actual data, i.e. Watt/hrs to Watts
			powConsumed = powConsp1 + powConsp2
			actualPowGain = convertItoA(curLinePowGain)
			totalPower += (actualPowGain - powConsumed)

			#incrementing the lines by 1
			curLineTime, curLinePowGain, curLineSol, curLineMode = nextLineTime, nextLinePowGain, nextLineSol, nextLineMode
			nextLineTime, nextLinePowGain, nextLineSol, nextLineMode = scrapeInfo(f.readline())

			#writeToOut(g, curLineTime, curLineMode, totalPower)
			g.write(str(curLineTime) + "," + str(curLineMode) + "," + str(actualPowGain) + "," + str(powConsumed) + "," + str(totalPower) + "\n")

		g.close()

if __name__ == "__main__":
	ReadCsv()























