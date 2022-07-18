n,m = map(int,input().split())
check = []

def dfs(d):
    if len(check) == m:
        print(*check)

    for i in range(d, n+1):
        if i not in check:
            check.append(i) #넣었다가
            dfs(i+1) #길이가 m이 될때까지 반복
            check.pop()
dfs(1)
