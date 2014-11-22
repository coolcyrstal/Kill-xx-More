import pygame
from pygame.locals import *

class GameScreen(object):

	def __init__(self, title, background_color, window_size = (1080,640), fps = 60):
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.background_color = background_color

		self.is_terminated = False

	def terminate(self):
		self.is_terminated = True

	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)

	def run(self):
		self.init()
		while not self.is_terminated:
			self.update()

			self.surface.fill(self.background_color)
			self.render(self.surface)
			pygame.display.update()

			self.clock.tick(self.fps)

	def init(self):
		self.__game_init()

	def render(self, surface):
		pass

	def update(self):
		pass