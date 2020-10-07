from itertools import *
import sys
from statistics import mean

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

with open("Inputs/updatedTimeline.csv") as f:
    curLine, nextLine, f = cleanHeader(f)
    interval = 30
    
    #sperating the elements(cloumns of the STK.csv) This is done for readability
    curLineTime, curLinePowGain, curLineSol, curLineMode = scrapeInfo(curLine)
    nextLineTime, nextLinePowGain, nextLineSol, nextLineMode = scrapeInfo(nextLine)

    currentCount = 0
    eclipseStat = []

    while nextLineTime != '':

        if curLinePowGain <= 0:
            currentCount += 1
        elif currentCount > 0:
            eclipseStat.append(currentCount)
            currentCount = 0

        curLineTime, curLinePowGain, curLineSol, curLineMode = nextLineTime, nextLinePowGain, nextLineSol, nextLineMode
        nextLineTime, nextLinePowGain, nextLineSol, nextLineMode = scrapeInfo(f.readline())
        
    print("Max eclipse length: " + str(max(eclipseStat) * interval) + " seconds")
    print("Min eclipse length: " + str(min(eclipseStat) * interval) + " seconds")
    print("Mean eclipse length: " + str(mean(eclipseStat) * interval) + " seconds")

    smallCount = 0
    for e in eclipseStat:
        if e == 3:
            smallCount += 1

    print(smallCount)