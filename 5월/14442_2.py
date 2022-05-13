from collections import deque
n,m,k = map(int,input().split())
board = [list(input()) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

#print(*board)
def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    queue = deque([(0,0,0,1)])
    dx, dy = [1,0,-1,0],[0,1,0,-1]
    visited[0][0][0] = 1

    while queue:
        x,y,cnt,dist = queue.popleft()
        if [x,y] == [n-1,m-1]:
            print(dist)
            exit()

        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny):
                if board[nx][ny] == '1' and cnt + 1 <= k and not visited[nx][ny][cnt+1]:
                        visited[nx][ny][cnt+1] = 1
                        queue.append((nx,ny,cnt+1,dist+1))
                elif board[nx][ny] == '0' and not visited[nx][ny][cnt]:
                        visited[nx][ny][cnt] = 1
                        queue.append((nx, ny, cnt, dist + 1))

bfs()
print(-1)
            
            
          
