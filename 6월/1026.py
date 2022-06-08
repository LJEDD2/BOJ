n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)
b = sorted(list(map(int,input().split())))

sumv = 0
for i,j in zip(a,b):
    sumv += i*j
print(sumv)
