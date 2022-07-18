from collections import deque
n,m,v = map(int,input().split())
board = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    board[a].append(b)
    board[b].append(a)

def dfs(x):
    print(x,end=" ")
    visited[x] = True
    for nx in sorted(board[x]):
        if not visited[nx]:
            dfs(nx)
            visited[nx] = True

def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        nx = queue.popleft()
        print(nx, end =' ')
        for i in sorted(board[nx]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False]*(n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)