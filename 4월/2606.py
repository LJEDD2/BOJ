from collections import deque
n = int(input())

def BFS(x):
    queue = deque([x])
    visited[x] = True

    while queue:
        virus = queue.popleft()
        for i in computer[virus]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return visited[x+1:].count(True)

computer = [[]*n for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(int(input())):
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)

print(BFS(1))
