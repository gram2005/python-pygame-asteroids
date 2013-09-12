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

#default_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sprites'))

#pygame stuff
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Arto asteroidai")
clock = pygame.time.Clock()

ateroids_num = 10
aster_list = []
missile_list = []

#images
bg = Base_image("bg_nebula_blue.png")
ship = Ship("ship1.png", "ship2.png", 400, 300)
for x in range(ateroids_num):
    aster = Asteroid("asteroid_blue.png")
    aster_list.append(aster)


done = False


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
    
    ship.update()
    
    for aster in aster_list:
        aster.update()
        
    rem_missile_list = []    
    for mis in missile_list:
        if mis.is_alive():
            mis.update()
        else:
            rem_missile_list.append(mis)
            
    for mis in rem_missile_list:
        missile_list.remove(mis)


################################################################################    
    # drawing
    screen.fill(white)
    
    bg.draw(screen)
    ship.draw(screen)
    
    for aster in aster_list:
        aster.draw(screen)
        
    for mis in missile_list:
            mis.draw(screen)

    pygame.display.flip()

################################################################################
    # clock
    clock.tick(60)
    
pygame.quit()