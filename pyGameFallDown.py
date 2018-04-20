import pygame
import sys
import random
import math

pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
done = False
is_blue = True
x = 30
y = 30
plat_x = 0

hole_size = 60
score = 0
spawn = 0
period = 200
plats_list = []
plat_ys_list = []
holes_list = []

clock = pygame.time.Clock()

pygame.font.init()

myfont = pygame.font.SysFont("Comic Sans MS", 20)
score_text = myfont.render("Score: " + str(score), False, (255, 255, 255))

def plat_create(): #Plat creator
        hole_rand = random.randint(0, 300)
        plat_y = height + 20
        hole = pygame.Rect(plat_x + hole_rand, plat_y, hole_size, 10)
        plat = pygame.Rect(plat_x, plat_y, width, 10)
        singles_list = [hole, plat, hole_rand, plat_y]
        return singles_list

def plat_update(h, p): #Plat drawer
        #singles_list = plat_create()
        plat = pygame.draw.rect(screen, (250, 0, 0), p)
        hole = pygame.draw.rect(screen, (0, 0, 0), h)
        
        
        #We need to return the values hole, plat, and plat_y while  still making them usable.
        #Rethunk. Solve please.
        
plats_list.append(plat_create())

while not done:
        for event in pygame.event.get(): #Event updater
                if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed() #Key presser
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        if period < 60:
                if period <= spawn: #Platform spawner
                        plats_list.append(plat_create())
                        period = 200 - 5*math.sqrt(score)
        elif period >= 60:
                if period <= spawn: #Platform spawner
                        plats_list.append(plat_create())

        y += 1.5
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255) #Color checker
        else: color = (255, 100, 0)

        player = pygame.Rect(x, y, 20, 20)

        for plat in plats_list: #Plat updater
                plat_update(plat[0], plat[1])
                plat[1].move_ip(0,-1)
                plat[0].move_ip(0,-1)
                if player.colliderect(plat[0]): #Collision detector
                        y += 0
                        score += 1
                        score_text = myfont.render("Score: " + str(score), False, (255, 255, 255))
                elif player.colliderect(plat[1]):
                        y -= 2.5

        if x > width + 5:
                player.move_ip(-width - 5, y)
        elif y > height:
                y -= 5

        player_draw = pygame.draw.rect(screen, color, player) #Player drawer
        screen.blit(score_text, (0,0))
        
        period -= 1 #Timer updater

        pygame.display.flip() #Ya mama dear, that's what I learned in this school, boom boom.
        clock.tick(60)
