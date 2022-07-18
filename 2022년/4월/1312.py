n,m,k = map(int, input().split())

for _ in range(k):
    n %= m
    n *= 10 

print(int(n//m))
