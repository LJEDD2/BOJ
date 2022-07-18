def solve(board,n):
    if n == 1:
        return board[0][0]

    sub = [[] for i in range(n // 2)]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            sub[i//2].append(sorted([board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]])[2])
    print(sub)
    return solve(sub,n//2)


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
print(solve(board,n))