n,m = map(int,input().split())
s_dict = {}
for i in range(1,n+1):
    name = input()
    s_dict[name] = str(i)
    s_dict[str(i)] = name

for _ in range(m): print(s_dict[input()])
