#!/usr/bin/python
import sys
import commands

def interpret(line):
	line = (line.replace('^','(')).replace('$',')')
	query = "[ch02-expressions], expr(" + line.replace(' ', ', ') + ", X), write(X), halt."	
	cmd = 'prolog -q -g "' + query + '"'
	return commands.getoutput(cmd)
	
for line in sys.stdin:
	if (len(line) <= 2):
		print line
	else: 
		print ((interpret(line.strip())).replace('(','')).replace(')','')
