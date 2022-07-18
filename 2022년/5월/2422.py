import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [[0]*n for _ in range(n)]

for i in range(m):
    x,y = map(int, input().split())
    visited[x-1][y-1] = 1
    visited[y-1][x-1] = 1

for i in visited : print(*i)

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if not visited[i][j] and not visited[i][k] and not visited[j][k]:
                print(i+1,j+1,k+1)
                cnt += 1


print(cnt)

