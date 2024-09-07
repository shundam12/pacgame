import pygame
import random
from pygame.locals import *
import sys
import time
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((450,450))  # 800*600の画面
    px=50
    py=50
    px2=50
    py2=350
    px3=200
    py3=350
    px4=300
    py4=350
    hx=350
    hy=200
    ex=300
    ey=300
    SIZE=50
    g1=1
    y1=1
    g2=1
    y2=7
    g3=4
    y3=7
    g4=6
    y4=7
    hg=4
    hr=7
    ct=0
    ar=[["n","n","c","n","n","n","n","n","n"],
        ["n","c","c","c","c","c","c","c","n"],
        ["n","c","c","c","n","c","c","c","n"],
        ["n","c","c","c","n","c","c","c","n"],
        ["n","c","n","c","n","c","c","c","n"],
        ["n","c","c","n","c","c","n","c","c"],
        ["n","c","c","c","c","c","c","c","n"],
        ["c","c","c","c","c","c","c","c","n"],
        ["n","n","n","n","n","c","n","n","n"]]
    gPng = pygame.image.load("hpatimon.png").convert_alpha()   #画像を読み込む
    ePng = pygame.image.load("patimon.png").convert_alpha()   #画像を読み込む
    pPng = pygame.image.load("pac.png").convert_alpha()   #画像を読み込む
    p2Png = pygame.image.load("pac2.png").convert_alpha()   #画像を読み込む
    p3Png = pygame.image.load("pac3.png").convert_alpha()   #画像を読み込む
    p4Png = pygame.image.load("pac4.png").convert_alpha()   #画像を読み込む
    while True:

        screen.fill((255,255,255))
        for g in range(9):
            for r in range(9):
                if ar[g][r]=="n":
                    pygame.draw.rect(screen, (255,0,0), Rect(SIZE*r,SIZE*g,SIZE,SIZE))
        screen.blit(gPng ,Rect(hx,hy,50,50))#オブジェクトを指定の座標に表示
        screen.blit(pPng ,Rect(px,py,50,50))#オブジェクトを指定の座標に表示
        screen.blit(p2Png ,Rect(px2,py2,50,50))#オブジェクトを指定の座標に表示
        screen.blit(p3Png ,Rect(px3,py3,50,50))#オブジェクトを指定の座標に表示
        screen.blit(p4Png ,Rect(px4,py4,50,50))#オブジェクトを指定の座標に表示
        rnd1=random.randint(1,4)
        rnd2=random.randint(1,4)
        rnd3=random.randint(1,4)
        rnd4=random.randint(1,4)
        print(hg)
        print(hr)
        ar[hg][hr]="n"
        ct=ct+1
        if ct==120:
            ct=0
            if rnd1==1 and ar[g1][y1+1]=="c" and hr==hr+1 or hr==hr-1 or hg==hg-1 or hg==hg+1:
                y1=y1+1
            
            if rnd1==2 and ar[g1][y1-1]=="c" and hr==hr+1 or hr==hr-1 or hg==hg-1 or hg==hg+1:
                y1=y1-1
            if rnd1==3 and ar[g1+1][y1]=="c" and hr==hr+1 or hr==hr-1 or hg==hg-1 or hg==hg+1:
                g1=g1+1
            if rnd1==4 and ar[g1-1][y1]=="c" and hr==hr+1 or hr==hr-1 or hg==hg-1 or hg==hg+1:
                g1=g1-1
            px=y1*50
            py=g1*50
            if rnd2==1 and ar[g2][y2+1]=="c":
                y2=y2+1
            if rnd2==2 and ar[g2][y2-1]=="c":
                y2=y2-1
            if rnd2==3 and ar[g2+1][y2]=="c":
                g2=g2+1
            if rnd2==4 and ar[g2-1][y2]=="c":
                g2=g2-1
            px2=y2*50
            py2=g2*50
            if rnd3==1 and ar[g3][y3+1]=="c":
                y3=y3+1
            if rnd3==2 and ar[g3][y3-1]=="c":
                y3=y3-1
            if rnd3==3 and ar[g3+1][y3]=="c":
                g3=g3+1
            if rnd3==4 and ar[g3-1][y3]=="c":
                g3=g3-1
            px3=y3*50
            py3=g3*50
            if rnd4==1 and ar[g4][y4+1]=="c":
                y4=y4+1
            if rnd4==2 and ar[g4][y4-1]=="c":
                y4=y4-1
            if rnd4==3 and ar[g4+1][y4]=="c":
                g4=g4+1
            if rnd4==4 and ar[g4-1][y4]=="c":
                g4=g4-1
            px4=y4*50
            py4=g4*50
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら
                pygame.quit()             
                sys.exit()                # 終了
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                  hr -=1  # 横方向の速度
                if event.key==K_RIGHT:
                  hr +=1  # 横方向の速度
                if event.key==K_UP:
                  hg -=1 # 横方向の速度
                if event.key==K_DOWN:
                  hg +=1  # 横方向の速度
        hx=hr*50
        hy=hg*50
        print(g1)
        print(y1)
        

if __name__ == "__main__":
    main()
