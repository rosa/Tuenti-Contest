#!/usr/bin/python
import sys

# load task data
f = open("in", 'r')

# read number of tasks
n = -1
while n == -1:
	line = f.readline()
	if (not line.startswith('#') and line != '' and not line.isspace()):
		n = int(line.strip())

# read times for the tasks
times = [[0,True] for k in range(0,n)]
while not line.startswith('#Task duration'):
	line = f.readline()

for i in xrange(0, n):
	line = f.readline()
	t = map(int, line.split(','))
	times[t[0]][0] = t[1]

# read dependencies for the tasks
dependencies = {}
while not line.startswith('#Task dependencies'):
	line = f.readline()

for line in f:
	d = map(int, line.split(','))
	dependencies[d[0]] = d[1:]
	times[d[0]][1] = False # mark the task as dependent, to check that in O(1)


def solveTask(task): 
	# no dependencies
	if times[task][1]:
		return times[task][0]	
	# solve dependencies
	dep = dependencies[task]
	deptimes = []
	for d in dep:
		deptimes.append(solveTask(d))
	res = max(deptimes) + times[task][0]
	# update times and dependencies 
	times[task] = [res, True]
	return res
		


# process queries
for line in sys.stdin:
	if not line.isspace() and not line == '':
		queries = map(int, line.split(','))
		
		# preprocess only the ones with dependencies higher than themselves
		# and higher than the minimum query
		for i in range(n-1,min(queries)-1,-1):
			if not times[i][1]:
				depi = dependencies[i]
				if min(depi) > i:
					solveTask(i)
							
		for q in queries:
			print str(q) + " " + str(solveTask(q))

