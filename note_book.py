import pygame
from messageBox import *

"""
note = {
  bool  'flag': "", 是否得到
  str  'text': "", 信息
  int  'page': "0,", 所在页面
  message  'box': '', messagbox
  bool  'had_box': '' 创建过messagebox
}
{'flag': False, 'text': "", 'page': None, 'box': None, 'had_box': False}
"""
class NoteBook():
    def __init__(self):
        self.image = pygame.image.load('image/notebook.jpg').convert()
        self.image = pygame.transform.scale(self.image, (600, 400))
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 100
        self.show = False
        self.notes_show = 0
        self.c_page = 0
        self.notes = [{'flag': False, 'text': "Weird collgue: A girl with a tail  and the other one without a feet ...and I swear that cat can talk!", 'page': None, 'box': None, 'had_box': False}, \
                      {'flag': False, 'text': "A wondering spirit: We saw a spirit wondering on the street...must be lefted from last night. It seems that she wanted to tell us something about her death.", 'page': None, 'box': None, 'had_box': False}, \
                      {'flag': False, 'text': "The dead girl looks just the same as the spirit we saw in the morning! It must be her. If she is not the target, than who? ", 'page': None, 'box': None, 'had_box': False}, \
                      {'flag': False, 'text': "I'm pretty sure I have never seen this man before. But the way he looked at me...it's like he has known me for    years.", 'page': None, 'box': None, 'had_box': False}, \
                      {'flag': False, 'text': "That ghost is weird, she looks really alive...and it seems that she wanted to tell us something.", 'page': None, 'box': None, 'had_box': False}, \
                      {'flag': False, 'text': "After the Reincarnation Dial turns three circles on the Karma Stone, half of my life will be shared with you. Then, even though we can't  live together, we die together", 'page': None, 'box': None, 'had_box': False}, \
                      {'flag': False, 'text': "The thing that attacked the dead girl is the starved ghost! Shen and Li are in danger!", 'page': None, 'box': None, 'had_box': False}]
        self.max_page = self.notes_show // 2

    def render(self):
        self.image = pygame.image.load('image/notebook.jpg').convert()
        self.image = pygame.transform.scale(self.image, (600, 400))
        for each in self.notes:
            if each['flag'] and not each['had_box']:
                page = self.notes_show // 2
                if self.notes_show % 2 == 0:
                    left = 30
                else:
                    left = 330
                top = 0
                box = MessageBox('image/note_detail.jpg', (left, top), 19, (0, 0, 0))
                box.render(each['text'], "font/england.ttf")
                self.notes_show += 1
                self.max_page = self.notes_show // 2
                each['had_box'] = True
                each['box'] = box
                each['page'] = page
        for each in self.notes:
            if each['had_box'] and each['page'] == self.c_page:
                self.image.blit(each['box'].image, each['box'].rect)