import pygame
from pygame.locals import *
import glob

class Pacman:
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 33
        self.height = 33
        self.animations = glob.glob("images/pacman/pacman_w*.png")
        self.ani_sheet_pos = 2
        self.ani_sheet_max = len(self.animations) - 1
        self.current_ani_sheet = pygame.image.load(self.animations[2])
        #self.eatSound = pygame.mixer.Sound('sounds/pacman/beep.wav')
        self.ani_max = 2
        self.ani_pos = 0
        self.speed = 5
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, pos, direction):
        if direction != self.ani_sheet_pos:
            self.ani_sheet_pos = direction
            self.current_ani_sheet = pygame.image.load(self.animations[self.ani_sheet_pos])
        if pos != 0:
            self.ani_speed-= 1
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0
            if self.ani_sheet_pos == 2 or self.ani_sheet_pos == 1:
                if self.x < 1280 and self.x >= -1:
                    self.x += pos
            else:
                if self.y < 720 and self.y >= -1:
                    self.y += pos
            if self.ani_speed == 0:
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos+=1 
        self.updateRectangle()

    def render(self, screen):
        screen.blit(self.current_ani_sheet, (self.x, self.y), (self.ani_pos*self.width, 0, self.width, self.height))

    def updateRectangle(self):
        self.rect.x = self.x
        self.rect.y = self.y

       


