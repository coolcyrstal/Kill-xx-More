import pygame
from pygame.locals import *

class Enemy(object):

	def __init__(self, surface):
		self.alien_type = 1
		self.alien = pygame.image.load("res/alien" + str(self.alien_type) + ".png")
		self.surface = surface
		self.alien_posx = 1300
		self.alien_posy = 320

	def render(self):
		self.surface.blit(self.alien, (self.alien_posx, self.alien_posy))

	def move(self):
		if self.check_alien() == False:
			self.alien_posx -= 5

	def update(self):
		self.move()

	def check_alien(self):
		if self.alien_posx < 400:
			return True
		else:
			return False

	def warp(self):
		if self.check_alien() == True:
			self.alien_posx = 1300