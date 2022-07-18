n,m = map(int,input().split())
nlist = sorted(list(map(int,input().split())))
visited = [0]*n
result = []

def dfs(d):
    if d == m:
        print(*result)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            result.append(nlist[i])
            dfs(d+1)
            result.pop()
            visited[i] = 0
dfs(0)

