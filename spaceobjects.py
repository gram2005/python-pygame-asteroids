import pygame
import math
import random

class Base_image():
    def __init__(self, image, x = 0, y = 0, v_x = 0, v_y = 0, angle = 0, angle_speed = 0):
        self.image = pygame.image.load(image).convert_alpha()
        self.display_image = self.image
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.angle = angle
        self.angle_speed = angle_speed
        self.position = [x, y]
        
    def update(self, alt = False):
        
        self.angle += self.angle_speed
        self.x += self.v_x
        self.y -= self.v_y        

        if 0 > self.x or self.x > 800:
            self.x = self.x % 800
        if 0 > self.y or self.y > 600:
                self.y = self.y % 600      

        if alt:        
            self.display_image = pygame.transform.rotozoom(self.image_alt, self.angle, 1)
        else:
            self.display_image = pygame.transform.rotozoom(self.image, self.angle, 1)
            
        self.obj_center = self.display_image.get_rect().center
        self.position = [self.x - self.obj_center[0], self.y - self.obj_center[1]]    
        
    def draw(self, screen):
        screen.blit(self.display_image, self.position)
        
        
class Ship(Base_image):
    def __init__(self, image, image_alt, x, y):
        self.image_alt = pygame.image.load(image_alt).convert_alpha()
        self.acc = 0
        self.moving = False
        Base_image.__init__(self, image, x, y)
        
    def set_angle_speed(self, value):
        self.angle_speed = value
        
    def get_angle(self):
        return self.angle
        
    def set_acc(self, value):
        self.acc = value
        
    def switch_state(self, value):
        self.moving = value
        
    def update(self):
        self.v_x = self.acc * math.cos(math.radians(self.angle))
        self.v_y = self.acc * math.sin(math.radians(self.angle))
        
        if not self.moving:
            Base_image.update(self)
        else:
            Base_image.update(self, True)        
                
        if not self.moving and self.acc > 0:
            self.acc -= 1.5/60
        elif self.acc < 0:
            self.acc = 0
        
       
class Asteroid (Base_image):
    def __init__(self, image):
        x = random.randrange(0, 800)
        y = random.randrange(0, 600)
        v_x = random.random()*6 - 3
        v_y = random.random()*6 - 3
        angle = random.randrange(0, 360)
        angle_speed = random.randrange(-10, 10)
        Base_image.__init__(self, image, x, y, v_x, v_y, angle, angle_speed)
