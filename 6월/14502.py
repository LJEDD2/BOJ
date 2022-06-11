import copy
from collections import deque
import sys
input = sys.stdin.readline()
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
result = 0

def OOB(x,y):
    return 0 <= x < n and 0 <= y < m

def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
           if board[i][j] == 0 :
               board[i][j] = 1
               dfs(cnt + 1)
               board[i][j] = 0
def bfs():
    global result
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    copy_ = copy.deepcopy(board)
    queue = deque()
    # VIRUS 위치 저장 및 퍼뜨리기
    for i in range(n):
        for j in range(m):
            if copy_[i][j] == 2 :
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for d_x,d_y in zip(dx,dy):
            nx , ny = x + d_x,y + d_y
            if OOB(nx,ny):
                if copy_[nx][ny] == 0:
                    copy_[nx][ny] = 2
                    queue.append((nx,ny))

    cnt = 0
    for i in copy_:
        cnt += i.count(0)
    result = max(result,cnt)

dfs(0)
print(result)
