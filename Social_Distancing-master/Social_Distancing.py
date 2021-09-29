#!/usr/bin/python3

import pygame, random, time, math, pygame.mixer

from pydub import AudioSegment
song = AudioSegment.from_mp3("song.mp3")

pygame.init()

bg = pygame.image.load('index.jpeg')
pygame.mixer.init()
pygame.mixer.music.load('final.wav')
#pygame.mixer.music.set_volume(0.7)
myfont = pygame.font.Font(None, 35)
screen = pygame.display.set_mode((1070, 720))
pling = pygame.mixer.Sound('pling.wav')
#pop = pygame.mixer.Sound('blop.wav')
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
win = pygame.display.set_mode((1028, 720))
x1 = 0
x2 = 950
y1 = 310
y2 = 310

def finddist(p1, p2):
        xdist = p1[0] - p2[0]
        if xdist < 0:
                xdist = -1 * xdist
        ydist = p1[1] - p2[1]
        if ydist < 0:
                ydist = -1 * ydist
        dist = math.sqrt(xdist**2 + ydist**2)
        return dist

screen_width = 1028
screen_height = 720

done = False
clock = pygame.time.Clock()

do_blit = False
pygame.mixer.music.play(-1)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        win.blit(bg, (0, 0))
        keyPressed = pygame.key.get_pressed()
        do_blit = False
        screen.fill(white)
        wise_decision_msg = myfont.render("Wise decision people, you should social distance.", 1, green)
        trouble_msg = myfont.render("Trouble! Trouble! You guys are too close to each other. ", 1, red)
        dist = finddist([x1,y1],[x2,y2])
        if dist > 225:
                if keyPressed[pygame.K_UP]:
                        y2 = y2 - 3
                if keyPressed[pygame.K_DOWN]:
                        y2 = y2 + 3
                if keyPressed[pygame.K_LEFT]:
                        x2 = x2 - 3
                if keyPressed[pygame.K_RIGHT]:
                        x2 = x2 + 3
                if keyPressed[pygame.K_w]:
                        y1 = y1 - 3
                if keyPressed[pygame.K_a]:
                        x1 = x1 - 3
                if keyPressed[pygame.K_s]:
                        y1 = y1 + 3
                if keyPressed[pygame.K_d]:
                        x1 = x1 + 3
        if dist <= 300 and dist > 225:
                now = time.time()
                later = time.time()
                while later - now < 0.03:
                        screen.blit(trouble_msg, (10, 400))
                        later = time.time()
        elif dist <= 225:
                pling.play()
                time.sleep(1)
                v = random.randint(1,2)
                if v == 1:
                        x1 = x2 - 550
                else:
                        x2 = x1 + 550
                do_blit = True
        rect_red = pygame.draw.rect(screen, red, (x1, y1, 70, 70))
        rect_blue = pygame.draw.rect(screen, blue, (x2, y2, 70, 70))
        pygame.display.update()
        clock.tick(60)
        if do_blit:
#                pop.play()
                now = time.time()
                later = time.time()
                while later - now < 2:
                        screen.blit(wise_decision_msg, (400, 10))
                        later = time.time()
                        pygame.display.update()
