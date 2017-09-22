import pygame
vec = pygame.math.Vector2
PLAYER_ACC = 0.1  # 가속
PLAYER_FRICTION = -0.08  # 마찰
PLAYER_GRAV = 0.3  # 중력

pygame.display.set_mode((1200, 700))


class Player:
    def __init__(self, stage, ground,  width, height):
        self.stage = stage
        self.walking = True  # 계속 움직이는 것처럼 보이게하는 상태
        self.jumping = False  # 점프 유무
        self.party = True  # 쫓아오는 용사무리
        self.current_frame = 0
        self.last_update = 0
        self.width = width
        self.height = height
        self.image = self.walk_frame[0]
        self.warrior = self.warrior_frame[0]
        self.healer = self.healer_frame[0]
        self.mage = self.mage_frame[0]
        self.ninja = self.ninja_frame[0]
        self.ranger = self.ranger_frame[0]
        self.rect = self.image.get_rect()
        self.pos = vec(340, self.height/2)  # 플레이어 시작 위치 (가로, 세로)
        self.vel = vec(0, 0)  # 속도계산
        self.acc = vec(0, 0)  # 가속계산
        self.ground_height = ground.get_height()

    class Image: #이미지 불러오기
        def __init__(self, filename):
            self.cut_image = pygame.image.load(filename).convert_alpha()

        def get_image(self, x, y, w, h):
            image = pygame.Surface((w, h), pygame.SRCALPHA)  # pygame.SRCALPHA -> png파일 배경 투명하게
            image.blit(self.cut_image, (0, 0), (x, y, w, h))  #( x, y)좌표가 lefttop이고, (w, h)만한 크기로 자르기
            return image

    slime = Image('resources/images/slime3Resized2.png')  # 슬라임이미지 불러오기
    warrior_img = Image('resources/images/warriorResized.png')
    healer_img = Image('resources/images/healerResized.png')
    mage_img = Image('resources/images/mageResized.png')
    ninja_img = Image('resources/images/ninjaResized.png')
    ranger_img = Image('resources/images/rangerResized.png')
    walk_frame = [slime.get_image(0, 0, 72, 72),
                  slime.get_image(72, 0, 72, 72),
                  slime.get_image(1144, 0, 72, 72),
                  slime.get_image(0, 72, 72, 72),
                  slime.get_image(72, 72, 72, 72),
                  slime.get_image(144, 72, 72, 72)]  # 걸어가는 모션(더 추가 가능)

    jump_frame = [slime.get_image(0, 144, 72, 72),
                  slime.get_image(72, 144, 72, 72),
                  slime.get_image(144, 144, 72, 72)]  # 점프할때 모션(더 추가 가능)

    warrior_frame = [warrior_img.get_image(0, 90, 80, 90),
                     warrior_img.get_image(80, 90, 80, 90),
                     warrior_img.get_image(160, 90, 80, 90)]

    healer_frame = [healer_img.get_image(0, 90, 80, 90),
                    healer_img.get_image(80, 90, 80, 90),
                    healer_img.get_image(160, 90, 80, 90)]

    mage_frame = [mage_img.get_image(0, 90, 80, 90),
                  mage_img.get_image(80, 90, 80, 90),
                  mage_img.get_image(160, 90, 80, 90)]

    ninja_frame = [ninja_img.get_image(0, 90, 80, 90),
                   ninja_img.get_image(80, 90, 80, 90),
                   ninja_img.get_image(160, 90, 80, 90)]

    ranger_frame = [ranger_img.get_image(0, 90, 80, 90),
                    ranger_img.get_image(80, 90, 80, 90),
                    ranger_img.get_image(160, 90, 80, 90)]

    def jump(self):
        self.vel.y = -10

    def animate(self):  # 이미지 바꾸는 함수 (애니메이션)
        now = pygame.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking:
            if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frame)
                self.image = self.walk_frame[self.current_frame]

        if self.vel.y != 0:
            self.jumping = True
        if self.jumping:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.jump_frame)
                self.image = self.jump_frame[self.current_frame]

        if self.party:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.warrior_frame)  # 용사파티 프레임수
                self.warrior = self.warrior_frame[self.current_frame]
                self.healer = self.healer_frame[self.current_frame]
                self.mage = self.mage_frame[self.current_frame]
                self.ninja = self.ninja_frame[self.current_frame]
                self.ranger = self.ranger_frame[self.current_frame]

    def move(self): #플레이어 움직이는 함수
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        bottomlimit = self.height - self.ground_height - self.image.get_height() #(게임화면 세로길이) - (Ground 세로길이) - (이미지 세로길이)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.pos.x += 2
        if pressed[pygame.K_LEFT]:
            self.pos.x -= 2

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + PLAYER_GRAV * self.acc

        if self.pos.y > bottomlimit + 1: #바닥(Ground) 밑으로 안떨어지게 하는 if문
            self.pos.y = bottomlimit + 1

        self.rect.midbottom = self.pos

        self.stage.blit(self.image, (self.pos.x, self.pos.y))
