import pygame


class Image:  # 이미지 불러오기
    def __init__(self, filename):
        self.cut_image = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, w, h):
        image = pygame.Surface((w, h), pygame.SRCALPHA)  # pygame.SRCALPHA -> png파일 배경 투명하게
        image.blit(self.cut_image, (0, 0), (x, y, w, h))  # (x, y)좌표가 lefttop이고, (w, h)만한 크기로 자르기
        return image


class Cloud:
    def __init__(self, stage, cloud, width, y):
        self.stage = stage
        self.cloud = cloud
        self.x = width
        self.y = y
        self.speed = 6

    def move(self):
        self.x -= self.speed
        self.stage.blit(self.cloud, (self.x, self.y))


class Ground:  # 플레이화면에서 땅
    def __init__(self, stage, ground, x, y):
        self.stage = stage
        self.ground_image = ground
        self.x = x
        self.y = y
        self.stage.blit(self.ground_image, (self.x, self.y))
        self.stage.blit(self.ground_image, (self.x + self.ground_image.get_width(), self.y))