#!/usr/bin/python
import sys


def binSearch(dist, df):
	if len(df) == 0:
		return 0
	elif len(df) == 1:
		return 0
	elif len(df) == 2:
		if dist >= df[1]: 
			return 1
		elif dist >= df[0]:
			return 0		
	else:
		m = len(df)/2
		if dist < df[m]:
			return binSearch(dist, df[:m])
		elif dist == df[m] or dist < df[m+1]:
			return m
		else:
			return binSearch(dist, df[m+1:]) + m + 1		
		

def solveCase(k, df, d, n):
	# no stops
	if (k >= df):
		return 'No stops'	
	res = ''
	j = 0
	dist = 0

	while (dist + k) < df:
		# find the last station before dist + k 
		# using binary search in d[j:n]
		stopAt = binSearch(dist + k, d[j:n]) + j
		j = stopAt + 1
		# if stopAt >= n:
		# 	res += str(dist + k)
		# 	break
		dist = d[stopAt]
		res += str(d[stopAt]) + ' '
		
	return res.strip()	


	

# read number of test cases
T = int(sys.stdin.readline())

for i in xrange(0,T):
	# read case data
	k = int(sys.stdin.readline())
	df = int(sys.stdin.readline())
	n =  int(sys.stdin.readline())
	d = map(int, sys.stdin.readline().split())
	print solveCase(k,df,d,n)
	
	