import pygame
import sys
import traceback
from pygame import *
from character import *
from map import *
from building import *
from entrance import *
from bag import *
from item import *
from messageBox import *
from fire import *
from random import *
from ghost_fire import *
from note_book import *
from time import *
from effect import *
"""initial"""
pygame.init()
pygame.mixer.init()
bg_size = width, height = 1000, 600
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("MyRPG")

"""加载地图，文件地址， 绘制坐标， 人物起始位置"""
map1 = Map('image/scene1_bk.png', 0, 0, 835, 315)
map2 = Map('image/dept_bk.png', 0, 0, 278, 500)
map2_0 = Map('image/dept_bk.png', 0, 0, 278, 400)
map2_1 = Map('image/dept_bk.png', 0, 0, 553, 429)
map3 = Map('image/scene3_bk.png', 0, 0, 278, 500)
map3_0 = Map('image/scene3_bk.png', 0, 0, 278, 500)
map4 = Map('image/scene4_bk.png', 0, 0, 534, 404)
map5_0 = Map('image/loudao_bk.png', 0, 0, 278, 500)
map5 = Map('image/ground.jpg', 0, 0, 50, 300)
map6 = Map('image/tiantai_bk.png', 0, 0, 510, 450)
map7 = Map('image/yiyuan1_bk.png', 0, 0, 375, 468)
map8 = Map('image/yiyuan2_bk.png', 0, 0, 510, 440)
map8_0 = Map('image/yiyuan2_bk.png', 0, 0, 860, 282)
"""测试物品"""
card = Item('image/card.png','This is an ID card', (350, 250))
card2 = Item('image/card.png', 'This is an ID card', (272, 477))
dial = Item('image/gui.png','This is a sundial', (272, 477))
bloodbag = Item('image/gui.png','This is a bloodbag', (639, 511))

"""this is our main character"""
main_chara = Character(2)
main_chara.moving_speed = 2
main_chara.load('image/guo.png', 32, 48, 4)

""""将主角单独加入一组"""
chara_group = pygame.sprite.Group()
chara_group.add(main_chara)
chara_group.update(pygame.time.get_ticks(), 120)

"""创建角色， 指定初始位置(相对屏幕)"""
"""NPC"""
zhu = Character(2)
zhu.load('image/zhu.png', 32, 48, 4)
zhu.rect.left, zhu.rect.top = 668, 409
temp = ["Oh~ I haven't seen a newcome for a long time.","Hi...! Is that a tail behind you!?","Oops~ Forget to hide it hahaha~"]
zhu.messages.append(temp)
temp = ['image/zhu_head.png','image/me_head.png','image/zhu_head.png']
zhu.person.append(temp)
zhu.event_id = 0 #对应线索编号

hui = Character(2)
hui.load('image/hui.png', 32, 48, 4)
hui.rect.left, hui.rect.top = 300, 250
hui.messages.append(["You don't have what I need"])
temp = ["Did you bring your ID card?","Yes , here you are.","(working ....)",\
                "OK, I've upload your information in the system. Now you are an official member of SID.",\
                "Thank yo...Ahhhh! ","(She doesn't have any feet!!)","Hmmm...pussy.","Cat! t...talked...","(Fanted)"]
hui.messages.append(temp)
hui.person.append(['image/hui_head.png'])
temp = ['image/hui_head.png','image/me_head.png','image/hui_head.png','image/hui_head.png','image/me_head.png','image/me_head.png',\
              "image/cat.png",'image/me_head.png','image/me_head.png']
hui.person.append(temp)
hui.item_flag = 2
hui.item_wanted = card

hui1 = Character(2)
hui1.load('image/hui.png', 32, 48, 4)
hui1.rect.left, hui1.rect.top = 300, 250
hui1.messages.append(["Mr.Zhao, we have a case. A girl was murdered in UDC(University of Dragon City) last night.",\
                      "Another one? (Sign) Let's go and check out.","Remember to take your card.","OK."])
