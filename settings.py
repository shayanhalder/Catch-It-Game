class Settings():
	def __init__(self):
		
		# game active flag
		self.game_active = False
		self.died_once = False
		self.reset_dynamic_settings()
		
		# screen settings
		self.screen_height = 800
		self.screen_length = 1200
		self.bg_color = 0, 0, 0
		self.end_color = 0, 160, 220		
		
		# ball settings
		
		self.ball_speed_constant = 0
		self.ball_radius = 30 
		self.shiverx_speed = 1
		self.shiverconstant = -1
		
		# spoiled fruit settings
		
		self.spoiledfruit_chance = 25
		
		# bullet settings
		self.bullet_color = 255, 255, 255 
		self.allowed_bullets = 1
		
		# fps updater location/settings
		self.fps_updater_x = 5
		self.fps_updater_y = 15
		self.fps_bgcolor = (213, 255, 0)
		
		# lives settings
		self.lives_bgcolor = (255, 255, 255)
		self.lives_x = self.screen_length - 150
		self.lives_y = 10
		
		# play button settings
		self.button_width = 450
		self.button_height = 250
		self.button_text_size = 100
		
		# powerup settings
		self.powerup_speed = 3
		self.powerup_direction = 1
		
	def reset_dynamic_settings(self):
		self.basket_lives = 20
		self.spoiled_fruit_speed = 1.2
		self.bullet_radius = 15
		self.ball_speed = 0.7
		self.ball_speed_constant = 0
		self.spoiledfruit_chance = 25
		self.basket_speed = 1
		self.speedscaleup = 1.1
		self.bullet_speed = 2.5
		self.score = 0
		
	def increase_speed(self):
		if self.ball_speed <= 3.2:
			self.ball_speed *= self.speedscaleup
		if self.basket_speed <= 3.0:
			self.basket_speed *= self.speedscaleup
		if self.spoiled_fruit_speed <= 4.2:
			self.spoiled_fruit_speed *= self.speedscaleup
		if self.bullet_speed <= 5.5:
			self.bullet_speed *= (self.speedscaleup-0.05)
		


