def solve_1941(n, m): # n이 행, m이 열
    arr = [[0] * n for _ in range(m)]
    dx, dy = [0,1,0,-1], [1,0,-1,0]  # 오른쪽
    cur_x, cur_y = 0, 0
    num = 1
    idx = 0

    while True:
        if num == n*m:
            print(cur_y, cur_x)
            break

        arr[cur_x][cur_y] = 1
        now_x, now_y = cur_x + dx[idx], cur_y + dy[idx]

        if 0 <= now_x < m and 0 <= now_y < n and arr[now_x][now_y] == 0:
            cur_x, cur_y = now_x, now_y
            num += 1

        else:
            idx = (idx+1)%4

# main
n,m = map(int,input().split())
solve_1941(n, m)

