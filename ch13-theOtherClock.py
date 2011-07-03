#!/usr/bin/python
import sys

# leds[i] number of leds turned on for digit i
leds = [1,0,4,1,1,2,1,1,4,0]

# leds05[i] number of leds turned on for digit i, for 0..5
leds05 = [2,0,4,1,1,2]


# changes from i to j for one digit 0..9
def chg(i,j):
	if j < i:
		return 0
	return reduce(lambda x,y: x+y, leds[i:j+1])

# changes from i to j for one digit 0..5
def chg05(i,j):
	if j < i:
		return 0
	return reduce(lambda x,y: x+y, leds05[i:j+1])


# for example, changes on 2 digits from 00 to 59 
complete = chg05(0,5) + 6*chg(0,9)
# or changes on 2 digits from 00 to 23
day = chg05(0,1) + leds05[2] + 2*chg(0,9) + chg(0,3)


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
		
		# for i in xrange(0, rs%10 + 1):
		# 	seconds += leds[i]
		seconds += chg05(0,rs/10) + (rs/10)*chg(0,9) + chg(0,rs%10)
		
		
		# count the on/off changes for minutes
		minutes = h*complete
		rm = m % 60
		minutes += chg05(0,rm/10) + (rm/10)*chg(0,9) + chg(0,rm%10)
		
		# for i in xrange(0, rm):
		# 	minutes += (leds05[i/10] + leds[i%10])*60
			
		# last minute was repeated (rs + 1) times instead of 60 (it wasn't completed)
		# minutes += (leds05[rm/10] + leds[rm % 10])*(rs+1)	
		
		
		# count the on/off changes for hours
		hours = d*day
		rh = h % 24
		hours += chg05(0,rh/10) + (rh/10)*chg(0,9) + chg(0,rh%10)
		
		
		# for i in xrange(0, rh):
		# 	hours += (leds05[i/10] + leds[i%10])
			
		# last hour was repeated s % 3600 + 1 times instead of 3600
		# hours += (leds05[rh/10] + leds[rh % 10])*(s % 3600 + 1)

		print hours + minutes + seconds + 27
	


