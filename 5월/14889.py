n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [0]*(n+1)
result = 1e9

def dfs(depth,idx):
    global result
    if depth == (n//2) :   #  한쪽 팀이 다 만들어짐
        start_team, link_team = 0,0
        for i in range(n):
            for j in range(i+1,n):
                if visited[i] and visited[j]:
                    start_team += (board[i][j] + board[j][i])
                elif not visited[i] and not visited[j]:
                    link_team += (board[i][j] + board[j][i])
        result = min(result,abs(start_team-link_team))
        return

    for i in range(idx,n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1,i+1) # 반복문을 최대한 줄여야 한다. 중복 x 
            visited[i] = 0

dfs(0,0)
print(result)
