#!/usr/bin/python

def numPaths(m, n):
	if m > 1 and n > 1:
		return numPaths(m, n-1) + numPaths(m-1, n)
	else:
		return 1
		
		
count = numPaths(8, 8)

print(count)
	