#!/usr/bin/python
import sys



for line in sys.stdin:
	# case: W L N lx ly ux uy color
	case = map(int, line.split())
	W, L, N = case[0:3]
	rectangles = case[3:]	
	canvas = [[1]*W for k in range(L)]
	colors = [0]*(N+1) # just to output them in order
	colors[0] = 1
	ncolors = {1:0}
	
	# paint N rectangles 
	for i in range(N):
		lx, ly, ux, uy, color = rectangles[i*5:(i+1)*5]
		colors[i+1] = color
		ncolors[color] = 0 
		# check that there is a rectangle
		if (lx < ux and ly < uy):
			# transform y coordinates
			if ly < 0: 
				ly = 0
			ly = L - ly  # excluded 
			
			if uy > L:
				uy = L
			uy = L - uy # included 
			
			# now rectangle is (lx, uy) - (ux, ly)
			for j in range(uy, ly):
				for k in range(lx, ux):
					canvas[j][k] = color


	for i in range(L):
		for j in range(W):
			ncolors[canvas[i][j]] += 1

	res = ''		
	for i in range(N+1):
		if (ncolors[colors[i]] > 0):
			res += str(colors[i]) + ' ' + str(ncolors[colors[i]]) + ' '
	print res.strip()		
		
		
							

