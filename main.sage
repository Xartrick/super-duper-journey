#!/usr/bin/env sage

from FrameManager import FrameManager
from VideoConverter import VideoConverter

from Animations.AnimationManager import AnimationManager

import argparse

FRAME_PATTERN = 'frames/frame-%04d.png'

def main():
	parser = argparse.ArgumentParser(description='Generate an animation with SageMath based on beat timing. For better result, BPM should be divisible by FPS.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('--output',           default='output/output.mp4', help='Output filename')
	parser.add_argument('--width',  type=int, default=1280,                help='Frame width')
	parser.add_argument('--height', type=int, default=720,                 help='Frame height')
	parser.add_argument('--fps',    type=int, default=30,                  help='Frame rate')
	parser.add_argument('--bpm',    type=int, default=150,                 help='Beat-per-minute')

	args = parser.parse_args()

	output = args.output
	width  = args.width
	height = args.height
	fps    = args.fps
	bpm    = args.bpm

	frameManager     = FrameManager(fps, bpm)
	animationManager = AnimationManager(frameManager, width, height)

	animationManager.initializeAnimations()

	totalFrames = animationManager.getAnimationFrames()

	print('Generating animation with {} frames...').format(totalFrames)
	
	frames = len(list(animationManager.render([(n, FRAME_PATTERN % i) for i, n in enumerate(range(1, totalFrames + 1))])))

	print
	print
	print('Animation generated with {}/{} frames!'.format(frames, totalFrames))
	
	if frames != totalFrames:
		print('Animation seems to be invalid (wrong frame count)')
	
	print
	print('Converting video...')
	print

	video_manager = VideoConverter(FRAME_PATTERN, output, fps)

	video_manager.convert()
	video_manager.clean()

	print
	print('Done!')

if __name__ == "__main__":
	main()
