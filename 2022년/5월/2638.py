from collections import deque
n,m=map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    global cheese
    queue = deque([(0,0)])
    dx, dy = [1,0,-1,0],[0,1,0,-1]
    visited = [[0]*m for i in range(n)]
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and not visited[nx][ny]:
                if board[nx][ny] >= 1:
                    board[nx][ny] += 1
                    cheese += 1
                else:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
def melt():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 3:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1

time = 0
while True:
    cheese = 0
    bfs()
    melt()

    if cheese == 0:
        print(time)
        break
    else:
        time+=1

