# -*- coding: utf-8 -*-

import os

class VideoConverter:
	input  = ''
	output = ''
	audio  = ''
	fps    = 0.0

	_tmp       = 'output/tmp.mp4'
	_tmp_audio = 'output/tmp_audio.mp4'

	def __init__(self, inputFiles, outputFile, audioFile, fps = 30):
		self.input  = inputFiles
		self.output = outputFile
		self.audio  = audioFile
		self.fps    = fps

	def convert(self):
		os.system('ffmpeg -y -framerate %i -i %s -c libx264 -pix_fmt yuv420p %s > /dev/null 2>&1' % (self.fps, self.input, self._tmp))
	
	def addAudio(self):
		os.system('ffmpeg -i %s -i %s -codec copy -shortest %s > /dev/null 2>&1' % (self._tmp, self.audio, self._tmp_audio))
		os.rename(self._tmp_audio, self._tmp)

	def clean(self):
		os.rename(self._tmp, self.output)

		directory = 'frames'
		files     = os.listdir(directory)

		for file in files:
			if file.endswith('.png'):
				os.remove(os.path.join(directory, file))
