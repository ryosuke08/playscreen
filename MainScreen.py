import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

class MainScreen(Screen_abc):
    
    # 画面生成
    def display(self):
        super().update()

        # 背景
        background0 = pygame.image.load("img2/WorldMap-A1.png")#マグマ
        background1 = pygame.image.load("img2/sugorikumiti1.png")#橋の上のタイル
        background2 = pygame.image.load("img2/CastleTown-C-2.png")#橋の手すり
        background3 = pygame.image.load("img2/CastleTown-C-1.png")#橋
        background4 = pygame.image.load("img2/masu.png")#すごろくのマスをなぞったマス
        background5 = pygame.image.load("img2/ozaki32.png")#尾崎
        background6 = pygame.image.load("img2/yuka.png")#マップ左上の地面マス
        background7 = pygame.image.load("img2/hasira.png")#柱
        background8 = pygame.image.load("img2/橋の手すり縦.png")#縦の手すり
        background9 = pygame.image.load("img2/橋の手すり横向き.png")#横の手すり
        background10 = pygame.image.load("img2\階段.png")
        background11 = pygame.image.load("img2\階段影.png")
        background12 = pygame.image.load("img2/階段　完成.png")
        background13 = pygame.image.load("img2/壁.png")
        background14 = pygame.image.load("img2/タイル白.png")
        background15 = pygame.image.load("img2/柱左.png")
        background16 = pygame.image.load("img2/街頭.png")
        background17 = pygame.image.load("img2/手すり上が消えてるやつ.png")
        background18 = pygame.image.load("img2/影.png")
        background19 = pygame.image.load("img2/影左下カット.png")
        background20 = pygame.image.load("img2/門.png")
        background21 = pygame.image.load("img2/門の壁.png")
        background22 = pygame.image.load("img2/sugorokumiti.png")#マグマの地面
        background23 = pygame.image.load("img2/マス土.png")
        background24 = pygame.image.load("img2/島の地面マス.png")
        background25 = pygame.image.load("img2/マグマ96.png")
        background26 = pygame.image.load("img2/マグマの中に岩.png")
        background27 = pygame.image.load("img2/骨.png")
        background28 = pygame.image.load("img2/火山.png")
        background29 = pygame.image.load("img2/墓.png")
        background30 = pygame.image.load("img2/井戸.png")
        background31 = pygame.image.load("img2/柱.png")
        background32 = pygame.image.load("img2/沢山の山.png")
        background33 = pygame.image.load("img2/岩複数.png")
        background34 = pygame.image.load("img2/壊れた壁（小）.png")
        background35 = pygame.image.load("img2/壊れた壁（大）.png")
        background36 = pygame.image.load("img2/マグマ32×32.png")
        background37 = pygame.image.load("img2/岩.png")
        background38 = pygame.image.load("img2/岩（大）.png")
        background39 = pygame.image.load("img2/寂れた井戸.png")
        background40 = pygame.image.load("img2/岩単体.png")
        background41 = pygame.image.load("img2/枯れた木.png")
        background42 = pygame.image.load("img2/右上岩.png")
        #キャラクター画像
        background042 = pygame.image.load("img2/売人.png")
        background043 = pygame.image.load("img2/魔王.png")
        background044 = pygame.image.load("img2/生首.png")
        background045 = pygame.image.load("img2/死体.png")
        background046 = pygame.image.load("img2/殺人鬼.png")
        background047 = pygame.image.load("img2/おばけ4.png")
        background048 = pygame.image.load("img2/ゴブリン.png")
        background049 = pygame.image.load("img2/猫にん_魔王猫.png")
        background050 = pygame.image.load("img2/殺人ゴブリン.png")
        background051 = pygame.image.load("img2/殺人（女）.png")
        #アイコン
        background43 = pygame.image.load("img2/はてなマス.png")#？マス
        #マス
        background001 = pygame.image.load("img2/reinbo-.png")

        # super().setBackground(background22)
        
        #  #すごろくます
        # for i in range(23):
        #  SC.screen.blit(background6,self.grid[8 + i][13])
        #  SC.screen.blit(background6,self.grid[8 + i][5])
        # for i in range(9):
        #  SC.screen.blit(background6,self.grid[8][5 + i])
        #  SC.screen.blit(background6,self.grid[30][5 + i])

        # #中央マグマ
        # SC.screen.blit(background0,self.grid[18][8])
        # #  SC.screen.blit(background0,self.grid[19][8 + i])
        # #  SC.screen.blit(background0,self.grid[20][8 + i])

        # #マグマ
        # for i in range(2):
        #  SC.screen.blit(background0,self.grid[4][4])
        # for i in range(2):
        #  SC.screen.blit(background0,self.grid[33][12])
        # #墓
        # SC.screen.blit(background29,self.grid[11][8])
        # #右下マグマ
        # for i in range(6):
        #  SC.screen.blit(background36,self.grid[34 + i][16])
        # for i in range(7):
        #  SC.screen.blit(background36,self.grid[32 + i][17])
        # for i in range(8):
        #  SC.screen.blit(background36,self.grid[30 + i][18])
        # for i in range(9):
        #  SC.screen.blit(background36,self.grid[28 + i][19])

        # #火山
        # SC.screen.blit(background28,self.grid[35][17])
        # #骨
        # SC.screen.blit(background27,self.grid[21][9])
        # #柱
        # SC.screen.blit(background31,self.grid[25][10])
        # #井戸
        # SC.screen.blit(background39,self.grid[25][6])
        # #沢山の山
        # SC.screen.blit(background32,self.grid[33][4])
        # #枯れた木
        # SC.screen.blit(background41,self.grid[13][6])
        # #岩単体
        # SC.screen.blit(background40,self.grid[33][3])
        # SC.screen.blit(background40,self.grid[34][5])
        # SC.screen.blit(background40,self.grid[34][6])
        # SC.screen.blit(background40,self.grid[34][7])
        # SC.screen.blit(background40,self.grid[38][6])
        # SC.screen.blit(background40,self.grid[38][7])
        # SC.screen.blit(background40,self.grid[39][6])
        # SC.screen.blit(background40,self.grid[35][8])
        # SC.screen.blit(background40,self.grid[36][8])
        # SC.screen.blit(background40,self.grid[37][8])
        # #壊れた壁（小）
        # SC.screen.blit(background34,self.grid[20][7])
        # #壊れた壁（大）
        # a = 0
        # for i in range(6):
        #  SC.screen.blit(background35,self.grid[8 + a][3])
        #  a += 4
        # #左下のマグマ
        # for i in range(6):
        #  SC.screen.blit(background36,self.grid[0 + i][14])
        # for i in range(7):
        #  SC.screen.blit(background36,self.grid[0 + i][15])
        # for i in range(8):
        #  SC.screen.blit(background36,self.grid[0 + i][16])
        # for i in range(9):
        #  SC.screen.blit(background36,self.grid[0 + i][17])
        # for i in range(10):
        #  SC.screen.blit(background36,self.grid[0 + i][18])
        # for i in range(13):
        #  SC.screen.blit(background36,self.grid[0 + i][19])

        # #右上マグマ
        # for i in range(6):
        #  SC.screen.blit(background36,self.grid[34 + i][3])
        # for i in range(5):
        #  SC.screen.blit(background36,self.grid[35 + i][4])
        # for i in range(4):
        #  SC.screen.blit(background36,self.grid[36 + i][5])
        # for i in range(2):
        #  SC.screen.blit(background36,self.grid[36 + i][6])
        # for i in range(2):
        #  SC.screen.blit(background36,self.grid[36 + i][7])

        # #マグマの中に浮かぶ岩
        # SC.screen.blit(background38,self.grid[2][15])
        # SC.screen.blit(background37,self.grid[6][18])
        # SC.screen.blit(background42,self.grid[38][4])

        # #魔王
        # SC.screen.blit(background043,self.grid[38][18])
        # #生首
        # SC.screen.blit(background044,self.grid[19][9])
        # #死体
        # SC.screen.blit(background045,self.grid[1][4])
        # #殺人ゴブリン
        # SC.screen.blit(background050,self.grid[2][4])
        # #おばけ
        # SC.screen.blit(background047,self.grid[7][7])
        # #猫にん魔王
        # SC.screen.blit(background049,self.grid[38][3])
        # #ゴブリン
        # SC.screen.blit(background048,self.grid[11][11])
        # # #ゴブリン
        # # SC.screen.blit(background051,self.grid[27][10])


        
        #super().setBackground(SC.backImg,(0,128,32,32))

        #ここまで背景
        
        #プレイヤー情報欄
        #Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        #for i in range(4):


        # def preyer_screen():

        #  super().setBox(SC.Black, (32*10, 0), 32*10, 32*3, 3) # 外枠
        #  display_player_color = pygame.Rect(1*32*10+3, 3, 32*10-3, 32*3-3)  # 背景色
        #  pygame.draw.rect(SC.screen, SC.White, display_player_color) # 背景色を枠内に配置
        #  SC.screen.blit(pygame.image.load('img/Ozaki.png'), ((32*2+16)+(32*10), 32+18)) # プレイヤーアイコン
        #  SC.screen.blit(pygame.image.load('img/Coin.png'), ((32*6+8)+(32*10), 32-12)) # コインアイコン
        #  SC.screen.blit(pygame.image.load('img/Building1.png'), ((32*6+8)+(32*10), 32+18)) # 物件アイコン
        #  super().setText_S('Player'+str(1+1), ((32*2)+(1*32*10), 32-14), 22, SC.Black) # プレイヤー名（仮）
        #  super().setText_L(str(i+1), ((32*1+2)+(32*10), 32+22), 26, SC.Black) # 順位（仮）
        #  super().setText_S('54枚', ((32*7+16)+(32*10), 32-16), 22, SC.Black) # コイン数
        #  super().setText_S('1件', ((32*7+16)+(32*10), 32+18), 22, SC.Black) # 物件数
        
            


        super().setBox(SC.Black, (32*10, 0), 32*10, 32*3, 3) # 外枠
        display_player_color = pygame.Rect(1*32*10+3, 3, 32*10-3, 32*3-3)  # 背景色
        pygame.draw.rect(SC.screen, SC.White, display_player_color) # 背景色を枠内に配置
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), ((32*2+16)+(32*10), 32+18)) # プレイヤーアイコン
        SC.screen.blit(pygame.image.load('img/Coin.png'), ((32*6+8)+(32*10), 32-12)) # コインアイコン
        SC.screen.blit(pygame.image.load('img/Building1.png'), ((32*6+8)+(32*10), 32+18)) # 物件アイコン
        super().setText_S('Player'+str(4), ((32*2)+(1*32*10), 32-14), 22, SC.Black) # プレイヤー名（仮）
        super().setText_L(str(2), ((32*1+2)+(32*10), 32+22), 26, SC.Black) # 順位（仮）
        super().setText_S('54枚', ((32*7+16)+(32*10), 32-16), 22, SC.Black) # コイン数
        super().setText_S('1件', ((32*7+16)+(32*10), 32+18), 22, SC.Black) # 物件数
        
        
        super().setBox(SC.Black, (2*32*10, 0), 32*10, 32*3, 3) # 外枠
        display_player_color = pygame.Rect(2*32*10+3, 3, 32*10-3, 32*3-3)  # 背景色
        pygame.draw.rect(SC.screen, SC.White, display_player_color) # 背景色を枠内に配置
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), ((32*2+16)+(2*32*10), 32+18)) # プレイヤーアイコン
        SC.screen.blit(pygame.image.load('img/Coin.png'), ((32*6+8)+(2*32*10), 32-12)) # コインアイコン
        SC.screen.blit(pygame.image.load('img/Building1.png'), ((32*6+8)+(2*32*10), 32+18)) # 物件アイコン
        super().setText_S('Player'+str(3), ((32*2)+(2*32*10), 32-14), 22, SC.Black) # プレイヤー名（仮）
        super().setText_L(str(1), ((32*1+2)+(2*32*10), 32+22), 26, SC.Black) # 順位（仮）
        super().setText_S('72枚', ((32*7+16)+(2*32*10), 32-16), 22, SC.Black) # コイン数
        super().setText_S('0件', ((32*7+16)+(2*32*10), 32+18), 22, SC.Black) # 物件数
        

        super().setBox(SC.Black, (3*32*10, 0), 32*10, 32*3, 3) # 外枠
        display_player_color = pygame.Rect(3*32*10+3, 3, 32*10-3, 32*3-3)  # 背景色
        pygame.draw.rect(SC.screen, SC.White, display_player_color) # 背景色を枠内に配置
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), ((32*2+16)+(3*32*10), 32+18)) # プレイヤーアイコン
        SC.screen.blit(pygame.image.load('img/Coin.png'), ((32*6+8)+(3*32*10), 32-12)) # コインアイコン
        SC.screen.blit(pygame.image.load('img/Building1.png'), ((32*6+8)+(3*32*10), 32+18)) # 物件アイコン
        super().setText_S('Player'+str(3+1), ((32*2)+(3*32*10), 32-14), 22, SC.Black) # プレイヤー名（仮）
        super().setText_L(str(3), ((32*1+2)+(3*32*10), 32+22), 26, SC.Black) # 順位（仮）
        super().setText_S('20枚', ((32*7+16)+(3*32*10), 32-16), 22, SC.Black) # コイン数
        super().setText_S('2件', ((32*7+16)+(3*32*10), 32+18), 22, SC.Black) # 物件数
        
        #preyer1
        super().setBox(SC.Black, (0, 0), 32*10, 32*3, 3) # 外枠
        display_player_color = pygame.Rect(3, 3, 32*10-3, 32*3-3)  # 背景色
        pygame.draw.rect(SC.screen, SC.White, display_player_color) # 背景色を枠内に配置
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), (80, 32+18)) # プレイヤーアイコン
        SC.screen.blit(pygame.image.load('img/Coin.png'), (207, 32-12)) # コインアイコン
        SC.screen.blit(pygame.image.load('img/Building1.png'), (207, 32+18)) # 物件アイコン
        super().setText_S('Player'+str(1), (64, 32-14), 22, SC.Black) # プレイヤー名（仮）
        super().setText_L(str(4), (32, 32+22), 26, SC.Black) # 順位（仮）
        super().setText_S('2枚', (250, 32-16), 22, SC.Black) # コイン数
        super().setText_S('3件', (250, 32+18), 22, SC.Black) # 物件数
        
        pygame.draw.rect(SC.screen, SC.Black, pygame.Rect(32*40-3, 32*0, 3, 32*3)) # 右端の外枠線を追加
        
        # プレイヤー情報欄の現在のプレイヤーのカーソル（仮）
        super().setText_S('●', (32*11, 32-12), 20, SC.Red)

        # 青マスを上辺と下辺に配置
        for i in range(12):
            SC.screen.blit(pygame.image.load('img/Blue.png'), self.grid[8+i*2][5])
            SC.screen.blit(pygame.image.load('img/Blue.png'), self.grid[8+i*2][13])
            i += 1

        # 青マスを左辺と右辺に配置
        for i in range(3):
            SC.screen.blit(pygame.image.load('img/Blue.png'), self.grid[8][7+i*2])
            SC.screen.blit(pygame.image.load('img/Blue.png'), self.grid[30][7+i*2])
            i += 1

        # 赤マスを上辺と下辺に配置
        for i in range(3):
            SC.screen.blit(pygame.image.load('img/Red.png'), self.grid[12+i*8][5])
            SC.screen.blit(pygame.image.load('img/Red.png'), self.grid[10+i*8][13])
            i += 1

        # 赤マスを左辺に配置
        SC.screen.blit(pygame.image.load('img/Red.png'), self.grid[8][9])

        # 黄色マス（物件マス）を配置
        # SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[24][5])
        # SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[22][13])
        SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[28][5])
        SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[30][5])
        SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[30][7])
        SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[30][11])
        SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[30][13])
        SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[28][13])

        #タイル
        SC.screen.blit(pygame.image.load('img2/yuka.png'), self.grid[22][13])

        #レインボーマス（ボーナスマス）
        SC.screen.blit(pygame.image.load('img2/reinbo-.png'), self.grid[22][13])

        # 紫色マス（特大マイナスマス）を配置
        SC.screen.blit(pygame.image.load('img/Purple.png'), self.grid[30][9])

        # 物件を配置（仮）
        SC.screen.blit(background042,self.grid[28][4])
        SC.screen.blit(background042,self.grid[30][4])
        SC.screen.blit(background042,self.grid[31][7])
        SC.screen.blit(background042,self.grid[31][11])
        SC.screen.blit(background042,self.grid[31][13])
        SC.screen.blit(background042,self.grid[28][14])

       

        #マスの上に？を表示
        #SC.screen.blit(background43,self.grid[28][13])

        # アイテムを配置（仮）
        # SC.screen.blit(pygame.image.load('img/Item.png'), (32*29, 32*11+5))
        # SC.screen.blit(pygame.image.load('img/Item.png'), (32*20+5, 32*12))

        # マス上に各プレイヤーを配置（仮）
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), self.grid[14][5]) # 現在のプレイヤー
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), self.grid[26][5])
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), self.grid[30][5])
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), self.grid[24][13])

        # マス上の現在のプレイヤーのカーソル（仮）
        super().setText_S('▼', self.grid[14][4], 32, SC.Red) # 現在のプレイヤー
        super().setText_S('▼', self.grid[24][12], 32, SC.Blue)
        super().setText_S('▼', self.grid[26][4], 32, SC.Yellow)
        super().setText_S('▼', self.grid[30][4], 32, SC.Green)
        


        # ターン表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        display_turn_color = pygame.Rect(32*1, 32*5, 32*5, 32*9)
        pygame.draw.rect(SC.screen, SC.White, display_turn_color)
        super().setTextBox_S('', SC.Black, SC.Black, self.grid[1][5], 32*5, 32*9, 3, 25, 10, 10)
        super().setText_S('ターン', (32*2, 32*6), 35, SC.Black)
        super().setText_S('8/15', (32*2+5, 32*8+10), 45, SC.Black)
        super().setText_S('【中盤】', (32+12, 32*11+10), 35, SC.Black)

        # ゲーム終了ボタン
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        button_color = pygame.Rect(32*1, 32*16, 32*5, 32*2)
        pygame.draw.rect(SC.screen, SC.White, button_color)
        super().setTextBox_S('', SC.Black, SC.Black, self.grid[1][16], 32*5, 32*2, 3, 25, 10, 10)
        super().setText_S('ゲーム終了', (32*1+16, 32*16+20), 25, SC.Black)

        # 説明表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        display_desc_color = pygame.Rect(32*8, 32*15, 32*23, 32*4)
        pygame.draw.rect(SC.screen, SC.White, display_desc_color)
        text = ['アイテム名：確定ダイス', '　１～６のサイコロの目を自由に決めれます。']
        super().setTextBox_S(text, SC.Black, SC.Black, self.grid[8][15], 32*23, 32*4, 3, 30, 20, 20)

        # サイコロ表示欄
        SC.screen.blit(pygame.image.load('img/Dice1.jpg'), self.grid[35][5])

        # アイテム表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        super().setText_L('アイテム', (32*35, 32*10), 24, SC.Black)
        display_item_color = pygame.Rect(32*34, 32*11, 32*5, 32*3)
        pygame.draw.rect(SC.screen, SC.White, display_item_color)
        text = ['　確定ダイス', '　確定ダイス', '　コイン強奪']
        super().setTextBox_S(text, SC.Black, SC.Black, self.grid[34][11], 32*5, 32*3, 3, 25, 10, 10)
        super().setText_S('→', (1090, 383), 32, SC.Red)#(32*37+12, 32*12+2)

    # イベント処理
    def getEvent(self):
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    SC.ScreenNum = 1

