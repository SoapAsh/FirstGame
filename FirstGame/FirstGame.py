import pygame
from InputHandler import *
from Pacman import *
from Wall import *
from pygame.locals import *
clock = pygame.time.Clock()

class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 1280, 720
 
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Super Pacman')
        self.highScore = 0
        self.pacman = Pacman(500,500)
        self.block_list = []
        self.sprite_list = []
        self.wallCount = 0
        self.level1 = open("level/level1.txt")
        self.levelWidth = 1
        self.levelXStart = self.weight - 100
        self.levelYStart = self.height - 100
        for line in self.level1 :
            for c in line:
                if c == 'W':
                    self.block_list.append(Wall(self.weight - self.levelXStart, self.height-self.levelYStart))
                    self.sprite_list.append(Wall(self.weight - self.levelXStart, self.height-self.levelYStart))
                self.levelXStart = self.levelXStart - 20
            self.levelWidth = 1
            self.levelYStart = self.levelYStart - 20
            self.levelXStart = 1180
        self.level1.close()
        self.inputHandler = InputHandler(self, self.pacman)
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        self.monospaceFont = pygame.font.SysFont("monospace", 15)
        self.highScoreTitle = self.monospaceFont.render("HIGH SCORE", 1, (255,255,255))
        self.highScoreText = self.monospaceFont.render(str(self.highScore), 1, (255,255,255))
        self._running = True

        

    def update(self):
        self.inputHandler.update()
        self.checkCollision()
        pygame.display.update()
        clock.tick(60)
        pass
    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.highScoreTitle, ((self.weight / 2) - (self.highScoreTitle.get_width() / 2), 20))
        self.screen.blit(self.highScoreText,  ((self.weight / 2) - (self.highScoreText.get_width() / 2), 35))
        self.pacman.render(self.screen)
        for block in self.block_list:
            block.render(self.screen)
        pass
    def on_cleanup(self):
        pygame.quit()

    def checkCollision(self):
        oldX = self.pacman.x
        oldY = self.pacman.y
        for block in self.block_list:
            if(self.pacman.rect.colliderect(block.rect)):
                if(self.pacman.velocityX > 0 or self.pacman.velocityX < 0):
                    self.pacman.x = oldX
                    self.pacman.velocityX = 0
                if(self.pacman.velocityY > 0 or self.pacman.velocityY < 0):
                    self.pacman.y = oldY
                    self.pacman.velocityY = 0

                
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self.update()
            self.render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()