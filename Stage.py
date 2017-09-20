import pygame
from Player import Player

class Stage:
    width = 1200
    height = 700
    FPS = 30
    fpsClock = pygame.time.Clock()

    Stage = pygame.display.set_mode((width, height))

    pygame.display.set_caption('M2Beat')
    player = None

    def __init__(self):
        pygame.display.set_caption("M2Beat")
        self.stage = pygame.display.set_mode((self.width, self.height))
        self.stage.fill((0, 0, 0))
        self.player = Player(self.stage, self.width, self.height)

    class Ground:
        def __init__(self, stage, x, y, w, h):
            self.stage = stage
            self.image = pygame.Surface((w, h))
            self.image.fill((0, 255, 0))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.stage.blit(self.image, (self.rect.x, self.rect.y))


    def start(self):
        finish = False
        while not finish :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True
            pygame.display.update()

            self.Ground(self.stage, 0, self.height - 50, self.width, 50)
            self.player.move()
            pygame.display.update()



game = Stage()
game.start()