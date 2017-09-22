import pygame, random
from Player import Player
JUMPLIMIT = 2 #점프 한도


class Stage:
    width = 1200 #가로
    height = 700 #세로
    FPS = 30
    fpsClock = pygame.time.Clock()
    player = None
    background = pygame.image.load('resources/images/backgroundCutResized.png')
    ground = pygame.image.load('resources/images/ground.png')
    cloud_list = [pygame.image.load('resources/images/cloud1.png'),
                  pygame.image.load('resources/images/cloud2.png'),
                  pygame.image.load('resources/images/cloud3.png'),
                  pygame.image.load('resources/images/cloud4.png')]
    clouds = []
    cloud_count = 1

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("M2Beat")
        self.stage = pygame.display.set_mode((self.width, self.height))
        self.stage.blit(self.background, (0, 0)) #배경 색
        self.player = Player(self.stage, self.ground, self.width, self.height)
        self.count = 0 #점프한 횟수(K_UP누른 횟수)

    def press_any_key(self):
        start = False
        while not start:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    start = True

    def draw_text(self, text, size, color, x, y): #시작화면 텍스트 만들 때 사용
        font = pygame.font.Font('freesansbold.ttf', size)
        text_suface = font.render(text, True, color)
        text_rect = text_suface.get_rect()
        text_rect.midtop = (x, y)
        self.stage.blit(text_suface, text_rect)

    def start_screen(self): #시작화면
        self.stage.blit(self.background, (0, 0))
        self.draw_text("PRESS ANY KEY", 90, (255, 255, 255), self.width/2, self.height/2)
        pygame.display.update()
        self.press_any_key()

    class Cloud:
        def __init__(self, stage, cloud, width, y):
            self.stage = stage
            self.cloud = cloud
            self.x = width
            self.y = y
            self.speed = 4

        def move(self):
            self.x -= self.speed
            self.stage.blit(self.cloud, (self.x, self.y))

    class Ground: #플레이화면에서 땅
        def __init__(self, stage, ground, x, y):
            self.stage = stage
            self.ground_image = ground
            self.x = x
            self.y = y
            self.stage.blit(self.ground_image, (self.x, self.y))
            self.stage.blit(self.ground_image, (self.x + self.ground_image.get_width(), self.y))

    def update(self): #플레이어 움직일 때 잔상 안남게 + 플레이어 움직임
        self.stage.blit(self.background, (0, 0))
        self.Ground(self.stage, self.ground, 0, self.height - self.ground.get_height())
        self.player.move()
        self.cloud_count -= 1
        if self.cloud_count == 0:
            cloud = self.Cloud(self.stage, self.cloud_list[random.randint(0, 3)], self.width, random.randint(0, 100))
            self.clouds.append(cloud)
            self.cloud_count = 120  # cloud_count가 작아지면 구름 갯수가 많아짐
        for cloud in self.clouds:
            cloud.move()
        if self.clouds[0].x == 0:
            self.clouds.pop()

    def start(self):
        finish = False
        while not finish:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True
                if event.type == pygame.KEYDOWN: #한번 눌렀을 때 실행
                    if event.key == pygame.K_UP and self.count < JUMPLIMIT:
                        self.player.jump()
                        self.count += 1
                    elif self.count == JUMPLIMIT:
                        if self.player.pos.y == self.height - self.ground.get_height() - self.player.image.get_height() + 1:
                            self.count = 0
            self.player.move()
            self.update()
            pygame.display.update()

game = Stage()
game.start_screen()
game.start()