hui1.person.append(['image/hui_head.png','image/zhao_head.png','image/hui_head.png','image/zhao_head.png'])

ghost = Character(2)
ghost.load('image/ghost_girl.png', 32, 48, 4)
ghost.rect.left, ghost.rect.top = 250, 100
ghost.messages.append(["It should not be me...","Are you OK?","(weeping)It was not coming for me..."])
ghost.person.append(['image/ghost_head.png','image/zhao_head.png','image/ghost_head.png'])
ghost.event_id = 1 #对应线索编号
ghost.once = 1

officer = Character(2)
officer.load('image/officer.png', 32, 48, 4)
officer.rect.left, officer.rect.top = 617, 104
officer.messages.append(["Special Investigation Dept. I'm Mr.Zhao. What is the situation now?","The body was discovered this morning,We speculate that the death time is around 1 am ",\
                    "Can I see the body?","Of course...but I should warn you, it's not a pretty picture.","Just show me.",\
                    "[The dead girl lies on the ground with her eyes and mouth wide open,the abdomen is cut open by some kind of weapon, and the internal organs are empty. ]",\
                    "This is not a normal case.","That's why I'm here.",\
                    "Ok, I'll take this case from now on.The transition document will be sent to you in two days. Now I want all your man to leave, I need to take a colser look.",\
                    "OK...."])
officer.person.append(['image/zhao_head.png','image/officer_head.png','image/zhao_head.png','image/officer_head.png',\
                       'image/zhao_head.png','image/zhao_head.png','image/officer_head.png','image/zhao_head.png', \
                       'image/zhao_head.png', 'image/officer_head.png', ])
officer.event_id = 2 #对应线索编号

shenwei = Character(2)
shenwei.load('image/shenwei.png', 32, 48, 4)
shenwei.rect.left, shenwei.rect.top = 822, 390
shenwei.messages.append(["Who are you?"])
shenwei.person.append(['image/shen_head.png'])
shenwei.messages.append(["Do you know this girl?","(Surprised)","Sir?","Yes. emmmm...I guess I know her.She's one of my students.You are ?","Zhao Yunlan from SID. This girl is the victim of the case last night.",\
                         "I've heard about the case. That's horrible... Do you need any help?","That would be wonderful.", \
                         "The teachers' office is in the red building overthere.Maybe you can look up for some information.","Thank you. Mr..?","Shen. My name is Shen Wei.",\
                         "Mr.Shen. Thank you for helping us. This is my name card, if you found anything more about this case you can call me.","Sure.You're welcomed."])
shenwei.person.append(['image/zhao_head.png','image/shen_head.png','image/zhao_head.png','image/shen_head.png',\
                       'image/zhao_head.png','image/shen_head.png','image/zhao_head.png','image/shen_head.png',\
                       'image/zhao_head.png','image/shen_head.png','image/zhao_head.png','image/shen_head.png'])
shenwei.event_id = 3
shenwei.item_flag = 2
shenwei.item_wanted = card2

student1 = Character(2)
student1.load('image/NPC1.png', 32, 48, 4)
student1.rect.left, student1.rect.top = 116, 117
student1.messages.append(["Excuse me do you know this girl? ","No. I don't know her."])
student1.person.append(['image/zhao_head.png','image/NPC1_head.png'])

student2 = Character(2)
student2.load('image/NPC2.png', 32, 48, 4)
student2.rect.left, student2.rect.top = 877, 178
student2.messages.append(["Excuse me do you know this girl? ","Emmmm...I don't think so."])
student2.person.append(['image/zhao_head.png','image/NPC2_head.png'])

grandma = Character(2)
grandma.load('image/grandma.png', 32, 48, 4)
grandma.rect.left, grandma.rect.top = 563, 286
grandma.messages.append(["Hello?","..."])
grandma.person.append(['image/zhao_head.png','image/grandma_head.png'])
grandma.once = 1
grandma.event_id = 4


