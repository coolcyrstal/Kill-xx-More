import pygame
from pygame.locals import *

from Bullet import Bullet

class Player(object):

	def __init__(self, surface):
		self.gun_type = 1
		self.player = pygame.image.load("res/player gunner" + str(self.gun_type) + ".png")
		self.bullet = Bullet(surface, self.gun_type)
		self.surface = surface
		self.player_posx = 100
		self.player_posy = 400
		self.check_change_gun = 1
		self.check = False
		self.fire_bullet = False
		self.bullet_posx = 480
		

	def render(self):
		self.surface.blit(self.player,(self.player_posx, 720 - self.player_posy))
		if self.check == True:
			self.player = pygame.image.load("res/player gunner" + str(self.gun_type) + ".png")
		

	def change_weapon(self):
		if pygame.key.get_pressed()[K_z]:
			self.gun_type = 1
		if pygame.key.get_pressed()[K_x]:
			self.gun_type = 2

	def update(self):
		self.change_weapon()
		if self.check_change_gun != self.gun_type:
			self.check = True
			self.check_change_gun = self.gun_type
		else:
			self.check = False
		self.fire()
		self.bullet_posx = self.bullet.bullet_posx
		

	def fire(self):
		if pygame.key.get_pressed()[K_SPACE]:
			self.fire_bullet = True

		if self.fire_bullet == True:
			self.bullet.render()
			self.bullet.move()
		else:
			self.bullet.bullet_posx = 480

		if self.bullet.check_bullet() == True:
			self.fire_bullet = False