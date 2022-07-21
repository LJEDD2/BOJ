def solve(board):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            row[board[i][j]] = 1
            col[board[j][i]] = 1
        if sum(row) != 9 or sum(col) != 9:
            return False

    for i in range(3):
        for j in range(3):
            thbyth = [0] * 10
            for x in range(3):
                for y in range(3):
                    thbyth[board[3*i+x][3*j+y]] = 1
            if sum(thbyth) != 9:
                return False

    return True

n = int(input())
for t in range(1,n+1):
    board = []
    col = input()
    if not col :
        for i in range(9):
            board.append(list(map(int,input().split())))
    else:
        board.append(list(map(int,col.split())))
        for i in range(8):
            board.append(list(map(int,input().split())))

    print(board)

    if solve(board):
        print(f'Case {t}: CORRECT')
    else:
        print(f'Case {t}: INCORRECT')