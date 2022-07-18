n = int(input())
result = []

def check(arr):
    for i in range(1,(len(arr)//2)+1):
        if arr[-i:] == arr[-2*i:-i]:
            return False
    return True

def dfs(depth):
    if not check(result):
        return

    if depth == n:
        print(*result, sep="")
        exit()

    for i in range(1,4):
        result.append(i)
        dfs(depth+1)
        result.pop()

dfs(0)
print(-1)