#!/usr/bin/python3

import pygame, random, time

pygame.init()

myfont = pygame.font.Font(None, 35)
screen = pygame.display.set_mode((1070, 720))

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

x1 = 0
x2 = 950
Trackline_for_y = 310

screen_width = 1028
screen_height = 720

done = False
clock = pygame.time.Clock()

do_blit = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        do_blit = False
        screen.fill(white)
        wise_decision_msg = myfont.render("Wise decision people, you should social distance.", 1, green)
        trouble_msg = myfont.render("Trouble! Trouble! You guys are too close to each other. ", 1, red)
        if x2 - x1 > 150:
                x1 = x1 + random.randint(0, 4)
                x2 = x2 - random.randint(0, 4)
        print(x2 - x1)
        if x2 - x1 <= 200 and x2 - x1 > 150:
                now = time.time()
                later = time.time()
                while later - now < 0.03:
#                        print("*#*#*")
                        print(time.time())
                        screen.blit(trouble_msg, (10, 400))
                        later = time.time()
        elif x2 - x1 <= 150:
                time.sleep(1)
                print("*")
                v = random.randint(1,2)
                if v == 1:
                        x1 = x2 - 550
                        """rect_red = pygame.draw.rect(screen, red, (x1, Trackline_for_y, 70, 70))
                        rect_blue = pygame.draw.rect(screen, blue, (x2, Trackline_for_y, 70, 70))"""
                        #pygame.display.update()
                        #print()
                        #rect_red = pygame.draw.rect(screen, white, (x1, Trackline_for_y, 70, 70))
                        #x2 = x1 + 250
                else:
                        x2 = x1 + 550
                        """rect_red = pygame.draw.rect(screen, red, (x1, Trackline_for_y, 70, 70))
                        rect_blue = pygame.draw.rect(screen, blue, (x2, Trackline_for_y, 70, 70))
                        pygame.display.update()"""
                        #rect_blue = pygame.draw.rect(screen, white, (x2, Trackline_for_y, 70, 70))
                        #x1 = x2 - 250
                do_blit = True
#                print("*#*")
#                print(x1,"\*/", x2)
                # -------------------------------------------
#                pygame.display.update()
        rect_red = pygame.draw.rect(screen, red, (x1, Trackline_for_y, 70, 70))
        rect_blue = pygame.draw.rect(screen, blue, (x2, Trackline_for_y, 70, 70))
        pygame.display.update()
        clock.tick(60)
        #pritn()
        if do_blit:
                now = time.time()
                later = time.time()
                while later - now < 2:
                        #print("*#*#*")
                        #print(time.time())
                        screen.blit(wise_decision_msg, (400, 10))
                        #print("time difference is: ", later - now)
                        later = time.time()
                        pygame.display.update()
"""
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        if x2 - x1 == 200:
                screen.blit(wise_decision_msg, (400, 10))
"""