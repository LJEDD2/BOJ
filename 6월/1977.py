import math
n = math.sqrt(int(input()))
m = math.sqrt(int(input()))
ans = []

if n == 1:
    ans.append(1)

for i in range(int(n)+1,int(m)+1):
    ans.append(i**2)

if ans:
    print(sum(ans),min(ans),sep='\n')
else:
    print(-1)
