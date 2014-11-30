import pygame
from pygame.locals import *

class Enemy(object):

	def __init__(self):
		self.alien_type = 1
		self.alien = pygame.image.load("res/alien" + str(self.alien_type) + ".png")