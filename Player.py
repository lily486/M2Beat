import pygame
from Image import Image
vec = pygame.math.Vector2
PLAYER_ACC = 0.1  # 가속
PLAYER_FRICTION = -0.08  # 마찰
PLAYER_GRAV = 0.3  # 중력
JUMP_LIMIT = 2
pygame.display.set_mode((1200, 700))


class Player(pygame.Rect):
    def __init__(self, stage, ground,  width, height):
        self.stage = stage
        self.walking = True  # 계속 움직이는 것처럼 보이게하는 상태
        self.jumping = False  # 점프 유무
        self.jump_count = 0  # 점프 횟수
        self.party = True  # 쫓아오는 용사무리
        self.current_frame = 0
        self.last_update_walk = 0
        self.last_update_jumping = 0
        self.last_update_party = 0
        self.width = width
        self.height = height
        self.image = self.walk_frame[0]
        self.warrior1 = self.warrior1_frame[0]
        self.warrior2 = self.warrior2_frame[0]
        self.warrior3 = self.warrior3_frame[0]
        self.warrior4 = self.warrior4_frame[0]
        self.rect = self.image.get_rect()
        self.pos = vec(250, 1200 - 86 - 48 + 4)  # 플레이어 시작 위치 (가로, 세로(=bottomlimit이랑 일치하게))
        self.x = 250
        self.vel = vec(0, 0)  # 속도계산
        self.acc = vec(0, 0)  # 가속계산
        self.ground_height = ground.get_height()

    slime = Image('resources/images/Slime4.png')  # 슬라임이미지 불러오기
    warrior_img = Image('resources/images/warrior_partyResized.png')

    walk_frame = [slime.get_image(0, 96, 48, 48),
                  slime.get_image(48, 96, 48, 48),
                  slime.get_image(96, 96, 48, 48)]  # 걸어가는 모션(더 추가 가능)

    jump_frame = [slime.get_image(0, 144, 48, 48),
                  slime.get_image(48, 144, 48, 48),
                  slime.get_image(96, 144, 48, 48)]  # 점프할때 모션(더 추가 가능)

    warrior1_frame = [warrior_img.get_image(510, 170 + 2, 85, 85),
                      warrior_img.get_image(595, 170 + 2, 85, 85),
                      warrior_img.get_image(680, 170 + 2, 85, 85)]

    warrior2_frame = [warrior_img.get_image(765, 170 + 2, 85, 85),
                      warrior_img.get_image(850, 170 + 2, 85, 85),
                      warrior_img.get_image(935, 170 + 2, 85, 85)]

    warrior3_frame = [warrior_img.get_image(0, 510 + 2, 85, 85),
                      warrior_img.get_image(85, 510 + 2, 85, 85),
                      warrior_img.get_image(170, 510 + 2, 85, 85)]

    warrior4_frame = [warrior_img.get_image(255, 510 + 2, 85, 85),
                      warrior_img.get_image(340, 510 + 2, 85, 85),
                      warrior_img.get_image(425, 510 + 2, 85, 85)]

    def jump(self):
        self.vel.y = -10
        self.jump_count += 1

    def animate(self):  # 이미지 바꾸는 함수 (애니메이션)
        now_walk = pygame.time.get_ticks()
        now_jumping = pygame.time.get_ticks()
        now_party = pygame.time.get_ticks()
        print("Test")

        if self.walking:
            if now_walk - self.last_update_walk > 100:  # 숫자가 작아질수록 애니메이션 속도가 빨라짐
                self.last_update_walk = now_walk
                self.current_frame = (self.current_frame + 1) % len(self.walk_frame)
                self.image = self.walk_frame[self.current_frame]

        if self.vel.y != 0:
            self.jumping = True
        elif self.pos.y == self.height - self.ground_height - self.image.get_height():
            self.jumping = False

        if self.jumping and not self.walking:
            if now_jumping - self.last_update_jumping > 100:
                self.last_update_jumping = now_jumping
                self.current_frame = (self.current_frame + 1) % len(self.jump_frame)
                self.image = self.jump_frame[self.current_frame]

        if self.party:
            if now_party - self.last_update_party > 100:
                self.last_update_party = now_party
                self.current_frame = (self.current_frame + 1) % len(self.warrior1_frame)  # 용사파티 프레임수
                self.warrior1 = self.warrior1_frame[self.current_frame]
                self.warrior2 = self.warrior2_frame[self.current_frame]
                self.warrior3 = self.warrior3_frame[self.current_frame]
                self.warrior4 = self.warrior4_frame[self.current_frame]

    def move(self):  # 플레이어 움직이는 함수
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        bottomlimit = self.height - self.ground_height - self.image.get_height()
        # bottiomlimit = (게임화면 세로길이) - (Ground 세로길이) - (플레이어 세로길이)
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + PLAYER_GRAV * self.acc

        if self.pos.y > bottomlimit + 4:  # 바닥(Ground) 밑으로 안떨어지게 하는 if문
            self.pos.y = bottomlimit + 4  # +4는 바닥이랑 제대로 맞추려고 ㅎ..
        for move in pygame.event.get():
            if self.jump_count == JUMP_LIMIT:
                if self.pos.y == bottomlimit + 4:
                    self.jump_count = 0
                    self.jumping = False
            if move.type == pygame.KEYDOWN:
                if move.key == pygame.K_UP and self.jump_count < JUMP_LIMIT:
                    self.jump()
                elif move.key == pygame.K_RIGHT:
                    pass
                elif move.key == pygame.K_LEFT:
                    pass
        self.rect.midbottom = self.pos

        self.stage.blit(self.image, (self.pos.x, self.pos.y))
        self.stage.blit(self.warrior1, (150, self.height - self.ground_height - self.warrior1.get_height() + 1))
        self.stage.blit(self.warrior2, (100, self.height - self.ground_height - self.warrior2.get_height() + 1))
        self.stage.blit(self.warrior3, (50, self.height - self.ground_height - self.warrior3.get_height() + 1))
        self.stage.blit(self.warrior4, (0, self.height - self.ground_height - self.warrior4.get_height() + 1))

    def intro(self):
        self.animate()
        bottomlimit = self.height - self.ground_height - self.image.get_height()
        if self.x < self.width + 300:
            self.stage.blit(self.image, (self.x, bottomlimit + 4))
            self.stage.blit(self.warrior1, (self.x - 150, self.height - self.ground_height - self.warrior1.get_height() + 1))
            self.stage.blit(self.warrior2, (self.x - 200, self.height - self.ground_height - self.warrior2.get_height() + 1))
            self.stage.blit(self.warrior3, (self.x - 250, self.height - self.ground_height - self.warrior3.get_height() + 1))
            self.stage.blit(self.warrior4, (self.x - 300, self.height - self.ground_height - self.warrior4.get_height() + 1))
            self.x += 3
        else:
            self.x = 0
