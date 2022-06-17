a,b = map(int,input().split())

if a - b < 0 or (a-b) % 2 != 0:
    print(-1)
else:
    n = (a+b)//2
    m = a-n
    print(max(n,m),min(n,m))
