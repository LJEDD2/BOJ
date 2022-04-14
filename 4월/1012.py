from collections import deque

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def BFS(x,y):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
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

for i in range(int(input())):
    m,n,k = map(int,input().split())
    board = [[0]*m for _ in range(n)]
    for i in range(k):
        c, r = map(int,input().split())
        board[r][c] = 1

    cnt = 0
    for x in range(n):
        for y in range(m):
            if board[x][y]:
                cnt += 1
                BFS(x,y)

    print(cnt)