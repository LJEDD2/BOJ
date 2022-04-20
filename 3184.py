from collections import deque

n,m = map(int,input().split())
board = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def BFS(x,y):
    global w, s
    dx, dy = [1,0,-1,0],[0,1,0,-1]
    queue = deque([(x,y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        if board[x][y] == 'v':
            w += 1
        elif board[x][y] == 'o':
            s += 1

        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and board[nx][ny] != '#' and visited[nx][ny] == 0 :
                queue.append((nx,ny))
                visited[nx][ny] = 1

wolf , sheep = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] != '#' and visited[i][j] == 0:
            w, s = 0, 0
            BFS(i,j)

            if w >= s :
                s = 0
            else:
                w = 0
            wolf += w
            sheep += s

print(sheep, wolf)
