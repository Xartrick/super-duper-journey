class FrameManager:
	fps = 0.0
	bpm = 0.0
	frame = 0

	def __init__(self, fps = 30, bpm = 150):
		self.fps = float(fps)
		self.bpm = float(bpm)

	def framesPerBar(self):
		return self.framesPerBeat() * 4.0

	def framesPerBeat(self):
		return (self.fps * 60.0) / self.bpm

	def framesPerSixteenth(self):
		return self.framesPerBeat() / 4.0

	def barCount(self):
		return int((self.frame - 1) / self.framesPerBar())

	def beatCount(self):
		return int((self.frame - 1) / self.framesPerBeat())

	def sixteenthCount(self):
		return int((self.frame - 1) / self.framesPerSixteenth())

	def beatModulo(self):
		return (self.beatCount() % 4) + 1

	def sixteenthModulo(self):
		return (self.sixteenthCount() % 4) + 1

	def isBar(self):
		return ((self.frame - 1) % self.framesPerBar()) == 0

	def isBeat(self):
		return ((self.frame - 1) % self.framesPerBeat()) == 0

	def isSixteenth(self):
		return ((self.frame - 1) % self.framesPerSixteenth()) == 0

	def getCurrentFrame(self):
		return self.frame

	def setCurrentFrame(self, n):
		self.frame = n
