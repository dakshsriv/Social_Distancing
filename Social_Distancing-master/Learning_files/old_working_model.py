#!/usr/bin/python3

import pygame

pygame.init()

bluecolor = (0, 0, 255)
myfont = pygame.font.SysFont("monospace",15) 
text = myfont.render("Wise decision to social distance!", myfont, bluecolor)

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


x1 = 0
x2 = 950
Trackline_for_y = 310

screen_width = 1028
screen_height = 720

screen=pygame.display.set_mode((screen_width, screen_height))

clock=pygame.time.Clock()
done=False
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    screen.fill(white)
    pygame.draw.rect(screen, red, (x1, Trackline_for_y, 70, 70))
    pygame.draw.rect(screen, blue, (x2, Trackline_for_y, 70, 70))
    screen.blit(text,(400, 10))
    pygame.display.update()
    clock.tick(40)