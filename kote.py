grid = [
    [2, 1, 2, 1],  # 0
    [2, 1, 3, 3],  # 1
    [2, 1, 2, 2],  # 2
    [1, 1, 1, 3],]  # 3
g_stk=[]
r_stk=[]
g=int(input()) #縦の位置 (3)を想定
r=int(input())#横の位置 (1)を想定

while True:
    under=g-1
    on=g+1
    light=r+1
    left=r-1
    if grid[on][r]==grid[g][r] :
        g_stk.append(on)
        r_stk.append(r)
    if grid[g][light]==grid[g][r]:
        g_stk.append(g)
        r_stk.append(light)
    if grid[under][r]==grid[g][r]:
        g_stk.append(under)
        r_stk.append(r)
    if grid[g][left]==grid[g][r]:
        g_stk.append(g)
        r_stk.append(left)
    g=g_stk(0)
    r=r_stk(0)
    
    

