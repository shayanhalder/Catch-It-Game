import pygame

class Bullet(pygame.sprite.Sprite):
	""" A class for bullets launched by the basket"""
	def __init__(self, game_settings, screen, basket):
		"""Initialize all the bullet attributes from settings and draw the bullet circle in the center of the basket"""
		super().__init__() # this calls pygame.sprite.Sprite and sets it equal to the name of the instance created of this class, which just creates a game object for managing a single bullet sprite. 
		
		self.game_settings = game_settings
		self.screen = screen
		self.basket = basket
		self.color = game_settings.bullet_color
		self.radius = game_settings.bullet_radius
		self.speed_factor = game_settings.bullet_speed
		self.spawnx = self.basket.rect.centerx
		self.rect = pygame.draw.circle(self.screen, self.color, (self.spawnx, self.basket.rect.centery), self.radius)
		self.y = float(self.rect.centery)
		
	def update(self, rel_speed):
		""" Move the bullet up """
		self.y -= rel_speed
		self.rect.centery = self.y
		pygame.draw.circle(self.screen, self.color, (self.spawnx, self.rect.centery), self.radius)
			
		
		
		
		
	
