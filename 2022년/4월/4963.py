from collections import deque
dx = [-1, 1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def BFS(x,y):
    queue = deque([(x,y)])
    board[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and board[nx][ny]:
                board[nx][ny] = 0
                queue.append((nx,ny))

while True:
    m , n = map(int,input().split())
    if n == 0 and m == 0:
        break

    board = [list(map(int,input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                cnt += 1
                BFS(i,j)

    print(cnt)
