import pygame
vec = pygame.math.Vector2


class Player :
    def __init__(self, stage, width, height):
        self.stage = stage
        self.width = width
        self.height = height
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.width/2, self.height/2)
        self.pos = vec(0, self.height-50)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.black = pygame.Surface((30, 30))
        self.black.fill((0,0,0))

    def jump(self):
        self.vel.y = -10

    def move(self):
        self.acc = vec(0, 0.5)
        pressed = pygame.key.get_pressed()
        keydown = pygame.KEYDOWN
        if keydown == pygame.K_UP:
            self.jump()
        if pressed[pygame.K_DOWN]:
            pass
        if pressed[pygame.K_RIGHT]:
            self.acc.x = 0.35
        if pressed[pygame.K_LEFT]:
            self.acc.x = -0.35

        self.acc.x += self.vel.x * (-0.08)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        if self.pos.x > self.width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.width
            self.stage.blit(self.black, (0, self.pos.y))
        if self.pos.y > self.height - 50:
            self.pos.y = self.height - 80

        self.stage.blit(self.image, (self.pos.x, self.pos.y))
        self.stage.blit(self.black, (self.pos.x - 30, self.pos.y))
        self.stage.blit(self.black, (self.pos.x + 30, self.pos.y))