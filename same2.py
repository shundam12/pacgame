import random
map=[
    [-2,-2,-2,-2],
    [-2,-2,-2,-2],
    [-2,-2,-2,-2],]


  # [
  # [0,2,0,-1],
  # [1,1,1,-1],
  # [0,1,0,1],]
g=int(input())
r=int(input())
stk=[]
pas=[]
map2=[]
for li in range(3):
    for il in range(4):
        rnd=random.randint(0,2)
        map[li][il]=rnd
print(map)

while True:
    
    pas.append((g,r))
    if g<2 and map[g+1][r]==map[g][r] and (g+1,r) not in pas:
        stk.append((g+1,r))
    
    if g>0 and map[g-1][r]==map[g][r] and (g-1,r) not in pas:
        stk.append((g-1,r))
    
    if r<3 and map[g][r+1]==map[g][r] and (g,r+1) not in pas:
        stk.append((g,r+1))
        
    if r>0 and map[g][r-1]==map[g][r] and (g,r-1) not in pas:
        stk.append((g,r-1))
        
    print("g=",g)
    print("r=",r)
    print("stk=",stk)
    print("pas=",pas)
    if stk==[]:
        break
    g,r=stk.pop(0)
 #先ず二次元配列の列を一つの配列にし直してそこから数値や位置を変える方向性で考える
a=0
b=0
for d in range(len(pas)):
    a,b=pas.pop(0)
    map[a][b]=-1
map3=[]
for i in range(4):
    map2=[]
    for l in range(3):
        map2.append(map[l][i])
    map3.append(map2)
print(map3)    
#配列の組み換えはできたから新しい一つ一つの配列を動かして元の形に戻す        
map4=[]
map5=[]
for h in range(4):
    map4=[]
    for f in range(3):
        if map3[h][f]==-1:
            pass
        else:
            map4.append(map3[h][f])
    map5.append(map4)
map5=list(filter(None,map5))
print("map5=",map5)

map6=[] 
for q in range(len(map5)):
    map6=[]
    for p in range(3):    
        map6=map5[q]
        if len(map6)<3:
            map6.insert(0,-1)
print("map5=",map5)
map7=[]
map8=[]
for o in range(3):
    map8=[]
    for k in range(len(map5)):
        map8.append(map5[k][o])
    map7.append(map8)
print(map7)