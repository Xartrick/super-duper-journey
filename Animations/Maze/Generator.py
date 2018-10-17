import numpy as np
import random

class Generator:
	EMPTY = ' '
	WALL  = '#'
	AGENT = 'o'
	GOAL  = 'x'
	
	def adjacent(self, cell):
		i,j = cell
		for (y,x) in ((1,0), (0,1), (-1, 0), (0,-1)):
			yield (i+y, j+x), (i+2*y, j+2*x)
	
	def generate(self, width, height): 
		width  += 2
		height += 2

		rows, cols = height, width
	
		maze = {}
	
		spaceCells = set()
		connected  = set()
		walls      = set()
	
		for i in range(rows):
			for j in range(cols):
				if (i % 2 == 1) and (j % 2 == 1):
					maze[(i,j)] = self.EMPTY
				else:
					maze[(i,j)] = self.WALL 
	
		for i in range(rows):
			maze[(i, 0)]        = self.WALL
			maze[(i, cols - 1)] = self.WALL
		
		for j in range(cols):
			maze[(0, j)]        = self.WALL
			maze[(rows - 1, j)] = self.WALL
	
		for i in range(rows):
			for j in range(cols):
				if maze[(i, j)] == self.EMPTY:
					spaceCells.add((i, j))
				if maze[(i, j)] == self.WALL:
					walls.add((i, j))

		connected.add((1, 1))

		while len(connected) < len(spaceCells):
			doA, doB = None, None
			cns      = list(connected)

			random.shuffle(cns)

			for (i,j ) in cns:
				if doA is not None:
					break
				
				for A, B in self.adjacent((i,j)):
					if A not in walls: 
						continue
					
					if (B not in spaceCells) or (B in connected):
						continue
					
					doA, doB = A, B

					break

			A, B    = doA, doB
			maze[A] = self.EMPTY

			walls.remove(A)
			
			spaceCells.add(A)

			connected.add(A)
			connected.add(B)
	
		TL = (1, 1)
		BR = (rows - 2, cols - 2)

		if rows % 2 == 0:
			BR = (BR[0] - 1, BR[1])
		
		if cols % 2 == 0:
			BR = (BR[0], BR[1] - 1)
	
		maze[TL] = self.AGENT
		maze[BR] = self.GOAL
	
		lines = []

		for i in range(rows):
			lines.append(''.join(maze[(i,j)] for j in range(cols)))
	
		return lines
