import pygame, random
from Player import Player
JUMPLIMIT = 2  # 점프 한도


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
            self.draw_title("M2Beat", 90, (255, 255, 255), self.width/2, self.height/4 - 20)
            self.draw_text("Start", 60, (0, 0, 0), self.width/2 + 20, self.height/2)
            self.draw_text("EXIT", 60, (0, 0, 0), self.width/2 + 20, self.height/2 + 100)
            self.draw_text(">", 60, (0, 0, 0), self.width/2 - 50, menu)
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
                    if event.key == pygame.K_KP_ENTER:
                        if menu == self.height/2:
                            start = True
                        if menu == self.height/2 + 100:
                            start = True
                            self.finish = True

    def draw_title(self, text, size, color, x, y):  # 시작화면 텍스트 만들 때 사용
        title_font = pygame.font.Font('resources/fonts/CulDeSac.ttf', size)
        text_title = title_font.render(text, True, color)
        text_rect = text_title.get_rect()
        text_rect.midtop = (x, y)
        self.stage.blit(text_title, text_rect)

    def draw_text(self, text, size, color, x, y):  # 시작화면 텍스트 만들 때 사용
        text_font = pygame.font.Font('resources/fonts/AmaticSC-Bold.ttf', size)
        text_surface = text_font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.stage.blit(text_surface, text_rect)

    class Cloud:
        def __init__(self, stage, cloud, width, y):
            self.stage = stage
            self.cloud = cloud
            self.x = width
            self.y = y
            self.speed = 8

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

    def update(self):  # 플레이어 움직일 때 잔상 안남게 + 플레이어 움직임
        self.stage.blit(self.background, (0, 0))
        self.Ground(self.stage, self.ground, 0, self.height - self.ground.get_height())
        self.player.move()
        self.cloud_count -= 1
        if self.cloud_count == 0:
            cloud = self.Cloud(self.stage, self.cloud_list[random.randint(0, 3)], self.width, random.randint(0, 100))
            self.clouds.append(cloud)
            self.cloud_count = 70  # cloud_count가 작아지면 구름 갯수가 많아짐
        for cloud in self.clouds:
            cloud.move()
        if self.clouds[0].x == -350:
            self.clouds.pop(-(len(self.cloud_list))-1)

    def start(self):
        while not self.finish:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                if event.type == pygame.KEYDOWN:  # 한번 눌렀을 때 실행
                    if event.key == pygame.K_UP and self.count < JUMPLIMIT:
                        self.player.jump()
                        self.count += 1
                    elif self.count == JUMPLIMIT:
                        if self.player.pos.y == self.height - self.ground.get_height() - self.player.image.get_height() + 4:
                            self.count = 0
                    self.player.jumping = False
            self.player.move()
            self.update()
            pygame.display.update()

game = Stage()
game.menu_choice()
game.start()
