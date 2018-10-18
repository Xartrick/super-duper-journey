# -*- coding: utf-8 -*-

from sage.all import Tachyon

class AnimationBase(object):
	frameManager = None
	width         = 0
	height        = 0
	duration      = 0
	window        = None

	def __init__(self, frameManager, width, height, duration):
		self.frameManager = frameManager
		self.width        = width
		self.height       = height
		self.duration     = duration

	def initializeWindow(self, camera_center, look_at):
		self.window = Tachyon(xres=self.width, yres=self.height, antialiasing=True, raydepth=10, camera_center=camera_center, look_at=look_at, updir=(0,1,0))

	def drawCube(self, pos_x, pos_y, pos_z, scale, texture):
		vertices = [
			[1, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 1, 1, 1, 0, 0, 0, 1],
			[1, 1, 0, 0, 1, 0, 0, 1, 1],
			[1, 1, 1, 1, 1, 0, 0, 1, 1],
			[0, 0, 0, 1, 0, 0, 1, 1, 0],
			[0, 1, 0, 1, 1, 0, 0, 0, 0],
			[0, 0, 1, 1, 0, 1, 1, 1, 1],
			[0, 1, 1, 1, 1, 1, 0, 0, 1],
			[0, 0, 0, 0, 1, 0, 0, 1, 1],
			[0, 1, 1, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 1, 1, 0, 1, 1, 1],
			[1, 1, 1, 1, 0, 0, 1, 0, 1]
		]

		for _ in vertices:
			self.window.triangle(
				[pos_x + _[0] * scale, pos_y + _[1] * scale, pos_z + _[2] * scale],
				[pos_x + _[3] * scale, pos_y + _[4] * scale, pos_z + _[5] * scale],
				[pos_x + _[6] * scale, pos_y + _[7] * scale, pos_z + _[8] * scale],
				texture
			)

		# # bottom
		# self.window.triangle([pos_x + 1.*scale,pos_y + 0.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 1.*scale], texture)
		# self.window.triangle([pos_x + 1.*scale,pos_y + 0.*scale,pos_z + 1.*scale], [pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 1.*scale], texture)
		# # top
		# self.window.triangle([pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 1.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 1.*scale,pos_z + 1.*scale], texture)
		# self.window.triangle([pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 1.*scale], [pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 1.*scale,pos_z + 1.*scale], texture)
		# # front
		# self.window.triangle([pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 0.*scale], [pos_x + 1.*scale,pos_y + 0.*scale,pos_z + 0.*scale], [pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 0.*scale], texture)
		# self.window.triangle([pos_x + 0.*scale,pos_y + 1.*scale,pos_z + 0.*scale], [pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 0.*scale], texture)
		# # back
		# self.window.triangle([pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 1.*scale], [pos_x + 1.*v,pos_y + 0.*scale,pos_z + 1.*scale], [pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 1.*scale], texture)
		# self.window.triangle([pos_x + 0.*scale,pos_y + 1.*scale,pos_z + 1.*scale], [pos_x + 1.*scale,pos_y + 1.*v,pos_z + 1.*scale], [pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 1.*scale], texture)
		# # left
		# self.window.triangle([pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 1.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 1.*scale,pos_z + 1.*scale], texture)
		# self.window.triangle([pos_x + 0.*scale,pos_y + 1.*scale,pos_z + 1.*scale], [pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 0.*scale], [pos_x + 0.*scale,pos_y + 0.*scale,pos_z + 1.*scale], texture)
		# # right
		# self.window.triangle([pos_x + 1.*scale,pos_y + 0.*scale,pos_z + 0.*scale], [pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 0.*scale], [pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 1.*scale], texture)
		# self.window.triangle([pos_x + 1.*scale,pos_y + 1.*scale,pos_z + 1.*scale], [pos_x + 1.*scale,pos_y + 0.*scale,pos_z + 0.*scale], [pos_x + 1.*scale,pos_y + 0.*scale,pos_z + 1.*scale], texture)

	def getDuration(self):
		return self.duration
