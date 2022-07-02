def bingo():
    b_cnt = 0 # 빙고 줄 개수
    
    # 세로줄 빙고개수 탐색
    for i in range(5):
        zero = 0 # 바뀐 0 개수
        for j in range(5):
            if not board[j][i]:
                zero += 1
        if zero == 5:
            b_cnt += 1
            
    # 가로줄 빙고개수 탐색
    for i in board:
        if not sum(i):
            b_cnt += 1
    
    # 대각선 빙고개수 탐색
    up = [] # 우하단
    down = [] #우상단
    for i in range(5):
        up.append(board[i][i])
        down.append(board[i][4-i])

    if not sum(up):
        b_cnt += 1
    if not sum(down):
        b_cnt += 1

    return b_cnt


# main
board = [list(map(int,input().split())) for _ in range(5)]
check = []
for i in range(5):
    check += input().split()

for n in check:
    flag = False
    for i in range(5):
        for j in range(5):
            if int(n) == board[i][j]:
                board[i][j] = 0
                flag = True
                break
        if flag:
            break

    if bingo() >= 3:
        print(check.index(n)+1)
        break
