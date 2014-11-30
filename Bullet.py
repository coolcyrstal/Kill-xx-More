import pygame
from pygame.locals import *

class Bullet(object):

	def __init__(self, surface, bullet_type):
		self.bullet = pygame.image.load("res/bullet" + str(bullet_type) + ".png")
		self.surface = surface
		self.bullet_posx = 500
		self.bullet_posy = 320

	def render(self):
		self.surface.blit(self.bullet, (self.bullet_posx, self.bullet_posy))

	def move(self):
		self.bullet_posx += 5

	def check(self):
		