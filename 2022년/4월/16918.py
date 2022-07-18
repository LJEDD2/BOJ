from collections import deque
r,c,time = map(int, input().split())
board = [list(input()) for _ in range(r)]
time -= 1
dx, dy = [1,0,-1,0],[0,1,0,-1]

def OOB(x,y):
    return 0 <= x < r and 0 <= y < c

def bombSet():
    for i in range(r):
        for j in range(c):
            if board[i][j] != 'O':
                board[i][j] = 'O'
def bomb():
    while queue:
        x, y = queue.popleft()
        board[x][y] = '.'
        for d_x, d_y in zip(dx, dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx, ny) and board[nx][ny] == 'O':
                board[nx][ny] = '.'

def print_():
    for i in board: print(*i, sep = "")

#게임진행
while time:
    queue = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                queue.append((i,j))
    bombSet()
    time -= 1

    if time == 0:
        break

    bomb()
    time -= 1

print_()

