board = [list(input()) for _ in range(10)]
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

def OOB(x, y): # out of bound
    return 0 <= x < 10 and 0 <= y < 10

def check(cx, cy):
    # 8방향탐색
    for i in range(8):
        cnt = 1
        empty = 0
        nx, ny = cx, cy
        for _ in range(4):
            nx += dx[i]
            ny += dy[i]
            if OOB(nx,ny):
                if board[nx][ny] == 'X':
                    cnt += 1
                elif board[nx][ny] == '.':
                    empty += 1
            else :
                break

        if cnt == 4 and empty == 1:
            print(1)
            exit()

for i in range(10):
    for j in range(10):
        if board[i][j] == 'X':
            check(i,j)
print(0)

