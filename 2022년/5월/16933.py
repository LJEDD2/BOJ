from collections import deque
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
board = [list(input()) for _ in range(n)]
visited = [[[[0,0] for _ in range(k+1)] for _ in range(m)] for _ in range(n)] #[x][y][count][is_day]
#print(*visited,sep='\n')

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    # x, y , dist, cnt , is_night
    # start = night (0)
    queue = deque([(0,0,1,0,0)])
    dir = [[1,0],[0,1],[-1,0],[0,-1]] # 제자리에 머무는 경우도 포함
    visited[0][0][0][0] = 1

    while queue:
        x, y, dist, cnt, is_night = queue.popleft()
        if [x,y] == [n-1,m-1]:
            print(dist)
            exit()
        for dx, dy in dir: # 5방향
            nx = x + dx
            ny = y + dy
            ncnt = cnt + 1
            if OOB(nx,ny):
                # 다음 좌표 값이 1일 때, 낮일 때 cnt가 k번 이하일 경우 이동이 가능하다.
                if board[nx][ny] == '1' and not is_night and ncnt <= k:
                    if not visited[nx][ny][ncnt][1]:
                        visited[nx][ny][ncnt][1] = 1
                        queue.append((nx,ny,dist+1,ncnt,1))

                # 다음 좌표 값이 0일 때 그냥 지나감 or
                # 현재 자리에서 움직일 수 없는 경우 (벽을 만났는데 밤일 때)
                # dist += 1
                elif (board[nx][ny] == '0' or  (nx == x and ny == y) ) and not visited[nx][ny][cnt][1-is_night]:
                    visited[nx][ny][cnt][1-is_night] = 1
                    queue.append((nx, ny, dist + 1, cnt, 1-is_night))

bfs()
print(-1)