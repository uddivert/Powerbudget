#This is the Timeline builder

def scrapeInfo(line):
	#this may get more complex later
	lineInfo = line.split(",")
	lineInfo[-1] = lineInfo[-1].replace("\n", "")

	#this if will only occur at the end of the file and helps exit cleanly
	if lineInfo[0] == '':
		return "nothing here"
	
	return lineInfo[1] + "," + lineInfo[2]

g = open("newTimeline.csv", "w+")
with open("./powertestdata.csv") as f:
	for x in range(2303):
		g.write(f.readline())
	
	date = 13
	Months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
	monthCount = 0
	month = Months[monthCount]
	hour = 11
	minute = 9
	second = 0
	dataEntries = 516100 # 6 months of data minus that data we have
	dayCount = 0

	mode = "Cruise - Idle"
	lines = f.readlines()
	numLines = len(lines)


	repeatCount = 0
	for i in range(dataEntries):
		mode = "Cruise - Idle"

		if repeatCount % 2 == 1:
			second = 0					#switches seconds every data point
			minute = (minute + 1) % 60	#increments minute by 1

			if minute <= 4 and minute >= 0:

				if (minute == 0):
					hour = (hour + 1) % 24


					if hour == 0 and (month == "May" or month == "Jul" or month == "Aug" or month == "Oct" or month == "Dec"):
						date = (date + 1) % 32			#sets the date 
						dayCount += 1

						if date == 0:
							date += 1
							monthCount += 1
							month = Months[monthCount]	#sets month

					elif hour == 0 and month == "Feb":
						date = (date + 1) % 29			#sets date
						dayCount += 1

						if date == 0:
							date += 1
							monthCount += 1
							month = Months[monthCount]	#sets month

					elif hour == 0:
						date = (date + 1) % 31			#sets date
						dayCount += 1

						if date == 0:
							date += 1
							monthCount += 1
							month = Months[monthCount]	#sets month
		else:
			second = 30

		if minute <= 3 and minute >= 0 and hour == 0:
			mode = "Data Downlink - Data Transmit"
		elif minute <= 4 and minute >= 0 and hour == 11 and dayCount%7 == 1:	#at 11am every seventh day for 4 min
			mode = "Scan - Target Point"
		elif minute <= 24 and minute >= 5 and hour == 11 and dayCount%7 == 1:	#at 11:05am every seventh day for 20 min
			mode = "Data Processing - SfM"

		repeatCount = (repeatCount + 1) % numLines

		g.write(str(date).zfill(2) + " " + str(month) + " 2020 " + str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2) + ".000,")
		g.write(scrapeInfo(lines[repeatCount-1]) + ",") #writing the correct power and SO values
		g.write(mode + "\n")

	g.close()
