import pygame
import random
from Player import Player
from Image import Cloud, Image
from Timer import Timer
from Obstacle import Obstacle
from Collide import Collide
from Rhythm import Rhythm
from Rank import Rank


pygame.font.init()
JUMP_LIMIT = 2  # 점프 한도

TITLE_FONT = pygame.font.Font('resources/fonts/CulDeSac.ttf', 90)
COUNT_FONT = pygame.font.Font('resources/fonts/Pixel.ttf', 80)
COMBO_FONT = pygame.font.Font('resources/fonts/AmaticSC-Bold.ttf', 40)
MENU_FONT = pygame.font.Font('resources/fonts/CALIBRATE1.ttf', 30)
GAMEOVER_FONT = pygame.font.Font('resources/fonts/grishenko_novoye_nbp.ttf', 60)
VALUE_FONT = pygame.font.Font('resources/fonts/grishenko_novoye_nbp.ttf', 25)

SPEED = 3  # 배경(구름), 장애물 움직이는 속도
ENTER = 13  # 엔터 키코드 (ASCII)


class Stage:
    width = 1200  # 가로
    height = 700  # 세로
    FPS = 30
    fpsClock = pygame.time.Clock()
    player = None
    background = pygame.image.load('resources/images/backResized.png')
    ground = pygame.image.load('resources/images/ground.png')
    cloud_list = [pygame.image.load('resources/images/cloud1.png'),
                  pygame.image.load('resources/images/cloud2.png'),
                  pygame.image.load('resources/images/cloud3.png'),
                  pygame.image.load('resources/images/cloud4.png')]
    finish = False
    playAgain = True
    exit = False
    life = Image('resources/images/heart_Resized2.png')  # 라이프 이미지 불러오기
    life_list = [life.get_image(0, 0, 36, 44),  # 꽉 찬 하트
                 life.get_image(36, 0, 36, 44)]  # 빈 하트
    box_img = pygame.image.load('resources/images/squareResized.png')

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("M2Beat")
        self.stage = pygame.display.set_mode((self.width, self.height))
        self.stage.blit(self.background, (0, 0))
        self.player = Player(self.stage, self.width, self.height)
        self.count = 0  # 점프한 횟수(K_UP 누른 횟수)
        self.cloud_count = 1
        self.clouds = []
        self.intro_clouds = []
        self.obstacles = []
        self.key = None
        self.collide = Collide(self.player, self.obstacles, self.stage)
        self.rhythm = Rhythm(self.obstacles, self.stage)
        self.score = 0
        self.bX = 1200
        self.bXtimer = 200
        self.Rank = Rank()
        self.obstacle_value = False

    def menu_choice(self):
        start = False
        pygame.display.update()
        menu = self.height/2
        pygame.mixer.music.load('resources/audio/intro.mp3')
        pygame.mixer.music.play(-1, 0.0)

        while not start:  # 초기 화면 설정 (Intro 화면 설정)
            self.stage.blit(self.background, (0, 0))
            intro_clouds = [Cloud(self.stage, self.cloud_list[0], 15, 87, 0),
                            Cloud(self.stage, self.cloud_list[1], 315, 32, 0),
                            Cloud(self.stage, self.cloud_list[2], 615, 45, 0),
                            Cloud(self.stage, self.cloud_list[3], 915, 25, 0)]
            for intro_cloud in intro_clouds:
                intro_cloud.move()
            self.text("M2BEAT", TITLE_FONT, (0, 0, 0), self.width/2, self.height/4 + 30)
            self.text("Start", MENU_FONT, (0, 0, 0), self.width/2, self.height/2)
            self.text("Exit", MENU_FONT, (0, 0, 0), self.width/2, self.height/2 + 100)
            self.text(">", MENU_FONT, (255, 255, 0), self.width/2 - 60, menu)
            self.player.intro()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = True
                    self.finish = True
                    self.exit = True
                    self.playAgain = False
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
                    if event.key == ENTER:
                        if menu == self.height/2:
                            start = True
                            pygame.mixer.music.stop()
                        if menu == self.height/2 + 100:
                            start = True
                            self.finish = True
                            self.exit = True
                            self.playAgain = False
                            pygame.mixer.music.stop()

    def text(self, text, font, color, x, y):  # 텍스트 그리는 함수
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        rect.midtop = (x, y)
        self.stage.blit(surface, rect)

    def update(self):  # 플레이어 움직일 때 잔상 안남게 + 플레이어 움직임
        self.stage.blit(self.background, (-self.bX, 0))
        if self.bX > 1:
            self.stage.blit(self.background, (-(self.bX - 1200), 0))
        self.bX += SPEED
        if self.bX >= 1200:
            self.bX = 0
        if self.bXtimer == 0:
            self.bXtimer = 200
        else:
            self.bXtimer -= 1
        self.player.move()
        self.cloud_count -= 1
        if self.cloud_count == 0:
            cloud = Cloud(self.stage, self.cloud_list[random.randint(0, 3)], self.width, random.randint(0, 100), SPEED)
            self.clouds.append(cloud)
            self.cloud_count = 100  # cloud_count 가 작아지면 구름 갯수가 많아짐
        for cloud in self.clouds:
            cloud.move()
        if self.clouds[0].x == -350:
            self.clouds.pop(-(len(self.clouds))-1)
        self.stage.blit(self.box_img, (850, self.height - 90 - 145))
        value_list = self.rhythm.ReturnValue()
        for value in value_list:
            # value[0] : Perfect/Great/Good 판정 글자 / value[1] : 글자의 y축 이동
            self.text(value[0], VALUE_FONT, (102, 102, 255), 880, self.height - self.ground.get_height() - value[1])
            value[1] += 1
            if value[1] == 300:
                value_list.remove(value)

    def play(self):
        pygame.mixer.music.load('resources/audio/bgm.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.pause()
        self.collide = Collide(self.player, self.obstacles, self.stage)
        self.playAgain = True
        clock = Timer(6, self.finish, self.stage, self.height)  # 시작하기 전 5초 세기 (몇 초 셀건지 바꾸려면 +1 해서 설정)
        clock.timer()
        clock.rhythm()
        clock.init()
        self.obstacles = clock.ReturnObj()
        self.rhythm = Rhythm(self.obstacles, self.stage)
        while not self.finish:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                    self.exit = True
                    self.playAgain = False
                    pygame.mixer.music.stop()
            self.update()
            self.player.move()
            if clock.Return() > 0:
                self.text(str(clock.Return()), COUNT_FONT, (0, 0, 0), self.width / 2, self.height / 2)

            for obj in self.obstacles:
                obj.move()
            self.collide.collider()
            self.rhythm.rhythm()
            combo = self.rhythm.ReturnCombo()
            self.text("COMBO", COMBO_FONT, (0, 0, 0), 1060, 400)
            self.text(str(combo), COMBO_FONT, (0, 0, 0), 1000, 400)
            life_count = self.rhythm.ReturnLife()
            if life_count == 3:
                self.stage.blit(self.life_list[0], (520, 635))
                self.stage.blit(self.life_list[0], (564, 635))
                self.stage.blit(self.life_list[0], (608, 635))
            elif life_count == 2:
                self.stage.blit(self.life_list[0], (520, 635))
                self.stage.blit(self.life_list[0], (564, 635))
                self.stage.blit(self.life_list[1], (608, 635))
            elif life_count == 1:
                self.stage.blit(self.life_list[0], (520, 635))
                self.stage.blit(self.life_list[1], (564, 635))
                self.stage.blit(self.life_list[1], (608, 635))
            else:  # 라이프 변수가 0일때 : 게임오버
                self.finish = True
                self.collide.init()
                pygame.mixer.music.stop()
                clock.Stop()
                clock.init()
            self.score = self.rhythm.ReturnScore()
            self.text("SCORE : ", COMBO_FONT, (0, 0, 0), self.width/2 - 50, 50)
            self.text(str(self.score), COMBO_FONT, (0, 0, 0), self.width/2 + 50, 50)
            pygame.display.update()

    def restart(self):
        choice = self.height/2 + 80
        name = []
        inputDone = False
        while self.playAgain:
            self.stage.blit(self.background, (0, 0))
            self.text("GAME OVER", GAMEOVER_FONT, (255, 0, 0), self.width/2, self.height/3)
            self.text("Replay", MENU_FONT, (0, 0, 0), self.width/2, self.height/2 + 80)
            self.text("EXIT", MENU_FONT, (0, 0, 0), self.width/2, self.height/2 + 180)
            self.text(">", MENU_FONT, (255, 255, 0), self.width/2 - 80, choice)
            self.text("YOUR SCORE : ", MENU_FONT, (0, 0, 0), self.width/2 - 60, self.height/3 - 100)
            self.text(str(self.score), MENU_FONT, (0, 0, 0), self.width/2 + 85, self.height/3 - 100)
            self.text("YOUR NAME : ", MENU_FONT, (0, 0, 0), self.width/2 - 60, self.height/3 - 150)
            if len(name) != 0:
                name_x = self.width/2 + 65
                for i in name:
                    self.text(i, MENU_FONT, (0, 0, 0), name_x, self.height/3 - 150)
                    name_x += 20
            if inputDone:
                self.text("INPUT IS DONE !", VALUE_FONT, (255, 0, 0), self.width/2, self.height/2 + 20)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playAgain = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        choice += 100
                    if event.key == pygame.K_UP:
                        choice -= 100
                    if event.unicode.isalpha():
                        if not len(name) == 3:
                            name.append(event.unicode.upper())
                    if event.key == pygame.K_BACKSPACE:
                        if not len(name) == 0:
                            name.pop()
                    if event.key == pygame.K_INSERT and not inputDone:
                        namae = "".join(name)
                        score_list = [self.score, namae]
                        self.Rank.writing(str(score_list))
                        self.Rank.reading()
                        inputDone = True
                if choice > self.height/2 + 180:  # 두가지 메뉴에서 벗어나지 않게 / 부등호 뒤에 EXIT 의 y 좌표
                    choice = self.height/2 + 180
                if choice < self.height/2 + 80:  # 부등호 뒤에 Replay 의 y 좌표
                    choice = self.height/2 + 80
                if event.type == pygame.KEYDOWN:
                    if event.key == ENTER:
                        if choice == self.height/2 + 80:
                            self.finish = False
                            self.playAgain = False
                            self.exit = False
                        if choice == self.height/2 + 180:
                            self.playAgain = False
                            self.exit = True
game = Stage()
game.menu_choice()
while not game.exit:
    game.play()
    game.restart()
