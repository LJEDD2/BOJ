n,m = map(int,input().split())
nlist = sorted(list(map(int,input().split())))
result = []

def dfs(d):
    if d == m:
        print(*result)
        return

    for i in range(n):
        result.append(nlist[i])
        dfs(d+1)
        result.pop()

dfs(0)
