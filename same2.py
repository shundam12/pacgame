map=[
    [0,2,0,1],
    [1,1,1,2],
    [0,1,0,2],]
  # [
  # [x,x,x,1],
  # [0,x,0,2],
  # [0,2,0,2],]
g=int(input())
r=int(input())
stk=[]
pas=[]
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
for i in range(len(pas)):
    z=pas.pop(0)
    map(z)="x"