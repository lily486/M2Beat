import pygame
from Image import Image


class Collide:
    obstacles = []

    def __init__(self, player, obstacles, stage):
        self.player = player
        self.obstacles = obstacles
        self.stage = stage
        self.life = Image('resources/images/heart_Resized2.png')  # 라이프 이미지 불러오기
        self.life_list = [self.life.get_image(0, 0, 36, 44),  # 꽉 찬 하트
                          self.life.get_image(36, 0, 36, 44)]  # 빈 하트
        self.life_count = 3  # 라이프 초기 설정값

    def collider(self):
       for obstacle in self.obstacles:
           if self.player.pos.x + 48 > obstacle.pos and self.player.pos.x < obstacle.pos + obstacle.x:
               if self.player.pos.y > obstacle.y_pos:
                   self.life_count -= 1
                   self.obstacles.remove(obstacle)

       if self.life_count == self.life_count == 3:  # 라이프 변수가 3일 때
           self.stage.blit(self.life_list[0], (20, 635))
           self.stage.blit(self.life_list[0], (64, 635))
           self.stage.blit(self.life_list[0], (108, 635))
       elif self.life_count == 2:  # 라이프 변수가 2일 때
           self.stage.blit(self.life_list[0], (20, 635))
           self.stage.blit(self.life_list[0], (64, 635))
           self.stage.blit(self.life_list[1], (108, 635))
       elif self.life_count == 1:  # 라이프 변수가 3일 때
           self.stage.blit(self.life_list[0], (20, 635))
           self.stage.blit(self.life_list[1], (64, 635))
           self.stage.blit(self.life_list[1], (108, 635))
