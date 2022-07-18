import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

time = 99999999999999
height = 0
inventory = 0
for i in range(257):
    #0부터 256의 높이까지 전체탐색 (브루트포스)
    #높이마다 사용되는 블록 수 초기화
    max = 0
    min = 0
    for x in range(n):
        for y in range(m):
            # 현재 높이 i와 비교해서 더 낮으면 인벤토리에서 블록을 가져와서 쌓아준다.
            if board[x][y] < i:
                min += i-board[x][y]
            # 더 높으면 블럭을 하나 없애준 후 인벤토리에 넣는다.
            else:
                max += board[x][y]-i

    #인벤토리로 들어가는 블록의 개수가 초기 인벤토리에 있던 블록 개수와 합쳐진다.
    inven = max + b

    #합쳐진 수가 인벤토리에서 빠지는 블록 개수보다 많아야한다.
    if inven < min: #블록 개수가 부족할 경우 높이를 올려서 다시 탐색한다. i+=1
        continue

    #걸리는 시간 계산
    # 블록을 빼서 인벤토리에 넣는 과정(max)이 2초 걸리고, 블록을 가져와서 높이를 쌓아주는 과정(min)이 1초가 걸린다.
    # 블록을 쌓아주고 빼준 개수에 대한 시간을 계산한다.
    t = 2*max + min
    # 최소 시간 저장
    if t <= time:
        time = t
        height = i
        inventory = inven

print(time, height, inventory)



