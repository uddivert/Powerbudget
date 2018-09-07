from itertools import *
import Component1
import Component2

test = True
interval = 0

def getInterval(line1, line2):
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
	return lineInfo

def cleanHeader(f):
	#cleaning the csv so just the data is left and the first two lines are set
	line1 = f.readline()

	while "Current Submode" not in line1:
		line1 = f.readline()

	line1 = f.readline()
	line2 = f.readline()
	return line1, line2, f

def convertItoA(*args):
	results = []
	count = 0
	for arg in args:
		results[count] = float(arg)*3600/getInterval(1,2)
		count += 1

def ReadCsv():
	#opens the timeline csv and scrapes the info from each line
	with open("powertestdata.csv") as f:
		totalPower = 0
		line1, line2, f = cleanHeader(f)
		interval = getInterval(line1, line2)
		line1Info = scrapeInfo(line1)
		line2Info = scrapeInfo(line2)

		g = open("engineOutput.csv", "w+")
		g.write("Time,Submode,Power Generated (W/hr), Power Consumed (W/hr), Battery Level(W)")
		while line2 != '':
			#plugs in the submode info to each component (line#Info[-1])
			powConsp1 = Component1.getPower(line1Info[-1], interval)
			powConsp2 = Component2.getPower(line1Info[-1], interval)
			wattGain, c1WattConsp, c2WattConsp = convertItoA(line1Info[1], powConsp1, powConsp2)
			totalPower += (float(line1Info[1]) - powConsp1 - powConsp2)

			#incrementing the line by 1
			line1Info = line2Info
			line2Info = scrapeInfo(f.readline())
			g.write(str(line1Info[0]) + "," + str(line1Info[-1]) + "," + str(totalPower) + "\n")
		g.close()

if __name__ == "__main__":
	ReadCsv()

