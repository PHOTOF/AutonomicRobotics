from pygame.locals import *
import pygame
import time
import math

class Player:
    x = 0
    y = 0
    step = 25
    rotateAngel = math.degrees(15)
    direction = math.degrees(0)

    def __init__(self):
        self.x=0
        self.y=0

        arrow = pygame.Surface((50, 50))
        arrow.fill((0, 0, 0))
        pygame.draw.line(arrow, (0, 0, 0), (0, 0), (25, 25))
        pygame.draw.line(arrow, (0, 0, 0), (0, 50), (25, 25))
        arrow.set_colorkey((255, 255, 255))

        angle = math.atan2(-(self.player.y - (self.player.y + 30)), self.player.x - (self.player.x + 30))
        ##Note that in pygame y=0 represents the top of the screen
        ##So it is necessary to invert the y coordinate when using math
        angle = math.degrees(angle)


class App:
    windowWidth = 800
    windowHeight = 600
    background = pygame.image.load('background.png')

    def __init__(self):
        self._image_surf = None
        self.player = Player
        pygame.init()
        screen=pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Quadcopter - URIEL FLUSS, LEVI DWORKIN, YOAV HENIG')
        screen.fill((0,0,0))
        screen.blit(self.background, self.background.get_rect())

        pygame.draw.line(screen, (0,0,0), (self.player.x, self.player.y), (self.player.x+30, self.player.y+30))


    def drawAng(angle, pos):
        nar=pygame.transform.rotate(arrow,angle)
        nrect=nar.get_rect(center=pos)
        screen.blit(nar, nrect)

        drawAng(angle, pos1)
        angle+=180
        drawAng(angle, pos2)
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):

        while (1):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.rotateRight()

            if (keys[K_LEFT]):
                self.player.rotateLeft()

            if (keys[K_UP]):
                self.player.moveForward()

            if (keys[K_DOWN]):
                self.player.moveBack()

            if (keys[K_ESCAPE]):
                self.on_cleanup()

            time.sleep(60.0 / 1000.0);
        self.on_cleanup()




if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()