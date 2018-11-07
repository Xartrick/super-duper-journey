from __future__ import print_function

import math
import random
from random import randint

class Generator:
	EMPTY = ' '
	WALL  = '#'
	AGENT = 'o'
	GOAL  = 'x'

	def __init__(self):
		pass

	def showCon(self):
		for i in range(len(self.connectedMaze)):
			if(i%self.WIDTH==0):
				print()
			print(self.connectedMaze[i],end=' ')

	def showMaze(self):
		for i in range(len(self.Maze)):
			if(i%(self.WIDTH*2+1)==0):
				print()
			print(self.Maze[i],end='')

	def showRemoved(self):
		for i in range(len(self.removedWall)):
			print(self.removedWall[i],end=' ')

	def isUsed(self,nb):
		for i in range(len(self.removedWall)):
			if nb == self.removedWall[i]:
				return True
		return False

	def initialize(self):
		for i in range(1,(self.WIDTH*self.HEIGHT) + 1 ):
			self.connectedMaze.append(i)

		height = self.HEIGHT*2 +1
		width = self.WIDTH*2 +1

		for i in range(height*width):
			self.Maze.append(self.EMPTY)

		for i in range(height):
			for j in range(width):
				if(i==0 or j == 0 or i==height-1 or j==width-1 or i%2==0 or j%2==0):
					self.Maze[i*width+j]=self.WALL
				if(i==1 and j==1):
					self.Maze[i*width+j]=self.AGENT
				if(i==height-2 and j==width-2):
					self.Maze[i*width+j]=self.GOAL

	def finished(self):
		end = True

		for i in range(len(self.connectedMaze)):
			if(self.connectedMaze[i] != 1):
				end = False
				break

		return end

	def randomGenerate(self):
		first = self.WIDTH*2+3
		last = len(self.Maze)-self.WIDTH*2-4

		height = self.HEIGHT*2 +1
		width = self.WIDTH*2 +1

		end=self.finished()

		while(not end):
			wall = randint(first,last)
			while( (((wall//width)%2) == ((wall%width)%2)) or (wall%width==0) or (wall%width == width-1) or (self.isUsed(wall)) ):
				wall = randint(first,last)

			ligne = int(wall//width)
			col = int(wall%width)

			if(ligne%2==0):
				ligne1 = (ligne-1)//2
				ligne2 = (ligne+1)//2
				col = (col-1)//2
				case1=self.connectedMaze[ligne1*self.WIDTH+col]
				case2=self.connectedMaze[ligne2*self.WIDTH+col]
				if(case1 != case2):
					newNb = min(case1,case2)
					oldNb = max(case1,case2)
					for i in range(len(self.connectedMaze)):
						if self.connectedMaze[i] == oldNb:
							self.connectedMaze[i] = newNb
					self.removedWall.append(wall)
					self.Maze[wall]=self.EMPTY

			else :
				col1 = (col-1)//2
				col2 = (col+1)//2
				ligne = (ligne-1)//2
				case1=self.connectedMaze[ligne*self.WIDTH+col1]
				case2=self.connectedMaze[ligne*self.WIDTH+col2]
				if(case1 != case2):
					newNb = min(case1,case2)
					oldNb = max(case1,case2)
					for i in range(len(self.connectedMaze)):
						if self.connectedMaze[i] == oldNb:
							self.connectedMaze[i] = newNb
					self.removedWall.append(wall)
					self.Maze[wall]=self.EMPTY

			end=self.finished()

	def generate(self, width, height):
		self.WIDTH=width
		self.HEIGHT=height
		self.connectedMaze=[]
		self.Maze=[]
		self.removedWall=[]

		self.initialize()
		self.randomGenerate()

		maze = []

		maze_line = ''

		for i in range(len(self.Maze)):
			if(i%(self.WIDTH*2+1)==0):
				if len(maze_line) > 0:
					maze.append(maze_line)
					maze_line = ''
			
			maze_line += self.Maze[i]
		
		maze.append(maze_line)

		return maze
