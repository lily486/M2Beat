import pygame
from Player import Player
JUMPLIMIT = 2 #점프 한도


class Stage:
    width = 1200 #가로
    height = 700 #세로
    FPS = 30
    fpsClock = pygame.time.Clock()
    player = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("M2Beat")
        self.stage = pygame.display.set_mode((self.width, self.height))
        self.stage.fill((0, 0, 0)) #배경 색
        self.player = Player(self.stage, self.width, self.height)
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
        self.stage.fill((0, 0, 0))
        self.draw_text("PRESS ANY KEY", 90, (255, 255, 255), self.width/2, self.height/2)
        pygame.display.update()
        self.press_any_key()

    class Ground: #플레이화면에서 땅(녹색)
        def __init__(self, stage, x, y, w, h):
            self.stage = stage
            self.ground_image = pygame.Surface((w, h))
            self.ground_image.fill((0, 255, 0))
            self.x = x
            self.y = y
            self.stage.blit(self.ground_image, (self.x, self.y))

    def update(self): #플레이어 움직일 때 잔상 안남게 + 플레이어 움직임
        self.stage.fill((0, 0, 0))
        self.player.move()
        self.Ground(self.stage, 0, self.height - 50, self.width, 50)

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
                        self.count = 0
            self.update()
            pygame.display.update()


game = Stage()
game.start_screen()
game.start()
