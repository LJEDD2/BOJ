n,m = map(int,input().split())
nlist = sorted(list(map(int,input().split())))
result = []

def dfs(d):
    if len(result) == m:
        print(*result)
        return

    for i in range(d,n):
        if nlist[i] not in result:
            result.append(nlist[i])
            dfs(i)
            result.pop()

dfs(0)
