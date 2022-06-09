import math
result = set()
n,m = map(int,input().split())
for i in range(1,int(math.sqrt(n))+1):
    if n%i == 0:
        result.add(i)
        result.add(n//i)
result = sorted(result)
if 1 <= m <= len(result):
    print(result[m-1])
else:
    print(0)
