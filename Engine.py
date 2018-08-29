import Component1
import Component2

def cleanHeader(f):
	line1 = f.readline()
	while "Current Submode" not in line1:
		line1 = f.readline()
	return f

def ReadCsv():
	with open("powertestdata.csv") as f:
		f = cleanHeader(f)
		line1 = f.readline()
		line2 = f.readline()
	print("The first line is " + line1)
	print("The second line is " + line2)

	f.close()

if __name__ == "__main__":
	ReadCsv()

