n, k = map(int,input().split())
number = []
result = []

def dfs(depth):
    if sum(result) > n:
        return

    if sum(result) == n:
        number.append(list(result))
        return

    # 1~3까지 차례대로 넣었다가 빼면서 반복
    for i in range(1,4):
        result.append(i)
        dfs(depth+1)
        result.pop()

dfs(0)
if len(number) >= k:
    print(*number[k-1],sep='+')
else:
    print(-1)
