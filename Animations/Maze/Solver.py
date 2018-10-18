from __future__ import print_function

import heapq

class PriorityQueue:
	def __init__(self):
		self.elements = []

	def empty(self):
		return len(self.elements) == 0

	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))

	def get(self):
		return heapq.heappop(self.elements)[1]

class SquareGrid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.walls = []

	def in_bounds(self, id):
		(x, y) = id
		return 0 <= x < self.width and 0 <= y < self.height

	def passable(self, id):
		return id not in self.walls

	def neighbors(self, id):
		(x, y) = id
		results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
		if (x + y) % 2 == 0:
			results.reverse()
		results = filter(self.in_bounds, results)
		results = filter(self.passable, results)
		return results

class Solver:
	def __init__(self):
		pass

	def solve(self, maze):
		graph = self.get_graph(maze)
		start = self.get_start(maze)
		goal  = self.get_goal(maze)

		came_from, cost_so_far = self.dijkstra_search(graph, start, goal)
		path = self.reconstruct_path(came_from, start, goal)

		return path
	
	def get_start(self, maze):
		for y_pos, y_maze in enumerate(maze):
			for x_pos, wall in enumerate(y_maze):
				if wall == 'o':
					return (x_pos, y_pos)
		
		return None
	
	def get_goal(self, maze):
		for y_pos, y_maze in enumerate(maze):
			for x_pos, wall in enumerate(y_maze):
				if wall == 'x':
					return (x_pos, y_pos)
		
		return None
	
	def get_graph(self, maze):
		size  = len(maze)
		graph = SquareGrid(size, size)
		walls = []
		

		for y_pos, y_maze in enumerate(maze):
			for x_pos, wall in enumerate(y_maze):
				if wall == '#':
					walls.append((x_pos, y_pos))

		graph.walls = walls

		return graph

	def dijkstra_search(self, graph, start, goal):
		frontier = PriorityQueue()
		frontier.put(start, 0)

		came_from = {start: None}
		cost_so_far = {start: 0}

		while not frontier.empty():
			current = frontier.get()

			if current == goal:
				break

			for next in graph.neighbors(current):
				new_cost = cost_so_far[current] + 1

				if next not in cost_so_far or new_cost < cost_so_far[next]:
					cost_so_far[next] = new_cost
					priority = new_cost
					frontier.put(next, priority)
					came_from[next] = current

		return came_from, cost_so_far

	def reconstruct_path(self, came_from, start, goal):
		current = goal
		path = [current]

		while current != start:
			current = came_from[current]
			path.append(current)
		
		path.reverse()

		return path
