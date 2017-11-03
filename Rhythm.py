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
        self.value_list = []
        self.life_count = 3

    def rhythm(self):
        pressed = pygame.key.get_pressed()
        for obj in self.arrows:
            pressed_key = obj.ReturnKey()
            if 850 + 25 < obj.pos + 50 < 850 + 75:
                if pressed[pygame.K_UP]:
                    if pressed_key == UP:
                        if 850 + 25 < obj.pos + 50 < 850 + 35:
                            value = ["Good", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 50
                        elif 850 + 35 <= obj.pos + 50 < 850 + 50:
                            value = ["Great", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 70
                        elif 850 + 50 <= obj.pos + 50 < 850 + 75:
                            value = ["Perfect", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0

                elif pressed[pygame.K_DOWN]:
                    if pressed_key == DOWN:
                        if 850 + 25 < obj.pos + 50 < 850 + 35:
                            value = ["Good", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 50
                        elif 850 + 35 <= obj.pos + 50 < 850 + 50:
                            value = ["Great", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 70
                        elif 850 + 50 <= obj.pos + 50 < 850 + 75:
                            value = ["Perfect", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_LEFT]:
                    if pressed_key == LEFT:
                        if 850 + 25 < obj.pos + 50 < 850 + 35:
                            value = ["Good", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 50
                        elif 850 + 35 <= obj.pos + 50 < 850 + 50:
                            value = ["Great", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 70
                        elif 850 + 50 <= obj.pos + 50 < 850 + 75:
                            value = ["Perfect", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
                elif pressed[pygame.K_RIGHT]:
                    if pressed_key == RIGHT:
                        if 850 + 25 < obj.pos + 50 < 850 + 35:
                            value = ["Good", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 50
                        elif 850 + 35 <= obj.pos + 50 < 850 + 50:
                            value = ["Great", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 70
                        elif 850 + 50 <= obj.pos + 50 < 850 + 75:
                            value = ["Perfect", 200]
                            self.value_list.append(value)
                            self.total += self.combo + 100
                        self.combo += 1
                        self.arrows.remove(obj)
                    else:
                        self.combo = 0
            elif obj.pos + 50 > 850 + 75:
                self.combo = 0

            if obj.pos + 50 > 965:
                self.life_count -= 1
                self.arrows.remove(obj)

    def ReturnCombo(self):
        return self.combo

    def ReturnScore(self):
        return self.total

    def ReturnValue(self):
        return self.value_list

    def ReturnLife(self):
        return self.life_count