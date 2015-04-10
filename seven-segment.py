import sys

if len(sys.argv) < 3:
	print("Usage inputFile outputFile")
	sys.exit()

lineIndex = 0

with open(sys.argv[1], "r") as inputFile:
	with open(sys.argv[2], "w") as outputFile:
		for line in inputFile:
			
			lineIndex += 1