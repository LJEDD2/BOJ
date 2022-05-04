n = int(input())
board = [0]*n
sumv = 0
def check(x):
    for i in range(x):
        # 0,0부터 차례로 채워나가므로 바로 위쪽 줄만 확인하면 된다.
        # 이전 배열에 해당 값이 있는지 확인
        # 대각선 양쪽 다 확인
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False
    return True

def dfs(depth):
    global sumv
    if depth == n:
        sumv += 1
        return

    for i in range(n):
        board[depth] = i
        if check(depth):
            dfs(depth+1)

dfs(0)
print(sumv)
