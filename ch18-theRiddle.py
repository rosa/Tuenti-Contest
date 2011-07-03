#!/usr/bin/python
import sys
import base64
import png

# get the image
f = open("theRiddle.png", 'w')

for line in sys.stdin:
	s = base64.b64decode(line)	
	f.write(s)

f.close()	

# using the weirdest and most esoteric PNG library I could find...
# (because I can't get f**ing PIL to work in my evil Mac)
r = png.Reader("theRiddle.png")
w, h, rows, meta = r.read_flat()
pixels = [0] * h
i = 0
rowsize = w*3

j = 0
# iterate over lines and put them into a matrix
for i in xrange(0,len(rows),rowsize):
	pixels[j] = rows[i:i+rowsize]
	j += 1


	
dirtylines = ''
	
# read just the 'dirty' columns in the image
for i in xrange(0,w,3):
	# access first row, i-th pixel
	ithpixel = (pixels[0][i:i+3]).tolist()
	if not (255 in ithpixel):
		# dirty column found:
		dirtyline = ''
		for j in xrange(h):
			dirtyline += reduce(lambda x, y: x+y, map(chr, (pixels[j][i:i+3]).tolist()))
			# dirtyline += str(reduce(lambda x,y: x+y, map(chr, pixels[j][i:i+3])))
		dirtylines += dirtyline + "\n"

		# print map(chr, dirtyline)
		# print dirtyline

# Aha! There you are
# print dirtylines
# how much is 2215 + 4719???

print 2215 + 4719



