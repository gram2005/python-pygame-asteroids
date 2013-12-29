import pygame
from spaceobjects import *

pygame.init()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

#pygame stuff
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Arto asteroidai")
clock = pygame.time.Clock()
basic_font = pygame.font.SysFont(None, 42)
game_over_font = pygame.font.SysFont(None, 60)

game_state = 'not started'
done = False

#images
background = Base_image("bg_nebula_blue.png")

 ################################################################################
while not done:
    # event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if game_state in ['not started', 'game over']:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = 'started'

        if game_state == 'running':
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

    if game_state in ['not started', 'game over']:
        start_text1 = basic_font.render('PRESS ENTER', True, white)
        start_text2 = basic_font.render('TO START THE GAME', True, white)

    if game_state == 'started':
        max_num_of_asteroids = 10
        asteroid_list = []
        missile_list = []
        asteroid_timer = 0
        num_of_lives = 3
        score = 0

        ship = Ship("ship1.png", "ship2.png", 400, 300)
        for x in range(max_num_of_asteroids):
            asteroid = Asteroid("asteroid_blue.png")
            asteroid_list.append(asteroid)
        game_state = 'running'

    if game_state == 'running':
        rem_asteroid_list = []
        rem_missile_list = []
        for asteroid in asteroid_list:
            for missile in missile_list:
                if missile.check_collision(asteroid):
                    rem_missile_list.append(missile)
                    rem_asteroid_list.append(asteroid)
                    score += 10

            if ship.check_collision(asteroid):
                rem_asteroid_list.append(asteroid)
                num_of_lives -= 1
                if num_of_lives == 0:
                    game_state = 'game over'

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

        if len(asteroid_list) < max_num_of_asteroids:
            asteroid_timer += 1

        if asteroid_timer == 60:
            asteroid = Asteroid("asteroid_blue.png")
            asteroid_list.append(asteroid)
            asteroid_timer = 0

        for asteroid in asteroid_list:
            asteroid.update()

        life_text = basic_font.render('Lives: ' + str(num_of_lives), True, white)
        score_text = basic_font.render('Score: ' + str(score), True, white)

    if game_state == 'game over':
        game_over_text = game_over_font.render('GAME OVER', True, white)

 ################################################################################
    # drawing
    screen.fill(white)
    
    background.draw(screen)

    if game_state in ['not started', 'game over']:
        pygame.draw.rect(screen, white, (200,100,400,400), 10)
        screen.blit(start_text1, (295,250))
        screen.blit(start_text2, (250,330))

    if game_state == 'running':
        ship.draw(screen)
    
        for asteroid in asteroid_list:
            asteroid.draw(screen)

        for missile in missile_list:
                missile.draw(screen)

        screen.blit(life_text, (688,10))
        screen.blit(score_text, (10,10))

    if game_state == 'game over':
        screen.blit(game_over_text, (275,170))


    pygame.display.flip()

 ################################################################################
    # clock
    clock.tick(60)
    
pygame.quit()
