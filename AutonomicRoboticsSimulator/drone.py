import pygame

class Drone(object):
    def __init__(self, image):
        self.where = 0 ,0
        self.direction = 0
        self.dregree = 0
        self.image = image

    def update(self, where, degree, direction, screen):
        self.where = where
        self.dregree = degree
        self.direction = direction
        self.image = pygame.transform.rotate(self.image, degree)
        self.draw(screen)

    def draw(self, screen):
        # create new surface with white BG
        drone = pygame.Surface((50, 50))
        drone.fill((0, 0, 0))

        # draw drone to screen and catch the rect that blit returns
        blittedRect = screen.blit(self.image, self.where)

        # LsensorBegin = (x + 50, y)
        # LsensorEnd = (100, 30)
        # RsensorBegin = (x + 50, y - 100)
        # RsensorEnd = (150, 150)
        # pygame.draw.line(screen, green, RsensorBegin, RsensorEnd, 4)
        # # pygame.draw.line(screen, green, LsensorBegin, LsensorEnd, 4)


def right(self):
# ##ROTATED
# #get center of drone for later
# oldCenter = blittedRect.center
#
# #rotate drone by DEGREE amount degrees
# rotatedSurf =  pygame.transform.rotate(drone, degree)
#
# #get the rect of the rotated drone and set it's center to the oldCenter
# rotRect = rotatedSurf.get_rect()
# rotRect.center = oldCenter
#
# #draw rotatedSurf with the corrected rect so it gets put in the proper spot
# screen.blit(rotatedSurf, rotRect)

# change the degree of rotation