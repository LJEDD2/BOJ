from collections import deque
m, n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def BFS():
    dx, dy = [1,0,-1,0],[0,1,0,-1]

    while queue:
        x,y = queue.popleft()
        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx,ny))


queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i,j))

BFS()

for i in board :
    #print(*i)
    if 0 in i:
        print(-1)
        exit()

print(max(map(max,board))-1)