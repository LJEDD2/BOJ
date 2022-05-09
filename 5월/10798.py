board = [list(input()) for _ in range(5)]
maxv = 0
ans = ''
for i in board:
    maxv = max(len(i),maxv)

for i in range(maxv):
    for j in range(5):
        try:
            print(board[j][i],end='')
        except IndexError:
            pass