grandma1 = Character(2)
grandma1.load('image/grandma.png', 32, 48, 4)
grandma1.rect.left, grandma1.rect.top = 840, 485
grandma1.messages.append(["Hello?","..."])
grandma1.person.append(['image/zhao_head.png','image/grandma_head.png'])
grandma1.once = 1

shenwei1 = Character(2)
shenwei1.load('image/shenwei.png', 32, 48, 4)
shenwei1.rect.left, shenwei1.rect.top = 563, 390
shenwei1.messages.append(["Hold tight!","(Shen pulled you and the girl back from the wall)","That was close! Thanks",\
                          "You, young lady! what the hell are you thinking !? ","(Crying)","Too dangerous.",\
                          "Yes, your teacher is right! Alright, stop crying. We need to get you to the hospital and tell your parents about this...",\
                          "(Crying loudly)","(Looking at the girl angrily)","If this man died back there because of your act, are you going to live with guilt or die because of it?",\
                          "S..sorry...","Well, I'm still standing here in one piece, so forget about that and move on. But you, young lady, you really should feel sorry for yourself",\
                          "Have you thought about what will your parents feel if you die? You are at such a young age.","Come on. Don't cry. Let's go to the hospital."])
shenwei1.person.append(['image/shen_head.png','image/shen_head.png','image/zhao_head.png','image/zhao_head.png',\
                       'image/Li_head.png','image/shen_head.png','image/zhao_head.png','image/Li_head.png',\
                       'image/shen_head.png','image/shen_head.png','image/Li_head.png','image/zhao_head.png',\
                       'image/zhao_head.png','image/zhao_head.png'])

shenwei2 = Character(2)
shenwei2.load('image/shenwei.png', 32, 48, 4)
shenwei2.rect.left, shenwei2.rect.top = 343, 118
shenwei2.messages.append(["She is up stairs.","Thank you professor.","Your arm is bleeding.","Well,just a bruise noth...","Let me help with it.",\
                          "Actually...I think I'll just clean it with water.","No. It's summer, you could get infected.","(Cleaning carefully)",\
                          "Professor Shen.","Yes?","Have we met before?","(Nervously)We... Yes. I saw you when you are solving a case last year.",\
                          "Oh... I see.","Thank you for this. I still have some questions for that girl,so..","Of course. See you.","(Leave)",\
                          "We've met before,not in that case, but a long time ago...",\
                          "[Nothing...There's nothing that he could remember... ",\
                          "Once a person crossed the modoribashi, drank waters of forgetfulness and entered the door of metempsychosis, all his memories were completely emptied. What else could you expect him to remember?]"])
shenwei2.person.append(['image/shen_head.png','image/zhao_head.png','image/shen_head.png','image/zhao_head.png','image/shen_head.png',\
                        'image/zhao_head.png','image/shen_head.png','image/shen_head.png',\
                       'image/zhao_head.png','image/shen_head.png','image/zhao_head.png','image/shen_head.png',\
                       'image/zhao_head.png','image/zhao_head.png','image/shen_head.png','image/zhao_head.png', \
                        'image/shen_head.png','image/shen_head.png'])

Li = Character(2)
Li.load('image/Li.png', 32, 48, 4)
Li.rect.left, Li.rect.top = 830, 204
Li.messages.append(["OK. Do you want to talk about why? ","Nothing...I was in a bad mood and...","Bad enough to make you kill yourself?","I...",\
                    "You are lying. The girl who died this mornig. It should be you, right? That thing got it wrong because she looks was coming for you.",\
                    "Please... I didn't know that...I'm sorry...I...","Then tell us the truth.",\
                    "Shadows...","What?","I saw dark, big shadows under the light that night...It was her! She want me dead!",\
                    "...","You've been seeing thing lately, didn't you?",\
                    "I see that your Eye of Spirit is not open. You are not born psychic, right? You must have touched something you shouldn't touch.",\
                    "This... it was passed down through my family.","A sundial.A sundial turns around once a day, the sun rises from the east and sets in the west once,which always comes full cycle, symbolizing endless life and reincarnation.",\
                    "What did you do with it?","I didn't do anything bad! I didn't! (crying)","Fine... I have to take this to our department. I'll come back tomorrow."])
