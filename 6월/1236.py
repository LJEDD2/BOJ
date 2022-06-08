n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
cnt_n = n
for i in board:
    if 'X' in i:
        cnt_n -= 1

cnt_m = m
for i in range(m):
    for j in range(n):
        if board[j][i] == 'X':
            cnt_m -= 1
            break

print(max(cnt_n,cnt_m))
