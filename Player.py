import pygame
vec = pygame.math.Vector2
PLAYER_ACC = 0.1
PLAYER_FRICTION = -0.08
PLAYER_GRAV = 0.3


class Image:
    def __init__(self, filename):
        self.cut_image = pygame.image.load(filename).convert()

    def get_image(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.cut_image, (0, 0), (x, y, w, h))
        return image


class Player:
    def __init__(self, stage, width, height):
        self.stage = stage
        self.walking = True
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_image()
        self.width = width
        self.height = height
        self.image = self.walk_frame[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.width/2, self.height/2)
        self.pos = vec(100, self.height - 80)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.walk_frame = None
        self.jump_frame = None

    def load_image(self):
        self.walk_frame = [self.stage.slime.get_image(0, 0, 30, 40),
                           self.stage.slime.get_image(30, 0, 30, 40)]
        self.jump_frame = [self.stage.slime.get_image(60, 0, 30, 40),
                           self.stage.slime.get_imgae(90, 0, 30, 40)]

    def jump(self):
        self.vel.y = -10

    def animate(self):
        now = pygame.time.get_ticks()

        if self.walking:
            if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frame)
            if self.vel.y != 0:
                self.jumping = True

        if self.jumping:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 1
                self.image = self.jump_frame

    def draw(self):
        self.stage.blit(self.image, (self.pos.x, self.pos.y))

    def move(self):
        self.acc = vec(0, PLAYER_GRAV)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            pass
        if pressed[pygame.K_LEFT]:
            pass

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + PLAYER_GRAV * self.acc

        if self.pos.y > self.height - 80:
            self.pos.y = self.height - 80

        self.rect.midbottom = self.pos

        self.stage.blit(self.image, (self.pos.x, self.pos.y))

