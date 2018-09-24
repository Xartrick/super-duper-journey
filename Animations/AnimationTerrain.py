from AnimationBase import AnimationBase

from sage.all import cos, sin, matrix, pi

from noise import pnoise2

class AnimationTerrain(AnimationBase):
	octave = 1

	def render(self, frameNumber, filename):
		self.frameManager.setCurrentFrame(frameNumber)

		camera_center = (1.0, 0.75, -1)
		look_at       = (0.5, 0.25, 1)

		look_at = (0.5, 0, 0.5)

		alpha = (2.0 * pi) * (float(frameNumber) / float(self.getDuration()))
		P     = matrix(2, 1, [1.0, 1.0])
		R     = matrix(2, 2, [cos(alpha), -sin(alpha), sin(alpha), cos(alpha)])

		pos = R * P

		camera_center = (float(pos[0][0]), 0.75, float(pos[1][0]))

		self.initializeWindow(camera_center, look_at)
		# self.window.light((0.5,1,-1), 0.2, (1,0.5,1))
		self.window.light((1, 2, -3), 0.2, (1, 0.5, 1))

		fpb        = float(self.frameManager.framesPerBeat()) * 2.0
		brightness = (frameNumber % fpb) / fpb
		color      = (0, 1.0 - brightness, 0)

		self.window.texture('green', ambient=0.2, diffuse=1.0, specular=0.0, opacity=1.0, color=color)

		self.octave = self.frameManager.beatCount() + 1

		cols  = 25
		rows  = 25
		scale = 1.0 / float(cols)

		for x in range(0, rows):
			for z in range(0, cols):
				self.window.triangle([x * scale,       self.terrain(x,   z+1, frameNumber), (z + 1) * scale], [x * scale, self.terrain(x, z,   frameNumber), z * scale],       [(x + 1) * scale, self.terrain(x+1, z, frameNumber), z * scale], 'green')
				self.window.triangle([(x + 1) * scale, self.terrain(x+1, z+1, frameNumber), (z + 1) * scale], [x * scale, self.terrain(x, z+1, frameNumber), (z + 1) * scale], [(x + 1) * scale, self.terrain(x+1, z, frameNumber), z * scale], 'green')

		self.window.save(filename)

	def terrain(self, x, y, offset=0.0):
		return pnoise2((float(offset) / 100.0) - (y / 100.0), (float(offset) / 100.0) - (x / 100.0), self.octave)
