from copy import deepcopy

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def spread(x,y):
    cnt = 0
    for d_x,d_y in zip(dx,dy):
        nx = x + d_x
        ny = y + d_y
        if OOB(nx,ny) and board[nx][ny] != -1:
            tmp[nx][ny] += board[x][y]//5
            cnt += 1
    tmp[x][y] += board[x][y] - ((board[x][y]//5)*cnt)


def clean(x,y,direction):
    board[x][y] = 0
    for i in range(4):
        while True:
            nx = x + dx[direction[i]]
            ny = y + dy[direction[i]]
            if OOB(nx,ny):
                if board[nx][ny] == -1:
                    return
                board[nx][ny] = tmp[x][y]
            else:
                break
            x, y = nx, ny

n,m,time = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
move_up =  [3,1,2,0]
move_down = [3,0,2,1]
cleaner = []

for _ in range(time):
    tmp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            if board[i][j] == -1:
                tmp[i][j] = -1
                cleaner.append([i,j])
                continue
            spread(i,j)

    board = deepcopy(tmp)

    x, y = cleaner.pop() # 청정기 아랫부분 pop
    clean(x,y+1,move_down)

    x, y = cleaner.pop() # 청정기 윗부분 pop
    clean(x,y+1,move_up)
sumv = 0

for i in board:
    sumv += sum(i)
print(sumv+2)