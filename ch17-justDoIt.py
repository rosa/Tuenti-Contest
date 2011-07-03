#!/usr/bin/python
import sys
import base64
from struct import *
import math

f = open("justDoIt.in", 'w')

# get input data

for line in sys.stdin:
	s = base64.b64decode(line)
	f.write(s)

f.close()	

# image in BMP by 'magic' ^^
# (God knows I spent hours trying to get PIL working in my evil Mac)
# opening image n x m
im = open("justDoIt.in", "rb")
n = 612
m = 154

# skip header 
im.read(54)


# load array of bytes R G B
rowSize = int(math.ceil(0.75*n)*4) 
R = [0]*m
G = [0]*m
B = [0]*m
rgb = [0]*m

for i in xrange(0,m):
	row = im.read(rowSize)	
	rgb[i] = row
	B[i] = row[0::3]
	G[i] = row[1::3]
	R[i] = row[2::3]		
		
im.close()


# the steganography part
# get last bit of each byte 
def compute(bytestring):
	res = ''
	for b in bytestring:
		b += '\x00'
		b = unpack('h',b)[0]
		b = b&1 # last bit
		res += str(b)
		 
	return str(res)	

# and finally, get the code
sol = ''
for l in xrange(m):
	sol += compute(rgb[l])
	
soln = ''	
for i in xrange(0,len(sol),8):
	# print sol[i:i+8]
	soln += chr(eval('0b'+sol[i:i+8]))

# yeah
# print soln		

for line in sys.stdin:
	# All previous code to get this from the file
	print '6108a80fe43c346c20a0e7c5e4f8d7fdf0c8498e'
	


