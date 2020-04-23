import pygame
from settings import Settings
import game_functions as gf
from basket import Basket
from ball import Ball
from spoiled_fruit import SpoiledFruit
from time import sleep 
from bullet import Bullet
from pygame.sprite import Group
from play_button import PlayButton
from powerup import Powerup

def run_game():
	pygame.init()
	game_settings = Settings()
	restored_settings = Settings()
	
	screen = pygame.display.set_mode((game_settings.screen_length, game_settings.screen_height))
	pygame.display.set_caption("Catch It!")
	screen.fill((0, 160, 220))
	
	# Create basket object
	basket = Basket(screen, game_settings)
	
	# Create ball object, generate position, draw starting position
	ball = Ball(game_settings, screen, basket)
	ball.generate_random_pos()
	ball.draw_ball()
	bullets = Group()

	
	 # Create spoiled fruit object, generate position, draw starting position
	spoiled_fruits = Group()
	spoiled_fruit = SpoiledFruit(game_settings, screen, basket)
	spoiled_fruits.add(spoiled_fruit)
	spoiled_fruit.generate_random_pos()
	spoiled_fruit.draw_ball()
	
	powerup = Powerup(game_settings, screen)	
	
	# Create clock object to measure fps
	clock = pygame.time.Clock() # This creates a Clock object that is used to track time, with the other methods that come along with it. 
	pygame.font.init() # Initializes font module
	fps_font = pygame.font.Font(None, 30) # This creates a new font object that we will use to display the fps. 'None' just tells it to use the default pygame font, 30 is font size. 
	fps_constant = 150
	
	lives_font = pygame.font.Font(None, 30)
	play_button = PlayButton(screen, game_settings, 'Play!', 50, game_settings.screen_height/2)
	play_again_button = PlayButton(screen, game_settings, 'Play Again', 50, game_settings.screen_height-200)
	play_button.draw_button()
	pygame.display.flip() 
	
	# Score for how many good fruits are caught. 
	score = pygame.font.Font(None, 50)
	
	# Pause text when game is paused
	pause = pygame.font.Font(None, 100)
	
	
	while True:
		gf.check_events(basket, bullets, screen, game_settings, 
			restored_settings, play_button, play_again_button, 
			spoiled_fruits, ball, pause)
		if game_settings.game_active == False:	
			clock.tick()
	
		
		if game_settings.game_active:
			
			gf.check_spoiledfruit_collisions(ball, basket, game_settings,
				screen, spoiled_fruit, bullets, spoiled_fruits)
			
			gf.check_other_collisions(game_settings, screen, basket,
				ball, spoiled_fruits, powerup)
				
			gf.check_powerup_collisions(game_settings, screen, powerup, basket, bullets)
				
			gf.check_game_assist(game_settings, ball, spoiled_fruits)
			
			gf.update_screen(screen, game_settings, basket, ball, 
				clock, fps_font, lives_font, bullets, spoiled_fruit, 
				spoiled_fruits, play_button, play_again_button, powerup,
				score, fps_constant)
		else:
			pygame.display.flip()
				
run_game()
