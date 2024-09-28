import pygame
import random
from pygame.locals import *
import sys
import time
class Monster:
    def __init__(self,img,g1,y1,goal):     #gが行でyが横
        self.img=img
        self.g1=g1
        self.y1=y1
        self.ct=0
        self.hp=1
        self.goal=goal
    def update(self,map):
      #monster関連(75~91)
        self.ct=self.ct+1
        if self.ct==3:
            self.ct=0
            rnd1=random.randint(1,4)
        
            if rnd1==1 and map[self.g1][self.y1+1]==0 :
                self.y1=self.y1+1
            if rnd1==2 and map[self.g1][self.y1-1]==0:
                self.y1=self.y1-1
            if rnd1==3 and (map[self.g1+1][self.y1]==0 or map[self.g1+1][self.y1]==self.goal):
                self.g1=self.g1+1
            if rnd1==4 and map[self.g1-1][self.y1]==0:
                self.g1=self.g1-1
        
            
    

    def draw(self,screen):
            px=self.y1*50
            py=self.g1*50
            screen.blit(self.img ,Rect(px,py,50,50))
def meiro(map,start,goal):
    N = len(map)  # 迷路のサイズ（N x N）
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上の移動（行列）
    stack = [(start, [start])]  # スタックには (現在の位置, 通過した経路) を保存
 
    while True:
       
        print("=====================")
        if stack==[]:
            break
        current, path = stack.pop(0)  # 現在位置と経路をスタックから取得
        if current == goal:
            return path  # ゴールに到達したら経路を返す

        # 移動可能な隣接セルを探索
        for d in directions:
            next_position = (current[0] + d[0], current[1] + d[1])
            print("d=",d,"next_position=",next_position)   # 次の位置が迷路内で、壁ではなく、まだ訪れていない場合
            if 0 <= next_position[0] < N and 0 <= next_position[1] < N and \
               map[next_position[0]][next_position[1]] == 0 and \
               next_position not in path:
                stack.append((next_position, path + [next_position]))  # 新しい位置をスタックに追加
                print("  stack=",stack)

    return None  # ゴールに到達する経路がない場合はNoneを返す
     

def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((450,450))  # 800*600の画面
    
    gPng = pygame.image.load("img/hpatimon.png").convert_alpha()   #画像を読み込む
    ePng = pygame.image.load("img/patimon.png").convert_alpha()   #画像を読み込む
    pPng = pygame.image.load("img/pac.png").convert_alpha()   #画像を読み込む　　monster関連
    p2Png = pygame.image.load("img/pac2.png").convert_alpha()   #画像を読み込む
    p3Png = pygame.image.load("img/pac3.png").convert_alpha()   #画像を読み込む
    p4Png = pygame.image.load("img/pac4.png").convert_alpha()   #画像を読み込む
    hx=350
    hy=200
    SIZE=50
    M1=Monster(pPng,0,1,5) #インスタンス化
    M2=Monster(p2Png,4,7,4)
    M3=Monster(p3Png,4,1,3)
    M4=Monster(p4Png,7,4,2)
    Ms=[M1,M2,M3,M4]
    win=100
    ct=0
    wct=0
    bg1=0
    hg=4
    hr=4
    hct=0
    map=[[1,5,1,1,1,1,1,1,1,],
         [1,0,0,0,0,0,0,0,4,],
         [1,0,0,0,0,0,0,0,1,],
         [1,0,0,0,0,0,0,0,1,],
         [1,0,0,0,0,0,0,0,1,],
         [1,0,0,0,0,0,0,0,1,],
         [1,0,0,0,0,0,0,0,1,],
         [3,0,0,0,0,0,0,0,1,],
         [1,1,1,1,1,1,1,2,1,],]

    ck = pygame.time.Clock()
    while True:
        ck.tick(30) #1秒間で30フレームになるように33msecのwait
        rnd1=random.randint(1,4)
        rnd2=random.randint(1,4)
        rnd3=random.randint(1,4)
        rnd4=random.randint(1,4)
        screen.fill((255,255,255))
        for g in range(9):
            for r in range(9):
                if map[g][r]==1:
                    pygame.draw.rect(screen, (100,100,100), Rect(SIZE*r,SIZE*g,SIZE,SIZE))
        pygame.draw.rect(screen,(250,150,150),Rect(350,400,SIZE,SIZE))
        pygame.draw.rect(screen,(255,0,0),Rect(0,350,SIZE,SIZE))
        pygame.draw.rect(screen,(200,255,0),Rect(400,50,SIZE,SIZE))
        pygame.draw.rect(screen,(0,0,255),Rect(50,0,SIZE,SIZE))
        # M1.update(map)
        # M2.update(map)
        # M3.update(map)
        # M4.update(map)
        for M in Ms:
            M.update(map)
        if M1.hp==1:
            M1.draw(screen)
        if M2.hp==1:
            M2.draw(screen)
        if M3.hp==1:
            M3.draw(screen)
        if M4.hp==1:
            M4.draw(screen)
        screen.blit(gPng ,Rect(hx,hy,50,50))#オブジェクトを指定の座標に表示
            
        wct=wct+1
        if wct==180:
            wct=0
            win=win-1
            if by1==M1.y1 and bg1==M1.g1:
                win=win-4
            if by2==M2.y1 and bg2==M2.g1:
                win=win-4
            if by3==M3.y1 and bg3==M3.g1:
                win=win-4
            if by4==M4.y1 and bg4==M4.g1:
                win=win-4
            if win<=0:
                print("you win")
                break
            print("win=",win)
            print("by1=",by1)
            print("bg1-",bg1)
            print("M1.y1=",M1.y1)
            print("M1.g1",M1.g1)

        pygame.display.update()

        # イベント処理
        map[hg][hr]=1
        hct=hct+2
        if hct>=3:
            for event in pygame.event.get():  # イベントを取得
                if event.type == QUIT:        # 閉じるボタンが押されたら
                    pygame.quit()             
                    sys.exit()                # 終了
                if event.type == KEYDOWN:
                    oldhr=hr
                    oldhg=hg
                    if event.key==K_LEFT:
                        hr -=1  # 横方向の速度
                        hct=hct-30
                    if event.key==K_RIGHT:
                        hr +=1  # 横方向の速度
                        hct=hct-30
                    if event.key==K_UP:
                        hg -=1 # 横方向の速度
                        hct=hct-30
                    if event.key==K_DOWN:
                        hg +=1  # 横方向の速度
                        hct=hct-30
                    if hr>=8 or hr<=0:
                        hr=oldhr
                    if hg>=8 or hg<=0:
                        hg=oldhg
        hx=hr*50
        hy=hg*50
        if M1.g1==8 or M1.g1==0 or M1.y1==8 or M1.y1==0:
            print("you lost")
            break
        if M2.g1==8 or M2.g1==0 or M2.y1==8 or M2.y1==0:
            print("you lost")
            break
        if M3.g1==8 or M3.g1==0 or M3.y1==8 or M3.y1==0:
            print("you lost")
            break
        if M4.g1==8 or M4.g1==0 or M4.y1==8 or M4.y1==0:
            print("you lost")
            break
        by1=M1.y1
        bg1=M1.g1
        by2=M2.y1
        bg2=M2.g1
        by3=M3.y1
        bg3=M3.g1
        by4=M4.y1
        bg4=M4.g1
    print("thank you for playing")        

if __name__ == "__main__":
    main()
