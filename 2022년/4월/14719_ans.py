h , w = map(int,input().split())
bar = list(map(int,input().split()))
sumv = 0

for i in range(w):
    sumv += min(max(bar[:i+1]),max(bar[i:]))-bar[i]
print(sumv)

