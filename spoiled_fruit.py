import pygame

from ball import Ball

class SpoiledFruit(Ball):
	
	def __init__(self, game_settings, screen, basket):
		super().__init__(game_settings, screen, basket)
		self.apple = 'spoiled_apple.bmp'
		self.orange = 'spoiled_orange.bmp'
		self.pear = 'spoiled_pear.bmp'
		self.ball_speed = self.game_settings.spoiled_fruit_speed
		
