k, l = map(int,input().split())
sugang = {}
for i in range(1,l+1):
    id = input()
    sugang[id] = i

print(*sorted(sugang, key = lambda x: sugang[x])[:k], sep='\n')