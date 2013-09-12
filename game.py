import pygame
import os
import math

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

#images
#bg = pygame.image.load("bg_nebula_blue.png").convert_alpha()
ship_no_ac = pygame.image.load("ship1.png").convert_alpha()
ship_ac = pygame.image.load("ship2.png").convert_alpha()
aster = pygame.image.load("asteroid_blue.png").convert_alpha()

#init variables
x = 400
y = 300
ship_x = x
ship_y = y
angle = 0
v_x = 0
v_y = 0
acc = 0
angle_speed = 0
ship = ship_no_ac
o_ship = ship
moving = False

done = False
class baseImage():
    def __init__(self, x = 0, y = 0):
        self.imgage = pygame.image.load("bg_nebula_blue.png").convert_alpha()
        self.position = [x, y]
        
    def draw(self, screen):
        screen.blit(self.imgage, self.position)
        
#class Asteroid(x, y, v_x, v_y, angle_speed):
    #def __init__():
        #self.image = pygame.image.load("asteroid_blue.png").convert_alpha()
        #self.angle = 0
        #self.angle_speed = angle_speed
        #self.v_x = v_x
        #self.v_y = v_y
        #self.position = [x, y]
        #pass
    #def update():
        #self.angle += self.angle_speed
        #self.position = [self.position[0] + self.v_x, self.position[1] + self.v_y]
    #def draw():
        #pass
bg = baseImage(0, 0)
################################################################################    
while done == False:
    # event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle_speed = 5
                #x_speed = -3
                o_ship = ship_ac
            if event.key == pygame.K_RIGHT:
                angle_speed = -5 
                o_ship = ship_ac
            if event.key == pygame.K_UP:
                acc = 5
                o_ship = ship_ac
                moving = True

              
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                angle_speed = 0 
                o_ship = ship_no_ac
            if event.key == pygame.K_RIGHT:
                angle_speed = 0 
                o_ship = ship_no_ac
            if event.key == pygame.K_UP:
                moving = False
                o_ship = ship_no_ac
                
################################################################################        
    # game logic
    angle += angle_speed
    v_x = acc * math.cos(math.radians(angle))
    #print(angle, math.radians(angle), math.sin(math.radians(angle)), acc)
    v_y = acc * math.sin(math.radians(angle))
    ship_x += v_x
    ship_y -= v_y
    if 0 > ship_x or ship_x > 800:
        ship_x = ship_x % 800
    if 0 > ship_y or ship_y > 600:
            ship_y = ship_y % 600    
    if not moving and acc > 0:
        acc -= 1.5/60
    elif acc < 0:
        acc = 0    
    
    
    ship = pygame.transform.rotozoom(o_ship, angle, 1)
    ship_center = ship.get_rect().center


################################################################################    
    # drawing
    screen.fill(white)
    
    #screen.blit(bg, [0,0])
    bg.draw(screen)
    screen.blit(ship, [ship_x - ship_center[0],ship_y - ship_center[1]])
    screen.blit(aster, [100, 100])

    pygame.display.flip()

################################################################################
    # clock
    clock.tick(60)
    
pygame.quit()