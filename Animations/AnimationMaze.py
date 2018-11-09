# -*- coding: utf-8 -*-

from __future__ import print_function

from AnimationBase import AnimationBase

from Maze.Generator import Generator
from Maze.Solver import Solver

class AnimationMaze(AnimationBase):
	def __init__(self, frameManager, width, height, duration):
		super(AnimationMaze, self).__init__(frameManager, width, height, duration)

		self.maze = Generator().generate(19, 19)
		self.solution = Solver().solve(self.maze)
	
	def render(self, frameNumber, filename):
		self.frameManager.setCurrentFrame(frameNumber)

		camera_center = (1.5, 1.0, 0.5)
		look_at       = self.getCameraLookAt()

		self.initializeWindow(camera_center, look_at)

		self.window.light((1, 2, -3), 0.2, (1, 1, 1))

		self.window.texture('blue',  ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=(0,0,1))
		self.window.texture('red',   ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=(1,0,0))
		self.window.texture('white', ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=(1,1,1))

		scale = self.getScale()

		for y_pos, y_maze in enumerate(self.maze):
			for x_pos, wall in enumerate(y_maze):
				if wall == '#':
					self.drawCube(scale * x_pos, 0, scale * y_pos, scale, 'blue')
				elif wall == 'x':
					self.drawCube(scale * x_pos, 0, scale * y_pos, scale, 'red')
		
		#for pos in self.solution:
		#	self.drawCube(scale * pos[0], 0, scale * pos[1], scale, 'white')
		
		player = self.getPlayerPosition()

		w = (scale / 2.0)

		self.window.sphere((player[0], w, player[1]), w, 'white')
		
		self.window.save(filename)

	def getPlayerPosition(self):
		pos_max = len(self.solution) - 1
		_       = pos_max * (float(self.frameManager.getCurrentFrame()) / float(self.getDuration()))
		step    = int(_)

		current_pos = self.solution[step]
		next_pos    = self.solution[min(pos_max, step + 1)]

		player = current_pos

		scale  = self.getScale()
		w      = (scale / 2.0)
		p       = (_ - step) * scale

		x = scale * player[0] + w
		y = scale * player[1] + w

		if current_pos[0] < next_pos[0]:
			x += p
		elif current_pos[0] > next_pos[0]:
			x -= p
		
		if current_pos[1] < next_pos[1]:
			y += p
		elif current_pos[1] > next_pos[1]:
			y -= p

		return (x, y)
	
	def getCameraLookAt(self):
		pos   = self.getPlayerPosition()
		scale = self.getScale()
		w     = (scale / 2.0)

		return (pos[0], w, pos[1])
	
	def getScale(self):
		return 1. / float(len(self.maze))
