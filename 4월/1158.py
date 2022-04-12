from collections import deque

n,k = map(int,input().split())
queue = deque([i+1 for i in range(n)])
ans = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print('<',end='')
print(*ans,sep=', ',end='')
print('>')
