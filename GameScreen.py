import pygame
from pygame.locals import *

from Player import Player

class GameScreen(object):

	def __init__(self, title, background_color, window_size = (1280,720), fps = 60):
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.background_color = background_color
		self.quit_game = False
		self.gameMenu = True
		self.howToPlayMenu = False
		self.startGame = False
		self.menuScreenPic = pygame.image.load("res/MenuScreen.png")
		self.howToPlayPic = pygame.image.load("res/how to play.png")
		self.gamePlayBG = pygame.image.load("res/background.png")
		

	#Initialize Screen
	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)
		self.player = Player(self.surface)

	def terminate(self):
		self.quit_game = True

	def run(self):
		self.init()
		while not self.quit_game:
			self.__handle_events()
			self.surface.fill(self.background_color)
			self.gameMenuSelection()
			if self.startGame == True:
				self.player.render()
				self.player.update()

			pygame.display.update()
			self.clock.tick(self.fps)

	def gameMenuSelection(self):
		if self.gameMenu == True:
			self.gameMenu_Screen()

		if self.howToPlayMenu == True:
			self.howToPlay_Screen()

		if self.startGame == True:
			self.gamePlay()

		if pygame.key.get_pressed()[K_1]:
			self.gameMenu = False
			self.howToPlayMenu = False
			self.startGame = True

		if pygame.key.get_pressed()[K_2]:
			self.gameMenu = False
			self.howToPlayMenu = True
			self.startGame = False

		if pygame.key.get_pressed()[K_3]:
			self.terminate()

	def gameMenu_Screen(self):
		self.surface.blit(self.menuScreenPic,(0,0))
		font = pygame.font.Font(None, 80)
		mygametext = font.render("Kill xx More", True, (255, 0, 0))
		textrect = mygametext.get_rect()
		textrect.centerx = self.surface.get_rect().centerx
		textrect.centery = self.surface.get_rect().centery - 150
		self.surface.blit(mygametext, textrect)
		font = pygame.font.Font(None, 40)
		self.surface.blit(font.render("1. Start Game", True, (255, 0, 0)), (textrect.centerx - 100, textrect.centery + 100))
		self.surface.blit(font.render("2. Control System", True, (255, 0, 0)), (textrect.centerx - 100, textrect.centery + 140))
		self.surface.blit(font.render("3. Exit Game", True, (255, 0, 0)), (textrect.centerx - 100, textrect.centery + 180))

	def howToPlay_Screen(self):
		self.surface.blit(self.howToPlayPic,(0,0))
		font = pygame.font.Font(None, 64)
		howtoplaytext = font.render("Control System", True, (0, 255, 0))
		textrect = howtoplaytext.get_rect()
		textrect.centerx = self.surface.get_rect().centerx
		textrect.centery = self.surface.get_rect().centery - 150
		self.surface.blit(howtoplaytext, textrect)
		font = pygame.font.Font(None, 32)
		self.surface.blit(font.render("Button Z <-> X : rifle <-> gatling", True, (0, 255, 0)), (500, 400))

	def gamePlay(self):
		self.surface.blit(self.gamePlayBG,(0,0))

	def init(self):
		self.__game_init()

	def render(self, surface):
		pass

	def update(self):
		print "hello"
		self.player.update()

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()

