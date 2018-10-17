# -*- coding: utf-8 -*-

from __future__ import print_function

from AnimationBase import AnimationBase

from Maze.Generator import Generator

class AnimationMaze(AnimationBase):
	def __init__(self, frameManager, width, height, duration):
		super(AnimationMaze, self).__init__(frameManager, width, height, duration)

		self.maze = Generator().generate(19, 19)
	
	def render(self, frameNumber, filename):
		self.frameManager.setCurrentFrame(frameNumber)

		camera_center = (1.0, 0.75, -1)
		look_at       = (0.5, 0.25, 1)

		self.initializeWindow(camera_center, look_at)

		self.window.light((1, 2, -3), 0.2, (1, 1, 1))

		self.window.texture('blue', ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=(0,0,1))
		self.window.texture('red', ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=(1,0,0))
		self.window.texture('green', ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=(0,1,0))

		maze_size  = len(self.maze)
		cube_scale = 1. / float(maze_size)

		for y_pos, y_maze in enumerate(self.maze):
			for x_pos, wall in enumerate(y_maze):
				if wall == '#':
					self.drawCube(cube_scale * x_pos, 0, cube_scale * y_pos, cube_scale, 'blue')
				elif wall == 'o':
					self.drawCube(cube_scale * x_pos, 0, cube_scale * y_pos, cube_scale, 'red')
				elif wall == 'x':
					self.drawCube(cube_scale * x_pos, 0, cube_scale * y_pos, cube_scale, 'green')
					
		self.window.save(filename)