Li.person.append(['image/zhao_head.png','image/Li_head.png','image/zhao_head.png','image/Li_head.png', \
                  'image/zhao_head.png',\
                  'image/Li_head.png','image/zhao_head.png',\
                  'image/Li_head.png', 'image/zhao_head.png','image/Li_head.png',\
                  'image/zhao_head.png','image/zhao_head.png',\
                  'image/zhao_head.png',\
                  'image/Li_head.png','image/zhao_head.png',\
                  'image/zhao_head.png','image/Li_head.png','image/zhao_head.png'])

zhu1 = Character(2)
zhu1.load('image/zhu.png', 32, 48, 4)
zhu1.rect.left, zhu1.rect.top = 434, 168
zhu1.messages.append(["Mr.Zhao. Wait! There is something you need to know. ","What?","The underworld department send us the report.Many ghosts got out yesterday, the servant spend a long time catching them.",\
                      "Most of them are sent back except one.","Which one?","A starved ghost.","What?! How can they left soemthing like this here?",\
                      "Well, you know they have been loaf on the job lately.","(Sign) OK...",\
                      "Wait, that's it! Now I understand everything! Oh no, Shen is still in the hospital! Call him now! We have to warn him!"])
zhu1.person.append(['image/zhu_head.png','image/zhao_head.png','image/zhu_head.png','image/zhu_head.png', \
                    'image/zhao_head.png','image/zhu_head.png','image/zhao_head.png','image/zhu_head.png','image/zhao_head.png','image/zhao_head.png'])
zhu1.event_id = 6 #对应线索编号

hui2 = Character(2)
hui2.load('image/hui.png', 32, 48, 4)
hui2.rect.left, hui2.rect.top = 274, 177
hui2.messages.append(["Where is the sundail?"])
hui2.person.append(['image/hui_head.png'])
hui2.messages.append(["Did you find anything ?","I searched for Li's backgorund, she was raised by her grandma alone. Two years ago, her grandma had a very serious brain hemorrhage.",\
                      "When she sent her to the hospital, the doctor said it was too late. However, her grandma was miraculously alive, but had symptoms of senile dementia.",\
                      "Poor girl.","And the sundail you talked about on the phone.I borrowed a book about it from the underwolrd.",\
                      "What does it do?","It is one of the four Holy Implement from the acient time. Its power can share one person's life to another.",\
                      "That's why her grandma is back alive! She give her life to save her.","Yes, but her grandma died two month ago. This not possible because Li is still alive.",\
                      "According to the book, as long as the giver is alive the recipient will live.Unless....",\
                      "Unless the giver kills the recipient.","But why? She loved her grandma so much that she use her life to save her. Why would she kill her again?",\
                      "Only Li can answer that. I'll go and ask her."])
hui2.person.append(['image/zhao_head.png','image/hui_head.png','image/hui_head.png','image/zhao_head.png','image/hui_head.png','image/zhao_head.png', \
                    'image/hui_head.png', 'image/hui_head.png','image/hui_head.png','image/zhao_head.png','image/hui_head.png','image/zhao_head.png'])
hui2.event_id = 5 #对应线索编号
hui2.item_flag = 2
hui2.item_wanted = dial

shenwei3 = Character(2)
shenwei3.load('image/shenwei.png', 32, 48, 4)
shenwei3.rect.left, shenwei3.rect.top = 99, 148
shenwei3.messages.append(["Are you alright ? ","I'm fine.Here is the starved ghost.","How did you....","Long story."])
shenwei3.person.append(['image/zhao_head.png','image/shen_head.png','image/zhao_head.png','image/shen_head.png'])


