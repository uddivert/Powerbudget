from itertools import *
from lib import MAIADCS
from lib import ClydeOBC
from lib import ClydeSBandAntenna
from lib import ClydeSunSensors
from lib import FsatiUHFTransiever
from lib import GomSpaceBP4
from lib import IDS
from lib import ISISUHFAntenna
from lib import P60PDU
from lib import P60AC
from lib import SolarPanels
from lib import Tx2i
#I know this looks ridiculous but the * would not work

test = True
interval = 30

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
	return interval

def scrapeInfo(line):
	#this may get more complex later
	lineInfo = line.split(",")
	lineInfo[-1] = lineInfo[-1].replace("\n", "")

	#this if will only occur at the end of the file and helps exit cleanly
	if lineInfo[0] == '':
		return lineInfo[0], 0, 0, 0
	return lineInfo[0], float(lineInfo[1]), float(lineInfo[2]), lineInfo[3]

def cleanHeader(f):
	#cleaning the csv so just the data is left and the first two lines are set
	line1 = f.readline()

	while "Current Submode" not in line1:
		line1 = f.readline()
		if line1 == '':
			print("please make sure your .csv file is formatted properly, you may be missing a header")
			sys.exit(1)

	line1 = f.readline()
	line2 = f.readline()
	return line1, line2, f

def convertItoA(arg):
	arg = (float(arg)/3600)*getInterval()
	return float(arg)
'''this function is essentail, it plugs in the interval and submode into each of the component files
and compiles them into an array and also sums them for a total power consumption. It is intentionally
verbose so it is easy to see if all the components are being called and returning info''' 
def calculateComps(curLineMode, interval):
	total = 0
	componentDraws = []
	componentDraws.append(MAIADCS.getPower(curLineMode, interval))
	componentDraws.append(ClydeOBC.getPower(curLineMode, interval))	
	componentDraws.append(ClydeSBandAntenna.getPower(curLineMode, interval))
	componentDraws.append(ClydeSunSensors.getPower(curLineMode, interval))
	componentDraws.append(FsatiUHFTransiever.getPower(curLineMode, interval))
	componentDraws.append(GomSpaceBP4.getPower(curLineMode, interval))
	componentDraws.append(IDS.getPower(curLineMode, interval))
	componentDraws.append(ISISUHFAntenna.getPower(curLineMode, interval))
	componentDraws.append(P60PDU.getPower(curLineMode, interval))
	componentDraws.append(P60AC.getPower(curLineMode, interval))
	componentDraws.append(SolarPanels.getPower(curLineMode, interval))
	componentDraws.append(Tx2i.getPower(curLineMode, interval))
	for x in range(len(componentDraws)):
		total += componentDraws[x]
	return total, componentDraws

def GenCsv():
	totalPower = 38
	valid = True

	#opens the timeline csv and scrapes the info from each line, processes, and writes to output.csv
	with open("./Inputs/powertestdata.csv") as f:
		curLine, nextLine, f = cleanHeader(f)
		interval = getInterval()
		
		#sperating the elements(cloumns of the STK.csv) This is done for readability
		curLineTime, curLinePowGain, curLineSol, curLineMode = scrapeInfo(curLine)
		nextLineTime, nextLinePowGain, nextLineSol, nextLineMode = scrapeInfo(nextLine)

		#opening the csv and adding the headers
		g = open("engineOutput.csv", "w+")
		g.write("Time,Submode,Power Generated (W),Power Consumed (W),Battery Level(W),,MAIADCS consumption,ClydeOBC consumption,ClydeSBandAntenna,"+
			"ClydeSunSensors,FsatiUHFTransiever,GomSpaceBP4,IDS,ISISUHFAntenna,P60PDU,P60AC,SolarPanels,Tx2i\n")

		while nextLineTime != '':

			#plugs in the submode info to each component (line#Info[-1])
			powConsumed, componentDraws = calculateComps(curLineMode, interval)

			#converts the instatanious data to actual data, i.e. Watt/hrs to Watts
			actualPowGain = convertItoA(curLinePowGain)
			totalPower += (actualPowGain - powConsumed)

			#incrementing the lines by 1
			curLineTime, curLinePowGain, curLineSol, curLineMode = nextLineTime, nextLinePowGain, nextLineSol, nextLineMode
			nextLineTime, nextLinePowGain, nextLineSol, nextLineMode = scrapeInfo(f.readline())

			#leveling the battery power if the gain is over capacity
			if totalPower > 38:
				totalPower = 38
				print("The power exceeded battery capacity and was leveled at time " + str(curLineTime))

			#writing all the info the the output.csv
			g.write(str(curLineTime) + "," + str(curLineMode) + "," + str(actualPowGain) + "," + str(powConsumed) + "," + str(totalPower) + ",")
			for x in range(len(componentDraws)):
				g.write("," + str(componentDraws[x]))
			g.write("\n")

			#if the power drops dangerously low, did not stop program altogether because I figure more info is always better
			if totalPower < 5:
				print("Power below 5W at " + str(curLineTime))
				valid = False

		#if the battery power never dropped too low
		if valid == True:
			print("This timeline has passed!")
		g.close()

if __name__ == "__main__":
	GenCsv()























