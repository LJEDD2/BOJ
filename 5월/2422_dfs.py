import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dislike = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    dislike[x].append(y)
    dislike[y].append(x)

check = []
visited = [0] * (n+1)
cnt = 0

def dfs(depth):
    global cnt
    if depth == 3:
        for icecream in check:
            for ban in dislike[icecream]:
                if visited[ban]:
                    return
        cnt += 1
        return

    for i in range(1,n+1):
        if not visited[i]:
            if check and check[-1] < i:
                continue
            visited[i] = 1
            check.append(i)
            dfs(depth+1)
            check.pop()
            visited[i] = 0

dfs(0)
print(cnt)
