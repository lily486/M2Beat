import pygame
import random


class Obstacle:
    def __init__(self, stage, width, height, speed):
        self.x = random.randint(30, 50)
        self.y = random.randint(30, 200)
        self.stage = stage
        self.pos = width
        self.height = height
        self.speed = speed
        self.obj = pygame.Surface((self.x, self.y))
        self.obj.fill((0, 0, 0))

    def move(self):
        self.pos -= self.speed
        self.stage.blit(self.obj, (self.pos, self.height - self.y - 86))
