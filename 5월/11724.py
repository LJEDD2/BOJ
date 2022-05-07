import sys
from collections import deque
input = sys.stdin.readline

u,v = map(int,input().split())
board = [[]*i for i in range(u+1)]
check = [0]*(u+1)
cnt = 0

for i in range(v):
    x,y = map(int,input().split())
    board[x].append(y)
    board[y].append(x)

def bfs(x):
    queue = deque([x])
    check[x] = 1

    while queue:
        nx = queue.popleft()
        for nx in board[nx]:
            if not check[nx]:
                queue.append(nx)
                check[nx] = 1


for i in range(1,u+1):
    if not check[i]:
        bfs(i)
        cnt += 1
print(cnt)
