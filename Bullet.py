import pygame
from pygame.locals import *

from enemy import Enemy

class Bullet(object):

	def __init__(self, surface, bullet_type):
		self.bullet = pygame.image.load("res/bullet" + str(bullet_type) + ".png")
		self.surface = surface
		self.bullet_posx = 480
		self.bullet_posy = 415
		self.alien = Enemy(self.surface)

	def render(self):
		self.surface.blit(self.bullet, (self.bullet_posx, self.bullet_posy))

	def move(self):
		self.bullet_posx += 50

	def check_bullet(self):
		if self.bullet_posx >= 1280:
			return True
		else:
			return False

	def check_fire_alien(self):
		if (self.bullet_posx <= self.alien.get_alien_posx() + 2) or (self.bullet_posx >= self.alien.get_alien_posx() - 2):
			return True
		else:
			return False
