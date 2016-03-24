from Pacman import *
from pygame.locals import *
from Pacman import *

class InputHandler(object):

     def __init__(self, game, pacman):
         self.game = game
         self.pacman = pacman
         self.pos = 0
         self.direction = 2

     def update(self):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game._running = False
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.direction = 2
                self.pos = 1
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.pos = 0
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.direction = 1
                self.pos = -1
            elif event.type == KEYUP and event.key == K_LEFT:
                self.pos = 0
            elif event.type == KEYDOWN and event.key == K_UP:
                self.direction = 3
                self.pos = -1
            elif event.type == KEYUP and event.key == K_UP:
                self.pos = 0
            elif event.type == KEYDOWN and event.key == K_DOWN:
                self.direction = 0
                self.pos = 1
            elif event.type == KEYUP and event.key == K_DOWN:
                self.pos = 0
         self.pacman.update(self.pos, self.direction)




