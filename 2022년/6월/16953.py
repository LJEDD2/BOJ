from collections import deque
n,m = map(int,input().split())

queue = deque([(n,0)])

while queue:
    now, minv = queue.popleft()

    if now == m:
        print(minv + 1)
        exit()

    if now * 2 <= m:
        queue.append([now*2,minv+1])
    if now * 10 + 1 <= m:
        queue.append([now*10+1,minv+1])

print(-1)