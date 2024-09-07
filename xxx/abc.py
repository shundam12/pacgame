def meiro(map,start,goal):
    N = len(map)  # 迷路のサイズ（N x N）
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上の移動（行列）
    stack = [(start, [start])]  # スタックには (現在の位置, 通過した経路) を保存
 
    while True:
       
        print("=====================")
        if stack==[]:
            break
        current, path = stack.pop()  # 現在位置と経路をスタックから取得
        if current == goal:
            return path  # ゴールに到達したら経路を返す

        # 移動可能な隣接セルを探索
        for d in directions:
            next_position = (current[0] + d[0], current[1] + d[1])
            print("d=",d,"next_position=",next_position)
# 次の位置が迷路内で、壁ではなく、まだ訪れていない場合
            if 0 <= next_position[0] < N and 0 <= next_position[1] < N and \
               map[next_position[0]][next_position[1]] == 0 and \
               next_position not in path:
                stack.append((next_position, path + [next_position]))  # 新しい位置をスタックに追加
                print("  stack=",stack)

    return None  # ゴールに到達する経路がない場合はNoneを返す

# 5x5迷路の例 (0は通路、1は壁)
# map = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0]
# ]

map = [
       [0,0,0,0,1,1],
       [0,1,0,1,1,0],
       [0,1,0,0,0,0],
       [0,0,1,0,1,0],
       [1,1,0,1,1,0],
       [0,0,0,0,0,0],
]
   
 
N = len(map)  # 迷路のサイズ（N x N）


# 迷路を解く
def main():
    print("**********************************")
    start = (0, 0)  # スタート位置
    goal = (N - 1, N - 1)  # ゴール位置
    path = meiro(map,start,goal)
    print("Path:", path)#行列で出力される
   

main()

