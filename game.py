import pygame
import os
import math
from spaceobjects import *

pygame.init()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
num_of_lifes = 3
score = 0

#default_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sprites'))

#pygame stuff
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Arto asteroidai")
clock = pygame.time.Clock()
basicFont = pygame.font.SysFont(None, 42)

max_num_of_ateroids = 10
asteroid_list = []
missile_list = []
ateroid_timer = 0
done = False

#images
bg = Base_image("bg_nebula_blue.png")
ship = Ship("ship1.png", "ship2.png", 400, 300)
for x in range(max_num_of_ateroids):
    asteroid = Asteroid("asteroid_blue.png")
    asteroid_list.append(asteroid)





################################################################################    
while done == False:
    # event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.set_angle_speed(5)
                ship.switch_state(True)
            if event.key == pygame.K_RIGHT:
                ship.set_angle_speed(-5)
                ship.switch_state(True)
            if event.key == pygame.K_UP:
                ship.set_acc(5)
                ship.switch_state(True)
            if event.key == pygame.K_SPACE:
                x, y = ship.get_missile_coord()
                v_x, v_y = ship.get_missile_speed()
                missile_list.append(Missile("shot2.png", x, y, v_x, v_y))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.set_angle_speed(0)
                ship.switch_state(False)
            if event.key == pygame.K_RIGHT:
                ship.set_angle_speed(0)
                ship.switch_state(False)
            if event.key == pygame.K_UP:
                ship.switch_state(False)
                
################################################################################        
    # game logic

    rem_asteroid_list = []
    rem_missile_list = []
    for asteroid in asteroid_list:
        for missile in missile_list:
            if missile.check_collision(asteroid):
                rem_missile_list.append(missile)
                rem_asteroid_list.append(asteroid)
                score += 1010

        if ship.check_collision(asteroid):
            rem_asteroid_list.append(asteroid)
            num_of_lifes -= 1
            
    for missile in rem_missile_list:
        try:
            missile_list.remove(missile)
        except:
            pass

    for asteroid in rem_asteroid_list:
        try:
            asteroid_list.remove(asteroid)
        except:
            pass
        
    rem_missile_list = []
    for missile in missile_list:
        if missile.is_alive():
            missile.update()
        else:
            rem_missile_list.append(missile)

    for missile in rem_missile_list:
        try:
            missile_list.remove(missile)
        except:
            pass
        
    ship.update()

    if len(asteroid_list) < max_num_of_ateroids:
        ateroid_timer += 1

    if ateroid_timer == 60:
        asteroid = Asteroid("asteroid_blue.png")
        asteroid_list.append(asteroid)
        ateroid_timer = 0
    
    for asteroid in asteroid_list:
        asteroid.update()

    life_text = basicFont.render('Lifes: ' + str(num_of_lifes), True, white)
    score_text = basicFont.render('Score: ' + str(score), True, white)


################################################################################    
    # drawing
    screen.fill(white)
    
    bg.draw(screen)
    ship.draw(screen)
    
    for asteroid in asteroid_list:
        asteroid.draw(screen)
        
    for missile in missile_list:
            missile.draw(screen)

    screen.blit(life_text, (688,10))
    screen.blit(score_text, (10,10))

    pygame.display.flip()

################################################################################
    # clock
    clock.tick(60)
    
pygame.quit()
