board = [list(input()) for _ in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if not(i+j)%2:
            if board[i][j] == 'F':
                ans += 1
print(ans)