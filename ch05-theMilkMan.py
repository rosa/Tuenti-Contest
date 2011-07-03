#!/usr/bin/python
import sys

# dynamic solution for 0-1 knapsack problem
def solveCase(n,limit,weight, milk):
	# m[i][w] : maximum amount of milk that can be attained with weight less than or equal to w using cows up to i
	m = [[0]*(limit+1) for k in range(0,n+1)]
	for w in xrange(0, limit+1):
		m[0][w] = 0
	for i in xrange(1,n+1):
		m[i][0] = 0
	for i in xrange(1,n+1):
		for w in xrange(0,limit+1):
			if weight[i-1] <= w: # if we can carry cow i-1
				m[i][w] = max(milk[i-1] + m[i-1][w-weight[i-1]], m[i-1][w]) # we take it only if it improves the solution 
			else: # cow i too fat
				m[i][w] = m[i-1][w]
	return str(m[n][limit])				

for line in sys.stdin:
	case = line.split()
	n = int(case[0])
	limit = int(case[1])
	weight = map(int, case[2].split(','))
	milk = map(int, case[3].split(','))	
	print solveCase(n, limit, weight, milk)


	# print n
	# print limit
	# print weight
	# print milk