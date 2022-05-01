n,m= map(int,input().split())
board = [list(input()) for _ in range(n)]

for k in range(n):
    for i in range(n-1):
        for j in range(m):
            if board[i][j] == 'o' and board[i+1][j] == '.':
                board[i][j], board[i+1][j] = '.', 'o'

for i in board: print(''.join(i))
