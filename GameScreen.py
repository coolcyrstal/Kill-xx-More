import pygame
from pygame.locals import *

class GameScreen(object):

	def __init__(self, title, background_color, window_size = (1280,720), fps = 60):
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.background_color = background_color
		self.is_terminated = False
		self.BG = pygame.image.load("res/MenuScreen.png")

	#Initialize Screen
	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()

	def terminate(self):
		self.is_terminated = True

	def run(self):
		self.init()
		while not self.is_terminated:
			self.__handle_events()

			self.update()

			self.surface.fill(self.background_color)
			self.gameMenu()
			pygame.display.update()

			self.clock.tick(self.fps)

	def gameMenu(self):
		self.surface.blit(self.BG,(0,0))
		font = pygame.font.Font(None, 80)
		mygametext = font.render("Kill xx More", True, (255, 0, 0))
		textrect = mygametext.get_rect()
		textrect.centerx = self.surface.get_rect().centerx
		textrect.centery = self.surface.get_rect().centery - 150
		self.surface.blit(mygametext, textrect)
		font = pygame.font.Font(None, 40)
		menutext_start = font.render("1. Start Game", True, (255, 0, 0))
		menutext_how_to_play = font.render("2. How To Play", True, (255, 0, 0))
		menutext_Exit = font.render("3. Exit Game", True, (255, 0, 0))
		self.surface.blit(menutext_start, (textrect.centerx - 100, textrect.centery + 100))
		self.surface.blit(menutext_how_to_play, (textrect.centerx - 100, textrect.centery + 140))
		self.surface.blit(menutext_Exit, (textrect.centerx - 100, textrect.centery + 180))

	def init(self):
		self.__game_init()

	def render(self, surface):
		pass

	def update(self):
		pass