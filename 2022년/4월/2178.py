from collections import deque

n, m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
dx, dy = [1,0,-1,0],[0,1,0,-1]

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def BFS(x,y):
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx,ny))
    print(board[n-1][m-1])

BFS(0,0)
for i in board : print(*i)
