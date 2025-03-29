  #0 1 2  
a=[[2,1,3],#0
   [3,1,3],#1
   [1,1,2],]#2 
stk=[]
last=[]
g=2
r=1
if a[g][r]==a[g][r+1]:
    stk.append((g,r+1))
if a[g][r]==a[g][r-1]:
    stk.append((g,r-1))
if g+1<3 and  a[g][r]==a[g+1][r]:
    stk.append((g+1,r))
if a[g][r]==a[g-1][r]:
    stk.append((g-1,r))
while True:

    tori=stk[0]
    last.append(stk.pop(0))
    if tori[1]+1<3 and a[tori[0]][tori[1]]==a[tori[0]][tori[1]+1]:
        stk.append((tori[0],tori[1]+1))
    if tori[1]-1>-1 and a[tori[0]][tori[1]]==a[tori[0]][tori[1]-1]:
        stk.append((tori[0],tori[1]-1))
    if tori[0]+1<3 and a[tori[0]][tori[1]]==a[tori[0]+1][tori[1]]:
        stk.append((tori[0]+1,tori[1]))
    if tori[0]-1>-1 and a[tori[0]][tori[1]]==a[tori[0]-1][tori[1]]:
        stk.append((tori[0]-1,tori[1]))
    l=last.pop(0)
    a(l)=0
    if stk==[]:
        break
    

