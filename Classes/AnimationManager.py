# -*- coding: utf-8 -*-

from __future__ import print_function

from sage.all import parallel

from Animations.AnimationTerrain import AnimationTerrain
from Animations.AnimationFractal import AnimationFractal
from Animations.AnimationMaze import AnimationMaze

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
		self.addAnimation(AnimationTerrain(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar()) * 32))
		self.addAnimation(AnimationFractal(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar() * 8)))
		self.addAnimation(AnimationMaze(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar()) * 4))
		self.addAnimation(AnimationMaze(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar()) * 4))
		self.addAnimation(AnimationMaze(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar()) * 4))
		self.addAnimation(AnimationMaze(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar()) * 4))
		self.addAnimation(AnimationTerrain(self.frameManager, self.width, self.height, int(self.frameManager.framesPerBar()) * 4))

	@parallel
	def render(self, frameNumber, filename):
		self.frameManager.setCurrentFrame(frameNumber)

		if self.frameManager.isBeat():
			print()
			print('{:3d}.{}.{} '.format(self.frameManager.barCount() + 1, self.frameManager.beatModulo(), self.frameManager.sixteenthModulo()), end='')

		animation = self.getCurrentAnimation()

		animation['animation'].render(frameNumber - animation['start'], filename)

		print('.', end='')

	def addAnimation(self, animation):
		start = self.getAnimationFrames()

		self.animations.append({
			'start':     start,
			'animation': animation
		})

	def getCurrentAnimation(self):
		current_frame = self.frameManager.getCurrentFrame()

		for animation in self.animations:
			start = animation['start'] + 1
			end   = start + animation['animation'].getDuration()

			if current_frame >= start and current_frame < end:
				return animation

		return None

	def getAnimationFrames(self):
		frames = 0

		for animation in self.animations:
			frames += animation['animation'].getDuration()

		return frames
	