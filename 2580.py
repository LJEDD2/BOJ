import sys
input = sys.stdin.readline
board= [list(map(int, input().split())) for _ in range(9)]
zero = [[x,y] for x in range(9) for y in range(9) if board[x][y] == 0]
empty = len(zero)

#가로
def Row(x,k):
    for i in range(9):
        if k == board[x][i]:
            return False
    return True

#세로
def Col(y,k):
    for i in range(9):
        if k == board[i][y]:
            return False
    return True

#3x3
def Square(x,y,k):
    x = x//3 * 3
    y = y//3 * 3
    for i in range(x,x+3):
        for j in range(y,y+3):
            if k == board[i][j]:
                return False
    return True


def dfs(depth):
    if depth == empty:
        for i in board: print(*i)
        exit()

    for k in range(1,10):
        x,y = zero[depth]
        if Row(x,k) and Col(y,k) and Square(x,y,k):
            board[x][y] = k
            dfs(depth+1)
            board[x][y] = 0

dfs(0)
