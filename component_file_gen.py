from itertools import *
import sys

#global variable submodes is a complete list of the permissable submodes 
submodes = []
components = []
#Class to define PowerState objects, there should be one for 
class PowerState:
	name = ""
	consumption = []
	stateSubmodes = []
	def __init__(self):
		self.name = ""
		self.consumption = []
		self.stateSubmodes = []

#Class to define each component, contains an array of PowerState objects
class Component:
	name = ""
	states = []
	def __init__(self):
		self.name = ""
		self.states = []



def cleanHeader(f):
	#cleaning the csv so just the data is left and the first two lines are set
	line1 = f.readline()

	#looping through to get rid of any info above the header line (instructions/ notes)
	while "Component" not in line1:
		line1 = f.readline()
		#if you reach the end of the file without hitting the header
		if line1 == '':
			print("Error: It seems like your config is missing the \"Component, Powerstates, Consumption (Watts)\" header. Please make sure your .csv file is formatted properly.\nThe header is an important indicator and should be placed at the very beginning of the component data.")
			f.close()
			sys.exit(1)

	#getting the relevent line and setting the submode array to the list
	line = f.readline()
	global submodes 
	submodes = line.split(",")
	while "\n" in submodes:
		submodes.remove("\n")
	while "" in submodes:
		submodes.remove("")

	#if the line that should have comtained the list of submodes is empty, print error and exit
	if submodes[0] == '':
		print("Error: It seems like your config file is missing its list of satellite modes.\nThe list should be comma-separated and be directly below the header line.")
		f.close()
		sys.exit(1)

	#If the header line and submode list were found return the remaining file data
	return f

def createComponent(f):
	comp = Component()					#creating the component object we'll use
	line = f.readline().split(",")		#parsing the first line
	comp.name = line[0]					#setting the name of the component object

	powStateCount = 0					#count of the number of powerStates
	#while loop to loop through each powerstate listed in the csv, pulling the name, their submodes, and their power consumption data
	while line[1] != "" and line[1] != '\n':
		powState = PowerState()			#creating the new Power State for this round of the loop
		powState.name = line[1]			#setting the name of this Power State

		subModeCount = 0				#incrementor to track the number of submodes applicable for this Power State
		#while there are still submodes to parse through
		while line[subModeCount + 2] != "" and line[subModeCount + 2] != '\n':
			endReached = False
			#checking to make sure the submodes are valid
			if "\n" in line[subModeCount + 2]:
				line[subModeCount + 2] = line[subModeCount + 2].replace("\n", "")
				endReached = True

			if line[subModeCount + 2] not in submodes:
				print("Warning: \"" + line[subModeCount + 2] + "\" is not a valid submode.\nCheck that the submode list below the header contains ALL possible submodes and that the submodes for component \"" + comp.name + "\" in power state \"" + powState.name +"\" are correctly spelled.\n")
			#appending to the submode list of this power state if it is valid and incrementing the subModeCount
			else:
				powState.stateSubmodes.append(line[subModeCount + 2])
				print("appended the submode " + line[subModeCount + 2] + " to "+ powState.name)

			if endReached:
				break
			subModeCount += 1
				#print("appended submode " + line[subModeCount + 1] + " to power state " + powState.name)

		#getting the next line and checking to see where there is a break, i.e. where the current power state ends
		line = f.readline().split(",")
		#print(line)
		if line == '':
			break
		while line[2] != "" and line[0] == "":
			powState.consumption.append(float(line[2]))		#pulling consumption data from the third cell
			#print("appended consumption " + line[2] + "to power state " + powState.name)		#testing/debug
			line = f.readline()								#moving to the next line
			if line == '':
				break

			#print("the next line was\n")					#testing/debug
			#print(line)									#testing/debug
		powStateCount += 1				#incrememnting the number of power states
		comp.states.append(powState)	#adding this power state to the component before moving on
		if line == '':
			break
		line = line.split(",")			#feeding the next line to the while loop, should be the start of a new power state


	print("The component " + comp.name + " has power states ")
	for x in comp.states:
		print(x.name)
		for y in x.consumption:
			print(y)
		for z in x.stateSubmodes:
			print(z)

	return line, f, comp

if __name__ == "__main__":
	f = open("./ComponentConfig.csv", "r+")	#opening the file for reading
	f = cleanHeader(f)						#getting the file without the header and pulling submode list
	#print(*submodes, sep = ", ")			#printing out the list of submodes for testing

	line = f.readline().split(",")
	#print(line)
	if line == '':
		f.close()
		exit(1)
	while(line[0] == ''):
		line, f, comp = createComponent(f)
		components.append(comp)
		
		if line == '':
			f.close()
			exit(1)


	g = open("testComp.csv", "w+")
	g.close()



	