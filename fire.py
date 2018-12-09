import pygame


class Fire(pygame.sprite.Sprite):
    def __init__(self, file, speed):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('image/%s_down.png' % file).convert_alpha(), pygame.image.load('image/%s_left.png' % file).convert_alpha(), pygame.image.load('image/%s_right.png' % file).convert_alpha(), pygame.image.load('image/%s_up.png' % file).convert_alpha()]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = None
        self.live_time = 60
        self.moving_speed = speed


    def move(self):
        self.rect = self.rect.move(self.speed)

    def prepare(self, direction, chara_rect):
        self.direction = direction
        if self.direction == 0:
            self.image = self.images[0]
            self.rect.left, self.rect.top = chara_rect.midbottom
            self.rect.left -= 6
            self.speed = [0, self.moving_speed]
        elif self.direction == 1:
            self.image = self.images[1]
            self.rect.left, self.rect.top = chara_rect.midleft
            self.rect.top -= 6
            self.speed = [-self.moving_speed, 0]
        elif self.direction == 2:
            self.image = self.images[2]
            self.rect.left, self.rect.top = chara_rect.midright
            self.rect.top -= 6
            self.speed = [self.moving_speed, 0]
        elif self.direction == 3:
            self.image = self.images[3]
            self.rect.left, self.rect.top = chara_rect.midtop
            self.rect.left -= 6
            self.speed = [0, -self.moving_speed]

