import os

class VideoConverter:
	input  = ''
	output = ''
	fps    = 0.0

	def __init__(self, input, output, fps = 30):
		self.input  = input
		self.output = output
		self.fps    = fps

	def convert(self):
		os.system('ffmpeg -framerate %i -i %s -c libx264 -pix_fmt yuv420p %s' % (self.fps, self.input, self.output))

	def clean(self):
		os.system('rm frames/*')
