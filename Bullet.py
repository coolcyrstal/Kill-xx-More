import pygame
from pygame.locals import *

class Bullet(object):

	def __init__(self, surface, bullet_type):
		self.bullet = pygame.image.load("res/bullet" + str(bullet_type) + ".png")
		self.surface = surface
		self.bullet_posx = 480
		self.bullet_posy = 415

	def render(self):
		self.surface.blit(self.bullet, (self.bullet_posx, self.bullet_posy))

	def move(self):
		self.bullet_posx += 50

	def check_bullet(self):
		if self.bullet_posx >= 1280:
			return True
		else:
			return False