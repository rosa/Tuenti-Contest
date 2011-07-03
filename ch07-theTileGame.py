#!/usr/bin/python
import sys


# Levenshtein distance between two strings: the minimum number of edits 
# needed to transform one string into the other, where edit operations are 
# add, remove and swap (of a single character)
def levenshteinDistance(s, t, op):
	m = len(s)
	n = len(t)
	# d[i][j] : Levenshtein distance between the first i 
	# characters of s and the first j characters of t
	d = [[0]*(n+1) for k in range(0,m+1)]
	
	for i in xrange(0,m+1):
		d[i][0] = i*op[1] # distance of any first string to an empty second string
	for j in xrange(1,n+1):
		d[0][j] = j*op[0] # distance of any second string to an empty first string
	
	for j in xrange(1,n+1):
		for i in xrange(1,m+1):
			if s[i-1] == t[j-1]:
				d[i][j] = d[i-1][j-1] # no operation required				
			else:
				# minimum of applying add, remove or swap
				d[i][j] = min(d[i][j-1] + op[0], d[i-1][j] + op[1], d[i-1][j-1] + op[2]) 
	return d[m][n]
				

for line in sys.stdin:
	if line != '' and not line.isspace():
		case = line.split()
		s, t = case[0], case[1]
		op = map(int, case[2].split(','))
		print levenshteinDistance(s, t, op)