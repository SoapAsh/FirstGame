from Pacman import *
from pygame.locals import *
from Pacman import *

class InputHandler(object):

     def __init__(self, game, pacman):
         self.game = game
         self.pacman = pacman
         self.direction = 2

     def update(self):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game._running = False
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.direction = 2
                self.pacman.velocityX = self.pacman.speed
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.pacman.velocityX = 0
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.direction = 1
                self.pacman.velocityX = -self.pacman.speed
            elif event.type == KEYUP and event.key == K_LEFT:
                self.pacman.velocityX = 0
            elif event.type == KEYDOWN and event.key == K_UP:
                self.direction = 3
                self.pacman.velocityY = -self.pacman.speed
            elif event.type == KEYUP and event.key == K_UP:
                self.pacman.velocityY = 0
            elif event.type == KEYDOWN and event.key == K_DOWN:
                self.direction = 0
                self.pacman.velocityY = self.pacman.speed
            elif event.type == KEYUP and event.key == K_DOWN:
                self.pacman.velocityY = 0
         self.pacman.update(self.direction)




