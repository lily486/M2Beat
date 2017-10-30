import pygame

LEFT = 2
UP = 1
RIGHT = 0
DOWN = 3


class Rhythm:
    obstacles = []

    def __init__(self, arrows, stage):
        self.arrows = arrows
        self.stage = stage
        self.combo = 0
        self.combos = []
        self.total = 0      # 총 점수


    def rhythm(self):
        pressed = pygame.key.get_pressed()
        for obj in self.arrows:
            pressed_key = obj.ReturnKey()
            if 320 < obj.pos < 395:
                if pressed[pygame.K_UP]:
                    if pressed_key == UP:
                        self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0

                elif pressed[pygame.K_DOWN]:
                    if pressed_key == DOWN:
                        self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_LEFT]:
                    if pressed_key == LEFT:
                        self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_RIGHT]:
                    if pressed_key == RIGHT:
                        self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
            elif obj.pos < 320:
                self.combo = 0

    def ReturnCombo(self):
        return self.combo

    def ReturnScore(self):
        return self.total