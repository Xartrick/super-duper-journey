# -*- coding: utf-8 -*-

from AnimationBase import AnimationBase

from sage.all import cos, sin, matrix, pi

from noise import pnoise2

class AnimationTerrain(AnimationBase):
	octave = 1
	divide = 100.0

	def render(self, frameNumber, filename):
		self.frameManager.setCurrentFrame(frameNumber)

		camera_center = (1.0, 0.75, -1)
		look_at       = (0.5, 0.25, 1)

		look_at = (0.5, 0, 0.5)

		self.initializeWindow(camera_center, look_at)

		self.window.light((1, 2, -3), 0.2, (1, 1, 1))

		fpb        = float(self.frameManager.framesPerBar()) * 2.0
		brightness = 1.0 - (((frameNumber - 1) % fpb) / fpb)
		color      = ((46.0 / 255.0) * brightness, (204.0 / 255.0) * brightness, (113.0 / 255.0) * brightness)
		
		self.window.texture('green', ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=color)

		if self.frameManager.barCount() >= 16:
			self.octave = 3
			self.divide = 75.0

			cols = 100
			rows = 100
		else:
			self.octave = 1
			self.divide = 100.0

			cols = 50
			rows = 50

		scale = 1.0 / float(cols)

		for row in range(0, rows):
			for col in range(0, cols):
				self.window.triangle([row * scale,       self.terrain(row,   col+1, frameNumber), (col + 1) * scale], [row * scale, self.terrain(row, col,   frameNumber), col * scale],       [(row + 1) * scale, self.terrain(row+1, col, frameNumber), col * scale], 'green')
				self.window.triangle([(row + 1) * scale, self.terrain(row+1, col+1, frameNumber), (col + 1) * scale], [row * scale, self.terrain(row, col+1, frameNumber), (col + 1) * scale], [(row + 1) * scale, self.terrain(row+1, col, frameNumber), col * scale], 'green')

		self.window.save(filename)

	def terrain(self, xPos, yPos, offset=0.0):
		return pnoise2((float(offset) / self.divide) - (yPos / self.divide), (float(offset) / self.divide) - (xPos / self.divide), self.octave)
