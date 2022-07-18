import sys
n,m = map(int,sys.stdin.readline().split())
s_dict = {}
for i in range(1,n+1):
    name = input()
    temp = str(i)
    s_dict[name] = temp
    s_dict[temp] = name

for _ in range(m): print(s_dict[input()])