"""为地图添加建筑"""
map1.add_building(Building('image/scene1_night.png', [map1.rect.left, map1.rect.top]))
map2.add_building(Building('image/dept.png',[map2.rect.left, map2.rect.top]))
map2_0.add_building(Building('image/dept.png',[map2_0.rect.left, map2_0.rect.top]))
map2_1.add_building(Building('image/dept.png',[map2_1.rect.left, map2_1.rect.top]))
map3.add_building(Building('image/scene3.png',[map3.rect.left, map3.rect.top]))
map3_0.add_building(Building('image/scene3.png',[map3.rect.left, map3.rect.top])) #end
map4.add_building(Building('image/scene4.png',[map4.rect.left, map4.rect.top]))
map5_0.add_building(Building('image/loudao.png',[map5_0.rect.left, map5_0.rect.top]))
map5.add_building(Building('image/wall.png', [0, 0]))
map6.add_building(Building('image/tiantai.png', [0, 0]))
map7.add_building(Building('image/yiyuan1.png', [0, 0]))
map8.add_building(Building('image/yiyuan2.png', [0, 0]))
map8_0.add_building(Building('image/yiyuan2.png', [0, 0]))
map9 = Map('image/boss_1.png', 0, 0, 0, 265)

"""为地图添加entrance:交互点， 通往地图、及位置"""
map1.add_entrance(Entrance(833+map1.rect.left, 873+map1.rect.left, 206+map1.rect.top,\
                           225+map1.rect.top, map2, 527+map2.rect.left, 533+map2.rect.top))
map2_0.add_entrance(Entrance(451+map2_0.rect.left, 578+map2_0.rect.left, 549+map2_0.rect.top,\
                           582+map2_0.rect.top, map3, 842+map3.rect.left, 242+map3.rect.top))
map3.add_entrance(Entrance(838+map3.rect.left, 873+map3.rect.left, 206+map3.rect.top,\
                           225+map3.rect.top, map2_0, 485+map2_0.rect.left, 500+map2_0.rect.top))
map3.add_entrance(Entrance(194+map3.rect.left, 281+map3.rect.left, 0+map3.rect.top,\
                           20+map3.rect.top, map4, 514+map4.rect.left, 498+map4.rect.top))
map4.add_entrance(Entrance(310+map4.rect.left, 344+map4.rect.left, 81+map4.rect.top,\
                           100+map4.rect.top, map5_0, 647+map5_0.rect.left, 400+map5_0.rect.top))

map4.add_entrance(Entrance(484+map4.rect.left, 560+map4.rect.left, 585+map4.rect.top,\
                           600+map4.rect.top, map3, 232+map5_0.rect.left, 66+map5_0.rect.top))



map5_0.add_entrance(Entrance(646+map5_0.rect.left, 741+map5_0.rect.left, 186+map5_0.rect.top,\
                           200+map5_0.rect.top, map5, 40+map5.rect.left, 298+map5.rect.top))

map5_0.add_entrance(Entrance(646+map5_0.rect.left, 741+map5_0.rect.left, 430+map5_0.rect.top,\
                           480+map5_0.rect.top, map4, 323+map4.rect.left, 118+map4.rect.top))

map5.add_entrance(Entrance(955+map5.rect.left, 1000+map5.rect.left, 260+map5.rect.top,\
                           340+map5.rect.top, map6, 720+map6.rect.left, 450+map6.rect.top))

map4.add_entrance(Entrance(316+map4.rect.left, 347+map4.rect.left, 355+map4.rect.top,\
                           375+map4.rect.top, map7, 541+map7.rect.left, 505+map7.rect.top))
map7.add_entrance(Entrance(645+map4.rect.left, 725+map4.rect.left, 0+map4.rect.top,\
                           84+map4.rect.top, map8, 686+map8.rect.left, 527+map8.rect.top))
