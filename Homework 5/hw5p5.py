#!/usr/bin/python

from collections import namedtuple

import sys

# wrestler type for code clarity
Wrestler = namedtuple("Wrestler", "name isBabyface unresolvedRivalryIndices")

Rivalry = namedtuple("Rivalry", "rival1 rival2")


wrestlers = []

wrestlerIndexFromName = dict()

rivalries = []

unresolvedRivalryIndices = []





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ POPULATE WRESTLERS ARRAY AND DICTIONARY
# isBabyface is initialized to null for all wrestlers
file = sys.argv[1]#"test.txt"

def parseFile(fileName):
	global wrestlers
	global rivalries
	
	f = open(fileName)
	
	# first line is the number of wrestlers
	wrestlerCount = int(f.readline())
	
#	print(wrestlerCount)
	
	wrestlerIndex = 0
	
	while wrestlerIndex < wrestlerCount:
		wrestlerName = f.readline().split()[0]
#		print(wrestlerName)
		wrestlers.append(Wrestler(wrestlerName, None, []))
		wrestlerIndex += 1
	
	rivalryCount = int(f.readline())
	
#	print(rivalryCount)
	
	rivalryIndex = 0
	
	while rivalryIndex < rivalryCount:
		rivalryLine = f.readline().split()
#		print(rivalryLine)
		rival1 = rivalryLine[0]
		rival2 = rivalryLine[1]
		
		rivalries.append(Rivalry(rival1, rival2))
		rivalryIndex += 1


def populateDictionary():
	global wrestlers
	wrestlerIndex = 0
	for wrestler in wrestlers:
		wrestlerIndexFromName[wrestler.name] = wrestlerIndex
		wrestlerIndex += 1
		



def populateArrays():
	global wrestlers
	global rivalries
	
#	wrestlers = [Wrestler("Adam", None), Wrestler("Dave", None), Wrestler("Loner1", None), Wrestler("Loner2", None), Wrestler("Loner3", None), Wrestler("Loner4", None), Wrestler("Frank", None), Wrestler("Zebra", None)]
#	rivalries = [Rivalry("Adam", "Dave"), Rivalry("Loner2", "Loner3"), Rivalry("Loner1", "Loner2"), Rivalry("Loner4", "Frank"), Rivalry("Frank", "Zebra"), Rivalry("Dave", "Loner1")]
	
	parseFile(file)
	populateDictionary()
	
	# add rivalries to wrestlers
	rivalryIndex = 0
	for rivalry in rivalries:
		rivalName1 = rivalry.rival1
		rivalIndex1 = wrestlerIndexFromName[rivalName1]
		
		rivalName2 = rivalry.rival2
		rivalIndex2 = wrestlerIndexFromName[rivalName2]
		
		# add the rivalry to both wrestlers
		temp = wrestlers[rivalIndex1].unresolvedRivalryIndices
		temp.append(rivalryIndex)
		wrestlers[rivalIndex1] = wrestlers[rivalIndex1]._replace(unresolvedRivalryIndices = temp)
		temp = wrestlers[rivalIndex2].unresolvedRivalryIndices
		temp.append(rivalryIndex)
		wrestlers[rivalIndex2] = wrestlers[rivalIndex2]._replace(unresolvedRivalryIndices = temp)
		
		rivalryIndex += 1
#	
#	print(wrestlers)
#	print(rivalries)




def populateUnresolvedRivalryIndices():
	# fill array with all valid indices of rivalries[] for the algorithm
	rivalryIndex = 0
	
	for rivalry in rivalries:
		unresolvedRivalryIndices.append(rivalryIndex)
		rivalryIndex += 1


def getReady():
	populateArrays()
	populateUnresolvedRivalryIndices()


def initializeFirstUnresolvedRivalry(withIndex):
#	print("initializeFirstUnresolvedRivalry()")
	global wrestlers
	global rivalries
	# meant to assign group to first pair of rivals
	unresolvedRivalryIndex = withIndex#unresolvedRivalryIndices[withUnresolvedRivalryIndex]
	
	rivalName1 = rivalries[unresolvedRivalryIndex].rival1
	rivalIndex1 = wrestlerIndexFromName[rivalName1]
	
	#wrestlers[rivalIndex1].isBabyface = True
	
	rivalName2 = rivalries[unresolvedRivalryIndex].rival2
	rivalIndex2 = wrestlerIndexFromName[rivalName2]
	#wrestlers[rivalIndex2].isBabyface = False
	
	
	# make sure a group cannot be inferred
	if (wrestlers[rivalIndex1].isBabyface is None) and (wrestlers[rivalIndex2].isBabyface is None):
		wrestlers[rivalIndex1] = wrestlers[rivalIndex1]._replace(isBabyface = True)
		wrestlers[rivalIndex2] = wrestlers[rivalIndex2]._replace(isBabyface = False)



