
def game_start():
    for i in range(n):
        for j in range(m):
            #초기 시간 설정
            if board[i][j] == '.':
                board[i][j] = ['.',0]
            else:
                board[i][j] = ['O',2]

def explode():
    for i in range(n):
        for j in range(m):
            # 현재위치 포함 동서남북 폭탄 폭발
            for d_x, d_y in dx, dy:
                nx,ny = x + d_x, y + d_y


def bomb():
    for i in range(n):
        for j in range(m):
            board[i][j][1] += 1

            if board[i][j] == '.':
                board[i][j][0] = 'O'
            elif board[i][j] == 3:
                explode()


n,m,time = map(int, input().split())
board = [list(input()) for _ in range(n)]
dx, dy = [1,0,-1,0,0],[0,1,0,-1,0]
idx = 0

#초깃값
game_start()

#게임진행
while time > 0:
    time -= 1

    if time%2 == 0:

    else:

#결과
for i in board:
    print(*i)
