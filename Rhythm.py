import pygame

DOWN = 0
LEFT = 1
RIGHT = 2
UP = 3


class Rhythm:
    def __init__(self, obstacles, stage):
        self.obstacles = obstacles
        self.stage = stage
        self.combo = 0

    def rhythm(self):
        for obj in self.obstacles:
            pressed_key = obj.ReturnKey()
            if obj.pos > 320 and obj.pos < 395:
                for keyboard in pygame.event.get():
                    if keyboard.key == pygame.KEYDOWN:
                        if keyboard.key == pygame.K_UP:
                            if pressed_key == UP:
                                self.combo += 1
                            else:
                                self.combo = 0
                        elif keyboard.key == pygame.K_RIGHT:
                            if pressed_key == RIGHT:
                                self.combo += 1
                            else:
                                self.combo = 0
                        elif keyboard.key == pygame.K_LEFT:
                            if pressed_key == LEFT:
                                self.combo += 1
                            else:
                                self.combo = 0
                        elif keyboard.key == pygame.DOWN:
                            if pressed_key == DOWN:
                                self.combo += 1
                            else:
                                self.combo = 0

    def ReturnCombo(self):
        return self.combo