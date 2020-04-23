import pygame
import sys
import time
from random import randint
from pygame.sprite import Sprite
from bullet import Bullet
from spoiled_fruit import SpoiledFruit
from settings import Settings
from powerup import Powerup

def check_keydown(event, screen, game_settings, basket, bullets, pause):
	if event.key == pygame.K_RIGHT:
		basket.moving_right = True
	if event.key == pygame.K_LEFT: 
		basket.moving_left = True
	if event.key == pygame.K_SPACE:
		if len(bullets) < game_settings.allowed_bullets:
			new_bullet = Bullet(game_settings, screen, basket)
			bullets.add(new_bullet)
	elif event.key == pygame.K_p:
		game_settings.game_active = not game_settings.game_active
		pause_image = pause.render('Paused', True, (255, 255, 255))
		pause_image_rect = pause_image.get_rect()
		pause_image_rect.centerx = game_settings.screen_length / 2
		pause_image_rect.centery = game_settings.screen_height / 2
		screen.blit(pause_image, pause_image_rect)
			
def check_keyup(event, basket):
	if event.key == pygame.K_RIGHT:
		basket.moving_right = False
	if event.key == pygame.K_LEFT:
		basket.moving_left = False


def check_events(basket, bullets, screen, game_settings,
	restored_settings, play_button, play_again_button, spoiled_fruits, 
	ball, pause):
	"""Respond to keypresses in the game"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit() 
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_button(play_button, play_again_button, game_settings, 
				restored_settings, mouse_x, mouse_y, bullets,
					spoiled_fruits, screen, basket, ball)	
			
		elif event.type == pygame.KEYDOWN:
			check_keydown(event, screen, game_settings, basket, bullets, pause)

		elif event.type == pygame.KEYUP:
			check_keyup(event, basket)
				
				
def check_button(play_button, play_again_button, game_settings, 
	restored_settings, mouse_x, mouse_y, bullets, spoiled_fruits, 
	screen, basket, ball):
	if not game_settings.died_once:
		button_pressed = play_button.bg_color_rect.collidepoint(mouse_x, 
			mouse_y)
	else:
		button_pressed = play_again_button.bg_color_rect.collidepoint(mouse_x,
			mouse_y)
	if button_pressed and not game_settings.game_active:
		game_settings.game_active = True
		ball.rect.centery = randint(50, 150)
		ball.rect.centerx = randint(100, game_settings.screen_length-100)
		game_settings.reset_dynamic_settings()	
		
		bullets.empty()	
		spoiled_fruits.empty()
		basket.reposition()		
		

def check_ball_pos(ball, game_settings):
	if ball.rect.bottom >= game_settings.screen_height:
		game_settings.basket_lives -= 1
		ball.generate_random_pos()
		ball.draw_ball()

def check_catch(ball, game_settings, screen, collision_rect, powerup, basket):
	if pygame.Rect.colliderect(collision_rect, ball.rect):

		ball.generate_random_pos()
		ball.draw_ball()
		ball.rect.centerx = ball.randx
		ball.rect.centery = ball.randy
		game_settings.score += 1
		
		chance = randint(1,2) 
		if chance == 1: # Makes the game slowly go faster as you catch more. 
			game_settings.increase_speed()	
			
		if basket.powerup_active == False:
			powerup_chance = randint(1, 7)
			if powerup_chance == 1 and powerup.active == False:
				powerup.active = True
				powerup.generate_position()

def refresh_spoiled_fruit(spoiled_fruits, game_settings, screen, basket):
	if len(spoiled_fruits.sprites()) == 0:
		new_spoiled_fruit = SpoiledFruit(game_settings, screen, basket)
		spoiled_fruits.add(new_spoiled_fruit)
		new_spoiled_fruit.generate_random_pos()
		new_spoiled_fruit.draw_ball()	

def check_bullet_collisions(bullets, spoiled_fruit, spoiled_fruits, ball):
	for bullet in bullets.sprites():
		if pygame.Rect.colliderect(spoiled_fruit.rect, bullet.rect):
			chance = randint(1,2)
			if chance == 1:
				spoiled_fruits.remove(spoiled_fruit)
								
		if pygame.Rect.colliderect(ball.rect, bullet.rect):
			ball.shiverx()

def check_basket_hurt(game_settings, collision_rect, spoiled_fruit, basket):
	if basket.powerup_active == False:
		if pygame.Rect.colliderect(collision_rect, spoiled_fruit.rect):
			game_settings.basket_lives -= 1
			spoiled_fruit.generate_random_pos()
			spoiled_fruit.draw_ball()	
				
def spawn_spoiled_fruit(game_settings, screen, spoiled_fruit, spoiled_fruits, basket):
	if spoiled_fruit.rect.top >= game_settings.screen_height:
		spoiled_fruit.generate_random_pos()
		spoiled_fruit.draw_ball()
		if game_settings.spoiledfruit_chance >= 7:
			game_settings.spoiledfruit_chance -= 1
			
		if len(spoiled_fruits) <= 8:
			more_spoiled_fruit = randint(1, game_settings.spoiledfruit_chance)
			if more_spoiled_fruit in range(2, 3):
				pass
			elif more_spoiled_fruit == 1:
				spoiled_fruit = SpoiledFruit(game_settings, screen, basket)
				spoiled_fruit.generate_random_pos()
				spoiled_fruit.draw_ball()
				spoiled_fruits.add(spoiled_fruit)					

				
def check_spoiledfruit_collisions(ball, basket, game_settings, screen, 
	spoiled_fruit, bullets, spoiled_fruits):
	
	if basket.powerup_active:
		collision_rect = basket.rect
		collision_rect = collision_rect.inflate(0, -165)
	else:	
		collision_rect = basket.rect.inflate(0, -85)

	for spoiled_fruit in spoiled_fruits.sprites():
		
		spawn_spoiled_fruit(game_settings, screen, spoiled_fruit, 
			spoiled_fruits, basket)	
		
		check_basket_hurt(game_settings, collision_rect, spoiled_fruit, basket)
			
		check_bullet_collisions(bullets, spoiled_fruit, spoiled_fruits, ball)

def check_other_collisions(game_settings, screen, basket, ball,
	spoiled_fruits, powerup):

	if basket.powerup_active:
		collision_rect = basket.rect
		collision_rect = collision_rect.inflate(0, -165)
	else:	
		collision_rect = basket.rect.inflate(0, -85)
		
	refresh_spoiled_fruit(spoiled_fruits, game_settings, screen, basket)		
		
	check_catch(ball, game_settings, screen, collision_rect, powerup, basket)
			
	check_ball_pos(ball, game_settings)
	
	
def check_powerup_collisions(game_settings, screen, powerup, basket, bullets):
	
	if powerup.active:
		for bullet in bullets.sprites():
			if pygame.Rect.colliderect(powerup.rect, bullet.rect):
				basket.bigger_basket_powerup()
				powerup.active = False

					
						
def delete_old_bullets(bullets):
	for bullet in bullets.sprites().copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
def get_fps_get_lives(clock, fps_font, screen, game_settings, lives_font, score):
	current_fps = int(clock.get_fps()) #this computes the fps of the game by averaging the last ten calls to clock.tick() (averages). then it 10 is divided by that value to get the average fps. 
	fps_updater = fps_font.render(('FPS: ' + str(current_fps)), True, 
		(255, 255, 255,)) # first arg: text you want to render, second arg: True = smooth edges, False = not smooth edges, third arg: color of the text (black in this case), 4th (optional) arg: color for the text background. 
	lives_font_image = lives_font.render(('LIVES LEFT: ' + str(game_settings.basket_lives)), True, (255, 255, 255))
	fps_updater_rect = fps_updater.get_rect()
	lives_font_rect = lives_font_image.get_rect()
	fps_updater_rect.x = game_settings.fps_updater_x
	lives_font_rect.x = game_settings.lives_x
	fps_updater_rect.centery = game_settings.fps_updater_y
	lives_font_rect.y = game_settings.lives_y
	screen.blit(lives_font_image, lives_font_rect)
	screen.blit(fps_updater, fps_updater_rect)
	show_score(game_settings, screen, score)

def show_score(game_settings, screen, score):
	score_image = score.render(str(game_settings.score), True, (255, 255, 255))
	score_image_rect = score_image.get_rect()
	score_image_rect.centerx = game_settings.screen_length / 2 
	score_image_rect.top = 0
	screen.blit(score_image, score_image_rect)
		
def game_over_procedure(game_settings, screen, play_button, play_again_button):
	game_settings.died_once = True
	game_over = pygame.image.load('gameover.bmp')
	game_over_rect = game_over.get_rect()
	game_over_rect.centerx = game_settings.screen_length / 2
	game_over_rect.centery = (game_settings.screen_height / 2) - 50

	screen.fill(game_settings.end_color)
	screen.blit(game_over, game_over_rect)
	
	if not game_settings.died_once:
		play_button.draw_button()
	else:
		play_again_button.draw_button()
	game_settings.game_active = False
	
		
def check_game_assist(game_settings, ball, spoiled_fruits):
	if ball.rect.centery <= game_settings.screen_height/2 and len(spoiled_fruits) >= 4:
		ball.box = True
	else:
		ball.box = False

def get_relative_speed(fps_constant, current_fps, game_settings):
	rel_speeds = []
	rel_basket = (game_settings.basket_speed * fps_constant) / current_fps
	rel_speeds.append(rel_basket)
	rel_ball = (game_settings.ball_speed * fps_constant) / current_fps
	rel_speeds.append(rel_ball)
	rel_spoiled = (game_settings.spoiled_fruit_speed * fps_constant) / current_fps
	rel_speeds.append(rel_spoiled)
	rel_bullet = (game_settings.bullet_speed * fps_constant) / current_fps
	rel_speeds.append(rel_bullet)
	rel_powerup = (game_settings.powerup_speed * fps_constant) / current_fps
	rel_speeds.append(rel_powerup)
	return rel_speeds
	
def update_screen(screen, game_settings, basket, ball, clock, fps_font,
		lives_font, bullets, spoiled_fruit, spoiled_fruits, play_button, 
		play_again_button, powerup, score, fps_constant):
	"""Fill screen with bg color and draw all sprites and images"""
	clock.tick()
	
	screen.fill(game_settings.bg_color)
	get_fps_get_lives(clock, fps_font, screen, game_settings, lives_font, score)
	current_fps = int(clock.get_fps())
	rel_speeds = get_relative_speed(fps_constant, current_fps, game_settings)
	
	basket.update_basket(rel_speeds[0])
	ball.update(rel_speeds[1])
	spoiled_fruits.update(rel_speeds[2])
	bullets.update(rel_speeds[3])
	delete_old_bullets(bullets)
	powerup.update(rel_speeds[4])
	
	if game_settings.basket_lives <= 0:
		game_over_procedure(game_settings, screen, play_button, play_again_button)
		
		
	pygame.display.flip() 
	 #this updates the clock object we created. it computes how many milliseconds have passed since the previous call of this function. 
	# we an argument in this function and that will make the game run no higher than that number we put. ex): clock.tick(60) --> game won't run higher than 60 fps. 
	# this happens because the function purposely slows down just the right amount so the time between clock.tick() functions is greater so the fps is lowered to the adjusted value.
