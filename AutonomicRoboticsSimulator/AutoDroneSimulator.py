from pygame.locals import *
import pygame
import math


def get_end(direction):
    last_color = (255, 255, 255, 255)
    for i in range(20, 100000):
        range_to_wall = i
        blackPos = int(x + i * math.cos(direction)), int(y + i * math.sin(direction))
        try:
            color = background.get_at(blackPos)
            if last_color != color:
                # last_color = color
                return [blackPos, range_to_wall]
        except IndexError:
            return [(int(x + (i-1) * math.cos(direction)), int(y + (i-1) * math.sin(direction))), range_to_wall]


# necessary pygame initializing
pygame.init()

# create a surface that will be seen by the user
background = pygame.image.load('backgrounds/p11.png')
screen = pygame.display.set_mode(background.get_rect().size)

# create a varibles for initial coordinates
x = 100
y = 100
surfR = 8

# create a varible for degrees pf rotation
degree = 0
rotate = 2.5
direction = 0
dRotate = rotate/58

# create lines and points lists for prescan sensors
lines = []
walls = []

# create variable for colors
white = (255, 255, 255)
green = (0, 255, 0)
gray = (224, 238, 238)
red = (223, 223, 0)

# create fail counter
failure = 0

while True:
    screen.fill((255, 255, 255))

    # create new surface with white BG
    drone = pygame.Surface((25, 25))
    drone.fill((0, 0, 0))
    drone = pygame.image.load('pygame.png')
    # drone = pygame.draw.rect(drone, (0, 255, 0), (x, y, x+50, y+50), 2)

    # draw the previous sensors
    for i in lines:
        pygame.draw.line(screen, gray, i[0], i[1], 1)
    for i in walls:
        pygame.draw.circle(screen, red, i, 1, 0)

    # What coordinates will the static image be placed:
    where = x, y

    # draw drone to screen and catch the rect that blit returns
    blittedRect = screen.blit(drone, where)

    begin = (x + surfR, y + surfR)
    RsensorEnd = get_end(direction + 0.5)[0]
    LsensorEnd = get_end(direction - 0.5)[0]
    MsensorEnd = get_end(direction)[0]

    rangeToRight = get_end(direction + 0.5)[1]
    rangeToLeft = get_end(direction - 0.5)[1]
    rangeToWall = get_end(direction)[1]

    pygame.draw.line(screen, green, begin, RsensorEnd, 1)
    pygame.draw.line(screen, green, begin, LsensorEnd, 1)
    pygame.draw.line(screen, green, begin, MsensorEnd, 1)

    print("Range to right: " + str(rangeToRight))
    print("Range to left: " + str(rangeToLeft))
    print("Range to wall: " + str(rangeToWall))

    lines.append((begin, RsensorEnd))
    lines.append((begin, LsensorEnd))
    lines.append((begin, MsensorEnd))
    walls.append(RsensorEnd)
    walls.append(LsensorEnd)

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if (keys[K_w]):
        # moveForward(x, y, )
        if background.get_at((int(x+surfR+math.cos(direction)), int(y+surfR+math.sin(direction))))!=white :
            failure += 1
            print("Failure: ", failure)
            # step back
            x -= math.cos(direction)
            y -= math.sin(direction)
            continue
        # #FORWARD
        x += math.cos(direction)
        y += math.sin(direction)

    if (keys[K_s]):
        # #BACKWARD
        x -= math.cos(direction)
        y -= math.sin(direction)

    if (keys[K_a]):
        # #ROTATED
        # get center of drone for later
        oldCenter = blittedRect.center

        # rotate drone by DEGREE amount degrees
        rotatedSurf = pygame.transform.rotate(drone, degree)

        # get the rect of the rotated drone and set it's center to the oldCenter
        rotRect = rotatedSurf.get_rect()
        rotRect.center = oldCenter

        # draw rotatedSurf with the corrected rect so it gets put in the proper spot
        screen.blit(rotatedSurf, rotRect)

        # change the degree of rotation
        degree += rotate
        if degree > 360:
            degree = 0

        direction -= dRotate
        if direction > 360:
            direction = 0

    if(keys[K_d]):
        # # ROTATED
        # get center of drone for later
        oldCenter = blittedRect.center

        # rotate drone by DEGREE amount degrees
        rotatedSurf = pygame.transform.rotate(drone, degree)

        # get the rect of the rotated drone and set it's center to the oldCenter
        rotRect = rotatedSurf.get_rect()
        rotRect.center = oldCenter

        # draw rotatedSurf with the corrected rect so it gets put in the proper spot
        screen.blit(rotatedSurf, rotRect)

        # change the degree of rotation
        degree -= rotate
        if degree > 360:
            degree = 0

        direction += dRotate
        if direction > 360:
            direction = 0

    # show the screen surface
    pygame.display.flip()

    # wait 60 ms until loop restart
    pygame.time.wait(10)


# pix = 2.5 cm
# RES 40 pix = 1.0 meter
# ft = 60.5
# mqx speed = 3m/s
# max acc = 2
# max ang = pi/sec
