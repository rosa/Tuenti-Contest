#!/usr/bin/python
import sys


# Dyanmic programming algorithm to find the longest common substring
# based on pseudocode from wikipedia
def longestCommonSubstring(s, t):
	m = len(s)
	n = len(t)
	# l[i][j] : common substring length array
	l = [[0]*(n+1) for k in range(0,m+1)]
	z = 0 # length of the longest common substring so far
	iz = 0 # end of the longest common substring so far 

	for i in xrange(1,m+1):
		for j in xrange(1,n+1):
			if s[i-1] == t[j-1]:  # increase the length of the common substring
				l[i][j] = l[i-1][j-1] + 1
				if l[i][j] > z:
					z = l[i][j]
					iz  = i
			else:
				l[i][j] = 0
	return s[iz-z: iz]


for line in sys.stdin:
	if line != '' and not line.isspace():
		case = line.split()
		s, t = case[0], case[1]
		print longestCommonSubstring(s,t)
		