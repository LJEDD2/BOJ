game = [list(map(int, input().split())) for _ in range(19)]
dx,dy = [1, 1, 0, -1],[0, 1, 1, 1]    # 아래 아래대각선 위 위대각선


def OOB(x, y): # 범위체크
    return 0 <= x < 19 and 0 <= y < 19

def check(cx, cy):
    stone = game[cx][cy]
    # 8방향탐색
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        cnt = 1
        while OOB(nx,ny) and game[nx][ny] == stone:
            cnt += 1

            if cnt == 5:
                if OOB(cx-dx[i], cy-dy[i]) and game[cx - dx[i]][cy - dy[i]] == stone: # 반대방향으로 같은게 더 있는지
                    break
                if OOB(nx+dx[i], ny+dy[i]) and game[nx][ny] == game[nx + dx[i]][ny+dy[i]]: # 6개 이상 넘어가면 승리 인정 x
                    break
                print(stone)
                print(cx+1, cy+1)
                exit()
            nx += dx[i]
            ny += dy[i]


for i in range(19):
    for j in range(19):
        if game[i][j]:
            check(i,j)

print(0)

