#!/usr/bin/python
import sys


def select(nodes, dist):
	mind = sys.maxint
	minn = -1
	for n in nodes:
		if dist[n] < mind:
			mind = dist[n]
			minn = n
	return minn		
	
# to compute shortest paths in graphs, but considering
# negative weights in edges :-)
# implementation based on Wikipedia's pseudocode
def BellmanFord(edges, source, target, n):
	startdate = 25000
	
	# Step 1: initialize graph
	dist = [sys.maxint]*n # distance from source to each node
	dist[source] = 0
	# pred = [None]*n # shortest path

	
	# Step 2: relax edges repeatedly
   	for i in xrange(n-1):
		for e in edges: # e = (u,v,dist) 
			u = e[0]
			v = e[1]
			if dist[u] + e[2] < dist[v]:
				dist[v] = dist[u] + e[2]
				# pred[v] = u
				
	# Step 3: check for negative-weight cycles
	for e in edges:
		u = e[0]
		v = e[1]
		if dist[u] + e[2] < dist[v]:
			return 'BAZINGA'
	
	# Step 4: construct path and compute distance	
	return str(dist[target] + startdate)		
			

for line in sys.stdin:
	case = line.split()
	
	# number of planets
	n = int(case[0])

	earth = int(case[1])
	atlantis = int(case[2])
	
	# read connections between planets
	edges = []
	for k in case[3:]:
		c = map(int, k.split(','))
		edges.append(c)	

	print BellmanFord(edges, earth, atlantis, n) 