from AnimationBase import AnimationBase

from sage.all import matrix, sin, cos, pi, random

class AnimationSphere(AnimationBase):
	def render(self, frameNumber, filename):
		self.frameManager.setCurrentFrame(frameNumber)

		camera_center = (1.0, 1.5, frameNumber / 30.0)
		look_at = (1.0, 1.0, -5.5)

		self.initializeWindow(camera_center, look_at)
		
		self.window.light((4,3,2), 0.2, (1,1,1))
		self.window.texture('t2', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1,0,0))
		self.window.texture('t3', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(0,1,0))
		self.window.texture('t4', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(0,0,1))
		self.window.texture('t5', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1,1,0))
		self.window.texture('t6', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1,0,1))
		self.window.texture('t7', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(0,1,1))
		self.window.sphere((1,1,0), 0.2, 't2')
		self.window.sphere((1,1,-1), 0.2, 't3')
		self.window.sphere((1,1,-2), 0.2, 't4')
		self.window.sphere((1,1,-3), 0.2, 't5')
		self.window.sphere((1,1,-4), 0.2, 't6')
		self.window.sphere((1,1,-5), 0.2, 't7')

		self.window.save(filename)
