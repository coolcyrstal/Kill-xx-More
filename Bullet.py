import pygame
from pygame.locals import *

class Bullet(object):

	def __init__(self):
		self.bullet = pygame.image.load("res/player gunner.png")
		self.surface = surface