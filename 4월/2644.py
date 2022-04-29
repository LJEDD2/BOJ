from collections import deque

n = int(input())
a,b = map(int,input().split())
k = int(input())

board = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(k):
    x,y = map(int,input().split())
    board[x].append(y)
    board[y].append(x)
print(board)

def bfs(s):
    queue = deque([s])
    visited[s] = 1
    while queue:
        x = queue.popleft()
        for nx in board[x]:
            if nx == b:
                print(visited[x])
                exit()
            if not visited[nx]:
                visited[nx] = visited[x]+1
                queue.append(nx)
bfs(a)
print(-1)
