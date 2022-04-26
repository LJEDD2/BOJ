from collections import deque
n,m = map(int,input().split())
maxv = 100001
arr = [0]*maxv
# 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치

def OOB(x):
    return 0 <= x <= 100000

def bfs():
    q = deque([n])
    #arr[n] = 1
    while q:
        x = q.popleft()
        if x == m:
            print(arr[m])
            break
        for i in(x-1,x+1,x*2):
            if OOB(i) and not arr[i]:
                arr[i] = arr[x] + 1
                q.append(i)
bfs()
