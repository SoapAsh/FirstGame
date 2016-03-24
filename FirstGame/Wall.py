import pygame
from pygame.locals import *
import glob

class Wall:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.image = pygame.image.load("images/objects/wall.png")
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    
    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))