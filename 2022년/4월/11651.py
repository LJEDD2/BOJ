nlist = sorted([list(map(int, input().split())) for _ in range(int(input()))] , key = lambda x : (x[1],x[0]))
for i in nlist: print(*i)