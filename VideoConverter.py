import os

class VideoConverter:
	input  = ''
	output = ''
	fps    = 0.0

	def __init__(self, inputFiles, outputFile, fps = 30):
		self.input  = inputFiles
		self.output = outputFile
		self.fps    = fps

	def convert(self):
		os.system('ffmpeg -framerate %i -i %s -c libx264 -pix_fmt yuv420p %s' % (self.fps, self.input, self.output))

	@classmethod
	def clean(cls):
		directory = 'frames'
		files     = os.listdir(directory)

		for file in files:
			if file.endswith('.png'):
				os.remove(os.path.join(directory, file))
