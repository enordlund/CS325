#!/usr/bin/python

from collections import namedtuple

import math

# coin type for code clarity
Coin = namedtuple("Coin", "value count")

# CKN object for code clarity
CKN = namedtuple("CKN", "c k n")

def optionalCKN(fromLine):
#	print("optionalCKN()")
	if " " in fromLine:
		dataList = [int(i) for i in fromLine.split(" ")]
		if len(dataList) == 3:
			return dataList
	return None

def createCKN(fromDataList):
#	print("createCKN()")
	
	ckn = CKN(fromDataList[0], fromDataList[1], fromDataList[2])
	return ckn
	
def parseData():
#	print("parseData()")
	
	# opening data file
	file = open("data.txt")
	
	cknArray = []
	
	# populating array with data from file
	for line in file.readlines():
		optionalDataList = optionalCKN(line)
		if optionalDataList != None:
			# the line successfully produced a dataList matching form of ckn data
			ckn = createCKN(optionalDataList)
			cknArray.append(ckn)
		
	# array has been populated with any CKN objects from data.txt
	file.close()
	return cknArray

def getOptimalSolution(forCKN):
#	print("getOptimalSolution()")
	
	c = forCKN.c
	k = forCKN.k
	n = forCKN.n
	
	solution = []
	
	while k >= 0:
#		print("k >= 0"),
#		print c
#		print k
#		print n
		
		coinValue = int(math.pow(c, k))
		coinCount = 0
		
#		print coinValue
		
		while n >= coinValue:
#			print("n > coinValue")
			coinCount += 1
			n = n - coinValue
		if coinCount > 0:
#			print("appending coin to solution")
			coin = Coin(coinValue, coinCount)
			solution.append(coin)
		
		k -= 1
	
	# solution is populated with Coin objects
	return solution

def solutionStringWithDelimeterLine(fromSolution, delimiterCharacter):
	string = ""
	for coin in fromSolution:
		string += str(coin.value)
		string += " "
		string += str(coin.count)
		string += "\n"
	
	string += delimiterCharacter
	string += "\n"
	
	return string

def writeSolutions():
	cknArray = parseData()
	
	file = open("change.txt", "w")
	
	for ckn in cknArray:
		solution = getOptimalSolution(ckn)
		solutionString = solutionStringWithDelimeterLine(solution, "~")
		
		# write the solution to the output file
		file.write(solutionString)
#		print(solutionString)
	
	file.close()
	
def printSolutionWithDelimeterLine(solution, lineCharacter):
#	print("printSolutionWithDelimeterLine()")
	
#	for coin in solution:
#		print coin.value,
#		print coin.count
#		print ""
	
#	print lineCharacter
	
	print solutionStringWithDelimeterLine(solution, lineCharacter)


def printSolutions():
#	print("printSolutions()")
	
	cknArray = parseData()
	
	for ckn in cknArray:
		solution = getOptimalSolution(ckn)
		printSolutionWithDelimeterLine(solution, "~")
		





writeSolutions()

