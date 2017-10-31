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
        self.value = None

    def rhythm(self):
        pressed = pygame.key.get_pressed()
        for obj in self.arrows:
            pressed_key = obj.ReturnKey()
            if 850 + 25 < obj.pos + 50 < 850 + 75:
                if pressed[pygame.K_UP]:
                    if pressed_key == UP:
                        if 850 + 25 < obj.pos + 50 < 850 + 35:
                            self.value = "Good"
                            self.total += self.combo + 50
                        elif 850 + 35 <= obj.pos + 50 < 850 + 50:
                            self.value = "Great"
                            self.total += self.combo + 70
                        elif 850 + 50 <= obj.pos + 50 < 850 + 75:
                            self.value = "Perfect"
                            self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0

                elif pressed[pygame.K_DOWN]:
                    if pressed_key == DOWN:
                        if 850 + 25 < obj.pos + 50 < 850 + 35:
                            self.value = "Good"
                            self.total += self.combo + 50
                        elif 850 + 35 <= obj.pos + 50 < 850 + 50:
                            self.value = "Great"
                            self.total += self.combo + 70
                        elif 850 + 50 <= obj.pos + 50 < 850 + 75:
                            self.value = "Perfect"
                            self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_LEFT]:
                    if pressed_key == LEFT:
                        if 850 + 25 < obj.pos + 50 < 850 + 35:
                            self.value = "Good"
                            self.total += self.combo + 50
                        elif 850 + 35 <= obj.pos + 50 < 850 + 50:
                            self.value = "Great"
                            self.total += self.combo + 70
                        elif 850 + 50 <= obj.pos + 50 < 850 + 75:
                            self.value = "Perfect"
                            self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_RIGHT]:
                    if pressed_key == RIGHT:
                        if 850 + 25 < obj.pos + 50 < 850 + 35:
                            self.value = "Good"
                            self.total += self.combo + 50
                        elif 850 + 35 <= obj.pos + 50 < 850 + 50:
                            self.value = "Great"
                            self.total += self.combo + 70
                        elif 850 + 50 <= obj.pos + 50 < 850 + 75:
                            self.value = "Perfect"
                            self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
            elif obj.pos + 50 > 850 + 75:
                self.combo = 0

    def ReturnCombo(self):
        return self.combo

    def ReturnScore(self):
        return self.total

    def ReturnValue(self):
        return self.value