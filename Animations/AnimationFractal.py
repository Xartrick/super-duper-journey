# -*- coding: utf-8 -*-

from AnimationBase import AnimationBase

from Fractal.Fractal import CreateMat, init_lignes

from sage.all import matrix, sin, cos, pi

class AnimationFractal(AnimationBase):
	current_stage = 0
	fractal       = None

	def render(self, frameNumber, filename):
		self.frameManager.setCurrentFrame(frameNumber)

		look_at = (0.5, 0, 0.5)

		alpha    = (2.0 * pi) * ((float(frameNumber)) / float(self.getDuration() / 8.0))
		p_matrix = matrix(2, 1, [1.0, 1.0])
		r_matrix = matrix(2, 2, [cos(alpha), -sin(alpha), sin(alpha), cos(alpha)])

		pos = r_matrix * p_matrix

		camera_center = (float(pos[0][0]), 0.75, float(pos[1][0]))

		self.initializeWindow(camera_center, look_at)

		self.window.light((1, 2, -3), 0.2, (1, 1, 1))

		self.window.texture('blue', ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=(0,0,1))

		stage = self.frameManager.barCount() % 4

		if self.fractal == None:
			self.fractal       = self.getFractal(stage)
			self.current_stage = stage
		elif self.current_stage != stage:
			self.fractal       = self.getFractal(stage)
			self.current_stage = stage

		fractal_size = self.getFractalSize(self.fractal)

		cube_scale = 1. / float(fractal_size)

		for y_pos, y_fractal in enumerate(self.fractal):
			for x_pos, x_y_fractal in enumerate(y_fractal):
				for z_pos, x_y_z_fractal in enumerate(x_y_fractal):
					if x_y_z_fractal == 1:
						self.drawCube(cube_scale * x_pos, cube_scale * y_pos, cube_scale * z_pos, cube_scale, 'blue')

		self.window.save(filename)

	def getFractalSize(self, fractal):
		return len(fractal[0])

	def getFractal(self, step):
		if (step == 0):
			return [
				[
					[0]
				]
			]
		
		matrix  = CreateMat(step)
		fractal = []

		for level in matrix.tabCouche:
			levels = []

			init_lignes(level)

			for line in level.lignes:
				levels.append(line)
			
			fractal.append(levels)

		return fractal
