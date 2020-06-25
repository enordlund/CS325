#!/usr/bin/python

from collections import namedtuple

import numpy as np

# item type for code clarity
Item = namedtuple("Item", "weight value")



def constructItemArrayBottomUp():
	# opening data file
	f = open("data.txt")
	
	# initializing empty array for items
	itemArray = [Item(0,0)]
	
	
	for line in f.readlines():
		if " " in line:
			# creating item for array from populated line
			dataList = [int(i) for i in line.split(" ")]
			# first is weight, second is value
			item = Item(dataList[0], dataList[1])
			itemArray.append(item)
	
	return itemArray
		
		
def constructItemArrayTopDown():
	# opening data file
	f = open("data.txt")
	
	# initializing empty array for items
	itemArray = []
	
	
	for line in f.readlines():
		if " " in line:
			# creating item for array from populated line
			dataList = [int(i) for i in line.split(" ")]
			# first is weight, second is value
			item = Item(dataList[0], dataList[1])
			itemArray.append(item)
	
	return itemArray
		
		



def emptyTable(items, capacity):
	#getting dimensions for table B
	rows = len(items)
	
	# columns is capacity + 1
	columns = capacity + 1
	
	
	# creating empty array for output
	table = [[0]*columns]*rows
	
	return table
	


# creating array of items from the data file
itemsBU = constructItemArrayBottomUp()

table = emptyTable(itemsBU, 6)



#print(table)

def optimalKnapsackBenefitBottomUp(items, capacity):
#	print("bottom up")
	itemCount = len(items)
	itemIndex = 0
	
	npTable = np.array([])
	
	while itemIndex < itemCount:
		
		
		capacityIndex = 0
		
		item = items[itemIndex]
		
		valuesRow = []
		
#		print(table)
		
		maxValue = 0
		
		while capacityIndex <= capacity:
#			print("Item index:")
#			print(itemIndex)
#			print("Capacity index:")
#			print(capacityIndex)
#			print("Item weight:")
#			print(item.weight)
			
			
			
			value = 0
			
			if itemIndex is 0:
				value = 0
			elif capacityIndex is 0:
				value = 0
			elif item.weight <= capacityIndex:
#				print("item weight <= capacity index")
#				print("table[itemIndex - 1][capacityIndex]:")
#				print(table[itemIndex-1][capacityIndex])
#				print("table[itemIndex - 1][capacityIndex - item.weight] + item.value: ")
#				print(table[itemIndex-1][capacityIndex - item.weight] + item.value)
				
				value = max([table[itemIndex-1][capacityIndex], table[itemIndex-1][capacityIndex - item.weight] + item.value])
			else:
#				print("item weight > capacity index")
				value = table[itemIndex - 1][capacityIndex]
			
#			print("value:")
#			print(value)
			if value > maxValue:
				maxValue = value
			valuesRow.append(value)
			capacityIndex += 1
		
#		print("valuesRow: ")
		print(valuesRow)
		table[itemIndex] = valuesRow
#		npTable = np.append(npTable, valuesRow)
		itemIndex += 1
#	print(npTable)
	print'Optimal benefit: ',
	print maxValue
	
		
optimalKnapsackBenefitBottomUp(itemsBU, 6)



#print(table)



def optimalKnapsackBenefitTopDown(items, itemsMaxIndex, capacity):
#	print("top down")
	item = items[itemsMaxIndex]
	
	if (itemsMaxIndex < 0) or (itemsMaxIndex >= items.count):
		outcome = 0
		#table[capacity][itemsMaxIndex] = outcome
		print("item ", itemsMaxIndex + 1, ", capacity ", capacity, "benefit: ", outcome)
		#print(outcome)
		return outcome
	elif item.weight > capacity:
		outcome = optimalKnapsackBenefitTopDown(items, itemsMaxIndex - 1, capacity)
		#table[capacity][itemsMaxIndex] = outcome
		print("item ", itemsMaxIndex + 1, ", capacity ", capacity, "benefit: ", outcome)
		#print(outcome)
		return outcome
	else:
		outcome = max([optimalKnapsackBenefitTopDown(items, itemsMaxIndex - 1, capacity), optimalKnapsackBenefitTopDown(items, itemsMaxIndex - 1, capacity - item.weight) + item.value])
		#table[capacity][itemsMaxIndex] = outcome
		print("item ", itemsMaxIndex + 1, ", capacity ", capacity, "benefit: ", outcome)
		#print(outcome)
		return outcome





#itemsTD = constructItemArrayTopDown()
##
### calculating optimal benefit
##print("Subsets:")
#print("top down")
#benefit = optimalKnapsackBenefitTopDown(itemsTD, 4, 6)
##
### printing outcome
#print("Optimal benefit:")
#print(benefit)



#testTable = emptyTable(itemsBU, 6)
#
#print(testTable)
#
#newRow = testTable[1]
#
#print(newRow)
#
##newRow[2] = 1
#
#print(newRow)
#
#testTable[1] = [2, 3]
#
#testTable[1][0] = testTable[0][3]
#
#testTable[0][3] = 5
#
#print(newRow)
#
##print(testTable[1])
#
#print(testTable)