map7.add_entrance(Entrance(505+map4.rect.left, 590+map4.rect.left, 590+map4.rect.top,\
                           600+map4.rect.top, map4, 388+map8.rect.left, 371+map8.rect.top))
map8_0.add_entrance(Entrance(976+map4.rect.left, 1000+map4.rect.left, 450+map4.rect.top,\
                           530+map4.rect.top, map9, 40+map9.rect.left, 250+map9.rect.top))
map8.add_entrance(Entrance(640+map4.rect.left, 720+map4.rect.left, 586+map4.rect.top,\
                           600+map4.rect.top, map7, 679+map7.rect.left, 168+map7.rect.top))
map9.add_entrance(Entrance(990+map4.rect.left, 1000+map4.rect.left, 250+map4.rect.top,\
                           350+map4.rect.top, map3_0, 129+map3.rect.left, 159+map3.rect.top))



"""为地图添加角色"""
map2.add_chara(zhu)
map2.add_chara(hui)
map3.add_chara(ghost)
map4.add_chara(officer)
map4.add_chara(shenwei)
map4.add_chara(student1)
map4.add_chara(student2)
map5_0.add_chara(grandma)
map2_0.add_chara(hui1)
map7.add_chara(shenwei2)
map8.add_chara(Li)
map8.add_chara(grandma1)
map2_1.add_chara(hui2)
map2_1.add_chara(zhu1)
map3_0.add_chara(shenwei3)
"""建立背包"""
bag = Bag(bg_size)
"""地图物品"""
map2_0.items.add(card2)
map8_0.items.add(bloodbag)
"""添加到背包"""
bag.add_item(card)
card.taked = True

"""对话框"""
"""图片样式， 位置坐标， 单行长度"""
message_box = MessageBox('image/message_box.jpg', (0, 0), 70, (255, 255, 255))

"""玩家子弹"""
"""此子弹png图片有误!!!!"""
for i in range(4):
    main_chara.bullets.add(Fire('fuzhou', 3))

"""鬼影天台地图"""
map6_charas = []
for x in range(6):
    chara = Character(0)
    chara.load('image/Li.png', 32, 48, 4)
    chara.once = 1
    direction = randint(1, 4)
    if direction == 1:
        chara.rect.left, chara.rect.top = randint(205, 770), randint(72, 110)#上
    elif direction == 2:
        chara.rect.left, chara.rect.top = randint(205, 570), randint(465, 495)#下
    elif direction == 3:
        chara.rect.left, chara.rect.top = randint(205, 210), randint(75, 500)#左
    elif direction == 4:
        chara.rect.left, chara.rect.top = randint(765, 770), randint(75, 320)#右
    map6_charas.append(chara)
    chara.messages.append(
        ["Ahhhhh!", "Hold my hand!","(You catched the girl but both of you are almost falling from the edge!)"])
    chara.person.append(['image/Li_head.png','image/zhao_head.png'])



"""躲避鬼火"""
for x in range(10):
    position = randint(70, 850), randint(150, 450)
    speed = [randint(1, 2), randint(1, 2)]
    ghostfire = GhostFire(position, speed)
    while pygame.sprite.spritecollide(ghostfire, map5.charas, False, pygame.sprite.collide_mask):
        ghostfire.rect.left, ghostfire.rect.top = randint(70, 850), randint(150, 450)
    map5.add_chara(ghostfire)


"""boss_room"""

has_out = Building('image/boss_wall_1.png', [0, 0])
no_out = Building('image/boss_wall_2.png', [0, 0])
has_out_f = Building('image/boss_wall_3.png', [0, 0])
map9.add_building(has_out)
boss = Character(1)
boss.load('image/boss.png', 64, 70, 3)
boss.rect.left, boss.rect.top = 1000, 265
boss.direction = 1
map9.add_chara(boss)
for x in range(100):
    boss.bullets.add(Fire('beng', 5))


"""hospital"""
ghost3 = Character(2)
ghost3.load('image/ghost.png', 33, 32, 3)
ghost3.rect.left, ghost3.rect.top = 220, 100
ghost3.direction = 0

