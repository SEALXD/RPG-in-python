from init import *


def main():
    """设置时钟"""
    frame_rate = pygame.time.Clock()
    """初始地图及初始位置"""
    c_map = map9
    main_chara.rect.left = c_map.start_left
    main_chara.rect.top = c_map.start_top
    """是否允许移动"""
    allow_to_move = True
    """是否改变角色形象"""
    change = 0
    #beginning()
    while True:
        c_map.charas.update(pygame.time.get_ticks(), 120)
        """获取当前时间"""
        ticks = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            """松开方向键，停止加载移动图"""
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    main_chara.moving = False
                if event.key == K_UP:
                    main_chara.moving = False
                if event.key == K_DOWN:
                    main_chara.moving = False
                if event.key == K_LEFT:
                    main_chara.moving = False
            if event.type == KEYDOWN:
                if event.key == K_m:
                    notebook.show = not notebook.show
                """按c与人物,物品互动"""
                if event.key == K_c:
                    for each in c_map.charas:
                        if at_point(main_chara, each.check_point):
                            if each.item_flag ==2 : #判断物品
                                if each.item_wanted.taked:
                                    throw(each.item_wanted)
                                    each.item_flag = -2
                                    talking(each.messages, each.person, 1)
                                    change = 1
                                else:
                                    talking(each.messages, each.person, 0)
                            else :
                                talking(each.messages, each.person, 0)
                            if each.event_id != -2:   #判断线索
                                notebook.notes[each.event_id]['flag'] = True
                            if each.once == 1:
                                c_map.charas.remove(each)
                            """特殊情况，换角色"""
                            if change == 1 and c_map == map2 and each == hui:
                                sleep(1)
                                blackout()
                                c_map = map2_0
                                main_chara.load('image/zhao.png', 32, 48, 4)
                                main_chara.rect.top = 150
                                main_chara.rect.left = 300
                                main_chara.update(pygame.time.get_ticks(),120)
                            if c_map == map6:
                                if each == shenwei1:
                                    sleep(1)
                                    blackout()
                                    c_map = map7
                                    main_chara.rect.top = 468
                                    main_chara.rect.left = 375
                                    pygame.mixer.music.stop()

                                else:
                                    shenwei1.rect.left = main_chara.rect.left + 30
                                    shenwei1.rect.top = main_chara.rect.top + 40
                                    map6.add_chara(shenwei1)
                            if c_map == map8 and each == Li:
                                sleep(1)
                                blackout()
                                bag.add_item(dial)
                                dial.taked = True
                                c_map = map2_1
                                main_chara.rect.left = 553
                                main_chara.rect.top = 429
                            if c_map == map2_1 and each == zhu1:
                                sleep(1)
                                blackout()
                                c_map = map8_0
                                main_chara.load('image/shenwei.png', 32, 48, 4)
                                main_chara.rect.top = 285
                                main_chara.rect.left = 868
                                main_chara.update(pygame.time.get_ticks(), 120)
                            if c_map == map3_0:
                                main_chara.load('image/zhao.png', 32, 48, 4)
                                main_chara.rect.top = 285
                                main_chara.rect.left = 868
                                main_chara.update(pygame.time.get_ticks(), 120)
                                if each == shenwei3:
                                    fin()
                    for each in c_map.items:
                        """添加物品进入背包"""
                        if at_point(main_chara, each.check_point):
                            if each == bloodbag:
                                c_map.items.remove(each)
                                if main_chara.blood < 8:
                                    main_chara.blood += 2
                            else:
                                bag.add_item(each)
                                each.taked = True
                                c_map.items.remove(each)

                if event.key == K_SPACE:
                    """控制子弹发射间隔"""
                    main_chara.attack(ticks, 600, 100, main_chara_attack, 500)
                if event.key == K_RIGHT:
                    """翻页"""
                    if notebook.show:
                        if notebook.c_page < notebook.max_page:
                            notebook.c_page += 1
                            book.play()
                if event.key == K_LEFT:
                    """翻页"""
                    if notebook.show:
                        if notebook.c_page > 0:
                            notebook.c_page -= 1
                            book.play()

            if event.type == MOUSEBUTTONDOWN:
                item_detail.show_message = False
                pos_x, pos_y = pygame.mouse.get_pos()
                """鼠标点击， 展开、折叠背包"""
                if bag.rect.left <= pos_x <= bag.rect.right and \
                        bag.rect.top <= pos_y <= bag.rect.bottom:
                    bag.show_details = not bag.show_details
                if bag.show_details:
                    if bag.bag_details_rect.left <= pos_x <= bag.bag_details_rect.right:
                        for x in range(len(bag.items)):
                            if bag.bag_details_rect.top+x*46+5 <= pos_y <= bag.bag_details_rect.top+(x+1)*46+5:
                                item_detail.show_message = not item_detail.show_message
                                item_detail.render(bag.items[x].introduction, None)
        c_map.charas.update(pygame.time.get_ticks(), 120)

        """获取按键"""
        key_pressed = pygame.key.get_pressed()
        if allow_to_move:
            if key_pressed[K_RIGHT]:
                main_chara.go_right(c_map, c_map.charas)
            if key_pressed[K_UP]:
                main_chara.go_up(c_map, c_map.charas)
            if key_pressed[K_LEFT]:
                main_chara.go_left(c_map, c_map.charas)
            if key_pressed[K_DOWN]:
                main_chara.go_down(c_map, c_map.charas)
        for each in c_map.entrances:
            """主角位于entrance"""
            if at_point(main_chara, each.check_point):
                """切换地图"""
                c_map = each.next_map
                screen.fill((0, 0, 0))
                main_chara.rect.left = each.to_point[0]
                main_chara.rect.top = each.to_point[1]
                pygame.mixer.music.stop()
                door.play()
                c_map.music_on = False
        """设置帧率"""
        frame_rate.tick(60)
        """绘制当前地图"""
        screen.fill((0, 0, 0))
        screen.blit(c_map.image, c_map.rect)
        c_map.charas.update(pygame.time.get_ticks(), 120)
        for each in c_map.buildings:
            screen.blit(each.image, each.rect)
        for each in c_map.items:
            if not each.taked:
                screen.blit(each.image, each.rect)
        """更新主角儿"""
        if ticks < main_chara.hitted_time + 600:
            draw_blood(main_chara)
        if main_chara.moving:
            chara_group.update(ticks, 120)
        chara_group.draw(screen)
        """绘制NPC"""
        for each in c_map.charas:
            c_map.charas.update(pygame.time.get_ticks(), 120)
            c_map.charas.draw(screen)

        if c_map == map5:
            if c_map.first_in:
                hint(screen, tips["ghost_fire"])
                c_map.first_in = False
                pygame.mixer.music.load("bgm/main_bgm.ogg")
                pygame.mixer.music.play(-1)
            for each in map5.charas:
                if each.alive:
                    if pygame.sprite.spritecollide(each, c_map.buildings, False, pygame.sprite.collide_mask):
                        each.side[0] = -each.side[0]
                        each.side[1] = -each.side[1]
                    map5.charas.remove(each)
                    if pygame.sprite.spritecollide(each, map5.charas, False, pygame.sprite.collide_mask):
                        each.side[0] = -each.side[0]
                        each.side[1] = -each.side[1]
                        each.speed[0] = randint(1, 4)
                        each.speed[1] = randint(1, 4)
                    map5.charas.add(each)
                    each.move()
                    if pygame.sprite.spritecollide(each, chara_group, False, pygame.sprite.collide_mask):
                        boom.play()
                        main_chara.blood -= 1
                        main_chara.hitted_time = ticks
                        each.alive = False
                        map5.charas.remove(each)
                    if each.alive:
                        screen.blit(each.image, each.rect)
        elif c_map == map6:
            if c_map.first_in:
                hint(screen, tips["girl"])
                pygame.mixer.music.load("bgm/Dungeon 1.mp3")
                pygame.mixer.music.play(-1)
                c_map.tick = ticks
                c_map.first_in = False
            for index, each in enumerate(map6_charas):
                """最后一个人"""
                if index == len(map6_charas) - 1:
                    each.rect.left, each.rect.top = 217, 247
                    map6.add_chara(each)
                    map6.charas.update(pygame.time.get_ticks(), 120)
                    map6.charas.draw(screen)
                elif ticks > c_map.tick + 1000 or index == 0:
                    if each.alive:
                        map6.add_chara(each)
                        map6.charas.update(pygame.time.get_ticks(), 120)
                        map6.charas.draw(screen)
                        if at_point(main_chara, each.check_point):
                            wind.play()
                            c_map.tick = ticks
                            each.alive = False
                            map6.charas.remove(each)
                    else:
                        continue
                break

        elif c_map == map8_0:
            if c_map.first_in:
                c_map.first_in = False
                pygame.mixer.music.load("bgm/Battle.mp3")
                pygame.mixer.music.play(-1)
            if ghost3.detect(main_chara):
                ghost3.find = True
            else:
                ghost3.go_around_y(c_map, chara_group, 100, 350)
            if ghost4.detect(main_chara):
                ghost4.find = True
            else:
                ghost4.go_around_x(c_map, chara_group, 20, 830)
            if ghost5.detect(main_chara):
                ghost5.find = True
            else:
                ghost5.go_around_x(c_map, chara_group, 100, 850)
            for each in c_map.charas:
                if each.find:
                    if not each.magic_now:
                        each.magic = Effect()
                        each.magic.load('image/Light1.png', 70, 70, 5)
                        each.magic_point = (main_chara.rect.left-20, main_chara.rect.top-10)
                        thunder1.play()
                    each.magic_now = each.perform_magic(screen, each.magic, ticks, each.magic_point, main_chara, 100)
                    if not each.magic_now:
                        each.find = False
                if ticks < each.hitted_time + 600:
                    draw_blood(each)
                if each.blood <= 0:
                    each.alive = False
                    c_map.charas.remove(each)

        elif c_map == map9:
            if c_map.first_in:
                if main_chara.rect.right > 100:
                    hint(screen, tips["boss"])
                    pygame.mixer.music.load("bgm/Boss Battle.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    boss_go_in(screen, boss)
                    map9.set_map('image/boss_4.png')
                    map9.add_building(no_out)
                    c_map.first_in = False
            if not c_map.first_in:
                if ticks < boss.hitted_time + 600:
                    draw_blood(boss)
                if boss.blood <= 0 and map9.buildings.has(no_out):
                    boss.alive = False
                    victory.play()
                    map9.charas.remove(boss)
                    map9.set_map('image/boss_bg.png')
                    map9.buildings.remove(no_out)
                    map9.buildings.remove(has_out)
                    map9.buildings.add(has_out_f)
                    pygame.mixer.music.stop()
                if main_chara.rect.top-25 < boss.rect.top:
                    boss.go_up(c_map, chara_group)
                else:
                    boss.go_down(c_map, chara_group)
                if main_chara.rect.left+150 < boss.rect.left:
                    boss.go_left(c_map, chara_group)
                else:
                    if boss.rect.left < 900:
                        boss.go_right(c_map, chara_group)
                boss.direction = 1
                if boss.alive:
                    boss.attack(ticks, 600, 150, boss_attack, 2000)
                    if not boss.magic_now:
                        boss.magic = Effect()
                        boss.magic.load('image/Thunder3.png', 100, 100, 5)
                        boss.magic_point = (randint(50, 750), randint(100, 320))
                        thunder2.play()
                    boss.magic_now = boss.perform_magic(screen, boss.magic, ticks, boss.magic_point, main_chara, 300)
                boss.update_bullet(screen, c_map, chara_group, ticks)
        else:
            if c_map.first_in:
                c_map.first_in = False
                pygame.mixer.music.load("bgm/Castle1.mp3")
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)

        """子弹"""
        main_chara.update_bullet(screen, c_map, c_map.charas, ticks)
        """"绘制背包，包内物品细节和提示"""
        screen.blit(bag.image, bag.rect)
        if bag.show_details:
            bag.blit_items()
            screen.blit(bag.bag_details, bag.bag_details_rect)
        if item_detail.show_message:
            screen.blit(item_detail.image, item_detail.rect)

        """notebook"""
        if notebook.show:
            notebook.render()
            screen.blit(notebook.image, notebook.rect)
            allow_to_move = False
        else:
            allow_to_move = True
        """死亡"""
        if main_chara.blood <= 0:
            ending()
        """更新画面"""
        pygame.display.update()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()