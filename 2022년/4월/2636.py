from collections import deque

n,m = map(int,input().split())
board = [list(input().split()) for _ in range(n)] # '0' , '1'로 저장

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

#이게 왜 골드5?
def bfs():
    dx, dy = [1,0,-1,0],[0,1,0,-1]
    queue = deque([(0,0)])
    cheese = 0
    while queue:
        x, y = queue.popleft()
        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and board[nx][ny] != 0:
            # 걍 다 0으로 바꿔버리면 되지않나 ?
                if board[nx][ny] == '0':
                    board[nx][ny] = 0
                    queue.append((nx,ny))

                if board[nx][ny] == '1':
                    board[nx][ny] = 0
                    cheese += 1
    return cheese

time = 0
result = []
while True:
    cheese = bfs()
    result.append(cheese)
    if cheese == 0:
        break
    time += 1
    for i in range(n):
        board[i] = list(map(str,board[i]))


print(time)
print(result[-2])