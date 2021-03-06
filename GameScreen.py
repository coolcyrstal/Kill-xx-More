import pygame
from pygame.locals import *

from Player import Player
from enemy import Enemy

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
		self.gameOverPic = pygame.image.load("res/gameover.png")
		self.score = 0
		self.hp_player = 7
		self.hp_player_pic = pygame.image.load("res/hp_player" + str(self.hp_player) + ".png")

	#Initialize Screen
	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)
		self.player = Player(self.surface)
		self.enemy = Enemy(self.surface)

	def terminate(self):
		self.quit_game = True

	#Run Game Screen
	def run(self):
		self.init()
		while not self.quit_game:
			self.__handle_events()
			self.surface.fill(self.background_color)
			self.gameMenuSelection()
			if self.startGame == True:
				self.show_ETC()
				self.player.update()
				self.enemy.update()
				self.damage()
				self.check_gameOver()

			pygame.display.update()
			self.clock.tick(self.fps)

	def show_ETC(self):
		self.player.render()
		self.enemy.render()
		self.score_Show()

	def damage(self):
		if self.enemy.check_alien() == True:
			self.hp_player -= 1
			self.enemy.warp()
			self.hp_player_pic = pygame.image.load("res/hp_player" + str(self.hp_player) + ".png")

	def check_gameOver(self):
		if self.hp_player <= 0:
			self.hp_player = 0
			self.gameOverState()


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
		self.surface.blit(font.render("Button Z <-> X : rifle <-> gatling", True, (0, 255, 0)), (textrect.centerx - 150, textrect.centery + 100))
		self.surface.blit(font.render("Button Spacebar : fire", True, (0, 255, 0)), (textrect.centerx - 150, textrect.centery + 140))

	def gameOverState(self):
		self.surface.blit(self.gameOverPic,(0,0))

	def gamePlay(self):
		self.surface.blit(self.gamePlayBG,(0,0))
		self.surface.blit(self.hp_player_pic, (50, 20))

	def score_Show(self):
		font = pygame.font.Font(None, 32)
		self.fire_True()
		score_render = font.render("score : " + str(self.score), True, (255, 0, 0))
		self.surface.blit(score_render, (1000, 50))
		

	def fire_True(self):
		if self.check_fire_alien():
			self.fire_bullet = False
			self.score += 50

	def check_fire_alien(self):
		if (self.player.bullet_posx + 50 <= self.enemy.alien_posx + 50) and (self.player.bullet_posx + 25 >= self.enemy.alien_posx):
			#self.enemy.alien_posx += 25
			return True
		else:
			return False

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

