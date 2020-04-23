import pygame

class PlayButton():
	
	def __init__(self, screen, game_settings, text, size, initialy):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.game_settings = game_settings
		self.width = self.game_settings.button_width
		self.height = self.game_settings.button_height
		self.initialy = initialy
		
		self.text = text
		self.size = size
		self.pic = 'playagain.bmp'
		self.bg_color = pygame.image.load(self.pic)
		self.bg_color = pygame.transform.scale(self.bg_color, (450, 250))
		self.bg_color_rect = self.bg_color.get_rect()
		self.bg_color_rect.centerx = self.screen_rect.centerx
		self.bg_color_rect.centery = self.initialy
		
		self.button = pygame.font.Font(None, self.size)
		
		self.button_rect = pygame.Rect(0, 0, self.width, self.height)
		
		self.button_msg = self.button.render(self.text, True, (50, 50, 220))
		self.button_msg_rect = self.button_msg.get_rect()
		self.button_msg_rect.center = self.bg_color_rect.center
		
	def draw_button(self):
		self.screen.blit(self.bg_color, self.bg_color_rect)
		self.screen.blit(self.button_msg, self.button_msg_rect)
		
		
		
