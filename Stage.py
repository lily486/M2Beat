import pygame
import random
from Player import Player
from Image import Cloud, Ground
from Timer import Timer
pygame.font.init()
JUMP_LIMIT = 2  # 점프 한도
TITLE_FONT = pygame.font.Font('resources/fonts/CulDeSac.ttf', 90)
MENU_FONT = pygame.font.Font('resources/fonts/AmaticSC-Bold.ttf', 60)


class Stage:
    width = 1200  # 가로
    height = 700  # 세로
    FPS = 30
    fpsClock = pygame.time.Clock()
    player = None
    background = pygame.image.load('resources/images/backgroundCutResized.png')
    ground = pygame.image.load('resources/images/ground.png')
    cloud_list = [pygame.image.load('resources/images/cloud1.png'),
                  pygame.image.load('resources/images/cloud2.png'),
                  pygame.image.load('resources/images/cloud3.png'),
                  pygame.image.load('resources/images/cloud4.png')]
    finish = False

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("M2Beat")
        self.stage = pygame.display.set_mode((self.width, self.height))
        self.stage.blit(self.background, (0, 0))
        self.player = Player(self.stage, self.ground, self.width, self.height)
        self.count = 0  # 점프한 횟수(K_UP누른 횟수)
        self.cloud_count = 1
        self.clouds = []

    def menu_choice(self):
        start = False
        pygame.display.update()
        menu = self.height/2

        while not start:
            self.stage.blit(self.background, (0, 0))
            self.text("M2Beat", TITLE_FONT, (255, 255, 255), self.width/2, self.height/4 - 20)
            self.text("Start", MENU_FONT, (0, 0, 0), self.width/2 + 20, self.height/2)
            self.text("Exit", MENU_FONT, (0, 0, 0), self.width/2 + 20, self.height/2 + 100)
            self.text(">", MENU_FONT, (0, 0, 0), self.width/2 - 50, menu)
            Ground(self.stage, self.ground, 0, self.height - self.ground.get_height())
            self.player.intro()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = True
                    self.finish = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu += 100
                    if event.key == pygame.K_UP:
                        menu -= 100
                if menu > self.height/2 + 100:
                    menu = self.height/2 + 100
                if menu < self.height/2:
                    menu = self.height/2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if menu == self.height/2:
                            start = True
                        if menu == self.height/2 + 100:
                            start = True
                            self.finish = True

    def text(self, text, font, color, x, y):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        rect.midtop = (x, y)
        self.stage.blit(surface, rect)

    def update(self):  # 플레이어 움직일 때 잔상 안남게 + 플레이어 움직임
        self.stage.blit(self.background, (0, 0))
        Ground(self.stage, self.ground, 0, self.height - self.ground.get_height())
        self.player.move()
        self.cloud_count -= 1
        if self.cloud_count == 0:
            cloud = Cloud(self.stage, self.cloud_list[random.randint(0, 3)], self.width, random.randint(0, 100))
            self.clouds.append(cloud)
            self.cloud_count = 100  # cloud_count가 작아지면 구름 갯수가 많아짐
        for cloud in self.clouds:
            cloud.move()
        if self.clouds[0].x == -350:
            self.clouds.pop(-(len(self.cloud_list))-1)

    def start(self):
        time = Timer(self.stage, 6)
        time.timer()
        while not self.finish:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                if event.type == pygame.KEYDOWN:  # 한번 눌렀을 때 실행
                    if event.key == pygame.K_UP and self.count < JUMP_LIMIT:
                        self.player.jump()
                        self.count += 1
                    elif self.count == JUMP_LIMIT:
                        if self.player.pos.y == self.height - self.ground.get_height() - self.player.image.get_height() + 4:
                            self.count = 0
                    self.player.jumping = False
            self.player.move()
            self.update()
            if time.Return()>0:
                self.text(str(time.Return()), TITLE_FONT, (255, 255, 255), self.width / 2, self.height / 4 - 20)
            pygame.display.update()

game = Stage()
game.menu_choice()
game.start()
