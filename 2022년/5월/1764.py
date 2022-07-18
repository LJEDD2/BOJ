n,m = map(int,input().split())
l = set([input() for _ in range(n)])
s = set([input() for _ in range(m)])

print(len(l&s),*sorted(l&s),sep='\n') # 교집합 판단

