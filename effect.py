import pygame

class Effect(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.master_image = None
        self.rect = None
        self.left, self.top = 0, 0
        self.columns = 0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 0
        self.frame_height = 0
        self.first_frame = 0
        self.last_frame = 0
        self.last_time = 0
        self.time_length = 4200
        self.magic_on = False

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        image = pygame.Surface([self.frame_width, self.frame_height])
        image.set_colorkey((0, 0, 0))
        image.blit(self.master_image, (0, 0), (0, 0, self.frame_width, self.frame_height))
        self.rect = image.get_rect()
        self.rect.left, self.rect.top = self.left, self.top
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def next(self, current_time, rate):
        if current_time > self.last_time + rate:
            self.frame += 1
            self.last_time = current_time
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def show(self, screen, current_time, rate):
        if self.frame < self.last_frame:
            self.next(current_time, rate)
            screen.blit(self.image, self.rect)
            return True
        else:
            return False

