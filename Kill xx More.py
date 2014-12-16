import pygame
from pygame.locals import *

import GameScreen

class Kill_xx_More_Game(GameScreen.GameScreen):
	BLACK = pygame.Color('black')

	def __init__(self):
		super(Kill_xx_More_Game, self).__init__('Kill_xx_More', Kill_xx_More_Game.BLACK)

	def init(self):
		super(Kill_xx_More_Game, self).init()

	def render(self, surface):
		pass

	def update(self):
		pass

def main():
    game = Kill_xx_More_Game()
    game.run()

if __name__ == '__main__': 
    main()