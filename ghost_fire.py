import pygame
from random import *

class GhostFire(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/fire.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.side = [choice([-1, 1]), choice([-1, 1])]
        self.speed = speed
        self.alive = True
        self.hitted_time = 0
        self.blood = -1
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect = self.rect.move((self.speed[0]*self.side[0], self.speed[1]*self.side[1]))


