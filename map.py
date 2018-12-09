import pygame


class Map(pygame.sprite.Sprite):
    """"文件地址， 绘制坐标， 人物起始位置(map1有效)"""
    def __init__(self, filename, x, y, s_x, s_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y
        self.buildings = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.charas = pygame.sprite.Group()
        self.entrances = []
        self.start_left, self.start_top = s_x, s_y
        self.music_on = False
        self.first_in = True
        self.tick = 0

    def add_building(self, building):
        self.buildings.add(building)

    def add_entrance(self, entrance):
        self.entrances.append(entrance)

    def add_chara(self, character):
        self.charas.add(character)

    def set_map(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()



