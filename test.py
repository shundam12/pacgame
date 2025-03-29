#問題 1: 配列の要素を合計する
#与えられた整数の配列（リスト）の全要素を合計する関数sum_elements(arr)を実装してください。
#例:
#def sum_elements(arr):

#   sum=0

#     for i in range(5):
#         sum=sum+arr[i]
#         #sum=sum+arr.pop(0)
#     return sum
# arr = [1, 2, 3, 4, 5]
# print(sum_elements(arr))
# 問題 2: 配列の最大値と最小値を求める
# 与えられた配列（リスト）の最大値と最小値をタプルで返す関数find_min_max(arr)を実装してください。
# 例:

# def find_min_max(arr):
#     mx=arr[0]
#     mn=arr[0]
#     for i in range(5):
#         if arr[i]>mx:
#             mx=arr[i]
#         if mn>arr[i]:
#             mn=arr[i]
        
#     return mn,mx
# arr = [-13, -10, -17, -14, -12]
# print(find_min_max(arr))  # 出力: (1, 7)

# 問題 3: 配列を逆順にする
# 与えられた配列（リスト）を逆順にして返す関数reverse_array(arr)を実装してください。
# 例:

  # 出力: [50, 40, 30, 20, 10]

 
#     rev=[]
#     for i in range(5):
#         rev.append(arr[4-i])
#     return rev
      
# arr = [10, 20, 30, 40, 50,60,70,80]
# a=-1
# while True:
    
#     a=a+1
#     arr[a],arr[len(arr)-1-a]=arr[len(arr)-1-a],arr[a]
#     if a==len(arr)-1-a:
#         break
#     elif a==len(arr)-2-a:
#         break
# print(arr)
# arr = [10, 20, 30, 40, 50,60,70,80]
# for i in range(int(len(arr)/2)):
#     arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
#  print(arr)
#  配列の中で重複している要素を見つける
# 与えられた配列（リスト）から重複している要素をすべて見つけてリストとして返す関数find_duplicates(arr)を実装してください。
# 例:
def find_duplicates(arr):
  tyo1=0
  tyo2=0
  a=0
  for i in range(int(len(arr))):
    for f in range(int(len(arr))):
    if tyo1 == 0 and len(arr)-1>=a+1 and arr[a]==arr[a+1]:
      tyo1=arr[a]
    if tyo1==0 and len(arr)-1>=a+2 and arr[a]==arr[a+2]:
      tyo1=arr[a]  
    if tyo1 == 0 and len(arr)-1>=a+3 and arr[a]==arr[a+3]:
      tyo1=arr[a]
    if tyo1 == 0 and len(arr)-1>=a+4 and arr[a]==arr[a+4]:
      tyo1=arr[a]
    if tyo1 == 0 and len(arr)-1>=a+5 and arr[a]==arr[a+5]:
      tyo1=arr[a]
    if tyo1==0 and len(arr)-1>=a+6 and arr[a]==arr[a+6]:
      tyo1=arr[a]
    if tyo1 != 0 and len(arr)-1>=a+1 and arr[a]==arr[a+1]:
      if tyo1 !=arr[a]:
        tyo2=arr[a]
    if tyo1 != 0 and len(arr)-1>=a+2 and arr[a]==arr[a+2]:
      if tyo1 !=arr[a]:
        tyo2=arr[a]
    if tyo1 != 0 and len(arr)-1>=a+3 and arr[a]==arr[a+3]:
      if tyo1 !=arr[a]:
        tyo2=arr[a]
    if tyo1 != 0 and len(arr)-1>=a+4 and arr[a]==arr[a+4]:
      if tyo1 !=arr[a]:
        tyo2=arr[a]
    if tyo1 != 0 and len(arr)-1>=a+5 and arr[a]==arr[a+5]:
      if tyo1 !=arr[a]:
        tyo2=arr[a]
    if tyo1 != 0 and len(arr)-1>=a+6 and arr[a]==arr[a+6]:
      if tyo1 !=arr[a]:
        tyo2=arr[a]
    if tyo2 !=0:
      break
    a=a+1
  return tyo1,tyo2
arr = [1, 2,0, 3, 2, 4, 5, 1,0]

print(find_duplicates(arr))  # 出力: [1, 2]
