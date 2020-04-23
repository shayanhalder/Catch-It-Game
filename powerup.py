import pygame

from random import randint

import time

class Powerup():
	def __init__(self, game_settings, screen):
		self.game_settings = game_settings
		self.screen = screen
		self.image = pygame.image.load('powerup.bmp')
		self.image = pygame.transform.scale(self.image, (50, 32))
		self.rect = self.image.get_rect()
		self.moving_right = True
		self.active = False
		self.cycles = 0
		
	def generate_position(self):
		self.cycles = 0
		
		if self.active:
			if self.game_settings.powerup_direction == 1:
				self.randx = 0
				self.moving_right = True
			else:
				self.randx = self.game_settings.screen_length
				self.moving_right = False
			
			self.randy = randint(50, 70)
			self.rect.centerx, self.rect.centery = self.randx, self.randy
		self.x = float(self.rect.centerx)

		
	def update(self, rel_speed):
		if self.active:
			self.x += rel_speed * self.game_settings.powerup_direction

			self.rect.centerx = self.x
		
		if self.rect.centerx <= 0 or self.rect.centerx >= self.game_settings.screen_length:
			self.cycles += 1
			self.game_settings.powerup_direction *= -1
		
		if self.cycles == 4:
			self.active = False
			self.moving_right = not self.moving_right
			self.game_settings.powerup_direction *= -1
			self.cycles = 0
			self.generate_position()
			
		if self.active: 
			self.screen.blit(self.image, self.rect)
			
		
			
		
		
		
		
		
		
