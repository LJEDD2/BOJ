from collections import deque

m,n,k = map(int,input().split())
board = [[0]*n for _ in range(m)]

def OOB(x,y):
    return 0 <= x < m and 0 <= y < n

def rectangle(x1,y1,x2,y2):
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j] = 1

def BFS(x,y,area):
    dx, dy = [1,0,-1,0],[0,1,0,-1]
    queue = deque([(x,y)])
    board[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and board[nx][ny] == 0:
                board[nx][ny] = 1
                area += 1
                queue.append((nx,ny))
    result.append(area)

for i in range(k):
    x,y,x_,y_ = map(int,input().split())
    rectangle(x,y,x_,y_)

result = []
for i in range(m):
    for j in range(n):
        if not board[i][j]:
            area = 1
            BFS(i,j,area)

print(len(result))
print(*sorted(result))
