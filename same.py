import random
import pygame
import sys
from pygame.locals import *
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800,600))  # 800*600の画面
    ar=[[1,0,3,3,3,1,0,3],
        [1,1,0,1,2,3,1,2],
        [3,0,3,2,0,0,0,2],
        [3,1,1,2,3,3,2,2],
        [2,0,0,1,0,3,1,2],
        [3,3,2,2,1,1,0,2]]
    stk=[]
    r=0
    g=0
    b=0
    mapx=0
    mapy=0
    #while True:
    screen.fill((255,255,255))
    for gyou in range(6):
        for l in range(8):
            r=0
            g=0
            b=0
            y=gyou*100
            x=l*100
            if ar[gyou][l]==1:
                r=255
            if ar[gyou][l]==2:
                g=255
            if ar[gyou][l]==3:
                b=255
            pygame.draw.rect(screen,(r,g,b),Rect(x,y,200,200))
        

    pygame.display.update()
    while True:
                # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら
                pygame.quit()             
                sys.exit()                # 終了

                print(x,y)
            elif event.type == MOUSEBUTTONDOWN:
                btn = event.button
                x, y = event.pos
                mapx=int(x/100)
                mapy=int(y/100)
                print(mapx,mapy,btn)
                print("y-1",ar[mapy-1][mapx])
                print("coler",ar[mapy][mapx])
                
            if btn==2 and mapy<5 and ar[mapy][mapx]==ar[mapy+1][mapx]:
                stk.append(ar[mapy+1][mapx])
            if btn==2 and mapx<7 and ar[mapy][mapx]==ar[mapy][mapx+1]:
                stk.append(ar[mapy][mapx+1])
            print(f"{mapy=} {mapx=}")
            if ar[mapy][mapx]==ar[mapy-1][mapx]:
                stk.append(ar[mapy-1][mapx])
            if ar[mapy][mapx]==ar[mapy][mapx-1]:
                stk.append(ar[mapy][mapx-1])
            print(stk)
        
            # horyu=stk.pop(0)
            # saikie.append(horyu)
            # if stk==[]:
                
            #     saikie=[]


                

if __name__ == "__main__":
        main()
         