ghost4 = Character(2)
ghost4.load('image/ghost.png', 33, 32, 3)
ghost4.rect.left, ghost4.rect.top = 20, 390
ghost4.direction = 2

ghost5 = Character(2)
ghost5.load('image/ghost.png', 33, 32, 3)
ghost5.rect.left, ghost5.rect.top = 850, 430
ghost5.direction = 1

map8_0.add_chara(ghost3)
map8_0.add_chara(ghost4)
map8_0.add_chara(ghost5)

"""消息盒"""
message_box = MessageBox('image/message_box.png', (0, 0), 70, (255, 255, 255))
item_detail = MessageBox('image/item_detail.jpg', (300, 225), 70, (0, 0, 0))
tips_box = MessageBox('image/item_detail.jpg', (300, 225), 70, (0, 0, 0))
notebook = NoteBook()



"""提示"""
tips = {"ghost_fire": "Escape from Wildfire",
        "girl": "The girl is trying to jump! Save her.",
        "boss": "finall battle!",
        "hospital": "their flash is dangerous!"}

##sound
main_chara_attack = pygame.mixer.Sound('sound/fire.wav')
boss_attack = pygame.mixer.Sound('sound/boss.wav')
boss_attack.set_volume(1.0)
monster = pygame.mixer.Sound('sound/monster.wav')
boss_close = pygame.mixer.Sound('sound/Close_boss.wav')
book = pygame.mixer.Sound('sound/book.wav')
victory = pygame.mixer.Sound('sound/victory.wav')
door = pygame.mixer.Sound('sound/door.wav')
thunder1 = pygame.mixer.Sound('sound/Thunder1.wav')
thunder2 = pygame.mixer.Sound('sound/Thunder2.wav')
boom = pygame.mixer.Sound('sound/boom.wav')
wind = pygame.mixer.Sound('sound/wind.wav')


def collide_test(main_chara, c_map):
    """人物与建筑碰撞"""
    if pygame.sprite.spritecollide(main_chara, c_map.buildings, False, pygame.sprite.collide_mask):
        return True
    """人物与物品碰撞"""
    if pygame.sprite.spritecollide(main_chara, c_map.items, False, pygame.sprite.collide_mask):
        return True
    """人物与人物碰撞"""
    if pygame.sprite.spritecollide(main_chara, c_map.charas, False, pygame.sprite.collide_mask):
        return True
    return False


def at_point(main_chara, point):
    """人物处于某交互点"""
    if point[0] <= main_chara.rect.left <= point[1] and point[2] <= main_chara.rect.top <= point[3]:
        return True
    else:
        return False


def draw_blood(chara):
    pygame.draw.line(screen, (255, 255, 255), (chara.rect.left, chara.rect.top - 5),\
                     (chara.rect.right, chara.rect.top - 5), 2)
    blood_remain = chara.blood / chara.BLOOD
    if blood_remain > 0.4:
        blood_color = (0, 255, 0)
    else:
        blood_color = (255, 0, 0)
    pygame.draw.line(screen, blood_color, (chara.rect.left, chara.rect.top - 5), \
                     (chara.rect.left + chara.rect.width*blood_remain, chara.rect.top - 5), 2)


def beginning():
    pygame.mixer.music.load('bgm/start.mp3')
    pygame.mixer.music.play()
    opening = ['image/opening0.png', 'image/opening1.png', 'image/opening2.png', 'image/opening3.png', 'image/opening3.png'] #最后一张显示不了所以多加一张。。。
    background = pygame.image.load(opening[0]).convert()
    count = 1
    while count < 5:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_SPACE]:
            background = pygame.image.load(opening[count]).convert()
            pygame.time.delay(1000)
            count += 1
        screen.blit(background, (0, 0))
        pygame.display.update()
    pygame.mixer.music.stop()

