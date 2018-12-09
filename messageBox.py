import pygame


class MessageBox():
    def __init__(self, file, position, length, color):
        self.file = file
        self.length = length
        self.color = color
        self.image = pygame.image.load(self.file).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.chara = None
        self.message = None
        self.show_message = False

    def render_talk(self, text, person):
        self.image = pygame.image.load(self.file).convert()
        myfont = pygame.font.Font(None, 30)
        front = 0
        #每行70字符
        stop = self.length
        top = 50
        while stop < len(text)+self.length:
            text_split = text[front:stop]
            front = stop
            stop += self.length
            top += 20
            text_image = myfont.render(text_split, True, self.color)
            text_image_rect = text_image.get_rect()
            text_image_rect.left = 10
            text_image_rect.top = top
            self.image.blit(text_image, text_image_rect)
        person_image = pygame.image.load(person).convert()
        person_image_rect = person_image.get_rect()
        person_image_rect.left = 10
        person_image_rect.top = 5
        self.image.blit(person_image, person_image_rect)

    def render(self, text, font):
        self.image = pygame.image.load(self.file).convert()
        myfont = pygame.font.Font(font, 30)
        front = 0
        # 每行70字符
        stop = self.length
        top = 30
        while stop < len(text) + self.length:
            text_split = text[front:stop]
            front = stop
            stop += self.length
            top += 20
            text_image = myfont.render(text_split, True, self.color)
            text_image_rect = text_image.get_rect()
            text_image_rect.left = 10
            text_image_rect.top = top
            self.image.blit(text_image, text_image_rect)