#!/usr/bin/python
import sys

# leds[i] number of leds turned on for digit i
leds = [6,2,5,5,4,5,6,3,7,6]

# changes from i to j for one digit
def chg(i,j):
	if j < i:
		return 0
	return reduce(lambda x,y: x+y, leds[i:j+1])

# for example, changes on 2 digits from 00 to 59 
complete = 10*chg(0,5) + 6*chg(0,9)
# or changes on 2 digits from 00 to 23
day = 10*chg(0,1) + 4*leds[2] + 2*chg(0,9) + chg(0,3)


for line in sys.stdin:
	# read seconds, minutes, hours
	if line != '' and not line.isspace():
		s = int(line.strip())
		m = s/60
		h = m/60
		d = h/24
		# if more than one day
		# 2401956
		# days = 0
		# if h >= 24:
		# 	d = h/24
		# 	h = h % 24	
		# 	m = m - d*24*60
		# 	s = s - d*24*3600
		# 	days = d*(day*3600 + 2*24*complete*60)
		
		# count the on/off changes for seconds
		seconds = m*complete
		rs = s % 60
		for i in xrange(0, rs + 1):
			seconds += leds[i/10] + leds[i%10]
	
		# count the on/off changes for minutes
		minutes = h*complete*60
		rm = m % 60
		for i in xrange(0, rm):
			minutes += (leds[i/10] + leds[i%10])*60
			
		# last minute was repeated (rs + 1) times instead of 60 (it wasn't completed)
		minutes += (leds[rm/10] + leds[rm % 10])*(rs+1)	
		
		
		# count the on/off changes for hours
		hours = d*day*3600
		rh = h % 24
		for i in xrange(0, rh):
			hours += (leds[i/10] + leds[i%10])*3600
			
		# last hour was repeated s % 3600 + 1 times instead of 3600
		hours += (leds[rh/10] + leds[rh % 10])*(s % 3600 + 1)
		print hours + minutes + seconds
	


	