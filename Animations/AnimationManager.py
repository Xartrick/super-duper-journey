from __future__ import print_function

from sage.all import parallel

from AnimationTerrain import AnimationTerrain
from AnimationFractal import AnimationFractal

class AnimationManager:
	frameManager = None
	width        = 0
	height       = 0
	animations   = []

	def __init__(self, frameManager, width, height):
		self.frameManager = frameManager
		self.width        = width
		self.height       = height

	def initializeAnimations(self):
		self.addAnimation(AnimationTerrain(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar()) * 4))
		self.addAnimation(AnimationFractal(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar()) * 4))

	@parallel
	def render(self, n, filename):
		self.frameManager.setCurrentFrame(n)

		animation = self.getCurrentAnimation()

		animation.render(n, filename)

		if self.frameManager.isBeat():
			print()
			print('{:3d}.{}.{} '.format(self.frameManager.barCount() + 1, self.frameManager.beatModulo(), self.frameManager.sixteenthModulo()), end='')

		print('.', end='')

	def addAnimation(self, animation):
		start = self.getAnimationFrames()

		self.animations.append({
			'start':     start,
			'animation': animation
		})

	# TODO : select correct animation based on current frame, animation's start frame and duration
	def getCurrentAnimation(self):
		currentFrame = self.frameManager.getCurrentFrame()

		for animation in self.animations:
			if animation['start'] >= currentFrame and animation['start'] + animation['animation'].getDuration() < currentFrame:
				return animation['animation']

		return self.animations[0]['animation']

	def getAnimationFrames(self):
		frames = 0

		for animation in self.animations:
			frames += animation['animation'].getDuration()

		return frames
