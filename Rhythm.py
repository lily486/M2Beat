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
        self.units = 0      # 총 맞춘 횟수
        self.munit = 0      # 틀린 횟수
        self.score = 0      # 콤보로 더해지는 점수
        self.total = 0      # 총 점수


    def rhythm(self):
        pressed = pygame.key.get_pressed()
        for obj in self.arrows:
            pressed_key = obj.ReturnKey()
            if 320 < obj.pos < 395:
                if pressed[pygame.K_UP]:
                    if pressed_key == UP:
                        self.combo += 1
                        self.munit = 0          # 틀린 횟수 초기화
                        self.units += 1         # 맞춘 횟수 +1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                        self.munit += 1         # 틀린 횟수 +1
                        self.units = self.units
                elif pressed[pygame.K_DOWN]:
                    if pressed_key == DOWN:
                        self.combo += 1
                        self.munit = 0
                        self.units += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                        self.munit += 1
                        self.units = self.units
                elif pressed[pygame.K_LEFT]:
                    if pressed_key == LEFT:
                        self.combo += 1
                        self.munit = 0
                        self.units += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                        self.munit += 1
                        self.units = self.units
                elif pressed[pygame.K_RIGHT]:
                    if pressed_key == RIGHT:
                        self.combo += 1
                        self.munit = 0
                        self.units += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                        self.munit += 1
                        self.units = self.units
            elif obj.pos < 320:
                self.combo = 0
                self.units = self.units

    def ReturnCombo(self):
        return self.combo

    def ReturnScore(self):
        self.score = (100 * self.combo / 100)       # 콤보로 추가되는 점수
        self.total = (100 * self.units) + (self.combo * self.score)     #맞춘횟수 백점단위 + 콤보로 추가되는 점수
        return self.total