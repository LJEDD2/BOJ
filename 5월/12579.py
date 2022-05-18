board = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
# 1 = O , 2 = X
n = int(input())
if n == 1:
    flag = True
else:
    flag = False

for k in range(9):
    x, y = map(int, input().split())

    if flag:
        board[x-1][y-1] = 1
    else:
        board[x-1][y-1] = 2
    flag = not flag

    for i in range(3):
        if board[x-1][0] == board[x-1][1] == board[x-1][2] or board[0][y-1] == board[1][y-1] == board[2][y-1] or \
            board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            print(board[x-1][y-1])
            exit()

print(0)
