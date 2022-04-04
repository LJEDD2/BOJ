n,m,count = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

while count > 0:
    #진행방향 : 좌 하 우 상
    for i in range(min(n,m)//2): # 회전시킬 그룹의 개수
        x, y = i, i #대각선으로 이동
        now = board[x][y]

        # 왼쪽으로 이동
        for j in range(i+1, n-i):
            x = j
            prev, board[x][y] = board[x][y], now
            now = prev

        # 아래쪽으로 이동
        for j in range(i+1, m-i):
            y = j
            prev,board[x][y] = board[x][y],now
            now = prev

        # 오른쪽으로 이동
        for j in range(i+1,n-i):
            x = n - j - 1 # 바로 위에 값

            prev, board[x][y] = board[x][y], now
            now = prev

        # 위쪽으로 이동
        for j in range(i+1, m-i):
            y = m - j - 1
            prev, board[x][y] = board[x][y], now
            now = prev
    count-=1
    
for i in board:
    print(*i)
