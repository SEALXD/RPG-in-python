import pygame
import math


class Character(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        # self.target_surface = target
        ## 当前帧图片
        self.image = None
        ## 移动序列图
        self.master_image = None
        self.rect = None
        ## 用于设置初始位置
        self.left, self.top = 0, 0
        ## 序列图列数
        self.columns = 0
        ## direction  up=3, right=2, left=1, down=0
        self.direction = 0
        ## 当前所在帧
        self.frame = 0
        self.old_frame = -1
        ## 每一帧图片宽、高
        self.frame_width = 0
        self.frame_height = 0
        ## 用于帧数循环
        self.first_frame = 0
        self.last_frame = 0
        self.last_time = 0
        ## 是否处于移动状态
        self.moving = False
        ## speed
        self.speed = [0, 0]
        ## 用于碰撞检测
        self.mask = None
        """角色交互点"""
        self.check_point = None
        self.messages = []
        self.person = []
        """用于触发事件或物品"""
        self.event_id = -2
        self.item_flag = 0 #2表示需要给出，-2说明已经给出 ，0说明没有此操作
        self.item_id = -2
        self.once = 0
        """生命值???"""
        self.blood = 8
        self.BLOOD = 8
        """存活??"""
        self.alive = True
        self.hitted_time = 0
        self.fire_time = 0
        """子弹"""
        self.bullets = pygame.sprite.Group()
        self.moving_speed = speed
        self.sound_time = 0
        self.radius = 200
        self.magic_now = False
        self.magic_point = None
        self.find = False
        self.magic = None
        self.magic_time = 0

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        image = pygame.Surface([self.frame_width, self.frame_height])
        image.set_colorkey((0, 0, 0))
        image.blit(self.master_image, (0, 0), (0, 0, self.frame_width, self.frame_height))
        self.rect = image.get_rect()
        self.rect.left, self.rect.top = self.left, self.top
        # self.rect = self.left, self.top, self.frame_width, self.frame_height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate):
        ## 该方向上始末帧
        self.first_frame = self.direction * self.columns
        self.last_frame = self.first_frame + self.columns - 1
        ## 当前帧图不在该方向上第一张
        if self.frame < self.first_frame:
            self.frame = self.first_frame
        ## 每rate换一帧
        if self.moving:
            if current_time > self.last_time + rate:
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = self.first_frame
                self.last_time = current_time
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.mask = pygame.mask.from_surface(self.image)
            self.old_frame = self.frame
            self.check_point = self.rect.left - self.rect.width, self.rect.left + self.rect.width,\
                               self.rect.top - self.rect.height, self.rect.top + self.rect.height

    def go_up(self, c_map, charas):
        self.moving = True
        ## 确定方向
        self.direction = 3
        self.speed = [0, -self.moving_speed]
        ## 改变位置
        self.rect = self.rect.move(self.speed)
        if self.collide_test(self, c_map, charas):
            self.speed = [0, self.moving_speed]
            self.rect = self.rect.move(self.speed)

    def go_down(self, c_map, charas):
        self.moving = True
        self.direction = 0
        self.speed = [0, self.moving_speed]
        self.rect = self.rect.move(self.speed)
        if self.collide_test(self, c_map, charas):
            self.speed = [0, -self.moving_speed]
            self.rect = self.rect.move(self.speed)

    def go_left(self, c_map, charas):
        self.moving = True
        self.direction = 1
        self.speed = [-self.moving_speed, 0]
        self.rect = self.rect.move(self.speed)
        if self.collide_test(self, c_map, charas):
            self.speed = [self.moving_speed, 0]
            self.rect = self.rect.move(self.speed)

    def go_right(self, c_map, charas):
        self.moving = True
        self.direction = 2
        self.speed = [self.moving_speed, 0]
        self.rect = self.rect.move(self.speed)
        if self.collide_test(self, c_map, charas):
            self.speed = [-self.moving_speed, 0]
            self.rect = self.rect.move(self.speed)

    def update_bullet(self, screen, c_map, charas, ticks):
        for each in self.bullets:
            """子弹已经被发射"""
            if each.active:
                """存在时间-1, 为0消亡"""
                each.live_time -= 1
                if each.live_time == 0:
                    each.active = False
                if each.active:
                    each.move()
                """谁被子弹打到了，出来blood -1"""
                chara_hitted = pygame.sprite.spritecollide(each, charas, False, pygame.sprite.collide_mask)
                if chara_hitted:
                    for people in chara_hitted:
                        people.hitted_time = ticks
                        people.blood -= 1
                """哎呀，撞到什么东西了，消亡"""
                if self.collide_test(each, c_map, charas):
                    each.active = False
                """嘿嘿，我还活着，还能继续跑"""
                if each.active:
                    screen.blit(each.image, each.rect)

    """sound pause"""
    def attack(self, ticks, time_pause, living_time, sound, sound_pause):
        if ticks > self.fire_time + time_pause:
            self.fire_time = ticks
            for each in self.bullets:
                if not each.active:
                    if ticks > self.sound_time + sound_pause:
                        self.sound_time = ticks
                        sound.play()
                    each.active = True
                    each.live_time = living_time
                    each.prepare(self.direction, self.rect)
                    break

    def collide_test(self, main_chara, c_map, charas):
        """人物与建筑碰撞"""
        if pygame.sprite.spritecollide(main_chara, c_map.buildings, False, pygame.sprite.collide_mask):
            return True
        """人物与物品碰撞"""
        if pygame.sprite.spritecollide(main_chara, c_map.items, False, pygame.sprite.collide_mask):
            return True
        """人物与人物碰撞"""
        if pygame.sprite.spritecollide(main_chara, charas, False, pygame.sprite.collide_mask):
            return True
        return False

    # from left to right
    def go_around_x(self, c_map, chara_group, x1, x2):
        ## direction  up=3, right=2, left=1, down=0
        if self.rect.left == x1:
            self.go_right(c_map, chara_group)
        elif x1 < self.rect.left < x2:
            if self.direction == 2:
                self.go_right(c_map, chara_group)
            else:
                self.go_left(c_map, chara_group)
        elif self.rect.left == x2:
            self.go_left(c_map, chara_group)

    # from top to bottom
    def go_around_y(self, c_map, chara_group, y1, y2):
        ## direction  up=3, right=2, left=1, down=0
        if self.rect.top == y1:
            self.go_down(c_map, chara_group)
        elif y1 < self.rect.top < y2:
            if self.direction == 0:
                self.go_down(c_map, chara_group)
            else:
                self.go_up(c_map, chara_group)
        elif self.rect.top == y2:
            self.go_up(c_map, chara_group)

    def detect(self, chara):
        if self.radius >= math.sqrt(
                (self.rect.left - chara.rect.left) ** 2 + (self.rect.top - chara.rect.top) ** 2):
            return True

    def perform_magic(self, screen, his_magic, ticks, point, chara, rate):
        his_magic.rect.left, his_magic.rect.top = point
        showing = his_magic.show(screen, ticks, rate)
        if not his_magic.magic_on:
            if his_magic.frame >= his_magic.last_frame // 2:
                if self.at_point(chara, (
                his_magic.rect.left, his_magic.rect.right, his_magic.rect.top, his_magic.rect.bottom)):
                    chara.blood -= 1
                    chara.hitted_time = ticks
                    his_magic.magic_on = True
        if showing:
            return True
        else:
            his_magic.frame = his_magic.first_frame
            return False

    def at_point(self, chara, point):
        if point[0] <= chara.rect.left <= point[1] and point[2] <= chara.rect.top <= point[3]:
            return True
        else:
            return False