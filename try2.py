from pygame.locals import *
import pygame
import time
import math


def getEnd(direction):
    last_color = (255, 255, 255, 255)
    for i in range(60, 400):
        blackPos = int(x + i * math.cos(direction)), int(y + i * math.sin(direction))
        try:
            color = screen.get_at(blackPos)
            if last_color != color:
                last_color = color
                return blackPos
        except IndexError:
            return int(x + (i-1) * math.cos(direction)), int(y + (i-1) * math.sin(direction))



#necessary pygame initializing
pygame.init()

#create a surface that will be seen by the user
background = pygame.image.load('background.png')
screen =  pygame.display.set_mode(background.get_rect().size)

#create a varibles for initial coordinates
x = 0
y = 0

#create a varible for degrees pf rotation
degree = 0
rotate = 2.5
direction = 0
dRotate = rotate/58

Rsensor = ()
green = (0,255,0)

while True:
    screen.fill((255,255,255))
    screen.blit(background, (0, 0))

    #create new surface with white BG
    surf =  pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    surf = pygame.image.load('pygame.png')


    #what coordinates will the static image be placed:
    where = x, y

    #draw surf to screen and catch the rect that blit returns
    blittedRect = screen.blit(surf, where)

    RsensorBegin = (x + 19, y + 19)
    RsensorEnd = getEnd(direction + 0.3)
    LsensorBegin = (x + 19, y + 19)
    LsensorEnd = getEnd(direction - 0.3)
    MsensorBegin = (x + 19, y + 19)
    MsensorEnd = getEnd(direction)
    pygame.draw.line(screen, green, RsensorBegin, RsensorEnd, 4)
    pygame.draw.line(screen, green, LsensorBegin, LsensorEnd, 4)
    pygame.draw.line(screen, green, MsensorBegin, MsensorEnd, 4)

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if (keys[K_UP]):
        ##FORWARD
        x += math.cos(direction)
        y += math.sin(direction)

    if (keys[K_DOWN]):
        ##BACKWARDS
        x -= math.cos(direction)
        y -= math.sin(direction)

    if (keys[K_LEFT]):
        ##ROTATED
        #get center of surf for later
        oldCenter = blittedRect.center

        #rotate surf by DEGREE amount degrees
        rotatedSurf =  pygame.transform.rotate(surf, degree)

        #get the rect of the rotated surf and set it's center to the oldCenter
        rotRect = rotatedSurf.get_rect()
        rotRect.center = oldCenter

        #draw rotatedSurf with the corrected rect so it gets put in the proper spot
        screen.blit(rotatedSurf, rotRect)

        #change the degree of rotation
        degree += rotate
        if degree > 360:
            degree = 0

        direction-=dRotate
        if direction>360:
            direction = 0

    if (keys[K_RIGHT]):
        ##ROTATED
        #get center of surf for later
        oldCenter = blittedRect.center

        #rotate surf by DEGREE amount degrees
        rotatedSurf =  pygame.transform.rotate(surf, degree)

        #get the rect of the rotated surf and set it's center to the oldCenter
        rotRect = rotatedSurf.get_rect()
        rotRect.center = oldCenter

        #draw rotatedSurf with the corrected rect so it gets put in the proper spot
        screen.blit(rotatedSurf, rotRect)

        #change the degree of rotation
        degree -= rotate
        if degree > 360:
            degree = 0

        direction += dRotate
        if direction > 360:
            direction = 0

    #show the screen surface
    pygame.display.flip()

    #wait 60 ms until loop restart
    pygame.time.wait(10)