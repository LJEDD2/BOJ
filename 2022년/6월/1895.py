n,m = map(int,input().split())
board = [list(map(int,input().split())) for i in range(n)]
T = int(input())
cnt = 0

for row in range(n-2):
    for col in range(m-2):
        result = []
        for r in range(row,row+3):
            for c in range(col,col+3):
                result.append(board[r][c])
        result.sort()
        #print(result)
        #print(result[4])
        # 어차피 필터가 3x3이라서 중앙값 = 제일 가운데 4번째 수
        if result[4] >= T:
            cnt += 1

print(cnt)

