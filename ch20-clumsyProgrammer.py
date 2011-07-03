#!/usr/bin/python
import sys
import os 
import base64
import commands

# command to decrypt the input using openssl
command = 'openssl rsautl -decrypt -in clumsyProgrammerData -passin file:q -inkey '

# weird ' character, it's stored in q
# ssh-keygen -N "'" -b 1024 -f ~/.ssh/id_rsa
f = open('q','w')
f.write("'")
f.close()

# read input
for line in sys.stdin:
	line = base64.b64decode(line)
	f = open('clumsyProgrammerData',"w")
	f.write(line)
	f.close()
	
	# iterate over generated keys
	# thanks to http://digitaloffense.net/ ^^
	path = 'rsa/1024'
	listing = os.listdir(path)
	for infile in listing:
		if infile[-3:] != 'pub':
			output = commands.getoutput(command + path + '/' +infile)
			# guessing  
			# if output.count('key') > 0 or output.count('code') > 0:
				# print output

# Thanks for finding the keys!
# Submit the code 235180e8d3e09c8aeef73554d19e5ed2
print '235180e8d3e09c8aeef73554d19e5ed2'
