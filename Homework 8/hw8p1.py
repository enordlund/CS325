#!/usr/bin/python

from collections import namedtuple
import math


Bin = namedtuple("Bin", "remainingCapacity")

Item = namedtuple("Item", "weight")

Set = namedtuple("Set", "items bins binCapacity")


def firstFit(items, bins, binCapacity):
	selfBins = bins[:]
	
	for item in items:
		itemAdded = False
		binIndex = 0
		for bin in selfBins:
			if bin.remainingCapacity >= item.weight:
				# the bin can fit the item, so add the item to the bin.
				newCapacity = bin.remainingCapacity - item.weight
				newBin = Bin(newCapacity)
				selfBins[binIndex] = newBin
				itemAdded = True
				break
			binIndex += 1
		if itemAdded == False:
			# the item didn't fit in any existing bins, so add it to a new bin.
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
		
		# find the best bin
		binIndex = 0
		for bin in selfBins:
			if ((bin.remainingCapacity >= item.weight) and (bin.remainingCapacity < bestBinCapacity)):
				# this bin has less space than the previous best bin, and it can fit the item.
				bestBinIndex = binIndex
				bestBinCapacity = bin.remainingCapacity
			binIndex += 1
		
		if bestBinIndex > -1:
			# add the item to the best bin
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

analyzeFile("./bin.txt")
