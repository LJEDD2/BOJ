n = int(input())
n_list = list(map(int,input().split()))
visited = [0]*10

# 연속하지 않는 경우의 좌표
board = {
    # row 기준 건너뛰는 좌표 : 건너뛴 수
    (1, 3) : 2, (3, 1) : 2, (4, 6) : 5, (6, 4) : 5, (7, 9) : 8, (9, 7) : 8,
    # col 기준 건너뛰는 좌표 : 건너뛴 수
    (1, 7) : 4, (7, 1) : 4, (2, 8) : 5, (8, 2) : 5, (3, 9) : 6, (9, 3) : 6,
    # 대각선 기준 건너뛰는 좌표 : 건너뛴 수
    (1, 9) : 5, (9, 1) : 5, (3, 7) : 5, (7, 3) : 5
}

for i in range(n-1):
    cx = n_list[i]
    nx = n_list[i+1]

    visited[cx] = True
    # 좌표가 연속하지 않을 경우
    if (cx,nx) in board:
        # 방문하지않고 건너뛰었을 경우
        idx = board[(cx,nx)]
        if not visited[idx]:
            print('NO')
            break
    # 연속할경우
    else:
        # 다음 좌표 이미 방문했을 때 break
        if visited[nx]:
            print('NO')
            break
else:
    print('YES')
