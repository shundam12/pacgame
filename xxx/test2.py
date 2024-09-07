"""
迷路の解き方　スタックを使う方法、深さ優先探索

使用する迷路５行５列
ar=[["n","n","n","n","n"],
    ["n","s","c","c","n"],
    ["n","c","n","n","n"],
    ["n","c","c","g","n"],
    ["n","n","n","n","n"]]

着目点（1,1）　　←行列の順,xyではないことに注意！

上下左右　　　　
ｘo x o        
            右　（1,2）　←これが取り出されて次の着目点になる
            下（2,1）
ーーーーーーーーーーーーーーーーースタック


上下左右　　　　
ｘo x o    
            下（2,1）
ーーーーーーーーーーーーーーーーースタック（トップが取り出される）

着目　右（1,2）←以下同様、スタックのトップが取り出されて次の着目点になっていく

上下左右　
ｘｘx o　　 
           下（2,1）
ーーーーーーーーーーーーーーーーースタック

着目　右（1,３）

上下左右　
ｘｘx x　　 

ーーーーーーーーーーーーーーーーースタック
着目　下（２,１）

上下左右
ｘoｘｘ

ーーーーーーーーーーーーーーーーースタック
着目　下（３，１）

上下左右
ｘｘｘo

----------------------------スタック
着目　右（３，２）

上下左右
ｘｘｘo

ーーーーーーーーーーーーーーーーースタック

"""
y=0
t=0




# ar=[["n","n","n","n","n"],
#     ["n","s","c","c","n"],
#     ["n","c","n","n","n"],
#     ["n","c","c","g","n"],
#     ["n","n","n","n","n"]]
ar=[["n","n","n","n","n","n"],
    ["n","s","c","c","c","n"],
    ["n","c","n","n","c","n"],
    ["n","c","c","n","c","n"],
    ["n","n","c","g","c","n"],
    ["n","n","n","n","n","n"]]
stk=[[1,1]]
path=[]
for i in range(100):
  print("round",str(i+1))
  tm=stk.pop(0)
  print(tm[0])
  print(tm[1])
  y=tm[1]
  t=tm[0]
  print("着目点は",t,y)
  print(ar)
  if ar[t][y]=="g":
    print("ゴール！")
    break
  else:
    print("ゴールでない")
    
  ny=y+1
  if ar[t][ny]=="c" or ar[t][ny]=="g":
    print("〇")
    stk.append([t,ny])
  else:
    print("×")
  ny=y-1
  if ar[t][ny]=="c" or ar[t][ny]=="g":
    print("〇")
    stk.append([t,ny])
  else:
    print("×")
  nt=t-1
  if ar[nt][y]=="c" or ar[nt][y]=="g":
    print("〇")
    stk.append([nt,y])
  else:
    print("×")
  nt=t+1
  if ar[nt][y]=="c" or ar[nt][y]=="g":
    print("〇")
    stk.append([nt,y])
  else:
    print("×")
  print(stk)
  ar[t][y]="b"
  path.append(tm)
  print(path)