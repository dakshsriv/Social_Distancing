#!/usr/bin/python3

import pygame, random, time

pygame.init()

myfont = pygame.font.Font(None, 35)
screen = pygame.display.set_mode((1070, 720))

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

x1 = 0
x2 = 950
Trackline_for_y = 310

screen_width = 1028
screen_height = 720

done = False
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(white)
        r1 = pygame.draw.rect(screen, red, (x1, Trackline_for_y, 70, 70))
        r2 = pygame.draw.rect(screen, blue, (x2, Trackline_for_y, 70, 70))
        text1 = myfont.render("Wise decision people, you should social distance.", 1, blue)
        if x2 - x1 > 150:
                x1 = x1 + random.randint(0, 4)
                x2 = x2 - random.randint(0, 4)
        print(x2 - x1)
        if x2 - x1 <= 150:
                print("*")
                v = random.randint(1,2)
                if v == 1:             #####################################  Make sure that the rectangle moves and THEN blits the wise_decision_msg ####################################################
                        x1 = x2 - 200
                else:
                        x2 = x1 + 200
#                print("*#*")
                now = time.time()
                later = time.time()
                while int((later - now).total_seconds() < 2):
                        print("*#*#*")       
                        print(time.time())
                        screen.blit(text1, (400, 10))
                        pygame.display.update()
        pygame.display.update()
        clock.tick(60)
"""
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        if x2 - x1 == 200:
                screen.blit(text1, (400, 10))
"""