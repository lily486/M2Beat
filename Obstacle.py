import pygame
import random
from Image import Image

DOWN = 0
LEFT = 1
RIGHT = 2
UP = 3


class Obstacle(pygame.Rect):
    obstacle_img = Image('resources/images/warrior_partyResized.png')
    obstacle_list = [obstacle_img.get_image(0, 2, 85, 85),
                     obstacle_img.get_image(0, 85 + 2, 85, 85),
                     obstacle_img.get_image(0, 170 + 2, 85, 85),
                     obstacle_img.get_image(0, 255 + 2, 85, 85)]

    def __init__(self, stage, width, height, speed):
        self.x = 85  # 장애물의 가로값
        self.y = 85  # 장애물의 세로값
        self.stage = stage
        self.pos = width
        self.y_pos = height - self.y - 86
        self.height = height
        self.speed = speed
        self.obj = self.obstacle_list[random.randint(0, 3)]
        self.key = None

    def move(self):
        self.pos -= self.speed
        self.stage.blit(self.obj, (self.pos, self.y_pos))
        if self.obj == self.obstacle_list[0]:
            self.key = DOWN
        elif self.obj == self.obstacle_list[1]:
            self.key = LEFT
        elif self.obj == self.obstacle_list[2]:
            self.key = RIGHT
        elif self.obj == self.obstacle_list[3]:
            self.key = UP

    def ReturnKey(self):
        return self.key
