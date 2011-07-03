#!/usr/bin/python
import sys
import math
from struct import *

# opening image n x m
im = open("trabaja.bmp", "rb")

n = 640
m = 817

# skip header
im.read(54)


# load array of bytes R G B
rowSize = int(math.ceil(0.75*n)*4) 
R = [0]*m
G = [0]*m
B = [0]*m


for i in xrange(0,m):
	row = im.read(rowSize)	
	B[i] = row[0::3]
	G[i] = row[1::3]
	R[i] = row[2::3]		
		
im.close()

# convert bytes to int and then computes the sum
def compute(bytestring):
	res = 0
	for b in bytestring:
		b += '\x00'
		res += unpack('h',b)[0]
	return str(res+1)	
	
	
# read input
for line in sys.stdin:
	comp = line[0]
	l = int(line[1:].strip()) 
	# access line l in image
	if l >= m:
		print 0
	else:
		l = m-l-1
		if comp == 'R':
			print compute(R[l])
		elif comp == 'G':
			print compute(G[l])
		elif comp == 'B':	
			print compute(B[l])
	

		
	
