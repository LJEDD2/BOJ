n,m = map(int,input().split())
check = []

# 현재 값과 비교해서 이미 한번 봤던 숫자는 방문 표시
# x < y 인지 비교

def dfs(d):
    if len(check) == m:
        print(*check)

    for i in range(d, n+1):
        if i not in check:
            check.append(i) #넣었다가
            dfs(i+1) #길이가 m이 될때까지 반복
            check.pop() # 빼고

dfs(1)
