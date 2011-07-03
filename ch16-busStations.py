#!/usr/bin/python
import sys

# Challenge 16 is the Maximum Flow Problem: find a feasible flow 
# (that is, without exceeding the capacity of the network, in 
# this case the number of buses that can travel from one station to another) 
# through a network with a single source (origin station)
# and single sink (destination city), that is maximum 
# http://en.wikipedia.org/wiki/Maximum_flow_problem



def edmondsKarp(C, source, sink):
	"""
	Implementation of Edmonds-Karp algorithm for computing max-flow in a network
	It is a variation of the Ford-Fulkerson method. I tried that before and it was
	too slow for the test case, so I gave this one a go. 

	The code is almost a translation from the pseudocode in Wikipedia:
	http://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm#Pseudocode
	
	C is the capacity matrix and the function returns the maximum flow from source
	to sink
	"""
	n = len(C) # number of nodes/stations
	
	# residual capacity from u to v is C[u][v] - F[u][v]
	F = [[0]*n for i in xrange(n)]
	
	while True:
		# find by BFS shortest path which has available capacity 
		# this will be the augmenting path (backwards, with parents)
		path = bfs(C, F, source, sink)
		if not path:
			break
			
		# backtrack search from destination
		flow = min(C[u][v] - F[u][v] for u,v in path)
		
		# traverse found path to update flow
		for u,v in path:
			F[u][v] += flow
			F[v][u] -= flow

	return sum(F[source][i] for i in xrange(n))


def bfs(C, F, source, sink):
	"""
	In the Edmonds-Karp algorithm, the new augmenting path must be the shortest path with
	available capacity, and it is found by breadth-first search 
	This is basically the only difference with the Ford-Fulkerson algorithm
	"""
	queue = [source]                 
	paths = {source: []}
	while len(queue) > 0:
		u = queue.pop(0)
		# for each station/node
		# (Note: in Wikiepdia's pseudocode they only consider neighbours of u here. I 
		# consider all nodes, and for those that aren't connected to u, C[u,v]=0)
		for v in xrange(len(C)):
			# if there is available capacity, and v is not seen before in search:	
			if C[u][v] - F[u][v] > 0 and v not in paths:
				paths[v] = paths[u] + [(u,v)]
				if v == sink:
					return paths[v]
				queue.append(v)
	# there is no path 
	return False


# read cases
for line in sys.stdin:
	case = line.split()
	n, orig, dest = case[0:3]
	n = int(n)
	
	# capacity matrix
	C = [[0]*n for i in xrange(n)]
    
	cities = {orig:0, dest:1}
	ic = 2
	roads = {}
	
	# build capacity matrix 
	for r in case[3:]:
		source, destination, cap = r.split(',')		
		isource, idestination = 0, 0
		
		if not source in cities:
			cities[source] = ic
			isource = ic
			ic += 1
		else:
			isource = cities[source]
			
		if not destination in cities:
			cities[destination] = ic
			idestination = ic
			ic += 1
		else:
			idestination = cities[destination]	

		C[isource][idestination] = int(cap)	
			
	print edmondsKarp(C, 0, 1)
	


		
		
