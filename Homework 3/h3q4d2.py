#!/usr/bin/python

from collections import namedtuple

# item type for code clarity
Item = namedtuple("Item", "number weight value")



def constructItemArrayBottomUp():
	# opening data file
	f = open("data.txt")
	
	# initializing empty array for items, adding an initial item to help with index 0 in the algorithm function.
	itemArray = [Item(0,0,0)]
	
	itemCount = 0
	
	for line in f.readlines():
		if " " in line:
			itemCount += 1
			# creating item for array from populated line
			dataList = [int(i) for i in line.split(" ")]
			# first is weight, second is value
			item = Item(itemCount, dataList[0], dataList[1])
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

# creating array of 0's
table = emptyTable(itemsBU, 22)



def optimalKnapsackBenefitBottomUp(items, capacity):
#	print("bottom up")
	itemCount = len(items)
	itemIndex = 0
	
	
	while itemIndex < itemCount:
		# iterating through rows of table
		
		
		capacityIndex = 0
		
		item = items[itemIndex]
		
		# storing rows to append to the table
		valuesRow = []
		
		
		maxValue = 0
		
		while capacityIndex <= capacity:
			# iterating through columns of each row
			
			value = 0
			
			if itemIndex is 0:
				# part of making index handling easier
				value = 0
			elif capacityIndex is 0:
				# part of making index handling easier
				value = 0
			elif item.weight <= capacityIndex:
				
				value = max([table[itemIndex-1][capacityIndex], table[itemIndex-1][capacityIndex - item.weight] + item.value])
			else:
#				print("item weight > capacity index")
				value = table[itemIndex - 1][capacityIndex]
			
			
			if value > maxValue:
				# update maxValue for printing the optimal benefit at the end
				maxValue = value
				
				
			# appending the determined value to the item row.
			valuesRow.append(value)
			capacityIndex += 1
		
		# printing the rows as they are completed for a prettier output
#		print(valuesRow)
		
		# appending the item row to the table
		table[itemIndex] = valuesRow
		
		itemIndex += 1
	
	print'Greatest Value: ',
	print maxValue
	return maxValue
	
	
	
	
# running the algorithm	
greatestValue = optimalKnapsackBenefitBottomUp(itemsBU, 22)


## printing table data to demonstrate final result stored in a single object.
#print "Table data: ",
#print(table)



def getComposition(ofTable, items):
	
	composition = []
	
	itemRowIndex = len(ofTable) - 1
	
	capacityIndex = len(ofTable[0]) - 1
	
	while itemRowIndex > 0:
		# Stepping through rows to find used items and their values
		if ofTable[itemRowIndex][capacityIndex] > ofTable[itemRowIndex - 1][capacityIndex]:
			# this item is part of an optimal subset.
			# add the item to the composition list
			item = items[itemRowIndex]
			composition.append(item)
			
			# then jump to next place
			itemWeight = item.weight
			capacityIndex -= itemWeight
		
		itemRowIndex -= 1
	
	# create arrays for printing
	
	print 'Composition: ',
	
	print(composition)
	

getComposition(table, itemsBU)