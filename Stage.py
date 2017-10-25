import pygame
import random
from Player import Player
from Image import Cloud, Ground, Image
from Timer import Timer
from Obstacle import Obstacle
from Collide import Collide
pygame.font.init()
JUMP_LIMIT = 2  # 점프 한도
TITLE_FONT = pygame.font.Font('resources/fonts/CulDeSac.ttf', 90)
COUNT_FONT = pygame.font.Font('resources/fonts/Pixel.ttf', 80)
MENU_FONT = pygame.font.Font('resources/fonts/AmaticSC-Bold.ttf', 60)
RESTART_FONT = pygame.font.Font('resources/fonts/CALIBRATE1.ttf', 30)
GAMEOVER_FONT = pygame.font.Font('resources/fonts/grishenko_novoye_nbp.ttf', 60)
SPEED = 4  # 배경(구름), 장애물 움직이는 속도


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
    playAgain = False
    exit = False
    life = Image('resources/images/heart_Resized2.png')  # 라이프 이미지 불러오기
    life_list = [life.get_image(0, 0, 36, 44),  # 꽉 찬 하트
                 life.get_image(36, 0, 36, 44)]  # 빈 하트

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("M2Beat")
        self.stage = pygame.display.set_mode((self.width, self.height))
        self.stage.blit(self.background, (0, 0))
        self.player = Player(self.stage, self.ground, self.width, self.height)
        self.count = 0  # 점프한 횟수(K_UP 누른 횟수)
        self.cloud_count = 1
        self.obstacle_count = 270
        self.clouds = []
        self.intro_clouds = []
        self.obstacles = []
        self.collide = Collide(self.player, self.obstacles, self.stage)

    def menu_choice(self):
        start = False
        pygame.display.update()
        menu = self.height/2

        while not start:  # 초기 화면 설정 (Intro 화면 설정)
            self.stage.blit(self.background, (0, 0))
            intro_clouds = [Cloud(self.stage, self.cloud_list[0], 15, 87, 0),
                            Cloud(self.stage, self.cloud_list[1], 315, 32, 0),
                            Cloud(self.stage, self.cloud_list[2], 615, 45, 0),
                            Cloud(self.stage, self.cloud_list[3], 915, 25, 0)]
            for intro_cloud in intro_clouds:
                intro_cloud.move()
            self.text("M2BEAT", TITLE_FONT, (255, 255, 255), self.width/2, self.height/4 + 30)
            self.text("Start", MENU_FONT, (0, 0, 0), self.width/2, self.height/2)
            self.text("Exit", MENU_FONT, (0, 0, 0), self.width/2, self.height/2 + 100)
            self.text(">", MENU_FONT, (0, 0, 0), self.width/2 - 80, menu)
            Ground(self.stage, self.ground, 0, self.height - self.ground.get_height())
            self.player.intro()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = True
                    self.finish = True
                    self.exit = True
                    self.playAgain = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu += 100
                    if event.key == pygame.K_UP:
                        menu -= 100
                if menu > self.height/2 + 100:  # 두가지 메뉴에서 벗어나지 않게
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
                            self.exit = True
                            self.playAgain = True

    def text(self, text, font, color, x, y):  # 텍스트 그리는 함수
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
            cloud = Cloud(self.stage, self.cloud_list[random.randint(0, 3)], self.width, random.randint(0, 100), SPEED)
            self.clouds.append(cloud)
            self.cloud_count = 100  # cloud_count가 작아지면 구름 갯수가 많아짐
        for cloud in self.clouds:
            cloud.move()
        if self.clouds[0].x == -350:
            self.clouds.pop(-(len(self.clouds))-1)

    def play(self):
        self.playAgain = False
        clock = Timer(6, self.finish)  # 시작하기 전 5초 세기 (몇 초 셀건지 바꾸려면 +1 해서 설정)
        clock.timer()
        while not self.finish:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                    self.exit = True
                    self.playAgain = True
            self.obstacle_count -= 1
            self.update()
            if clock.Return() > 0:
                self.text(str(clock.Return()), COUNT_FONT, (255, 255, 255), self.width / 2, self.height / 2)
            if self.obstacle_count == 0:
                obstacle = Obstacle(self.stage, self.width, self.height, SPEED)
                self.obstacles.append(obstacle)
                self.obstacle_count = 250
            for obj in self.obstacles:
                obj.move()
            life_count = self.collide.collider()
            if life_count == 3:
                self.stage.blit(self.life_list[0], (20, 635))
                self.stage.blit(self.life_list[0], (64, 635))
                self.stage.blit(self.life_list[0], (108, 635))
            elif life_count == 2:
                self.stage.blit(self.life_list[0], (20, 635))
                self.stage.blit(self.life_list[0], (64, 635))
                self.stage.blit(self.life_list[1], (108, 635))
            elif life_count == 1:
                self.stage.blit(self.life_list[0], (20, 635))
                self.stage.blit(self.life_list[1], (64, 635))
                self.stage.blit(self.life_list[1], (108, 635))
            else:  # 라이프 변수가 0일때 : 게임오버
                self.finish = True
                self.collide.init()
                self.obstacle_count = 270
            self.player.move()
            pygame.display.update()

    def restart(self):
        choice = self.height/2 + 80
        while not self.playAgain:
            self.stage.blit(self.background, (0, 0))
            Ground(self.stage, self.ground, 0, self.height - self.ground.get_height())
            self.text("GAME OVER", GAMEOVER_FONT, (255, 0, 0), self.width/2, self.height/3)
            self.text("Replay", RESTART_FONT, (255, 255, 255), self.width/2, self.height/2 + 80)
            self.text("EXIT", RESTART_FONT, (255, 255, 255), self.width/2, self.height/2 + 180)
            self.text(">", RESTART_FONT, (255, 255, 0), self.width/2 - 80, choice)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playAgain = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        choice += 100
                    if event.key == pygame.K_UP:
                        choice -= 100
                if choice > self.height/2 + 180:  # 두가지 메뉴에서 벗어나지 않게 / 부등호 뒤에 EXIT 의 y 좌표
                    choice = self.height/2 + 180
                if choice < self.height/2 + 80:  # 부등호 뒤에 Replay 의 y 좌표
                    choice = self.height/2 + 80
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if choice == self.height/2 + 80:
                            self.finish = False
                            self.playAgain = True
                            self.exit = False
                        if choice == self.height/2 + 180:
                            self.playAgain = True
                            self.exit = True
game = Stage()
game.menu_choice()
while not game.exit:
    game.play()
    game.restart()
