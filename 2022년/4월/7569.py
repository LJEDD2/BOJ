from collections import deque
m,n,h = map(int,input().split())
board = [[[] for _ in range(n)]  for _ in range(h)]

def OOB(x,y,z):
    return  0 <= x < n and 0 <= y < m and 0 <= z < h

def BFS():
    # 상하좌우 앞뒤
    dxyz = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
    while queue:
        h_, x, y = queue.popleft()
        for dx, dy, dz in dxyz:
            nx = x + dx
            ny = y + dy
            nz = h_ + dz
            if OOB(nx,ny,nz) and board[nz][nx][ny] == 0:
                board[nz][nx][ny] = board[h_][x][y] + 1
                queue.append((nz,nx,ny))

# 3차원..?
# input
for i in range(h):
    for j in range(n):
        board[i][j] = list(map(int,input().split()))

queue = deque()
for h_ in range(h):
    for x in range(n):
        for y in range(m):
            if board[h_][x][y] == 1:
                queue.append((h_,x,y))

BFS()

for i in board: print(i)

count = 0
for h_ in range(h):
    for i in board[h_]:
        if 0 in i:
            print(-1)
            exit()
        count = max(count,max(i))
print(count-1)
