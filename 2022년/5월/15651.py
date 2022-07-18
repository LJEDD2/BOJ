n,m = map(int,input().split())
check = []
def dfs(d):
    if d == m:
        print(*check)
        return

    for i in range(n):
        check.append(i+1) #넣었다가
        dfs(d+1) #길이가 m이 될때까지 반복
        check.pop()
dfs(0)