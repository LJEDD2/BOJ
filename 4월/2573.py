from collections import deque

n, m = map(int,input().split())
ocean = [list(map(int,input().split())) for _ in range(n)]
year = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

# 주변이 0이면 녹인다
def melt(v):
    for i in range(n):
        for j in range(m):
            if ocean[i][j] != 0:
                cnt = 0
                v[i][j] = 1
                for d_x,d_y in zip(dx,dy):
                    nx = i + d_x
                    ny = j + d_y
                    if OOB(nx,ny) and v[nx][ny] == 0:
                        if ocean[nx][ny] == 0:
                            cnt += 1
                melt_h = ocean[i][j] - cnt
                if melt_h < 0:
                    ocean[i][j] = 0
                else:
                    ocean[i][j] = melt_h
    return  ocean

def BFS(x,y):
    queue = deque([(x,y)])
    # 다시 0으로 방문표시
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and visited[nx][ny]:
                visited[nx][ny] = 0
                queue.append((nx,ny))

for year in range(301):
    # 덩어리 count하기 위한 방문표시 table 초기화
    visited = [[0] * m for _ in range(n)]
    melt(visited)
    cnt = 0

    for x in range(n):
        for y in range(m):
            if visited[x][y]:
                cnt += 1
                # 빙산 덩어리가 몇 개인지 탐색
                BFS(x,y)

    if cnt >= 2:
        print(year)
        exit()

print(0)
