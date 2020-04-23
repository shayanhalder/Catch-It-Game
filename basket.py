import pygame

import time

class Basket():
		
	def __init__(self, screen, game_settings):
		
		self.screen = screen
		self.game_settings = game_settings
		
		self.image = pygame.image.load('basket.bmp')
		self.image = pygame.transform.scale(self.image, (74, 77))
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		self.moving_right = False
		self.moving_left = False
		self.powerup_active = False
		
		
	def update_basket(self, rel_speed):
		if self.moving_left and self.rect.left > 0:
			self.centerx -= rel_speed
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += rel_speed
			
			
		if self.powerup_active:
			now = time.time()
			if now >= self.t_end:
				self.image = pygame.transform.scale(self.image, (74, 77))
				self.powerup_active = False
				self.rect = self.image.get_rect()
				self.centery += 42
				self.game_settings.bullet_radius -= 15
			
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
		self.screen.blit(self.image, self.rect)
		
	def reposition(self):
		self.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def bigger_basket_powerup(self):
		self.t_end = time.time() + 15
		self.powerup_active = True
		self.image = pygame.transform.scale(self.image, (148, 154))
		self.game_settings.bullet_radius += 15
		self.rect = self.image.get_rect()
		self.centery -= 42
		
