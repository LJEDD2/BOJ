a,b,c = map(int,input().split())

sumv = {}
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            v = i+j+k
            if sumv.get(v):
                sumv[v] += 1
            else:
                sumv[v]= 1
print(sorted(sumv.items(), key = lambda x : -x[1])[0][0])