def fin():
    pygame.mixer.music.load('bgm/start.mp3')
    pygame.mixer.music.play()
    ending = ['image/end1.png', 'image/end2.png','image/end1.png']  # 最后一张显示不了所以多加一张。。。
    background = pygame.image.load(ending[0]).convert()
    count = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_SPACE]:
                background = pygame.image.load(ending[count]).convert()
                pygame.time.delay(1000)
                count += 1
            if count == 3:
                pygame.quit()
                sys.exit()
            screen.blit(background, (0, 0))
            pygame.display.update()
    pygame.mixer.music.stop()

def ending():
    background = pygame.image.load('image/gameover.jpg').convert()
    background = pygame.transform.scale(background, (1000, 600))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))
        pygame.display.update()


def talking(messages,person,havethings):
    front = 0
    pic = 0
    while front < len(messages[havethings]):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_c:
                    front += 1
                    pic = front % len(person[havethings])
        if front == len(messages[havethings]):
            break
        message_box.render_talk(messages[havethings][front],person[havethings][pic])  #0为没有满足条件时的话
        screen.blit(message_box.image, message_box.rect)
        pygame.display.update()

def blackout():
    tick = pygame.time.get_ticks()
    screen.fill((0,0,0))
    while True:
        if pygame.time.get_ticks() - tick >2000:
            break
        pygame.display.update()

def throw(item):
    bag.items.remove(item)
    item.taked = False
    bag.bag_details = pygame.image.load('image/bag_detail.jpg')


def boss_go_in(screen, boss):
    in_tick = pygame.time.get_ticks()
    background = pygame.image.load('image/boss_1.png').convert_alpha()
    monster.play()
    first_close = True
    ready = False
    close_tick = 0
    laser_1 = Effect()
    laser_1.load("image/Laser2.png", 192, 192, 5)
    laser_1.rect.left, laser_1.rect.top = 650, 80
    laser_2 = Effect()
    laser_2.load("image/Laser2.png", 192, 192, 5)
    laser_2.rect.left, laser_2.rect.top = 430, 0
    laser_3 = Effect()
    laser_3.load("image/Laser2.png", 192, 192, 5)
    laser_3.rect.left, laser_3.rect.top = 490, 250
    laser_4 = Effect()
    laser_4.load("image/Laser2.png", 192, 192, 5)
    laser_4.rect.left, laser_4.rect.top = 145, 20
    laser_5 = Effect()
    laser_5.load("image/Laser2.png", 192, 192, 5)
    laser_5.rect.left, laser_5.rect.top = 200, 280
    while True:
        pygame.time.Clock().tick(60)
        ticks = pygame.time.get_ticks()
        screen.blit(background, (0, 0))
        chara_group.draw(screen)
        map9.charas.update(pygame.time.get_ticks(), 120)
        map9.charas.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if ticks > in_tick + 1000:
            if boss.rect.left > 800:
                boss.go_left(map9, chara_group)
            else:
                ready = True
        if ready:
            if ticks < in_tick + 7500:
                if first_close:
                    boss_close.play()
                    first_close = False
                    close_tick = ticks
                else:
                    if ticks > close_tick + 500:
                        monster.play()
                        laser_1.show(screen, ticks, 100)
                        background = pygame.image.load('image/boss_2.png').convert_alpha()
            elif ticks < in_tick + 9500:
                monster.play()
                laser_2.show(screen, ticks, 100)
                laser_3.show(screen, ticks, 100)
                background = pygame.image.load('image/boss_3.png').convert_alpha()
            elif ticks < in_tick + 11500:
                monster.play()
                laser_4.show(screen, ticks, 100)
                laser_5.show(screen, ticks, 100)
                background = pygame.image.load('image/boss_4.png').convert_alpha()
            else:
                break

        pygame.display.update()

def hint(screen, text):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_c:
                    return

        tips_box.render(text, None)
        screen.blit(tips_box.image, tips_box.rect)
        pygame.display.update()


