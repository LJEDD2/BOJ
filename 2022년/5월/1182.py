n,k = map(int,input().split())
nlist = list(map(int,input().split()))
num = []
result = []
visited = [0]*n

def dfs(d):
    if sum(num) == k and len(num) != 0:
        result.append(list(num))

    for i in range(d,n):
        if not visited[i]:
            visited[i] = 1
            num.append(nlist[i])
            dfs(i)
            num.pop()
            visited[i] = 0

dfs(0)
print(len(result))