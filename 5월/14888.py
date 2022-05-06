n = int(input())
num = list(map(int,input().split()))
option = list(map(int,input().split()))

# -10억 < result < 10억
# 초기값
maxv = -int(1e9)
minv = int(1e9)
result = num[0]

def dfs(result,depth,add,sub,multi,division):
    global maxv, minv

    if depth == n:
        maxv = max(result,maxv)
        minv = min(result,minv)
        return

    if add:
        dfs(result + num[depth], depth + 1, add - 1, sub, multi, division)
    if sub:
        dfs(result - num[depth], depth + 1, add, sub - 1, multi, division)
    if multi:
        dfs(result * num[depth], depth + 1, add, sub, multi - 1, division)
    if division:
        dfs(int(result / num[depth]), depth + 1, add, sub, multi, division - 1)

dfs(result,1,*option)
print(maxv,minv,sep='\n')
