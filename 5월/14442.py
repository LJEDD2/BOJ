from collections import deque
n,m,k = map(int,input().split())
board = [list(input()) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)]for _ in range(n)]

dx, dy = [1,0,-1,0],[0,1,0,-1]

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    queue = deque([(0,0,0)])
    visited[0][0] = [1]*(k+1)

    while queue:
        x,y,cnt = queue.popleft()
        if x == n-1 and y == m-1:
            print(visited[x][y][cnt])
            for i in visited: print(i)
            exit()
        for d_x,d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            broken = cnt + 1
            if OOB(nx,ny) and not visited[nx][ny][cnt]:
                if board[nx][ny] == '0':
                    queue.append((nx,ny,cnt))
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1

                if board[nx][ny] == '1' and broken <= k:
                    queue.append((nx,ny,broken))
                    visited[nx][ny][broken] = visited[x][y][cnt] + 1
bfs()
print(-1)