def checkRivalry(withIndex):
#	print "checkRivalry(",
#	print withIndex,
#	print ")"
	rivalName1 = rivalries[withIndex].rival1
	rivalIndex1 = wrestlerIndexFromName[rivalName1]
	rivalGroup1 = wrestlers[rivalIndex1].isBabyface
	
	rivalName2 = rivalries[withIndex].rival2
	rivalIndex2 = wrestlerIndexFromName[rivalName2]
	rivalGroup2 = wrestlers[rivalIndex2].isBabyface
	
	
	
	# remove this rivalry from the unresolved rivalry arrays, since it will be resolved by the end of this function (prevents infinite loop)
	unresolvedRivalryIndices.remove(withIndex)
	
	temp = wrestlers[rivalIndex1].unresolvedRivalryIndices
	temp.remove(withIndex)
	wrestlers[rivalIndex1] = wrestlers[rivalIndex1]._replace(unresolvedRivalryIndices = temp)
	temp = wrestlers[rivalIndex2].unresolvedRivalryIndices
	temp.remove(withIndex)
	wrestlers[rivalIndex2] = wrestlers[rivalIndex2]._replace(unresolvedRivalryIndices = temp)
	
	
	if (rivalGroup1 is None) and (rivalGroup2 is None):
#		print("adding to unresolved")
		# can't infer groups, so add the index to the unresolved rivalries
#		unresolvedRivalryIndices.append(withIndex)
		
		# assign opposing groups to both
		initializeFirstUnresolvedRivalry(withIndex)
		
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ loop through all of rival1's and rival2's unresolved rivalries
		# first, rival1
		for rivalryIndex in wrestlers[rivalIndex1].unresolvedRivalryIndices:
			success = checkRivalry(rivalryIndex)
			if success is False:
				return False
		# second, rival2
		for rivalryIndex in wrestlers[rivalIndex2].unresolvedRivalryIndices:
			success = checkRivalry(rivalryIndex)
			if success is False:
				return False
	elif rivalGroup1 is None:
#		print("adding group to rival 1")
		# infer group from rivalGroup2
		wrestlers[rivalIndex1] = wrestlers[rivalIndex1]._replace(isBabyface = not rivalGroup2)
		
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ loop through all of rival1's unresolved rivalries
		for rivalryIndex in wrestlers[rivalIndex1].unresolvedRivalryIndices:
			success = checkRivalry(rivalryIndex)
			if success is False:
				return False
	elif rivalGroup2 is None:
#		print("adding group to rival 2")
		# infer group from rivalGroup1
		wrestlers[rivalIndex2] = wrestlers[rivalIndex2]._replace(isBabyface = not rivalGroup1)
		
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ loop through all of rival2's unresolved rivalries
		for rivalryIndex in wrestlers[rivalIndex2].unresolvedRivalryIndices:
			checkRivalry(rivalryIndex)
	elif rivalGroup1 is rivalGroup2:
#		print("caught contradiction")
		# neither is none, so checking that they are not the same
		# the groups are the same, indicating that groups cannot be determined.
		return False
#	else:
#		print("rivalry passed")
		
	# the rivalry was successfully compared
	return True

def checkUnresolvedRivalries():
#	print("Checking unresolved rivalries")
	# manually assign the first rivalry to get started
	#initializeFirstUnresolvedRivalry()
	
	unresolvedRivalryCount = len(unresolvedRivalryIndices)
	unresolvedRivalryIndex = 0
	
	#initializeFirstUnresolvedRivalry(unresolvedRivalryIndex)
	
	# always start with this larger than possible for the first run of the while loop
	lastUnresolvedIndex = unresolvedRivalryCount
	
	lastCount = unresolvedRivalryCount - unresolvedRivalryIndex
	
	# assign the rest of the rivalries if possible
	while len(unresolvedRivalryIndices) > 0:
		rivalryIndex = unresolvedRivalryIndices[0]
		
		success = checkRivalry(rivalryIndex)
		
		if success is False:
			# caught rivalry contradiction
			return False
		
		lastUnresolvedIndex = rivalryIndex
		unresolvedRivalryIndex += 1
		unresolvedRivalryCount = len(unresolvedRivalryIndices)
	
	# no contradictions were found
	return True
	


getReady()


if checkUnresolvedRivalries() is True:
	print("Yes")
	
	babyfaces = []
	heels = []
	
	for wrestler in wrestlers:
		if wrestler.isBabyface is True:
			babyfaces.append(wrestler.name)
		else:
			heels.append(wrestler.name)
	
	print "Babyfaces:",
	
	for babyface in babyfaces:
		print babyface,
		
	print("")
	print "Heels:",
	
	for heel in heels:
		print heel,
	print("")
else:
	print("No")