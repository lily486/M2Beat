import pygame

DOWN = 0
LEFT = 1
RIGHT = 2
UP = 3


class Rhythm:
    obstacles = []

    def __init__(self, obstacles, stage):
        self.obstacles = obstacles
        self.stage = stage
        self.combo = 0
        self.combos = []

    def rhythm(self):
        pressed = pygame.key.get_pressed()
        for obj in self.obstacles:
            pressed_key = obj.ReturnKey()
            if 320 < obj.pos < 395:
                if pressed[pygame.K_UP]:
                    if pressed_key == UP:
                        self.combo += 1
                        self.obstacles.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_DOWN]:
                    if pressed_key == DOWN:
                        self.combo += 1
                        self.obstacles.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_LEFT]:
                    if pressed_key == LEFT:
                        self.combo += 1
                        self.obstacles.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_RIGHT]:
                    if pressed_key == RIGHT:
                        self.combo += 1
                        self.obstacles.remove(obj)
                    else:
                        self.combo = 0
            elif obj.pos < 320:
                self.combo = 0

    def ReturnCombo(self):
        return self.combo