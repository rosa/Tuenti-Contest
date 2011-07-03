#!/usr/bin/python
import sys
import math


# state of the lights
# lights = []


# def lightsOn(l,t):
# 	# base case: there is only one light 
# 	# it would be on for an odd number of seconds
# 	if l==1:
# 		lights[l-1] = (t%2 != 0)
# 	else:
# 		lightsOn(l-1,t)	
# 		# light l 
# 		frec = math.pow(2,l-1)
# 		state = t/frec 
# 		# the light would be on if it's the right turn
# 		# and if the neighbour is off
# 		lights[l-1] = (state%2 != 0) and not lights[l-2]


def writeLights(n,t):
	res = ''
	# for t odd, even lights on and viceversa
	even = (t%2 == 0)
	for i in xrange(n):
		if (even and i%2!=0) or (not even and i%2==0):
			res += str(i) + ' '
	if res == '':
		return 'All lights are off :('
	else:
		return res.strip()
		


# read number of test cases
N = int(sys.stdin.readline())

# read and solve each case
for i in xrange(0,N):
	l = int(sys.stdin.readline())
	t = int(sys.stdin.readline())
	# in t seconds, only the first t lights would be enabled
	# initially, all n enabled lights off
	n = min(t,l)
	print writeLights(n,t)
