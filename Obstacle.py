import pygame
import random
from Image import Image

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3


class Obstacle:
    fireball_img = pygame.image.load('resources/images/Fireball.png')
    oarrow_img = pygame.image.load('resources/images/oarrow.png')
    lightning_img = pygame.image.load('resources/images/lightningResized.png')
    kunai_img = pygame.image.load('resources/images/kunaiResized.png')
    obstacle_list = [fireball_img, oarrow_img, lightning_img, kunai_img]
    arrow_img = pygame.image.load('resources/images/arrow_resized.png')
    arrow_list = [pygame.transform.rotate(arrow_img, 0),
                  pygame.transform.rotate(arrow_img, 90),
                  pygame.transform.rotate(arrow_img, 180),
                  pygame.transform.rotate(arrow_img, 270)]

    def __init__(self, stage, height, speed):
        self.x = 40  # 장애물의 가로값
        self.y = 40  # 장애물의 세로값
        self.stage = stage
        self.pos = 280  # 장애물이 처음 생성되는 지점의  x좌표
        self.y_pos = height - self.y - 86
        self.height = height
        self.speed = speed
        self.index = random.randint(0, 3)
        self.arrow = self.arrow_list[self.index]
        self.key = None
        self.obj = self.obstacle_list[self.index]  # 장애물 생성

    def move(self):
        self.pos += self.speed
        self.stage.blit(self.arrow, (self.pos, self.y_pos - 90))
        self.stage.blit(self.obj, (self.pos, self.y_pos))
        if self.arrow == self.arrow_list[0]:
            self.key = RIGHT
        elif self.arrow == self.arrow_list[1]:
            self.key = DOWN
        elif self.arrow == self.arrow_list[2]:
            self.key = LEFT
        elif self.arrow == self.arrow_list[3]:
            self.key = UP

    def ReturnKey(self):
        return self.key
