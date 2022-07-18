n,m = map(int,input().split())
check = []

# 중복이 허용된 조합
def dfs(d):
    if len(check) == m:
        print(*check)
        return

    for i in range(d,n+1):
        check.append(i)
        dfs(i)
        check.pop()
dfs(1)
