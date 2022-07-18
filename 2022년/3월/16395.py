board = [[1 for _ in range(i)] for i in range(1,31)]

for i in range(2,30):
    for j in range(1,i):
        board[i][j] = board[i-1][j-1] + board[i-1][j]

n,k = map(int,input().split())
print(board[n-1][k-1])