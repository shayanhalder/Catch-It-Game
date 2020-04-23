import pygame

from random import randint

class Ball(pygame.sprite.Sprite):
	def __init__(self, game_settings, screen, basket):
		super().__init__() #creates instance of pygame.sprite.Sprite, which can be added to a Group. 
		self.screen = screen
		self.game_settings = game_settings
		self.basket = basket
		self.apple = 'apple.bmp'
		self.orange = 'orange.bmp'
		self.pear = 'pear.bmp'
		self.ball_speed = self.game_settings.ball_speed 
		self.box = False
		
		
	def generate_random_pos(self):
		self.randy = randint(50, 70)			
		self.ball_time = (self.game_settings.screen_height - self.randy)/(float(self.ball_speed))
		self.max_basket_distance = float(self.game_settings.basket_speed) * self.ball_time
		self.randx1 = int(self.basket.rect.centerx - self.max_basket_distance) + 50
		self.randx2 = int(self.basket.rect.centerx + self.max_basket_distance) - 50
		if self.randx1 <= 0:
			self.randx1 += abs(65-self.randx1)
		if self.randx2 >= self.game_settings.screen_length:
			self.randx2 -= abs((self.game_settings.screen_length-65)-self.randx2)
		self.randx = randint(self.randx1, self.randx2)
		if self.randx in range(self.basket.rect.centerx-90, self.basket.rect.centerx+90):
			self.randx = self.basket.rect.centerx + randint(-150, 150)
			
		self.image_chance = randint(1, 3)	
		
	def draw_ball(self): 
		if self.image_chance == 1:
			self.apple_image = pygame.image.load(self.apple)
			self.scalex = 50
			self.scaley = 50
			self.apple_image = pygame.transform.scale(self.apple_image, (self.scalex, self.scaley))
			self.rect = self.apple_image.get_rect()
			self.rect.x = self.randx
			self.rect.y = self.randy
			self.y = float(self.rect.centery)
			
		elif self.image_chance == 2:
			self.orange_image = pygame.image.load(self.orange)
			self.scalex = 50
			self.scaley = 57
			self.orange_image = pygame.transform.scale(self.orange_image, (self.scalex, self.scaley))
			self.rect = self.orange_image.get_rect()
			self.rect.x = self.randx
			self.rect.y = self.randy
			self.y = float(self.rect.centery)
		else:
			self.pear_image = pygame.image.load(self.pear)
			self.scalex = 50
			self.scaley = 70
			self.pear_image = pygame.transform.scale(self.pear_image, (self.scalex, self.scaley))
			self.rect = self.pear_image.get_rect()
			self.rect.x = self.randx
			self.rect.y = self.randy	
			self.y = float(self.rect.centery)
			
	def draw_lines(self):
		pygame.draw.line(self.screen, (50,50,255), (self.rect.x, self.rect.y), (self.rect.x + self.scalex, self.rect.y), 3)
		pygame.draw.line(self.screen, (50,50,255), (self.rect.x, self.rect.y + self.scaley), (self.rect.x + self.scalex, self.rect.y + self.scaley), 3)
		pygame.draw.line(self.screen, (50,50,255), (self.rect.x, self.rect.y), (self.rect.x, self.rect.y + self.scaley), 3)
		pygame.draw.line(self.screen, (50,50,255), (self.rect.x + self.scalex, self.rect.y), (self.rect.x + self.scalex, self.rect.y + self.scaley), 3)
		
			
	def update(self, rel_speed):
		if self.image_chance == 1:
			self.y += rel_speed
			self.rect.centery = self.y
			self.screen.blit(self.apple_image, self.rect)
			if self.box:
				self.draw_lines()
				
		elif self.image_chance == 2:
			self.y += rel_speed
			self.rect.centery = self.y
			self.screen.blit(self.orange_image, self.rect)
			if self.box:
				self.draw_lines()
		else:
			self.y += rel_speed
			self.rect.centery = self.y
			self.screen.blit(self.pear_image, self.rect)
			if self.box:
				self.draw_lines()
			
	def shiverx(self):
		x_change = 10
		if self.game_settings.ball_speed >= 3:
			x_change = 50
		for x in range(9):
			self.rect.centerx += x_change* self.game_settings.shiverconstant
			self.game_settings.shiverconstant *= -1
	
			
