import sys

# check the arguments
if len(sys.argv) < 3:
	print("Usage: inputfile outputfile")

numTestCases = 0
currentLineNum = 0
currentLine = ""

print("input: %s output: %s" % (sys.argv[1], sys.argv[2]))

# calculates and outputs the correct answer for each case
def writeOutput(caseNum, credit, numItems, prices, output):
	#print("credit: %s numItems: %s prices: %s" % (credit, numItems, prices))

	# split each price out
	pricesList = prices.split(" ")

	# loop through each price
	for priceIndex in range(0, len(pricesList)):
		price = int(pricesList[priceIndex])

		# first make sure the price by itself isn't greater than the credit
		if price < credit:
			# loop through every other item
			for otherPriceIndex in range(0, len(pricesList)):
				otherPrice = int(pricesList[otherPriceIndex])
				# make sure it isn't the current price, and check to see if it matches
				if priceIndex != otherPriceIndex and price + otherPrice == credit:
					print("MATCH")
					firstIndex = 0
					secondIndex = 0

					if priceIndex < otherPriceIndex:
						firstIndex = priceIndex
						secondIndex = otherPriceIndex
					else:
						firstIndex = otherPriceIndex
						secondIndex = priceIndex

					# write to the output file
					output.write("Case #%s: %s %s\n" % (caseNum, firstIndex + 1, secondIndex + 1))

					# return, because the answer has been found
					return

caseNum = 0

with open(sys.argv[1], "r") as inputFile:
	with open(sys.argv[2], "w") as output:
		for currentLine in input:
			currentLine = currentLine.rstrip()
			if not currentLine: 
				continue

			# grab the number of test cases
			if currentLineNum == 0:
				numTestCases = int(currentLine)
				print("Cases: %s" % (numTestCases))
			else:
				currentFieldIndex = (currentLineNum - 1) % 3

				# write the output for the previous case (if not on the first case)
				# and collect the credit amount
				if currentFieldIndex == 0:
					if currentLineNum > 1:
						writeOutput(caseNum, credit, numItems, prices, output)

					credit = int(currentLine)
					caseNum += 1
				# number of items	
				elif currentFieldIndex == 1:
					numItems = int(currentLine)
				# prices
				elif currentFieldIndex == 2:
					prices = currentLine

			currentLineNum += 1

		# make sure the last case is written
		writeOutput(caseNum, credit, numItems, prices, output)