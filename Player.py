import pygame
vec = pygame.math.Vector2
PLAYER_ACC = 0.1
PLAYER_FRICTION = -0.08
PLAYER_GRAV = 0.3


class Player:
    def __init__(self, stage, width, height):
        self.stage = stage
        self.width = width
        self.height = height
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.width/2, self.height/2)
        self.pos = vec(100, self.height - 80)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.vel.y = -10

    def move(self):
        self.acc = vec(0, PLAYER_GRAV)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.pos.x += 1
        if pressed[pygame.K_LEFT]:
            self.pos.x -= 1

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + PLAYER_GRAV * self.acc

        if self.pos.y > self.height - 80:
            self.pos.y = self.height - 80

        self.rect.midbottom = self.pos

        self.stage.blit(self.image, (self.pos.x, self.pos.y))

