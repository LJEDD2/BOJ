n,m = map(int,input().split())
nlist = sorted(list(map(int,input().split())))
visited = [0]*n
result = []

# 자식 노드끼리의 정보 전달이 어떻게 될지
# 자식이 부모의 정보를 볼 때 -> 부모가 파라미터로 넘겨줌
# 부모가 자식의 정보를 볼 때 -> 자식이 return값으로 부모에게 전달
# 그럼 자식끼리는 ? prev에 이전 값을 따로 저장해서 중복이 있는지 확인
def dfs(d):
    if len(result) == m:
        print(*result)
        return

    prev = 0
    for i in range(d,n):
        if not visited[i] and prev != nlist[i]:
            visited[i] = 1
            result.append(nlist[i])
            prev = nlist[i]
            dfs(i+1)
            result.pop()
            visited[i] = 0
dfs(0)
