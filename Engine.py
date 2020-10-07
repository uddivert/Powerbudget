from itertools import *
import sys
from lib import CubeSpaceADCS
from lib import ClydeOBC
from lib import ClydeSBandAntenna
from lib import ClydeSunSensors
from lib import FsatiUHFTransiever
from lib import ImperxC4180
from lib import BlackflyColorCam
from lib import ISISUHFAntenna
from lib import SolarPanels
from lib import Tx2i
from lib import XUA
from lib import CSLBAT
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
def calculateComps(curLineMode, interval, curLineTime):
	total = 0
	componentDraws = []
	componentDraws.append(CubeSpaceADCS.getPower(curLineMode, interval))
	componentDraws.append(ClydeOBC.getPower(curLineMode, interval))

	litmusDraw = ClydeSBandAntenna.getPower(curLineMode, interval)
	if litmusDraw < 0:
		print("Error occurred at time " + curLineTime)
		exit()

	componentDraws.append(ClydeSBandAntenna.getPower(curLineMode, interval))
	componentDraws.append(ClydeSunSensors.getPower(curLineMode, interval))
	componentDraws.append(FsatiUHFTransiever.getPower(curLineMode, interval))
	componentDraws.append(ImperxC4180.getPower(curLineMode, interval))
	componentDraws.append(BlackflyColorCam.getPower(curLineMode, interval))
	componentDraws.append(ISISUHFAntenna.getPower(curLineMode, interval))
	componentDraws.append(SolarPanels.getPower(curLineMode, interval))
	componentDraws.append(Tx2i.getPower(curLineMode, interval))
	componentDraws.append(XUA.getPower(curLineMode, interval))
	componentDraws.append(CSLBAT.getPower(curLineMode, interval))
	for x in range(len(componentDraws)):
		total += componentDraws[x]

	#total power draw is in units of joules!!
	return total, componentDraws

def GenCsv(powerCoeff, outfile):
	totalPower = 80
	valid = True

	#opens the timeline csv and scrapes the info from each line, processes, and writes to output.csv
	with open("Inputs/updatedTimeline.csv") as f:
		curLine, nextLine, f = cleanHeader(f)
		interval = getInterval()
		
		#sperating the elements(cloumns of the STK.csv) This is done for readability
		curLineTime, curLinePowGain, curLineSol, curLineMode = scrapeInfo(curLine)
		nextLineTime, nextLinePowGain, nextLineSol, nextLineMode = scrapeInfo(nextLine)

		#opening the csv and adding the headers
		g = open(outfile, "w+")
		g.write("Time,Submode,Power Generated (Joule),Power Consumed (Joule),Battery Level(Wh),,MAIADCS consumption,ClydeOBC consumption,ClydeSBandAntenna,"+
			"ClydeSunSensors,FsatiUHFTransiever,GomSpaceBP4,ImperxC4180,BlackflyColorCam,ISISUHFAntenna,P60PDU,P60AC,SolarPanels,Tx2i\n")

		lineCount = 0 				#counts the number of lines of data the will be processed
		totalPowerSum = totalPower	#holds the sum of the Battery Power for calculating the mean
		powerUseage = []
		solarGen = []
		maxBat = 0
		minBat = 81
		minOccured = ""
		maxOccured = ""
		while nextLineTime != '':

			#plugs in the submode info to each component (line#Info[-1])
			powConsumed, componentDraws = calculateComps(curLineMode, interval, curLineTime)

			#this is a jerry rigged way to get the heater on the BP4 to turn on if in eclipse
			if curLinePowGain <= 0:
				powConsumed += (1.6	 * interval)
			#Comment out below after a 6U simulation is made
			# else:
			# 	curLinePowGain *= 1.25
			#converts Joules/sec to joules over the given interval
			actualPowGain = powerCoeff * (curLinePowGain * getInterval())
			solarGen.append(actualPowGain/getInterval())
			
			#in units of joules
			totalPower += (actualPowGain - powConsumed)/3600
			powerUseage.append(powConsumed/interval)

			#incrementing the lines by 1
			curLineTime, curLinePowGain, curLineSol, curLineMode = nextLineTime, nextLinePowGain, nextLineSol, nextLineMode
			nextLineTime, nextLinePowGain, nextLineSol, nextLineMode = scrapeInfo(f.readline())

			#leveling the battery power if the gain is over capacity
			if totalPower > 80:
				totalPower = 80
				# print("The power exceeded battery capacity and was leveled at time " + str(curLineTime))

			#writing all the info the the output.csv
			g.write(str(curLineTime) + "," + str(curLineMode) + "," + str(actualPowGain) + "," + str(powConsumed) + "," + str(totalPower) + ",")
			for x in range(len(componentDraws)):
				g.write("," + str(componentDraws[x]))
			g.write("\n")

			#calculating the stats
			lineCount += 1
			totalPowerSum += totalPower 	#Watt-hours
			if totalPower > maxBat:
				maxBat = totalPower
				maxOccured = str(curLineTime)
			if totalPower < minBat:
				minBat = totalPower
				minOccured = str(curLineTime)
			

			#if the power drops below 0, stops program altogether
			if totalPower <= 0:
				print("\n----------------------------------------------------\nThe battery ran out of power at time " + str(curLineTime) + " after " + str(lineCount * interval)+ " seconds")
				valid = False
				break
			

		#if the battery power never dropped too low
		if valid == True:
			print("This timeline has passed!")
		else:
			print("This timeline has failed!")
		print("Analysis: \nBattery mean power = " + str(totalPowerSum/lineCount) + " Watt hours")
		print("Battery minimum = " + str(minBat) + " Watt-hours occurred at " + minOccured)
		print("Battery maximum = " + str(maxBat) + " Watt-hours occurred at " + maxOccured)
		print("Minimum power consumed = " + str(min(powerUseage)) + " Watts")
		print("Maximum power consumed = " + str(max(powerUseage)) + " Watts")
		print("Average power consumed = " + str(sum(powerUseage)/len(powerUseage)) + " Watts")
		print("Minimum power generated = " + str(min(solarGen)) + " Watts")
		print("Maximum power generated = " + str(max(solarGen)) + " Watts")
		print("Average power generated = " + str(sum(solarGen)/len(solarGen)) + " Watts")

		g.write("Analysis: \nBattery mean power = " + str(totalPowerSum/lineCount) + " Watt hours")
		g.write("Battery minimum :," + str(minBat) + " Watt-hours, occurred at :," + minOccured + "\n")
		g.write("Battery maximum :," + str(maxBat) + " Watt-hours, occurred at :," + maxOccured + "\n")
		g.close()

if __name__ == "__main__":
	while(True):
		try:
			userIn = input("Please enter the power coefficient (0,1] you would like to use. \n")
			powerCoeff = float(userIn)
			if powerCoeff <= 1 and powerCoeff > 0:
				break
			else:
				print("Sorry that is not a valid 0-1 value.")
		except:
			print("Sorry that is not a valid 0-1 value.")
	outfile = "./outputs/" + str(userIn) + "engineOutput.csv"
	GenCsv(powerCoeff, outfile)