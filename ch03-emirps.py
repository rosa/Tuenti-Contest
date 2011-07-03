#!/usr/bin/python
import sys
import random
import math

# The Miller-Rabin primality test
def toBinary(n):
	r = []
	while (n > 0):
		r.append(n % 2)
		n = n / 2
	return r


# test(a, n) -> bool Tests whether n is complex.
# 
#   Returns:
#     - True, if n is complex.
#     - False, if n is probably prime.
def test(a, n):
	b = toBinary(n - 1)
	d = 1
	for i in xrange(len(b) - 1, -1, -1):
		x = d
		d = (d * d) % n
		if d == 1 and x != 1 and x != n - 1:
			return True # Complex
		if b[i] == 1:
			d = (d * a) % n
	if d != 1:
		return True # Complex
	return False # Prime


# MillerRabin(n, s = 1000) -> bool Checks whether n is prime or not
# 
# Returns:
#   - True, if n is probably prime.
#   - False, if n is complex.
def MillerRabin(n, s = 20):
	for j in xrange(1, s + 1):
		a = random.randint(1, n - 1)
		if (test(a, n)):
			return False # n is complex
	return True # n is prime
  

# Reverse an integer x
def reverse(x):
	xreversed = str(x)[::-1]
	xreversed = xreversed.lstrip('0')
	if (len(xreversed)!=len(str(x))):
		return 0
	return int(xreversed)


emirpList = [13,17,31,37,71,73,79,97,107,113,149,157,167,179,199,311,337,347,359,389,701,709,733,739,743,751,761,769,907,937,941,953,967,971,983,991,1009,1021,1031,1033,1061,1069,1091,1097,1103,1109,1151,1153,1181,1193]
acc = reduce(lambda x,y: x+y, emirpList)

for line in sys.stdin:
	n = int(line)
	if n > emirpList[-1]:
		next = emirpList[-1] + 1
		res = acc
		for i in xrange(next, n+1):
			# test if i is emirp
			rev = reverse(i)
			if (rev > 0 and rev < i and rev in emirpList) or (rev > 0 and rev > i and MillerRabin(i) and MillerRabin(rev)):
				acc += i
				emirpList.append(i)
		print acc	
	else:
		res = 0
		for i in emirpList:
			if (i > n):	
				print res
				break
			else:
				res += i			

