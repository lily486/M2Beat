import pygame


class Collide:
    obstacles = []

    def __init__(self, player, obstacles, stage):
        self.player = player
        self.obstacles = obstacles
        self.stage = stage
        self.life_count = 3  # 라이프 초기 설정값

    def collider(self):
       for obstacle in self.obstacles:
           if self.player.pos.x + 48 > obstacle.pos and self.player.pos.x < obstacle.pos + obstacle.x:
               if self.player.pos.y > obstacle.y_pos:
                   self.life_count -= 1
                   self.obstacles.remove(obstacle)
           if obstacle.pos < 215:
               self.obstacles.remove(obstacle)
       return self.life_count

    def init(self):
        self.life_count = 3
