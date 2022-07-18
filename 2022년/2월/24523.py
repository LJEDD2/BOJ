"""
시간초과
n = int(input())
s_list = list(map(int,input().split()))

for i in range(n):
    flag =True
    for j in range(i+1,n):
        if s_list[i] != s_list[j]:
            print(j+1, end=" ")
            flag = False
            break
    if flag ==True:
        print(-1,end=" ")
"""
import sys
input = sys.stdin.readline

n = int(input())
s_list = [0]+list(map(int, input().split()))
idx = [-1] * (n+1)
pos = -1

for i in range(n-1,0,-1):
    if s_list[i] != s_list[i+1]:
        pos = i+1
    idx[i] = pos
print(*idx[1:])

