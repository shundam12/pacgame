import random
import pygame
import sys
from pygame.locals import *
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((600,600))  # 800*600の画面
    ar=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
    stk=[]
    r=0
    g=0
    b=0
    mapx=0
    mapy=0
    #while True:
    screen.fill((255,255,255))
    for gyou in range(4):
        for l in range(4):
            rnd=random.randint(1,3)
            r=0
            g=0
            b=0
            y=gyou*150
            x=l*150
            if rnd==1:
                r=255
            if rnd==2:
                g=255
            if rnd==3:
                b=255
            pygame.draw.rect(screen,(r,g,b),Rect(x,y,200,200))
            ar[gyou][l]=rnd

    pygame.display.update()
    print(ar)
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
                mapx=int(x/150)
                mapy=int(y/150)
                print(mapx,mapy,btn)
                print("y-1",ar[mapy-1][mapx])
                print("coler",ar[mapy][mapx])
            if mapy<3 and ar[mapy][mapx]==ar[mapy+1][mapx]:
                stk.append(ar[mapy+1][mapx])
            if mapx<3 and ar[mapy][mapx]==ar[mapy][mapx+1]:
                stk.append(ar[mapy][mapx+1])
            print(f"{mapy=} {mapx=}")
            if ar[mapy][mapx]==ar[mapy-1][mapx]:
                stk.append(ar[mapy-1][mapx])
            if ar[mapy][mapx]==ar[mapy][mapx-1]:
                stk.append(ar[mapy][mapx-1])
            # horyu=stk.pop(0)
            # saikie.append(horyu)
            # if stk==[]:
                
            #     saikie=[]


                

if __name__ == "__main__":
        main()
        