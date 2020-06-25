#!/usr/bin/python

from collections import namedtuple
import math

from random import randrange

Bin = namedtuple("Bin", "remainingCapacity")

Item = namedtuple("Item", "weight")

Set = namedtuple("Set", "items bins binCapacity")


def firstFit(items, bins, binCapacity):
	selfBins = bins[:]
	
#	print(selfBins)
	
	for item in items:
		itemAdded = False
		binIndex = 0
		for bin in selfBins:
			if bin.remainingCapacity >= item.weight:
				newCapacity = bin.remainingCapacity - item.weight
				newBin = Bin(newCapacity)
				selfBins[binIndex] = newBin
				itemAdded = True
				break
			binIndex += 1
		if itemAdded == False:
			newCapacity = binCapacity - item.weight
			newBin = Bin(newCapacity)
			selfBins.append(newBin)
	
	# return the number of bins
	return len(selfBins)






def sortItemsDecreasing(items):
	selfItems = items[:]
	
	selfItems.sort(reverse=True)
	
	return selfItems


def firstFitDecreasing(items, bins, binCapacity):
	# sort the items in decreasing weight
	selfItems = sortItemsDecreasing(items)
	
	# return the number of bins
	return firstFit(selfItems, bins, binCapacity)
	
	

def bestFit(items, bins, binCapacity):
	selfBins = bins[:]
	
	for item in items:
		itemAdded = False
		bestBinIndex = -1
		bestBinCapacity = 2 * binCapacity # always greater than any analyzed bin capacity
		
		binIndex = 0
		for bin in selfBins:
			if ((bin.remainingCapacity >= item.weight) and (bin.remainingCapacity < bestBinCapacity)):
				bestBinIndex = binIndex
				bestBinCapacity = bin.remainingCapacity
			binIndex += 1
		
		if bestBinIndex > -1:
			newCapacity = selfBins[bestBinIndex].remainingCapacity - item.weight
			newBin = Bin(newCapacity)
			selfBins[bestBinIndex] = newBin
			itemAdded = True
		else:
			# item not added to existing bins, so add another bin
			newCapacity = binCapacity - item.weight
			newBin = Bin(newCapacity)
			selfBins.append(newBin)
	
	return len(selfBins)
	
	
	

def parseSet():
#	items = [Item(2), Item(4), Item(3), Item(8), Item(6), Item(1), Item(5), Item(7)]
#	capacity = 10
#	bins = [Bin(capacity)]
	
	
	
	specs = Set(items, bins, capacity)
	
	return specs
	

def runAnalysis(onSet, setNumber):
	selfItems = onSet.items[:]
	selfBins = onSet.bins[:]
	selfCapacity = onSet.binCapacity
	
	# first test first-fit
	firstFitCount = firstFit(selfItems, selfBins, selfCapacity)
	
	# test first-fit decreasing
	firstFitDecreasingCount = firstFitDecreasing(selfItems, selfBins, selfCapacity)
	
	# test best fit
	bestFitCount = bestFit(selfItems, selfBins, selfCapacity)
	
	# print the output
	print "Test Case",
	print setNumber,
	print "First Fit:",
	print firstFitCount,
	print ", First Fit Decreasing:",
	print firstFitDecreasingCount,
	print ", Best Fit:",
	print bestFitCount
	




def analyzeFile(fileName):
	# open the file
	f = open(fileName)
	
	setCount = int(f.readline())
	
	setNumber = 1
	while setNumber <= setCount:
		# parse the set
		setCapacity = int(f.readline())
		setItemCount = int(f.readline())
		
		# populate the array with the weights
		setItemWeightsStrings = f.readline().split(" ")
		
		setItems = []
		itemIndex = 0
		while itemIndex < setItemCount:
			newItemWeight = int(setItemWeightsStrings[itemIndex])
			newItem = Item(newItemWeight)
			setItems.append(newItem)
			
			itemIndex += 1
		
		# create the set
		setBins = [Bin(setCapacity)]
		newSet = Set(setItems, setBins, setCapacity)
		
		# analyze the set
		runAnalysis(newSet, setNumber)
		
		setNumber += 1
		
	f.close()

#analyzeFile("./bin.txt")



def randomSet():
	maxCapacity = randrange(100) + 1
	itemCount = randrange(100) + 1
	
	#create array of items
	items = []
	itemIndex = 0
	while itemIndex < itemCount:
		# make sure the item weight doesn't exceed the maximum capacity
		itemWeight = randrange(maxCapacity) + 1
		newItem = Item(itemWeight)
		items.append(newItem)
		
		itemIndex += 1
	
	bins = [Bin(maxCapacity)]
	
	newSet = Set(items, bins, maxCapacity)
	return newSet


def randomSets():
	setCount = randrange(100)+20
	
	sets = []
	setIndex = 0
	while setIndex < setCount:
		newSet = randomSet()
		sets.append(newSet)
		
		setIndex += 1
	
	return sets


def testAlgorithms():
	sets = randomSets()
	
	setNumber = 1
	for testSet in sets:
		runAnalysis(testSet, setNumber)
		setNumber += 1
		
		
		
testAlgorithms()