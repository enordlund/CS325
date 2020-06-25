#!/usr/bin/python

import math

testAlpha = 0.6


testArray = [3,2]

# sorting array of size n
def badSort(intArray, alpha):
	n = len(intArray)
	
	workingArray = intArray
	
	print("n = ", n)
	
	if (n == 2) and (workingArray[0] > workingArray[1]):
		# swap elements
		temp = workingArray[1]
		workingArray[1] = workingArray[0]
		workingArray[0] = temp
		#print(workingArray)
		#return workingArray
	elif (n > 2):
		m = alpha * n
		m = math.ceil(m)
		upper = int(m - 1)
		upper2 = int(n - 1)
		lower = int(n - m)
		workingArray[0:upper] = badSort(workingArray[0:upper], alpha)
		workingArray[lower:upper2] = badSort(workingArray[lower:upper2], alpha)
		workingArray[0:upper] = badSort(workingArray[0:upper], alpha)
	print("workingArray", workingArray)
	return workingArray
	
	
	
outArray = badSort(testArray, testAlpha)

print("output: ", outArray)
