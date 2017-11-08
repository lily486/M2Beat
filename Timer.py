import threading
from Obstacle import Obstacle
import pygame
SPEED = 3.5


class Timer:
    def __init__(self, count, finish, stage, height):
        self.count = count
        self.finish = finish
        self.obstacle_value = False
        self.stage = stage
        self.height = height
        self.obstacles = []
        self.time = -25

    def timer(self):
        timer = threading.Timer(1, self.timer)
        self.count -= 1
        timer.start()
        if self.count == 0 or self.finish:
            timer.cancel()

    def rhythm(self):
        rhythm = threading.Timer(0.09, self.rhythm)
        print(self.time)
        self.time += 1
        rhythm.start()
        if self.time == 2:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 6:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 8:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 14:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
            pygame.mixer.music.unpause()
        elif self.time == 18:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 20:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 26:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 30:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 32:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 37:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 39:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 49:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 51:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 53:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 55:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 60:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 62 :
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 76:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 80:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 82:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 87:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 89:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 99:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 101:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 103:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 105:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 110:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 112:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 126:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 127:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 129:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 130:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 138:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 139:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 141:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 142:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        # elif self.time == 1234:
        #     obstacle = Obstacle(self.stage, self.height, SPEED)
        #     self.obstacles.append(obstacle)
        # elif self.time == 110:
        #     obstacle = Obstacle(self.stage, self.height, SPEED)
        #     self.obstacles.append(obstacle)
        # elif self.time == 112:
        #     obstacle = Obstacle(self.stage, self.height, SPEED)
        #     self.obstacles.append(obstacle)
        # elif self.time == 126:
        #     obstacle = Obstacle(self.stage, self.height, SPEED)
        #     self.obstacles.append(obstacle)
        # elif self.time == 128:
        #     obstacle = Obstacle(self.stage, self.height, SPEED)
        #     self.obstacles.append(obstacle)
        # elif self.time == 130:
        #     obstacle = Obstacle(self.stage, self.height, SPEED)
        #     self.obstacles.append(obstacle)
            rhythm.cancel()
        elif self.time > 180:
            rhythm.cancel()

    def Return(self):
        return self.count

    def ReturnObj(self):
        return self.obstacles

    def init(self):
        self.obstacles = []
