from pygame.locals import *
import pygame
import time
import math


class Player:
    x = []
    y = []
    step = 25
    rotateAngel = 15
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, length):
            self.x.append(0)
            self.y.append(0)

    def update(self):

        # self.updateCount = self.updateCount + 1
        # if self.updateCount &gt; self.updateCountMax:
        #
        #     # update previous positions
        #     for i in range(self.length - 1, 0, -1):
        #         print
        #         "self.x[" + str(i) + "] = self.x[" + str(i - 1) + "]"
        #         self.x[i] = self.x[i - 1]
        #         self.y[i] = self.y[i - 1]
        #
            # update position of head of snake
            # if self.direction == 0:
            #     self.x[0] = self.x[0] + self.step
            # if self.direction == 1:
            #     self.x[0] = self.x[0] - self.step
            # if self.direction == 2:
            #     self.y[0] = self.y[0] - self.step
            # if self.direction == 3:
            #     self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def rotateRight(self):
        if (self.x[0] == App.windowWidth - self.step):
            return
        # nar = pygame.transform.rotate(_image_surf, self.rotateAngel)
        # nrect = nar.get_rect(center=pos)
        # screen.blit(nar, nrect)
        # self.direction = self.direction + self.rotateAngel
        self.x[0] = self.x[0] + self.step

    def rotateLeft(self):
        if self.x[0] == 0:
            return
        # self.direction = 1
        self.x[0] = self.x[0] - self.step

    def moveForward(self):
        if self.y[0] == 0:
            return
        # self.direction = 2
        self.y[0] = self.y[0] - self.step

    def moveBack(self):
        if self.y[0] == App.windowHeight - self.step:
            return
        # self.direction = 3
        self.y[0] = self.y[0] + self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x[0], self.y[0]))


class App:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player(1)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)



        pygame.display.set_caption('Quadcopter - URIEL FLUSS, LEVI DWORKIN, YOAV HENIG')
        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()
        pass

    def on_render(self):
        background = pygame.image.load('background.png')
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(background, background.get_rect())

        self.player.draw(self._display_surf, self._image_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
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
                self._running = False
            self.on_loop()
            self.on_render()

            time.sleep(60.0 / 1000.0);
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()