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

#images
bg = Base_image("bg_nebula_blue.png")
ship = Ship("ship1.png", "ship2.png", 400, 300)
aster = pygame.image.load("asteroid_blue.png").convert_alpha()

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

################################################################################    
    # drawing
    screen.fill(white)
    
    bg.draw(screen)
    ship.draw(screen)

    screen.blit(aster, [100, 100])

    pygame.display.flip()

################################################################################
    # clock
    clock.tick(60)
    
pygame.quit()