import pygame
import random


class Obstacle(pygame.Rect):
    obstacle = pygame.Surface((100, 100))

    def __init__(self, stage, width, height, speed):
        self.x = random.randint(30, 50)  # 장애물의 가로값
        self.y = random.randint(30, 200)  # 장애물의 세로값
        self.stage = stage
        self.pos = width
        self.y_pos = height - self.y - 86
        self.height = height
        self.speed = speed
        self.obj = pygame.Surface((self.x, self.y))  # 직사각형 생성
        self.obj.fill((0, 0, 0))  # 색깔 채우기

    def move(self):
        self.pos -= self.speed
        self.stage.blit(self.obj, (self.pos, self.y_pos))
        print("test")
