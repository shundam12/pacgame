#  配列の中で重複している要素を見つける
# 与えられた配列（リスト）から重複している要素をすべて見つけてリストとして返す関数find_duplicates(arr)を実装してください。
# 例:
def find_duplicates(arr):
  a=0
  b=0
  c=[]
  for i in range(int(len(arr))):
    b=0
    if a<int(len(arr)):
        for f in range(int(len(arr))):
            print("fa=",a)
            print("fb=",b)
            if b<int(len(arr)):
                if a<b and arr[a]==arr[b]:
                    print("a=",a)
                    print("b=",b)
                    c.append(arr[a])
            b=b+1
    a=a+1
    
  
  return c
arr = [1, 2,0, 3, 2, 4, 5, 1,0]
#(0,7)(1,4)(2,8)
print(find_duplicates(arr))  # 出力: [1, 2]