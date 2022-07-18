# 체스 - 퀸
# 가로-세로-대각선으로 모두 움직일 수가 있고, 사거리 내에 있으면 잡아먹힌다(?)
# 퀸 n개가 서로 공격할 수 없게 놓는 경우의 수
# 0,0부터 가능한 범위 탐색한다음 깊이마다 겹치는 부분?은 가지치기 해줘야한다는거 같은데 뭐 어쩌라는 건지 도저히 모루게따

# 1차원 배열에다가 현재 값이랑
# 이전의 깊이랑 현재랑 비교해주는 방법
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