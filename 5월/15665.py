nlist = sorted(list(map(int,input().split())))
visited = [0]*n
result = []

# 자식 노드끼리의 정보 전달이 어떻게 될지
# 자식이 부모의 정보를 볼 때 -> 부모가 파라미터로 넘겨줌
# 부모가 자식의 정보를 볼 때 -> 자식이 return값으로 부모에게 전달
# 그럼 자식끼리는 ? prev에 이전 값을 따로 저장해서 중복이 있는지 확인
def dfs(d):
    if d == m:
        print(*result)
        return

    prev = 0
    for i in range(n):
        # 중복 검사 제거
        if prev != nlist[i]:
            result.append(nlist[i])
            prev = nlist[i]
            dfs(d+1)
            result.pop()
dfs(0)
