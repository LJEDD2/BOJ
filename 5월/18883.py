n, m = map(int,input().split())
nlist = [ i for i in range(1,n*m+1)]
for i in range(n):
    print(*nlist[i*m:i*m+m])
    
